#!/usr/bin/env python3
"""Canvas LMS Course Exporter - Full archive of all Park University courses.

Exports courses into a semester-organized offline archive with submissions,
grades, file downloads, and master index.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

API_BASE = "https://canvas.park.edu/api/v1"
OUTPUT_DIR = Path("/home/me/documents/park/canvas_scrape/output")
CONFIG_PATH = Path("/home/me/documents/park/canvas_scrape/config.json")

BASE_DELAY = 0.3
MAX_RETRIES = 3


def load_token() -> str:
    """Load API token from config.json, falling back to CANVAS_TOKEN env var."""
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
            token = cfg.get("canvas_token", "")
            if token:
                return token
    token = os.environ.get("CANVAS_TOKEN", "")
    if not token:
        print("Error: No API token found. Set CANVAS_TOKEN env var or create config.json")
        sys.exit(1)
    return token


TOKEN = load_token()
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# ---------------------------------------------------------------------------
# Term / semester helpers
# ---------------------------------------------------------------------------

TERM_MAP = {
    "S1": "spring_1",
    "S2": "spring_2",
    "U1": "summer",
    "F1": "fall_1",
    "F2": "fall_2",
}

# Course code -> clean short title fallback (used when name doesn't parse cleanly)
COURSE_CATALOG: Dict[str, str] = {
    "BI101": "Biological Concepts",
    "CJ316": "Cybersecurity Administration",
    "CS152": "Intro Python Programming",
    "CS202": "Secure Programming",
    "CS208": "Discrete Mathematics",
    "CS225": "Programming Concepts",
    "CS240": "Web Programming I",
    "CS252": "Object-Oriented Programming",
    "CS300": "Technology in a Global Society",
    "CS305": "Intro Artificial Intelligence",
    "CS319": "Computer Architecture",
    "CS335": "Intro Cybersecurity",
    "CS351": "Computer Operating Systems",
    "CS352": "Data Structures",
    "CS365A": "Computer Networking I",
    "CS366A": "Computer Networking II",
    "CS369": "OS Administration",
    "CS371": "Internetworking",
    "CS372": "Advanced Networking",
    "CS375": "Secure Operation",
    "CS377": "Digital Forensics",
    "EN105": "First Year Writing Seminar I",
    "EN106": "First Year Writing II",
    "EN234": "Intro to Fiction",
    "EN306C": "Professional Writing",
    "IS205": "Managing Info Systems",
    "IS361": "Data Management Concepts",
    "IS362": "Applied Database Management",
    "LE300G": "Integrative Capstone",
    "MA120": "Basic Statistics",
    "MA125": "Intermediate Algebra",
    "PO200": "American National Government",
    "PY101": "Physical World",
}


def parse_semester(canvas_name: str, start_at: str = "") -> Tuple[str, str]:
    """Extract year + term from Canvas course name or start date.

    Examples:
        "CS152DLAS2A2021"     -> ("2021", "spring_2")
        "BI101DLBS1A2022"     -> ("2022", "spring_1")
        "MA125DLAF1A2021"     -> ("2021", "fall_1")
    Falls back to inferring from start_at date if name has no section code.
    """
    # Pattern: term code [SUF][12] followed by section letter + 4-digit year
    # e.g. CS152DLAS2A2021 -> S2 + A + 2021
    m = re.search(r'([SUF][12])A(\d{4})', canvas_name)
    if m:
        term_code = m.group(1).upper()
        year = m.group(2)
        term_name = TERM_MAP.get(term_code, term_code.lower())
        return (year, term_name)

    # Fallback: infer from start_at date
    # Park 8-week terms: S1=Jan, S2=Mar, U1=May/Jun, F1=Aug/Sep, F2=Oct/Nov/Dec
    if start_at:
        date_m = re.match(r'(\d{4})-(\d{2})', start_at)
        if date_m:
            year = date_m.group(1)
            month = int(date_m.group(2))
            if month in (12,):
                # Dec start = next year's spring_1
                return (str(int(year) + 1), "spring_1")
            if month in (1, 2):
                return (year, "spring_1")
            if month in (3, 4):
                return (year, "spring_2")
            if month in (5, 6, 7):
                return (year, "summer")
            if month in (8, 9):
                return (year, "fall_1")
            if month in (10, 11):
                return (year, "fall_2")

    # Last resort: try to find just a year in the name
    m2 = re.search(r'(\d{4})', canvas_name)
    if m2:
        return (m2.group(1), "unknown")
    return ("unknown", "unknown")


def clean_course_name(code: str, full_name: str) -> str:
    """Strip section code junk from course name.

    Example:
        code="BI101DLBS1A2022", full_name="BI101DLBS1A2022 Biological Concepts"
        -> "BI101_Biological_Concepts"
    """
    # Extract the base course code (letters + digits + optional suffix letter)
    # Anchor on 'DL' section marker: BI101DL..., CS365ADL..., EN306CDL...
    base_code_m = re.match(r'([A-Z]{2,4}\d{3}[A-Z]?)DL', code)
    if not base_code_m:
        # Fallback for codes without DL (e.g. short codes from API)
        base_code_m = re.match(r'([A-Z]{2,4}\d{3}[A-Z]?)', code)
    base_code = base_code_m.group(1) if base_code_m else code[:6]

    # Remove the section code prefix from the full name to get just the title
    # The full name often starts with the full section code
    title = full_name
    # Try removing the section code prefix
    for prefix in [code, base_code]:
        if title.startswith(prefix):
            title = title[len(prefix):].strip()
            break

    # If we still have the full name with no separation, try catalog
    if not title or title == full_name:
        title = COURSE_CATALOG.get(base_code, full_name)

    # Clean up the title
    title = re.sub(r'[^\w\s\-]', '', title).strip()
    title = re.sub(r'\s+', '_', title)

    return f"{base_code}_{title}" if title else base_code


def normalize_module_name(name: str) -> str:
    """Normalize module name to lowercase, zero-padded folder name.

    Examples:
        "Unit 1"             -> "unit_01"
        "Unit 12"            -> "unit_12"
        "Course Information"  -> "course_information"
        "Week 3: Databases"  -> "week_03"
    """
    name = name.strip()

    # Match "Unit X", "Week X", "Module X" patterns
    m = re.match(r'(unit|week|module)\s*(\d+)', name, re.IGNORECASE)
    if m:
        label = m.group(1).lower()
        num = int(m.group(2))
        return f"{label}_{num:02d}"

    # Otherwise just clean it
    cleaned = re.sub(r'[^\w\s\-]', '', name).strip().lower()
    return re.sub(r'\s+', '_', cleaned)[:60]


def clean_item_filename(title: str, module_name: str = "") -> str:
    """Clean item title for filename, stripping redundant unit prefix.

    If the file lives in unit_01/, strip "Unit 1 " prefix from the title.
    "Unit 1 Discussion 1" -> "discussion_1"
    "Unit 1 Quiz"         -> "quiz"
    "Course Overview"     -> "course_overview"
    """
    cleaned = title.strip()

    # Strip "Unit X " or "Week X " prefix since file is already in that folder
    cleaned = re.sub(r'^(Unit|Week|Module)\s*\d+\s*[-:.]?\s*', '', cleaned, flags=re.IGNORECASE)

    # Make filesystem safe
    cleaned = re.sub(r'[^\w\s\-]', '', cleaned).strip()
    cleaned = re.sub(r'\s+', '_', cleaned).lower()

    return cleaned[:80] if cleaned else "untitled"


# ---------------------------------------------------------------------------
# HTML to text converter
# ---------------------------------------------------------------------------

class HTMLToText(HTMLParser):
    """Simple HTML to plain text converter."""

    BLOCK_TAGS = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr"}
    ENDLINE_TAGS = BLOCK_TAGS | {"table"}
    SKIP_TAGS = {"script", "style"}

    def __init__(self) -> None:
        super().__init__()
        self._text: List[str] = []
        self._skip = False

    def handle_starttag(self, tag: str, attrs: List[tuple]) -> None:
        if tag in self.SKIP_TAGS:
            self._skip = True
            return
        if tag == "br":
            self._text.append("\n")
        elif tag in self.BLOCK_TAGS:
            self._text.append("\n")
        elif tag == "a":
            for attr_name, attr_val in attrs:
                if attr_name == "href":
                    self._text.append(f" [link: {attr_val}] ")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS:
            self._skip = False
        elif tag in self.ENDLINE_TAGS:
            self._text.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip:
            self._text.append(data)

    def get_text(self) -> str:
        joined = "".join(self._text)
        return re.sub(r"\n{3,}", "\n\n", joined).strip()


def html_to_text(html: Optional[str]) -> str:
    if not html:
        return ""
    parser = HTMLToText()
    parser.feed(html)
    return parser.get_text()


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def build_url(endpoint: str, params: Optional[Dict[str, str]] = None) -> str:
    url = f"{API_BASE}/{endpoint}"
    if params:
        query = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{query}"
    if "?" in url:
        return f"{url}&per_page=100"
    return f"{url}?per_page=100"


def api_get(endpoint: str, params: Optional[Dict[str, str]] = None) -> Any:
    """Make a GET request to the Canvas API with pagination, retries, and rate limiting."""
    url = build_url(endpoint, params)
    all_results: List[dict] = []

    while url:
        data = None
        for attempt in range(MAX_RETRIES):
            req = urllib.request.Request(url, headers=HEADERS)
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = json.loads(resp.read().decode())

                    if not isinstance(data, list):
                        return data

                    all_results.extend(data)
                    url = None
                    link_header = resp.getheader("Link", "")
                    if link_header:
                        for part in link_header.split(","):
                            if 'rel="next"' in part:
                                url = part.split("<")[1].split(">")[0]
                                break
                    break  # success, exit retry loop

            except urllib.error.HTTPError as exc:
                if exc.code == 429:
                    retry_after = int(exc.headers.get("Retry-After", 5))
                    print(f"  [Rate limited] Waiting {retry_after}s...")
                    time.sleep(retry_after)
                    continue
                if attempt < MAX_RETRIES - 1:
                    delay = BASE_DELAY * (2 ** attempt)
                    print(f"  [API Error {exc.code}] {endpoint} - retry in {delay:.1f}s")
                    time.sleep(delay)
                    continue
                print(f"  [API Error {exc.code}] {endpoint} - giving up")
                return all_results if all_results else []

            except Exception as exc:
                if attempt < MAX_RETRIES - 1:
                    delay = BASE_DELAY * (2 ** attempt)
                    print(f"  [Error] {endpoint}: {exc} - retry in {delay:.1f}s")
                    time.sleep(delay)
                    continue
                print(f"  [Error] {endpoint}: {exc} - giving up")
                return all_results if all_results else []

        time.sleep(BASE_DELAY)

    return all_results


# ---------------------------------------------------------------------------
# File download
# ---------------------------------------------------------------------------

def download_file(url: str, dest_path: Path) -> bool:
    """Download a binary file from Canvas using auth token.

    Returns True on success, False on failure.
    """
    if dest_path.exists():
        return True  # already downloaded

    dest_path.parent.mkdir(parents=True, exist_ok=True)

    for attempt in range(MAX_RETRIES):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=60) as resp:
                with open(dest_path, "wb") as f:
                    while True:
                        chunk = resp.read(8192)
                        if not chunk:
                            break
                        f.write(chunk)
            return True

        except urllib.error.HTTPError as exc:
            if exc.code == 429:
                retry_after = int(exc.headers.get("Retry-After", 5))
                time.sleep(retry_after)
                continue
            if attempt < MAX_RETRIES - 1:
                time.sleep(BASE_DELAY * (2 ** attempt))
                continue
            print(f"    [Download failed {exc.code}] {dest_path.name}")
            return False

        except Exception as exc:
            if attempt < MAX_RETRIES - 1:
                time.sleep(BASE_DELAY * (2 ** attempt))
                continue
            print(f"    [Download error] {dest_path.name}: {exc}")
            return False

    return False


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def safe_filename(name: str) -> str:
    """Make a string safe for use as a filename."""
    return re.sub(r"[^\w\s\-]", "", name).strip().replace(" ", "_")[:80]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def add_line(lines: List[str], line: str = "") -> None:
    lines.append(line)


def categorize_assignment(name: str) -> str:
    """Auto-detect assignment category from name."""
    lower = name.lower()
    if "discussion" in lower:
        return "Discussion"
    if "quiz" in lower:
        return "Quiz"
    if "exam" in lower or ("final" in lower and "exam" in lower):
        return "Exam"
    if "homework" in lower or "hw" in lower:
        return "Homework"
    if "experiment" in lower or "lab" in lower:
        return "Lab"
    if "project" in lower or "capstone" in lower:
        return "Project"
    if "paper" in lower or "essay" in lower or "report" in lower:
        return "Paper"
    if "midterm" in lower:
        return "Exam"
    return "Other"


# ---------------------------------------------------------------------------
# Grade record
# ---------------------------------------------------------------------------

class GradeRecord:
    """Accumulates grade data during export."""

    def __init__(self) -> None:
        self.entries: List[Dict[str, Any]] = []

    def add(self, name: str, score: Optional[float], points_possible: Optional[float],
            due_date: str = "", assignment_id: Optional[int] = None) -> None:
        self.entries.append({
            "name": name,
            "category": categorize_assignment(name),
            "score": score,
            "points_possible": points_possible,
            "due_date": due_date,
            "assignment_id": assignment_id,
        })

    def generate_grades_md(self, course_name: str) -> str:
        """Generate per-course grades.md content."""
        lines = [f"# Grades - {course_name}", ""]

        if not self.entries:
            lines.append("No graded assignments found.")
            return "\n".join(lines) + "\n"

        # Category summary
        categories: Dict[str, Dict[str, float]] = {}
        for e in self.entries:
            cat = e["category"]
            if cat not in categories:
                categories[cat] = {"earned": 0.0, "possible": 0.0, "count": 0}
            if e["score"] is not None and e["points_possible"]:
                categories[cat]["earned"] += e["score"]
                categories[cat]["possible"] += e["points_possible"]
                categories[cat]["count"] += 1

        lines.append("## Summary by Category")
        lines.append("")
        lines.append("| Category | Earned | Possible | Pct | Count |")
        lines.append("|----------|-------:|--------:|----:|------:|")

        total_earned = 0.0
        total_possible = 0.0
        for cat in sorted(categories.keys()):
            d = categories[cat]
            pct = (d["earned"] / d["possible"] * 100) if d["possible"] > 0 else 0
            lines.append(f"| {cat} | {d['earned']:.1f} | {d['possible']:.1f} | {pct:.1f}% | {int(d['count'])} |")
            total_earned += d["earned"]
            total_possible += d["possible"]

        overall_pct = (total_earned / total_possible * 100) if total_possible > 0 else 0
        lines.append(f"| **Total** | **{total_earned:.1f}** | **{total_possible:.1f}** | **{overall_pct:.1f}%** | **{sum(int(d['count']) for d in categories.values())}** |")
        lines.append("")

        # Letter grade
        letter = pct_to_letter(overall_pct)
        lines.append(f"**Estimated Grade:** {letter} ({overall_pct:.1f}%)")
        lines.append("")

        # Full assignment list
        lines.append("## All Assignments")
        lines.append("")
        lines.append("| Assignment | Category | Score | Possible | Due |")
        lines.append("|------------|----------|------:|---------:|-----|")
        for e in self.entries:
            score_str = f"{e['score']:.1f}" if e["score"] is not None else "-"
            poss_str = f"{e['points_possible']:.1f}" if e["points_possible"] else "-"
            due = e["due_date"][:10] if e["due_date"] else ""
            lines.append(f"| {e['name']} | {e['category']} | {score_str} | {poss_str} | {due} |")

        lines.append("")
        return "\n".join(lines) + "\n"

    def get_totals(self) -> Dict[str, Any]:
        """Return course totals for master grades file."""
        total_earned = 0.0
        total_possible = 0.0
        graded_count = 0
        for e in self.entries:
            if e["score"] is not None and e["points_possible"]:
                total_earned += e["score"]
                total_possible += e["points_possible"]
                graded_count += 1
        pct = (total_earned / total_possible * 100) if total_possible > 0 else 0
        return {
            "earned": total_earned,
            "possible": total_possible,
            "pct": pct,
            "letter": pct_to_letter(pct),
            "count": graded_count,
        }


def pct_to_letter(pct: float) -> str:
    if pct >= 93:
        return "A"
    if pct >= 90:
        return "A-"
    if pct >= 87:
        return "B+"
    if pct >= 83:
        return "B"
    if pct >= 80:
        return "B-"
    if pct >= 77:
        return "C+"
    if pct >= 73:
        return "C"
    if pct >= 70:
        return "C-"
    if pct >= 67:
        return "D+"
    if pct >= 63:
        return "D"
    if pct >= 60:
        return "D-"
    return "F"


def gpa_value(letter: str) -> float:
    table = {
        "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0,
    }
    return table.get(letter, 0.0)


# ---------------------------------------------------------------------------
# Export: syllabus
# ---------------------------------------------------------------------------

def fetch_syllabus(course_id: int, course_name: str, course_dir: Path) -> None:
    print("  Fetching syllabus...")
    course_detail = api_get(f"courses/{course_id}", {"include[]": "syllabus_body"})
    if isinstance(course_detail, dict) and course_detail.get("syllabus_body"):
        syllabus_text = html_to_text(course_detail["syllabus_body"])
        write_text(
            course_dir / "syllabus.md",
            f"# Syllabus - {course_name}\n\n{syllabus_text}\n",
        )
        print("    Syllabus saved.")


# ---------------------------------------------------------------------------
# Export: announcements (separate file)
# ---------------------------------------------------------------------------

def export_announcements(course_id: int, course_name: str, course_dir: Path) -> None:
    print("  Fetching announcements...")
    announcements = api_get(
        f"courses/{course_id}/discussion_topics", {"only_announcements": "true"}
    )
    if not announcements:
        return

    lines = [f"# Announcements - {course_name}", ""]

    for ann in announcements:
        title = ann.get("title", "Untitled")
        add_line(lines, f"## {title}")
        if ann.get("posted_at"):
            add_line(lines, f"*Posted: {ann['posted_at']}*")
            add_line(lines)
        if ann.get("message"):
            add_line(lines, html_to_text(ann["message"]))
            add_line(lines)
        add_line(lines, "---")
        add_line(lines)

    write_text(course_dir / "announcements.md", "\n".join(lines).strip() + "\n")
    print(f"    {len(announcements)} announcements saved.")


# ---------------------------------------------------------------------------
# Export: module items (single-pass with grades + file downloads)
# ---------------------------------------------------------------------------

def export_module_item(course_id: int, mod_dir: Path, item: dict,
                       grades: GradeRecord, exported_ids: set) -> None:
    """Export a single module item, collecting grade data."""
    item_title = item.get("title", "Untitled")
    item_type = item.get("type", "Unknown")
    mod_name = mod_dir.name  # for filename cleaning

    if item_type == "Page" and item.get("page_url"):
        page = api_get(f"courses/{course_id}/pages/{item['page_url']}")
        if isinstance(page, dict) and page.get("body"):
            page_text = html_to_text(page["body"])
            fname = clean_item_filename(item_title, mod_name) + ".md"
            write_text(mod_dir / fname, f"# {item_title}\n\n{page_text}\n")
        return

    if item_type == "Assignment" and item.get("content_id"):
        content_id = item["content_id"]
        exported_ids.add(content_id)

        assignment = api_get(f"courses/{course_id}/assignments/{content_id}")
        if not isinstance(assignment, dict):
            return

        a_text = [f"# {item_title}", ""]
        due_at = assignment.get("due_at", "")
        pts = assignment.get("points_possible")

        if due_at:
            add_line(a_text, f"**Due:** {due_at}")
        if pts:
            add_line(a_text, f"**Points Possible:** {pts}")
        if assignment.get("submission_types"):
            add_line(a_text, f"**Submission Types:** {', '.join(assignment['submission_types'])}")
        if assignment.get("description"):
            add_line(a_text)
            add_line(a_text, "## Instructions")
            add_line(a_text)
            add_line(a_text, html_to_text(assignment["description"]))

        # Fetch submission
        sub = api_get(
            f"courses/{course_id}/assignments/{content_id}/submissions/self",
            {"include[]": "submission_comments"},
        )
        score = None
        if isinstance(sub, dict):
            score = sub.get("score")
            if sub.get("submitted_at") or score is not None:
                add_line(a_text)
                add_line(a_text, "---")
                add_line(a_text)
                add_line(a_text, "## My Submission")
                add_line(a_text)
                if score is not None:
                    add_line(a_text, f"**Score:** {score}/{pts}")
                    if sub.get("grade"):
                        add_line(a_text, f"**Grade:** {sub['grade']}")
                if sub.get("submitted_at"):
                    add_line(a_text, f"**Submitted:** {sub['submitted_at']}")
                    if sub.get("late"):
                        add_line(a_text, "**Late:** Yes")
                if sub.get("body"):
                    add_line(a_text)
                    add_line(a_text, html_to_text(sub["body"]))
                if sub.get("url"):
                    add_line(a_text)
                    add_line(a_text, f"**URL:** {sub['url']}")

                # Download submission attachments
                if sub.get("attachments"):
                    add_line(a_text)
                    add_line(a_text, "### Submitted Files")
                    add_line(a_text)
                    files_dir = mod_dir / "files"
                    for att in sub["attachments"]:
                        display = att.get("display_name", att.get("filename", "file"))
                        add_line(a_text, f"- **{display}**")
                        dl_url = att.get("url")
                        if dl_url:
                            dest = files_dir / display
                            if download_file(dl_url, dest):
                                add_line(a_text, f"  - Downloaded: `files/{display}`")

                # Feedback
                if sub.get("submission_comments"):
                    add_line(a_text)
                    add_line(a_text, "### Instructor Feedback")
                    add_line(a_text)
                    for comment in sub["submission_comments"]:
                        author = comment.get("author_name", "Unknown")
                        created = comment.get("created_at", "")
                        add_line(a_text, f"**{author}** ({created}):")
                        add_line(a_text)
                        add_line(a_text, f"> {comment.get('comment', '')}")
                        add_line(a_text)

        # Record grade
        grades.add(item_title, score, pts, due_at, content_id)

        fname = clean_item_filename(item_title, mod_name) + ".md"
        write_text(mod_dir / fname, "\n".join(a_text).strip() + "\n")
        return

    if item_type == "Discussion" and item.get("content_id"):
        content_id = item["content_id"]
        disc = api_get(f"courses/{course_id}/discussion_topics/{content_id}")
        if not isinstance(disc, dict):
            return

        # Track the assignment_id if this discussion is graded
        assignment_id = disc.get("assignment_id")
        if assignment_id:
            exported_ids.add(assignment_id)

        d_text = [f"# {item_title}", ""]
        if disc.get("message"):
            add_line(d_text, html_to_text(disc["message"]))

        score = None
        pts = disc.get("points_possible")
        due_at = disc.get("due_at", "")

        if assignment_id:
            sub = api_get(
                f"courses/{course_id}/assignments/{assignment_id}/submissions/self",
                {"include[]": "submission_comments"},
            )
            if isinstance(sub, dict):
                score = sub.get("score")
                if score is not None:
                    add_line(d_text)
                    add_line(d_text, f"**My Score:** {score}/{pts or '?'}")

                # Fetch my discussion entries
                entries = api_get(
                    f"courses/{course_id}/discussion_topics/{content_id}/entries"
                )
                if isinstance(entries, list) and entries:
                    my_user_id = sub.get("user_id")
                    my_entries = [e for e in entries if e.get("user_id") == my_user_id]
                    if my_entries:
                        add_line(d_text)
                        add_line(d_text, "---")
                        add_line(d_text)
                        add_line(d_text, "## My Discussion Posts")
                        add_line(d_text)
                        for entry in my_entries:
                            add_line(d_text, f"**Posted:** {entry.get('created_at', '')}")
                            add_line(d_text)
                            if entry.get("message"):
                                add_line(d_text, html_to_text(entry["message"]))
                                add_line(d_text)
                            add_line(d_text, "---")
                            add_line(d_text)

                if sub.get("submission_comments"):
                    add_line(d_text)
                    add_line(d_text, "### Feedback")
                    add_line(d_text)
                    for comment in sub["submission_comments"]:
                        author = comment.get("author_name", "")
                        body = comment.get("comment", "")
                        add_line(d_text, f"**{author}:** {body}")
                        add_line(d_text)

        # Record grade
        grades.add(item_title, score, pts, due_at, assignment_id)

        fname = clean_item_filename(item_title, mod_name) + ".md"
        write_text(mod_dir / fname, "\n".join(d_text).strip() + "\n")
        return

    if item_type == "Quiz" and item.get("content_id"):
        content_id = item["content_id"]
        exported_ids.add(content_id)

        quiz = api_get(f"courses/{course_id}/quizzes/{content_id}")
        if not isinstance(quiz, dict):
            return

        q_text = [f"# {item_title}", ""]
        due_at = quiz.get("due_at", "")
        pts = quiz.get("points_possible")

        if due_at:
            add_line(q_text, f"**Due:** {due_at}")
        if pts:
            add_line(q_text, f"**Points:** {pts}")
        if quiz.get("time_limit"):
            add_line(q_text, f"**Time Limit:** {quiz['time_limit']} minutes")
        if quiz.get("description"):
            add_line(q_text)
            add_line(q_text, html_to_text(quiz["description"]))

        # Try to get quiz submission score via assignment
        score = None
        quiz_assignment_id = quiz.get("assignment_id")
        if quiz_assignment_id:
            exported_ids.add(quiz_assignment_id)
            sub = api_get(
                f"courses/{course_id}/assignments/{quiz_assignment_id}/submissions/self",
                {"include[]": "submission_comments"},
            )
            if isinstance(sub, dict):
                score = sub.get("score")
                if score is not None:
                    add_line(q_text)
                    add_line(q_text, f"**My Score:** {score}/{pts}")
                if sub.get("submission_comments"):
                    add_line(q_text)
                    add_line(q_text, "### Feedback")
                    add_line(q_text)
                    for comment in sub["submission_comments"]:
                        author = comment.get("author_name", "")
                        body = comment.get("comment", "")
                        add_line(q_text, f"**{author}:** {body}")
                        add_line(q_text)

        # Record grade
        grades.add(item_title, score, pts, due_at, quiz_assignment_id)

        fname = clean_item_filename(item_title, mod_name) + ".md"
        write_text(mod_dir / fname, "\n".join(q_text).strip() + "\n")
        return

    if item_type == "File" and item.get("url"):
        # Download course files (PowerPoints, PDFs, etc.)
        files_dir = mod_dir / "files"
        file_data = api_get(f"courses/{course_id}/files/{item.get('content_id', '')}")
        if isinstance(file_data, dict):
            filename = file_data.get("display_name", item_title)
            dl_url = file_data.get("url")
            if dl_url:
                dest = files_dir / filename
                if download_file(dl_url, dest):
                    print(f"      Downloaded: {filename}")
                    # Write a reference md file
                    fname = clean_item_filename(item_title, mod_name) + ".md"
                    write_text(mod_dir / fname, f"# {item_title}\n\nFile: `files/{filename}`\n")
        return

    if item_type == "ExternalUrl":
        url = item.get("external_url", "")
        fname = clean_item_filename(item_title, mod_name) + ".md"
        write_text(mod_dir / fname, f"# {item_title}\n\n**URL:** {url}\n")
        return

    if item_type == "ExternalTool":
        url = item.get("external_url", "")
        fname = clean_item_filename(item_title, mod_name) + ".md"
        content = f"# {item_title}\n\n**External Tool**\n"
        if url:
            content += f"**URL:** {url}\n"
        write_text(mod_dir / fname, content)
        return


# ---------------------------------------------------------------------------
# Export: modules
# ---------------------------------------------------------------------------

def export_modules(course_id: int, course_dir: Path, grades: GradeRecord,
                   exported_ids: set, readme: List[str]) -> None:
    print("  Fetching modules...")
    modules = api_get(f"courses/{course_id}/modules")
    if not modules:
        return

    add_line(readme, "## Modules")
    add_line(readme)

    for mod in modules:
        mod_name = mod["name"]
        mod_id = mod["id"]
        folder_name = normalize_module_name(mod_name)

        add_line(readme, f"### {mod_name}")
        print(f"    Module: {mod_name} -> {folder_name}/")

        mod_dir = course_dir / folder_name
        mod_dir.mkdir(exist_ok=True)

        items = api_get(f"courses/{course_id}/modules/{mod_id}/items")
        if items:
            for item in items:
                item_title = item.get("title", "Untitled")
                item_type = item.get("type", "Unknown")
                fname = clean_item_filename(item_title, mod_name)
                add_line(readme, f"- [{item_type}] [{item_title}](./{folder_name}/{fname}.md)")
                export_module_item(course_id, mod_dir, item, grades, exported_ids)

        add_line(readme)


# ---------------------------------------------------------------------------
# Export: orphan assignments (not in any module)
# ---------------------------------------------------------------------------

def export_orphans(course_id: int, course_dir: Path, grades: GradeRecord,
                   exported_ids: set) -> int:
    """Fetch all assignments and export any not already covered by modules."""
    print("  Checking for orphan assignments...")
    all_assignments = api_get(f"courses/{course_id}/assignments")
    if not all_assignments:
        return 0

    orphans = [a for a in all_assignments if a["id"] not in exported_ids]
    if not orphans:
        print("    No orphan assignments found.")
        return 0

    print(f"    Found {len(orphans)} orphan assignments")
    misc_dir = course_dir / "misc"
    misc_dir.mkdir(exist_ok=True)

    for assignment in orphans:
        a_name = assignment.get("name", "Untitled")
        a_id = assignment["id"]
        pts = assignment.get("points_possible")
        due_at = assignment.get("due_at", "")

        a_text = [f"# {a_name}", ""]
        if due_at:
            add_line(a_text, f"**Due:** {due_at}")
        if pts:
            add_line(a_text, f"**Points Possible:** {pts}")
        if assignment.get("submission_types"):
            add_line(a_text, f"**Submission Types:** {', '.join(assignment['submission_types'])}")
        if assignment.get("description"):
            add_line(a_text)
            add_line(a_text, "## Instructions")
            add_line(a_text)
            add_line(a_text, html_to_text(assignment["description"]))

        # Fetch submission
        sub = api_get(
            f"courses/{course_id}/assignments/{a_id}/submissions/self",
            {"include[]": "submission_comments"},
        )
        score = None
        if isinstance(sub, dict):
            score = sub.get("score")
            if sub.get("submitted_at") or score is not None:
                add_line(a_text)
                add_line(a_text, "---")
                add_line(a_text)
                add_line(a_text, "## My Submission")
                add_line(a_text)
                if score is not None:
                    add_line(a_text, f"**Score:** {score}/{pts}")
                    if sub.get("grade"):
                        add_line(a_text, f"**Grade:** {sub['grade']}")
                if sub.get("submitted_at"):
                    add_line(a_text, f"**Submitted:** {sub['submitted_at']}")
                    if sub.get("late"):
                        add_line(a_text, "**Late:** Yes")
                if sub.get("body"):
                    add_line(a_text)
                    add_line(a_text, html_to_text(sub["body"]))

                if sub.get("attachments"):
                    add_line(a_text)
                    add_line(a_text, "### Submitted Files")
                    add_line(a_text)
                    files_dir = misc_dir / "files"
                    for att in sub["attachments"]:
                        display = att.get("display_name", att.get("filename", "file"))
                        add_line(a_text, f"- **{display}**")
                        dl_url = att.get("url")
                        if dl_url:
                            dest = files_dir / display
                            if download_file(dl_url, dest):
                                add_line(a_text, f"  - Downloaded: `files/{display}`")

                if sub.get("submission_comments"):
                    add_line(a_text)
                    add_line(a_text, "### Instructor Feedback")
                    add_line(a_text)
                    for comment in sub["submission_comments"]:
                        author = comment.get("author_name", "Unknown")
                        created = comment.get("created_at", "")
                        add_line(a_text, f"**{author}** ({created}):")
                        add_line(a_text)
                        add_line(a_text, f"> {comment.get('comment', '')}")
                        add_line(a_text)

        grades.add(a_name, score, pts, due_at, a_id)

        fname = safe_filename(a_name) + ".md"
        write_text(misc_dir / fname, "\n".join(a_text).strip() + "\n")

    return len(orphans)


# ---------------------------------------------------------------------------
# Export: single course
# ---------------------------------------------------------------------------

def export_course(course: dict) -> Optional[Dict[str, Any]]:
    """Export a single course. Returns course summary dict for master index."""
    course_id = course["id"]
    course_name = course.get("name", f"course_{course_id}")
    course_code = course.get("course_code", "")

    # Parse semester from the full name (contains section code with term info)
    year, term = parse_semester(course_name, course.get("start_at", ""))
    semester_folder = f"{year}_{term}"

    # Clean course folder name
    folder_name = clean_course_name(course_name.split()[0] if " " in course_name else course_code, course_name)

    course_dir = OUTPUT_DIR / semester_folder / folder_name
    course_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'=' * 60}")
    print(f"COURSE: {course_name} ({course_code})")
    print(f"  -> {semester_folder}/{folder_name}/")
    print(f"{'=' * 60}")

    # Initialize grade tracking
    grades = GradeRecord()
    exported_ids: set = set()  # track assignment IDs covered by modules

    # Build README
    readme: List[str] = []
    add_line(readme, f"# {course_name}")
    add_line(readme)
    add_line(readme, f"- **Code:** {course_code}")
    add_line(readme, f"- **ID:** {course_id}")
    add_line(readme, f"- **Semester:** {year} {term.replace('_', ' ').title()}")
    if course.get("start_at"):
        add_line(readme, f"- **Start:** {course['start_at']}")
    if course.get("end_at"):
        add_line(readme, f"- **End:** {course['end_at']}")
    add_line(readme)

    # Export components
    fetch_syllabus(course_id, course_name, course_dir)
    export_modules(course_id, course_dir, grades, exported_ids, readme)
    orphan_count = export_orphans(course_id, course_dir, grades, exported_ids)
    if orphan_count:
        add_line(readme, f"## Miscellaneous ({orphan_count} orphan assignments)")
        add_line(readme, f"See [misc/](./misc/) for assignments not in any module.")
        add_line(readme)
    export_announcements(course_id, course_name, course_dir)

    # Write grades.md
    grades_content = grades.generate_grades_md(course_name)
    write_text(course_dir / "grades.md", grades_content)
    print("  Grades summary saved.")

    # Write README.md
    write_text(course_dir / "README.md", "\n".join(readme).strip() + "\n")
    print(f"  -> Saved to {course_dir}/")

    # Return summary for master index
    totals = grades.get_totals()
    base_code_m = re.match(r'([A-Z]{2,4}\d{3}[A-Z]?)', course_code)
    base_code = base_code_m.group(1) if base_code_m else course_code

    return {
        "name": course_name,
        "code": course_code,
        "base_code": base_code,
        "folder": f"{semester_folder}/{folder_name}",
        "semester_folder": semester_folder,
        "year": year,
        "term": term,
        "grade_pct": totals["pct"],
        "grade_letter": totals["letter"],
        "earned": totals["earned"],
        "possible": totals["possible"],
        "count": totals["count"],
    }


# ---------------------------------------------------------------------------
# Master index and grades files
# ---------------------------------------------------------------------------

def build_master_index(summaries: List[Dict[str, Any]]) -> str:
    lines = ["# Canvas Course Archive - Master Index", ""]
    lines.append(f"Total courses: {len(summaries)}")
    lines.append("")

    # By semester
    lines.append("## Courses by Semester")
    lines.append("")

    semesters: Dict[str, List[Dict[str, Any]]] = {}
    for s in summaries:
        key = s["semester_folder"]
        if key not in semesters:
            semesters[key] = []
        semesters[key].append(s)

    for sem in sorted(semesters.keys()):
        courses = semesters[sem]
        sem_display = sem.replace("_", " ").title()
        lines.append(f"### {sem_display}")
        lines.append("")
        lines.append("| Course | Grade | Folder |")
        lines.append("|--------|------:|--------|")
        for c in sorted(courses, key=lambda x: x["base_code"]):
            lines.append(f"| {c['name']} | {c['grade_letter']} ({c['grade_pct']:.0f}%) | [{c['base_code']}](./{c['folder']}/README.md) |")
        lines.append("")

    # By department
    lines.append("## Courses by Department")
    lines.append("")

    departments: Dict[str, List[Dict[str, Any]]] = {}
    for s in summaries:
        dept = re.match(r'([A-Z]+)', s["base_code"])
        dept_code = dept.group(1) if dept else "OTHER"
        if dept_code not in departments:
            departments[dept_code] = []
        departments[dept_code].append(s)

    for dept in sorted(departments.keys()):
        courses = departments[dept]
        lines.append(f"### {dept}")
        lines.append("")
        for c in sorted(courses, key=lambda x: x["base_code"]):
            sem = c["year"] + " " + c["term"].replace("_", " ").title()
            lines.append(f"- [{c['base_code']}](./{c['folder']}/README.md) - {c['name']} ({sem}) [{c['grade_letter']}]")
        lines.append("")

    return "\n".join(lines) + "\n"


def build_master_grades(summaries: List[Dict[str, Any]]) -> str:
    lines = ["# Master Grades Dashboard", ""]

    if not summaries:
        lines.append("No course data.")
        return "\n".join(lines) + "\n"

    # Overall stats
    total_earned = sum(s["earned"] for s in summaries)
    total_possible = sum(s["possible"] for s in summaries)
    overall_pct = (total_earned / total_possible * 100) if total_possible > 0 else 0

    # GPA calculation
    valid = [s for s in summaries if s["count"] > 0]
    if valid:
        gpa = sum(gpa_value(s["grade_letter"]) for s in valid) / len(valid)
    else:
        gpa = 0.0

    lines.append("## Overall")
    lines.append("")
    lines.append(f"- **Courses:** {len(summaries)}")
    lines.append(f"- **Graded Courses:** {len(valid)}")
    lines.append(f"- **Total Points:** {total_earned:.0f} / {total_possible:.0f}")
    lines.append(f"- **Overall Percentage:** {overall_pct:.1f}%")
    lines.append(f"- **Estimated GPA:** {gpa:.2f}")
    lines.append("")

    # Per-semester averages
    lines.append("## By Semester")
    lines.append("")
    lines.append("| Semester | Courses | Avg Grade | Semester GPA |")
    lines.append("|----------|--------:|----------:|------------:|")

    semesters: Dict[str, List[Dict[str, Any]]] = {}
    for s in summaries:
        key = s["semester_folder"]
        if key not in semesters:
            semesters[key] = []
        semesters[key].append(s)

    for sem in sorted(semesters.keys()):
        courses = semesters[sem]
        sem_valid = [c for c in courses if c["count"] > 0]
        if sem_valid:
            sem_pct = sum(c["grade_pct"] for c in sem_valid) / len(sem_valid)
            sem_gpa = sum(gpa_value(c["grade_letter"]) for c in sem_valid) / len(sem_valid)
        else:
            sem_pct = 0
            sem_gpa = 0
        sem_display = sem.replace("_", " ").title()
        lines.append(f"| {sem_display} | {len(courses)} | {sem_pct:.1f}% | {sem_gpa:.2f} |")
    lines.append("")

    # All courses table
    lines.append("## All Courses")
    lines.append("")
    lines.append("| Course | Semester | Earned | Possible | Pct | Grade |")
    lines.append("|--------|----------|-------:|---------:|----:|------:|")
    for s in sorted(summaries, key=lambda x: (x["year"], x["term"], x["base_code"])):
        sem = s["year"] + " " + s["term"].replace("_", " ").title()
        lines.append(f"| {s['base_code']} {s['name'][:40]} | {sem} | {s['earned']:.0f} | {s['possible']:.0f} | {s['grade_pct']:.1f}% | {s['grade_letter']} |")

    lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI + main
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export Canvas LMS course data to organized offline archive."
    )
    parser.add_argument(
        "--course",
        help="Course name substring or exact ID to export only that course.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip courses that already have a README.md.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        dest="list_only",
        help="List all courses without exporting.",
    )
    return parser.parse_args()


def fetch_all_courses() -> List[dict]:
    """Fetch both completed and active courses, deduplicate by ID."""
    print("Fetching course list (completed + active)...")
    completed = api_get("courses", {"enrollment_state": "completed"})
    active = api_get("courses", {"enrollment_state": "active"})

    seen: set = set()
    courses: List[dict] = []
    for c in (completed or []) + (active or []):
        if not isinstance(c, dict):
            continue
        cid = c.get("id")
        if cid and cid not in seen:
            seen.add(cid)
            courses.append(c)

    return courses


def filter_courses(courses: List[dict], selector: Optional[str]) -> List[dict]:
    if not selector:
        return courses
    selector_lower = selector.lower()
    filtered: List[dict] = []
    for course in courses:
        course_id = str(course.get("id", ""))
        course_name = course.get("name", "").lower()
        course_code = course.get("course_code", "").lower()
        if (selector == course_id
                or selector_lower in course_name
                or selector_lower in course_code):
            filtered.append(course)
    return filtered


def course_already_done(course: dict) -> bool:
    """Check if a course already has a README.md (for --resume)."""
    name = course.get("name", "")
    year, term = parse_semester(name, course.get("start_at", ""))
    section_code = name.split()[0] if " " in name else course.get("course_code", "")
    folder_name = clean_course_name(section_code, name)
    readme = OUTPUT_DIR / f"{year}_{term}" / folder_name / "README.md"
    return readme.exists()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    args = parse_args()

    courses = fetch_all_courses()
    if not courses:
        print("No courses found!")
        sys.exit(1)

    # Apply filter
    courses = filter_courses(courses, args.course)
    if not courses:
        print("No matching courses found for the provided filter.")
        sys.exit(1)

    # List mode
    if args.list_only:
        print(f"\nFound {len(courses)} courses:\n")
        for idx, course in enumerate(courses, start=1):
            code = course.get("course_code", "")
            name = course.get("name", "")
            year, term = parse_semester(name, course.get("start_at", ""))
            done = " [DONE]" if course_already_done(course) else ""
            print(f"  {idx:3d}. [{course['id']}] {code} - {name} ({year} {term}){done}")
        return

    # Resume mode: filter out already-done courses
    if args.resume:
        before = len(courses)
        courses = [c for c in courses if not course_already_done(c)]
        skipped = before - len(courses)
        if skipped:
            print(f"Resuming: skipping {skipped} already-exported courses.")
        if not courses:
            print("All courses already exported!")
            return

    total = len(courses)
    print(f"\nExporting {total} courses:")

    # Export
    summaries: List[Dict[str, Any]] = []
    for idx, course in enumerate(courses, start=1):
        try:
            print(f"\n[{idx}/{total}]", end="")
            result = export_course(course)
            if result:
                summaries.append(result)
        except Exception as exc:
            print(f"  [Error exporting {course.get('name', '?')}]: {exc}")
            import traceback
            traceback.print_exc()

    # Build master files
    if summaries:
        print("\nBuilding master index...")
        write_text(OUTPUT_DIR / "INDEX.md", build_master_index(summaries))
        print("Building master grades dashboard...")
        write_text(OUTPUT_DIR / "GRADES.md", build_master_grades(summaries))

    print(f"\n{'=' * 60}")
    print(f"Export complete! {len(summaries)}/{total} courses exported.")
    print(f"Files saved to: {OUTPUT_DIR}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
