#!/usr/bin/env python3
"""Generic Canvas LMS course exporter.

Exports Canvas courses to a local Markdown archive with modules, assignments,
submissions, grades, announcements, syllabus content, and downloaded files.

Configuration is intentionally CLI/env driven so the script can be reused with
any Canvas instance, not just one school or one local folder layout.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple


DEFAULT_OUTPUT_DIR = Path("canvas_export")
DEFAULT_CONFIG_PATH = Path("config.json")
DEFAULT_TOKEN_ENV = "CANVAS_TOKEN"
DEFAULT_BASE_DELAY = 0.3
DEFAULT_MAX_RETRIES = 3


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ExportConfig:
    api_base: str
    output_dir: Path
    token: str
    base_delay: float = DEFAULT_BASE_DELAY
    max_retries: int = DEFAULT_MAX_RETRIES
    include_submissions: bool = True
    download_files: bool = True
    group_by: str = "term"


def load_json_config(config_path: Path) -> Dict[str, Any]:
    """Load optional JSON config for Canvas connection settings."""
    if config_path.exists():
        with config_path.open(encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
        raise SystemExit(f"Config file must contain a JSON object: {config_path}")
    return {}


def load_token(config: Dict[str, Any], config_path: Path, token_env: str) -> str:
    """Load a Canvas API token from config JSON or an environment variable."""
    for key in ("canvas_token", "token", "access_token"):
        token = str(config.get(key, "")).strip()
        if token:
            return token

    token = os.environ.get(token_env, "").strip()
    if token:
        return token

    raise SystemExit(
        f"No API token found. Set {token_env} or add canvas_token to {config_path}."
    )


def load_canvas_url(config: Dict[str, Any], config_path: Path) -> str:
    """Load the Canvas base URL from config JSON."""
    for key in ("canvas_url", "canvas_base_url", "base_url"):
        value = str(config.get(key, "")).strip()
        if value:
            return value

    raise SystemExit(
        f"No Canvas URL found. Add canvas_url to {config_path}, "
        "for example https://canvas.example.edu."
    )


def normalize_api_base(value: str) -> str:
    """Accept either a Canvas root URL or a full /api/v1 URL."""
    base = value.rstrip("/")
    if base.endswith("/api/v1"):
        return base
    return f"{base}/api/v1"


# ---------------------------------------------------------------------------
# Text and filename helpers
# ---------------------------------------------------------------------------


class HTMLToText(HTMLParser):
    """Small dependency-free HTML to plain text converter."""

    BLOCK_TAGS = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr"}
    ENDLINE_TAGS = BLOCK_TAGS | {"table"}
    SKIP_TAGS = {"script", "style"}

    def __init__(self) -> None:
        super().__init__()
        self._text: List[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag in self.SKIP_TAGS:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag == "br":
            self._text.append("\n")
        elif tag in self.BLOCK_TAGS:
            self._text.append("\n")
        elif tag == "a":
            href = next((val for name, val in attrs if name == "href"), None)
            if href:
                self._text.append(f" [link: {href}] ")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if self._skip_depth:
            return
        if tag in self.ENDLINE_TAGS:
            self._text.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self._text.append(data)

    def get_text(self) -> str:
        text = "".join(self._text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def html_to_text(html: Optional[str]) -> str:
    if not html:
        return ""
    parser = HTMLToText()
    parser.feed(html)
    return parser.get_text()


def slugify(value: str, max_len: int = 80, lower: bool = False) -> str:
    value = html_to_text(value)
    value = re.sub(r"[^\w\s.-]", "", value, flags=re.UNICODE).strip()
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"_+", "_", value)
    if lower:
        value = value.lower()
    return value[:max_len].strip("._-") or "untitled"


def module_folder_name(name: str) -> str:
    match = re.match(r"(unit|week|module)\s*(\d+)", name.strip(), re.IGNORECASE)
    if match:
        return f"{match.group(1).lower()}_{int(match.group(2)):02d}"
    return slugify(name, max_len=60, lower=True)


def item_filename(title: str) -> str:
    cleaned = re.sub(
        r"^(unit|week|module)\s*\d+\s*[-:.]?\s*",
        "",
        title.strip(),
        flags=re.IGNORECASE,
    )
    return slugify(cleaned, max_len=80, lower=True) + ".md"


def course_folder_name(course: Dict[str, Any]) -> str:
    code = str(course.get("course_code") or "").strip()
    name = str(course.get("name") or f"course_{course.get('id', 'unknown')}").strip()

    if code and name.lower().startswith(code.lower()):
        title = name[len(code):].strip(" -:_")
        if title:
            return f"{slugify(code, 35)}_{slugify(title, 70)}"
    if code:
        return slugify(code, 90)
    return slugify(name, 90)


def infer_year_month(date_value: str) -> str:
    match = re.match(r"(\d{4})-(\d{2})", date_value or "")
    if match:
        return f"{match.group(1)}_{match.group(2)}"
    return "unknown_date"


def term_folder_name(course: Dict[str, Any], group_by: str) -> str:
    if group_by == "none":
        return ""

    term = course.get("term")
    if group_by == "term" and isinstance(term, dict):
        name = str(term.get("name") or "").strip()
        if name:
            return slugify(name, max_len=70, lower=True)

    if group_by in {"term", "date"}:
        return infer_year_month(str(course.get("start_at") or course.get("created_at") or ""))

    return "courses"


def add_line(lines: List[str], line: str = "") -> None:
    lines.append(line)


def markdown_doc(title: str) -> List[str]:
    return [f"# {title}", ""]


def markdown_table_cell(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


# ---------------------------------------------------------------------------
# Canvas API client
# ---------------------------------------------------------------------------


class CanvasClient:
    def __init__(self, config: ExportConfig) -> None:
        self.config = config
        self.headers = {"Authorization": f"Bearer {config.token}"}

    def build_url(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> str:
        endpoint = endpoint.lstrip("/")
        url = f"{self.config.api_base}/{endpoint}"
        query: Dict[str, Any] = {"per_page": 100}
        if params:
            query.update(params)
        return f"{url}?{urllib.parse.urlencode(query, doseq=True)}"

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """GET from Canvas API, following pagination for list responses."""
        url = self.build_url(endpoint, params)
        results: List[dict] = []

        while url:
            data = None
            for attempt in range(self.config.max_retries):
                req = urllib.request.Request(url, headers=self.headers)
                try:
                    with urllib.request.urlopen(req, timeout=30) as resp:
                        raw = resp.read().decode("utf-8")
                        data = json.loads(raw) if raw else None
                        if not isinstance(data, list):
                            return data

                        results.extend(data)
                        url = self._next_page(resp.getheader("Link", ""))
                        break
                except urllib.error.HTTPError as exc:
                    if exc.code == 429:
                        retry_after = int(exc.headers.get("Retry-After", 5))
                        print(f"  [rate limited] waiting {retry_after}s")
                        time.sleep(retry_after)
                        continue
                    if attempt < self.config.max_retries - 1:
                        delay = self.config.base_delay * (2 ** attempt)
                        print(f"  [api {exc.code}] {endpoint}; retry in {delay:.1f}s")
                        time.sleep(delay)
                        continue
                    print(f"  [api {exc.code}] {endpoint}; giving up")
                    return results if results else []
                except Exception as exc:
                    if attempt < self.config.max_retries - 1:
                        delay = self.config.base_delay * (2 ** attempt)
                        print(f"  [error] {endpoint}: {exc}; retry in {delay:.1f}s")
                        time.sleep(delay)
                        continue
                    print(f"  [error] {endpoint}: {exc}; giving up")
                    return results if results else []

            time.sleep(self.config.base_delay)

        return results

    @staticmethod
    def _next_page(link_header: str) -> Optional[str]:
        for part in link_header.split(","):
            if 'rel="next"' in part:
                match = re.search(r"<([^>]+)>", part)
                if match:
                    return match.group(1)
        return None

    def download(self, url: str, dest_path: Path) -> bool:
        if dest_path.exists():
            return True

        dest_path.parent.mkdir(parents=True, exist_ok=True)
        for attempt in range(self.config.max_retries):
            req = urllib.request.Request(url, headers=self.headers)
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    with dest_path.open("wb") as f:
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
                if attempt < self.config.max_retries - 1:
                    time.sleep(self.config.base_delay * (2 ** attempt))
                    continue
                print(f"    [download {exc.code}] {dest_path.name}")
                return False
            except Exception as exc:
                if attempt < self.config.max_retries - 1:
                    time.sleep(self.config.base_delay * (2 ** attempt))
                    continue
                print(f"    [download error] {dest_path.name}: {exc}")
                return False

        return False


# ---------------------------------------------------------------------------
# Grades
# ---------------------------------------------------------------------------


def categorize_assignment(name: str) -> str:
    lower = name.lower()
    category_rules = [
        ("Discussion", ("discussion",)),
        ("Quiz", ("quiz",)),
        ("Exam", ("exam", "midterm", "final")),
        ("Homework", ("homework", "hw")),
        ("Lab", ("experiment", "lab")),
        ("Project", ("project", "capstone")),
        ("Paper", ("paper", "essay", "report")),
    ]
    for category, needles in category_rules:
        if any(needle in lower for needle in needles):
            return category
    return "Other"


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


class GradeBook:
    def __init__(self) -> None:
        self.entries: List[Dict[str, Any]] = []

    def add(
        self,
        name: str,
        score: Optional[float],
        points_possible: Optional[float],
        due_date: str = "",
        assignment_id: Optional[int] = None,
    ) -> None:
        self.entries.append(
            {
                "name": name,
                "category": categorize_assignment(name),
                "score": score,
                "points_possible": points_possible,
                "due_date": due_date,
                "assignment_id": assignment_id,
            }
        )

    def totals(self) -> Dict[str, Any]:
        earned = 0.0
        possible = 0.0
        count = 0
        for entry in self.entries:
            if entry["score"] is not None and entry["points_possible"]:
                earned += float(entry["score"])
                possible += float(entry["points_possible"])
                count += 1
        pct = (earned / possible * 100) if possible else 0.0
        return {
            "earned": earned,
            "possible": possible,
            "pct": pct,
            "letter": pct_to_letter(pct),
            "count": count,
        }

    def to_markdown(self, course_name: str) -> str:
        lines = [f"# Grades - {course_name}", ""]
        if not self.entries:
            lines.append("No graded assignments found.")
            return "\n".join(lines) + "\n"

        by_category: Dict[str, Dict[str, float]] = {}
        for entry in self.entries:
            category = entry["category"]
            by_category.setdefault(category, {"earned": 0.0, "possible": 0.0, "count": 0.0})
            if entry["score"] is not None and entry["points_possible"]:
                by_category[category]["earned"] += float(entry["score"])
                by_category[category]["possible"] += float(entry["points_possible"])
                by_category[category]["count"] += 1

        lines.extend(
            [
                "## Summary by Category",
                "",
                "| Category | Earned | Possible | Pct | Count |",
                "|----------|-------:|---------:|----:|------:|",
            ]
        )

        for category in sorted(by_category):
            data = by_category[category]
            pct = (data["earned"] / data["possible"] * 100) if data["possible"] else 0
            lines.append(
                f"| {category} | {data['earned']:.1f} | {data['possible']:.1f} | "
                f"{pct:.1f}% | {int(data['count'])} |"
            )

        totals = self.totals()
        lines.extend(
            [
                f"| **Total** | **{totals['earned']:.1f}** | **{totals['possible']:.1f}** | "
                f"**{totals['pct']:.1f}%** | **{totals['count']}** |",
                "",
                f"**Estimated Grade:** {totals['letter']} ({totals['pct']:.1f}%)",
                "",
                "## Assignments",
                "",
                "| Assignment | Category | Score | Possible | Due |",
                "|------------|----------|------:|---------:|-----|",
            ]
        )

        for entry in self.entries:
            score = f"{entry['score']:.1f}" if entry["score"] is not None else "-"
            possible = f"{entry['points_possible']:.1f}" if entry["points_possible"] else "-"
            due = str(entry["due_date"] or "")[:10]
            lines.append(
                f"| {markdown_table_cell(entry['name'])} | {entry['category']} | "
                f"{score} | {possible} | {due} |"
            )

        return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Exporter
# ---------------------------------------------------------------------------


class CourseExporter:
    def __init__(self, client: CanvasClient, config: ExportConfig) -> None:
        self.client = client
        self.config = config

    def write_text(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_lines(self, path: Path, lines: List[str]) -> None:
        self.write_text(path, "\n".join(lines).strip() + "\n")

    def course_dir(self, course: Dict[str, Any]) -> Path:
        group_folder = term_folder_name(course, self.config.group_by)
        if group_folder:
            return self.config.output_dir / group_folder / course_folder_name(course)
        return self.config.output_dir / course_folder_name(course)

    def course_done(self, course: Dict[str, Any]) -> bool:
        return (self.course_dir(course) / "README.md").exists()

    def export_course(self, course: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        course_id = course["id"]
        course_name = str(course.get("name") or f"course_{course_id}")
        course_code = str(course.get("course_code") or "")
        course_dir = self.course_dir(course)
        course_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'=' * 60}")
        print(f"COURSE: {course_name} ({course_code or course_id})")
        print(f"  -> {course_dir.relative_to(self.config.output_dir)}")
        print(f"{'=' * 60}")

        grades = GradeBook()
        exported_assignment_ids: Set[int] = set()
        readme = markdown_doc(course_name)
        add_line(readme, f"- **Canvas ID:** {course_id}")
        if course_code:
            add_line(readme, f"- **Code:** {course_code}")
        if isinstance(course.get("term"), dict) and course["term"].get("name"):
            add_line(readme, f"- **Term:** {course['term']['name']}")
        if course.get("start_at"):
            add_line(readme, f"- **Start:** {course['start_at']}")
        if course.get("end_at"):
            add_line(readme, f"- **End:** {course['end_at']}")
        add_line(readme)

        self.export_syllabus(course_id, course_name, course_dir)
        self.export_modules(course_id, course_dir, grades, exported_assignment_ids, readme)
        orphan_count = self.export_orphan_assignments(course_id, course_dir, grades, exported_assignment_ids)
        if orphan_count:
            add_line(readme, f"## Miscellaneous Assignments")
            add_line(readme)
            add_line(readme, f"{orphan_count} assignments were not attached to a module.")
            add_line(readme, "See [misc/](./misc/).")
            add_line(readme)
        self.export_announcements(course_id, course_name, course_dir)

        self.write_text(course_dir / "grades.md", grades.to_markdown(course_name))
        self.write_lines(course_dir / "README.md", readme)

        totals = grades.totals()
        return {
            "name": course_name,
            "code": course_code,
            "id": course_id,
            "folder": str(course_dir.relative_to(self.config.output_dir)),
            "group": term_folder_name(course, self.config.group_by) or "courses",
            "earned": totals["earned"],
            "possible": totals["possible"],
            "grade_pct": totals["pct"],
            "grade_letter": totals["letter"],
            "graded_count": totals["count"],
        }

    def export_syllabus(self, course_id: int, course_name: str, course_dir: Path) -> None:
        print("  Fetching syllabus...")
        detail = self.client.get(f"courses/{course_id}", {"include[]": ["syllabus_body"]})
        if isinstance(detail, dict) and detail.get("syllabus_body"):
            self.write_text(
                course_dir / "syllabus.md",
                f"# Syllabus - {course_name}\n\n{html_to_text(detail['syllabus_body'])}\n",
            )

    def export_announcements(self, course_id: int, course_name: str, course_dir: Path) -> None:
        print("  Fetching announcements...")
        announcements = self.client.get(
            f"courses/{course_id}/discussion_topics",
            {"only_announcements": "true"},
        )
        if not announcements:
            return

        lines = markdown_doc(f"Announcements - {course_name}")
        for announcement in announcements:
            title = announcement.get("title", "Untitled")
            add_line(lines, f"## {title}")
            if announcement.get("posted_at"):
                add_line(lines, f"*Posted: {announcement['posted_at']}*")
                add_line(lines)
            if announcement.get("message"):
                add_line(lines, html_to_text(announcement["message"]))
                add_line(lines)
            add_line(lines, "---")
            add_line(lines)

        self.write_lines(course_dir / "announcements.md", lines)

    def export_modules(
        self,
        course_id: int,
        course_dir: Path,
        grades: GradeBook,
        exported_assignment_ids: Set[int],
        readme: List[str],
    ) -> None:
        print("  Fetching modules...")
        modules = self.client.get(f"courses/{course_id}/modules")
        if not modules:
            return

        add_line(readme, "## Modules")
        add_line(readme)
        for module in modules:
            mod_name = module.get("name", "Untitled Module")
            mod_id = module["id"]
            folder = module_folder_name(mod_name)
            mod_dir = course_dir / folder
            mod_dir.mkdir(exist_ok=True)

            print(f"    Module: {mod_name} -> {folder}/")
            add_line(readme, f"### {mod_name}")

            items = self.client.get(f"courses/{course_id}/modules/{mod_id}/items")
            if items:
                for item in items:
                    title = item.get("title", "Untitled")
                    item_type = item.get("type", "Unknown")
                    filename = item_filename(title)
                    add_line(readme, f"- [{item_type}] [{title}](./{folder}/{filename})")
                    self.export_module_item(course_id, mod_dir, item, grades, exported_assignment_ids)
            add_line(readme)

    def export_module_item(
        self,
        course_id: int,
        mod_dir: Path,
        item: Dict[str, Any],
        grades: GradeBook,
        exported_assignment_ids: Set[int],
    ) -> None:
        title = item.get("title", "Untitled")
        item_type = item.get("type", "Unknown")

        if item_type == "Page" and item.get("page_url"):
            page = self.client.get(f"courses/{course_id}/pages/{item['page_url']}")
            if isinstance(page, dict) and page.get("body"):
                self.write_text(mod_dir / item_filename(title), f"# {title}\n\n{html_to_text(page['body'])}\n")
            return

        if item_type == "Assignment" and item.get("content_id"):
            assignment_id = int(item["content_id"])
            exported_assignment_ids.add(assignment_id)
            assignment = self.client.get(f"courses/{course_id}/assignments/{assignment_id}")
            if isinstance(assignment, dict):
                self.export_assignment(course_id, mod_dir, assignment, title, grades)
            return

        if item_type == "Discussion" and item.get("content_id"):
            self.export_discussion(course_id, mod_dir, item, grades, exported_assignment_ids)
            return

        if item_type == "Quiz" and item.get("content_id"):
            self.export_quiz(course_id, mod_dir, item, grades, exported_assignment_ids)
            return

        if item_type == "File":
            self.export_file(course_id, mod_dir, item)
            return

        if item_type in {"ExternalUrl", "ExternalTool"}:
            url = item.get("external_url", "")
            label = "External Tool" if item_type == "ExternalTool" else "External URL"
            content = f"# {title}\n\n**{label}**\n"
            if url:
                content += f"\n**URL:** {url}\n"
            self.write_text(mod_dir / item_filename(title), content)

    def add_assignment_metadata(
        self,
        lines: List[str],
        due_at: str,
        points: Optional[float],
        submission_types: Optional[Sequence[str]] = None,
        points_label: str = "Points Possible",
    ) -> None:
        if due_at:
            add_line(lines, f"**Due:** {due_at}")
        if points is not None:
            add_line(lines, f"**{points_label}:** {points}")
        if submission_types:
            add_line(lines, f"**Submission Types:** {', '.join(submission_types)}")

    def fetch_submission(self, course_id: int, assignment_id: int) -> Optional[Dict[str, Any]]:
        if not self.config.include_submissions:
            return None
        submission = self.client.get(
            f"courses/{course_id}/assignments/{assignment_id}/submissions/self",
            {"include[]": ["submission_comments"]},
        )
        return submission if isinstance(submission, dict) else None

    def add_text_section(self, lines: List[str], heading: str, html: Optional[str]) -> None:
        text = html_to_text(html)
        if not text:
            return
        add_line(lines)
        add_line(lines, heading)
        add_line(lines)
        add_line(lines, text)

    def export_assignment(
        self,
        course_id: int,
        folder: Path,
        assignment: Dict[str, Any],
        title_override: Optional[str],
        grades: GradeBook,
    ) -> None:
        assignment_id = assignment["id"]
        title = title_override or assignment.get("name", "Untitled")
        due_at = assignment.get("due_at", "")
        points = assignment.get("points_possible")

        lines = markdown_doc(title)
        self.add_assignment_metadata(
            lines,
            due_at,
            points,
            assignment.get("submission_types"),
        )
        self.add_text_section(lines, "## Instructions", assignment.get("description"))

        score = self.add_submission(course_id, assignment_id, folder, lines, points)
        grades.add(title, score, points, due_at, assignment_id)
        self.write_lines(folder / item_filename(title), lines)

    def add_submission(
        self,
        course_id: int,
        assignment_id: int,
        folder: Path,
        lines: List[str],
        points: Optional[float],
    ) -> Optional[float]:
        submission = self.fetch_submission(course_id, assignment_id)
        if not submission:
            return None

        score = submission.get("score")
        has_content = (
            submission.get("submitted_at")
            or score is not None
            or submission.get("body")
            or submission.get("url")
            or submission.get("attachments")
            or submission.get("submission_comments")
        )
        if not has_content:
            return score

        add_line(lines)
        add_line(lines, "---")
        add_line(lines)
        add_line(lines, "## Submission")
        add_line(lines)
        if score is not None:
            add_line(lines, f"**Score:** {score}/{points if points is not None else '?'}")
            if submission.get("grade"):
                add_line(lines, f"**Grade:** {submission['grade']}")
        if submission.get("submitted_at"):
            add_line(lines, f"**Submitted:** {submission['submitted_at']}")
        if submission.get("late"):
            add_line(lines, "**Late:** Yes")
        if submission.get("body"):
            add_line(lines)
            add_line(lines, html_to_text(submission["body"]))
        if submission.get("url"):
            add_line(lines)
            add_line(lines, f"**URL:** {submission['url']}")

        self.add_attachment_list(folder, lines, submission.get("attachments", []))
        self.add_submission_feedback(submission, lines)

        return score

    def add_attachment_list(
        self,
        folder: Path,
        lines: List[str],
        attachments: Sequence[Dict[str, Any]],
    ) -> None:
        if not attachments:
            return

        add_line(lines)
        add_line(lines, "### Submitted Files")
        add_line(lines)
        files_dir = folder / "files"
        for attachment in attachments:
            display = attachment.get("display_name") or attachment.get("filename") or "file"
            add_line(lines, f"- **{display}**")
            url = attachment.get("url")
            if self.config.download_files and url:
                dest = files_dir / slugify(display, max_len=120)
                if self.client.download(url, dest):
                    add_line(lines, f"  - Downloaded: `files/{dest.name}`")

    def export_discussion(
        self,
        course_id: int,
        folder: Path,
        item: Dict[str, Any],
        grades: GradeBook,
        exported_assignment_ids: Set[int],
    ) -> None:
        title = item.get("title", "Untitled")
        discussion_id = item["content_id"]
        discussion = self.client.get(f"courses/{course_id}/discussion_topics/{discussion_id}")
        if not isinstance(discussion, dict):
            return

        assignment_id = discussion.get("assignment_id")
        if assignment_id:
            exported_assignment_ids.add(int(assignment_id))

        lines = markdown_doc(title)
        if discussion.get("message"):
            add_line(lines, html_to_text(discussion["message"]))

        score = None
        points = discussion.get("points_possible")
        due_at = discussion.get("due_at", "")
        if assignment_id and self.config.include_submissions:
            submission = self.fetch_submission(course_id, int(assignment_id))
            if submission:
                score = submission.get("score")
                if score is not None:
                    add_line(lines)
                    add_line(lines, f"**Score:** {score}/{points if points is not None else '?'}")
                self.add_discussion_entries(course_id, discussion_id, submission, lines)
                self.add_submission_feedback(submission, lines)

        grades.add(title, score, points, due_at, assignment_id)
        self.write_lines(folder / item_filename(title), lines)

    def add_discussion_entries(
        self,
        course_id: int,
        discussion_id: int,
        submission: Dict[str, Any],
        lines: List[str],
    ) -> None:
        user_id = submission.get("user_id")
        if not user_id:
            return
        entries = self.client.get(f"courses/{course_id}/discussion_topics/{discussion_id}/entries")
        if not isinstance(entries, list):
            return
        user_entries = [entry for entry in entries if entry.get("user_id") == user_id]
        if not user_entries:
            return

        add_line(lines)
        add_line(lines, "---")
        add_line(lines)
        add_line(lines, "## Discussion Posts")
        add_line(lines)
        for entry in user_entries:
            add_line(lines, f"**Posted:** {entry.get('created_at', '')}")
            add_line(lines)
            if entry.get("message"):
                add_line(lines, html_to_text(entry["message"]))
                add_line(lines)
            add_line(lines, "---")
            add_line(lines)

    def add_submission_feedback(self, submission: Dict[str, Any], lines: List[str]) -> None:
        if not submission.get("submission_comments"):
            return
        add_line(lines)
        add_line(lines, "### Feedback")
        add_line(lines)
        for comment in submission["submission_comments"]:
            author = comment.get("author_name", "Unknown")
            created = comment.get("created_at", "")
            body = html_to_text(comment.get("comment", ""))
            label = f"**{author}**"
            if created:
                label += f" ({created})"
            add_line(lines, f"{label}:")
            add_line(lines)
            add_line(lines, f"> {body}")
            add_line(lines)

    def export_quiz(
        self,
        course_id: int,
        folder: Path,
        item: Dict[str, Any],
        grades: GradeBook,
        exported_assignment_ids: Set[int],
    ) -> None:
        title = item.get("title", "Untitled")
        quiz = self.client.get(f"courses/{course_id}/quizzes/{item['content_id']}")
        if not isinstance(quiz, dict):
            return

        lines = markdown_doc(title)
        due_at = quiz.get("due_at", "")
        points = quiz.get("points_possible")
        self.add_assignment_metadata(lines, due_at, points, points_label="Points")
        if quiz.get("time_limit"):
            add_line(lines, f"**Time Limit:** {quiz['time_limit']} minutes")
        self.add_text_section(lines, "## Description", quiz.get("description"))

        score = None
        assignment_id = quiz.get("assignment_id")
        if assignment_id:
            exported_assignment_ids.add(int(assignment_id))
            score = self.add_submission(course_id, int(assignment_id), folder, lines, points)

        grades.add(title, score, points, due_at, assignment_id)
        self.write_lines(folder / item_filename(title), lines)

    def export_file(self, course_id: int, folder: Path, item: Dict[str, Any]) -> None:
        title = item.get("title", "Untitled")
        file_data = None
        if item.get("content_id"):
            file_data = self.client.get(f"courses/{course_id}/files/{item['content_id']}")

        filename = title
        url = item.get("url")
        if isinstance(file_data, dict):
            filename = file_data.get("display_name") or file_data.get("filename") or title
            url = file_data.get("url") or url

        lines = markdown_doc(title)
        if self.config.download_files and url:
            dest = folder / "files" / slugify(filename, max_len=120)
            if self.client.download(url, dest):
                add_line(lines, f"File: `files/{dest.name}`")
        elif url:
            add_line(lines, f"File URL: {url}")

        self.write_lines(folder / item_filename(title), lines)

    def export_orphan_assignments(
        self,
        course_id: int,
        course_dir: Path,
        grades: GradeBook,
        exported_assignment_ids: Set[int],
    ) -> int:
        print("  Checking for assignments outside modules...")
        assignments = self.client.get(f"courses/{course_id}/assignments")
        if not assignments:
            return 0

        orphans = [
            assignment
            for assignment in assignments
            if assignment.get("id") not in exported_assignment_ids
        ]
        if not orphans:
            return 0

        misc_dir = course_dir / "misc"
        misc_dir.mkdir(exist_ok=True)
        for assignment in orphans:
            self.export_assignment(course_id, misc_dir, assignment, None, grades)
        return len(orphans)


# ---------------------------------------------------------------------------
# Course discovery and master files
# ---------------------------------------------------------------------------


def fetch_courses(client: CanvasClient, states: Sequence[str]) -> List[Dict[str, Any]]:
    print(f"Fetching courses ({', '.join(states)})...")
    courses: List[Dict[str, Any]] = []
    seen: Set[int] = set()

    for state in states:
        batch = client.get(
            "courses",
            {
                "enrollment_state": state,
                "include[]": ["term"],
            },
        )
        if not isinstance(batch, list):
            continue
        for course in batch:
            if not isinstance(course, dict):
                continue
            course_id = course.get("id")
            if course_id and course_id not in seen:
                seen.add(course_id)
                courses.append(course)

    return courses


def filter_courses(courses: Iterable[Dict[str, Any]], selector: Optional[str]) -> List[Dict[str, Any]]:
    if not selector:
        return list(courses)

    selector_lower = selector.lower()
    selected: List[Dict[str, Any]] = []
    for course in courses:
        course_id = str(course.get("id", ""))
        name = str(course.get("name", "")).lower()
        code = str(course.get("course_code", "")).lower()
        if selector == course_id or selector_lower in name or selector_lower in code:
            selected.append(course)
    return selected


def build_master_index(summaries: List[Dict[str, Any]]) -> str:
    lines = ["# Canvas Course Archive", ""]
    lines.append(f"Total courses exported: {len(summaries)}")
    lines.append("")

    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for summary in summaries:
        grouped.setdefault(summary["group"], []).append(summary)

    for group in sorted(grouped):
        lines.append(f"## {group.replace('_', ' ').title()}")
        lines.append("")
        lines.append("| Course | Grade | Folder |")
        lines.append("|--------|------:|--------|")
        for course in sorted(grouped[group], key=lambda item: (item["code"], item["name"])):
            label = course["code"] or course["name"]
            grade = (
                f"{course['grade_letter']} ({course['grade_pct']:.0f}%)"
                if course["graded_count"]
                else "-"
            )
            lines.append(
                f"| {markdown_table_cell(course['name'])} | {grade} | "
                f"[{markdown_table_cell(label)}](./{course['folder']}/README.md) |"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def build_master_grades(summaries: List[Dict[str, Any]]) -> str:
    lines = ["# Canvas Grades Summary", ""]
    if not summaries:
        lines.append("No courses exported.")
        return "\n".join(lines) + "\n"

    total_earned = sum(summary["earned"] for summary in summaries)
    total_possible = sum(summary["possible"] for summary in summaries)
    overall_pct = (total_earned / total_possible * 100) if total_possible else 0
    graded_courses = [summary for summary in summaries if summary["graded_count"]]

    lines.append(f"- **Courses:** {len(summaries)}")
    lines.append(f"- **Courses with grades:** {len(graded_courses)}")
    lines.append(f"- **Total points:** {total_earned:.1f} / {total_possible:.1f}")
    lines.append(f"- **Overall percentage:** {overall_pct:.1f}%")
    lines.append("")
    lines.append("| Course | Earned | Possible | Pct | Grade |")
    lines.append("|--------|-------:|---------:|----:|------:|")
    for summary in sorted(summaries, key=lambda item: (item["group"], item["code"], item["name"])):
        course = summary["code"] or summary["name"]
        lines.append(
            f"| [{markdown_table_cell(course)}](./{summary['folder']}/README.md) | "
            f"{summary['earned']:.1f} | {summary['possible']:.1f} | "
            f"{summary['grade_pct']:.1f}% | {summary['grade_letter'] if summary['graded_count'] else '-'} |"
        )

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export Canvas LMS course content to a local Markdown archive."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Archive destination directory. Default: {DEFAULT_OUTPUT_DIR}",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help=f"JSON config containing canvas_url and canvas_token. Default: {DEFAULT_CONFIG_PATH}",
    )
    parser.add_argument(
        "--token-env",
        default=DEFAULT_TOKEN_ENV,
        help=f"Environment variable containing the Canvas token. Default: {DEFAULT_TOKEN_ENV}",
    )
    parser.add_argument(
        "--course",
        help="Course ID, code substring, or name substring to export.",
    )
    parser.add_argument(
        "--states",
        nargs="+",
        default=["active", "completed"],
        choices=["active", "completed", "invited", "creation_pending", "deleted"],
        help="Enrollment states to fetch. Default: active completed",
    )
    parser.add_argument(
        "--group-by",
        choices=["term", "date", "none"],
        default="term",
        help="How to group exported course folders. Default: term",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        dest="list_only",
        help="List matching courses without exporting.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Skip courses that already have README.md.",
    )
    parser.add_argument(
        "--no-submissions",
        action="store_true",
        help="Do not fetch submission bodies, comments, scores, or attachments.",
    )
    parser.add_argument(
        "--no-downloads",
        action="store_true",
        help="Do not download files; keep file URLs/references only.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_json = load_json_config(args.config)
    token = load_token(config_json, args.config, args.token_env)
    canvas_url = load_canvas_url(config_json, args.config)
    config = ExportConfig(
        api_base=normalize_api_base(canvas_url),
        output_dir=args.output_dir,
        token=token,
        include_submissions=not args.no_submissions,
        download_files=not args.no_downloads,
        group_by=args.group_by,
    )
    client = CanvasClient(config)
    exporter = CourseExporter(client, config)

    courses = fetch_courses(client, args.states)
    courses = filter_courses(courses, args.course)
    if not courses:
        raise SystemExit("No matching courses found.")

    if args.list_only:
        print(f"\nFound {len(courses)} courses:\n")
        for idx, course in enumerate(courses, start=1):
            code = course.get("course_code", "")
            name = course.get("name", "")
            group = term_folder_name(course, args.group_by)
            done = " [DONE]" if exporter.course_done(course) else ""
            print(f"  {idx:3d}. [{course['id']}] {code} - {name} ({group}){done}")
        return

    if args.resume:
        before = len(courses)
        courses = [course for course in courses if not exporter.course_done(course)]
        skipped = before - len(courses)
        if skipped:
            print(f"Resume: skipping {skipped} already-exported courses.")
        if not courses:
            print("All matching courses already exported.")
            return

    config.output_dir.mkdir(parents=True, exist_ok=True)
    summaries: List[Dict[str, Any]] = []
    total = len(courses)
    print(f"\nExporting {total} course(s).")

    for idx, course in enumerate(courses, start=1):
        try:
            print(f"\n[{idx}/{total}]", end="")
            summary = exporter.export_course(course)
            if summary:
                summaries.append(summary)
        except Exception as exc:
            print(f"  [export error] {course.get('name', '?')}: {exc}")
            import traceback

            traceback.print_exc()

    if summaries:
        exporter.write_text(config.output_dir / "INDEX.md", build_master_index(summaries))
        exporter.write_text(config.output_dir / "GRADES.md", build_master_grades(summaries))

    print(f"\nExport complete: {len(summaries)}/{total} course(s).")
    print(f"Files saved to: {config.output_dir}")


if __name__ == "__main__":
    main()
