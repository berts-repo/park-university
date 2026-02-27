# Canvas Course Scraper

Exports all Park University Canvas LMS courses into an organized offline archive with submissions, grades, file downloads, and a master index.

## Setup

1. Create `config.json` in this directory with your Canvas API token:

```json
{
  "canvas_token": "REDACTED"
}
```

Alternatively, set the `CANVAS_TOKEN` environment variable.

2. Requires Python 3.7+ (no external dependencies).

## Usage

```bash
# List all courses (no export)
python3 canvas_export.py --list

# Export a single course by name or code
python3 canvas_export.py --course BI101

# Export all courses
python3 canvas_export.py

# Resume a previous run (skips courses that already have a README.md)
python3 canvas_export.py --resume
```

## Output Structure

```
output/
  INDEX.md                          # Master index by semester and department
  GRADES.md                         # Master grades dashboard with GPA
  2021_spring_1/
    MA125_Intermediate_Algebra/
      README.md                     # Course overview with module links
      syllabus.md
      grades.md                     # Per-course grades by category
      announcements.md
      course_information/
        course_overview.md
        ...
      unit_01/
        overview.md
        discussion_1.md             # Prompt + my posts + score + feedback
        homework.md                 # Instructions + score + submission + feedback
        quiz.md
        files/                      # Downloaded PowerPoints, docs, etc.
      unit_02/
        ...
      misc/                         # Orphan assignments not in any module
  2021_spring_2/
    CS152_Introduction_to_Python_Programming/
      ...
```

## Features

- Semester-organized folders parsed from Canvas course codes
- Single-pass export (no duplicate API calls)
- Downloads binary files (PowerPoints, Word docs, PDFs, submission uploads)
- Per-course grades with category breakdown and estimated letter grade
- Master grades dashboard with semester averages and estimated GPA
- Orphan assignment detection for items not in any module
- Retry with exponential backoff and rate limit handling
- Resume support to continue interrupted exports
