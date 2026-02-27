# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

An offline archive of Park University CS degree coursework (2021–2024) for a cybersecurity-focused student. The archive spans the full degree — from intro programming through advanced security and networking — and is the source material for portfolio work, research, and knowledge retrieval.

**Core cybersecurity courses in the archive:**
- `CS202_Secure_Programming` — secure coding practices
- `CS335_Introduction_to_Cybersecurity`
- `CS375_Secure_Operation`
- `CS377_Digital_Forensics`
- `CJ316_Cybersecurity_Administration`
- `CS365A/CS366A/CS371/CS372` — networking I/II, internetworking, advanced networking
- `CS351_Computer_Operating_Systems`, `CS369_Operating_System_Administration`

Supporting technical depth: `CS305_AI`, `CS319_Computer_Architecture`, `CS352_Data_Structures`, `CS252_OOP`, `CS240_Web_Programming`.

## Archive Data Layout

```
{year}_{term}_{session}/          # e.g. 2023_fall_1/
  {COURSE_CODE}_{Course_Name}/
    README.md                     # Navigation hub — links all modules/items
    syllabus.md
    grades.md                     # Per-course grade breakdown by category
    announcements.md
    course_information/
    unit_01/ … unit_NN/
      *.md                        # One file per Canvas item (page/assignment/discussion/quiz)
    misc/                         # Orphan assignments not attached to any module
unknown_unknown/                  # Courses with unparseable term/year metadata
canvas_scrape/                    # Scraper that generated this archive
```

Each course `README.md` is the navigation hub — start there when exploring a course.

## Scraper (`canvas_scrape/canvas_export.py`)

Exports Canvas LMS courses to this Markdown archive format. Python 3.7+, no external dependencies.

**Configuration** — create `canvas_scrape/config.json`:
```json
{ "canvas_token": "YOUR_TOKEN_HERE" }
```
Or set `CANVAS_TOKEN` as an environment variable. Update the hardcoded `OUTPUT_DIR` and `CONFIG_PATH` paths at the top of the script before running.

```bash
python3 canvas_scrape/canvas_export.py --list      # list courses, no export
python3 canvas_scrape/canvas_export.py --course CS377  # export one course
python3 canvas_scrape/canvas_export.py             # export all
python3 canvas_scrape/canvas_export.py --resume    # resume interrupted export
```

**Key internals:** `api_get()` handles pagination + backoff; `export_module_item()` branches by Canvas item type (`Page`, `Assignment`, `Discussion`, `Quiz`, `File`); `GradeRecord` aggregates grades into `grades.md`; `build_master_index()` / `build_master_grades()` produce top-level `INDEX.md` and `GRADES.md`.
