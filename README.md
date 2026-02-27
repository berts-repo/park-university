# Park University — B.S. Computer Science Coursework Archive

Full coursework archive from a B.S. in Computer Science at Park University (2021–2024), with a cybersecurity and networking concentration. 33 courses exported from Canvas LMS into structured Markdown using a [custom scraper](./canvas_scrape/canvas_export.py).

---

## Focus Areas

### Cybersecurity

| Course | Name | Semester |
|--------|------|----------|
| [CS202](./2021_fall_1/CS202_Secure_Programming) | Secure Programming | 2021 Fall 1 |
| [CS335](./2022_spring_1/CS335_Introduction_to_Cybersecurity) | Introduction to Cybersecurity | 2022 Spring 1 |
| [CS375](./2022_fall_1/CS375_Secure_Operation) | Secure Operation | 2022 Fall 1 |
| [CS377](./2024_spring_1/CS377_Digital_Forensics) | Digital Forensics | 2024 Spring 1 |
| [CJ316](./2023_summer/CJ316_Cybersecurity_Administration) | Cybersecurity Administration | 2023 Summer |

### Networking

| Course | Name | Semester |
|--------|------|----------|
| [CS365A](./2021_fall_1/CS365A_Computer_Networking_I) | Computer Networking I | 2021 Fall 1 |
| [CS366A](./2022_spring_2/CS366A_Computer_Networking_II) | Computer Networking II | 2022 Spring 2 |
| [CS371](./2022_summer/CS371_Internetworking) | Internetworking | 2022 Summer |
| [CS372](./2024_spring_1/CS372_Advanced_Networking) | Advanced Networking | 2024 Spring 1 |

### Systems & Architecture

| Course | Name | Semester |
|--------|------|----------|
| [CS319](./2022_spring_2/CS319_Computer_Architecture) | Computer Architecture | 2022 Spring 2 |
| [CS351](./2022_fall_1/CS351_Computer_Operating_Systems) | Computer Operating Systems | 2022 Fall 1 |
| [CS369](./2023_spring_1/CS369_Operating_System_Administration) | Operating System Administration | 2023 Spring 1 |

### Programming & Software

| Course | Name | Semester |
|--------|------|----------|
| [CS152](./2021_spring_2/CS152_Introduction_to_Python_Programming) | Introduction to Python Programming | 2021 Spring 2 |
| [CS225](./2023_spring_2/CS225_Programming_Concepts) | Programming Concepts | 2023 Spring 2 |
| [CS240](./2023_fall_1/CS240_Web_Programming_I) | Web Programming I | 2023 Fall 1 |
| [CS252](./2022_fall_2/CS252_Object-Oriented_Programming) | Object-Oriented Programming | 2022 Fall 2 |
| [CS352](./2023_summer/CS352_Data_Structures) | Data Structures | 2023 Summer |

### Theory & Foundations

| Course | Name | Semester |
|--------|------|----------|
| [CS208](./2021_summer/CS208_Discrete_Mathematics) | Discrete Mathematics | 2021 Summer |
| [CS300](./2021_summer/CS300_Technology_in_a_Global_Society) | Technology in a Global Society | 2021 Summer |
| [CS305](./2023_fall_2/CS305_Introduction_to_Artificial_Intelligence) | Introduction to Artificial Intelligence | 2023 Fall 2 |

### Information Systems & Data

| Course | Name | Semester |
|--------|------|----------|
| [IS205](./2021_spring_1/IS205_Managing_Information_Systems) | Managing Information Systems | 2021 Spring 1 |
| [IS361](./2021_fall_2/IS361_Data_Management_Concepts) | Data Management Concepts | 2021 Fall 2 |
| [IS362](./2024_spring_2/IS362_Applied_Database_Management) | Applied Database Management | 2024 Spring 2 |

### General Education

| Course | Name | Semester |
|--------|------|----------|
| [EN105](./2021_spring_1/EN105_First_Year_Writing_Seminar_I_Critical_Reading_Writing_and_Thinking_Across_Conte) | First Year Writing Seminar I | 2021 Spring 1 |
| [EN106](./2021_spring_2/EN106_First_Year_Writing_II_Academic_Research_and_Writing) | First Year Writing II | 2021 Spring 2 |
| [EN234](./2021_fall_2/EN234_Introduction_to_Fiction-_WI) | Introduction to Fiction | 2021 Fall 2 |
| [EN306C](./2023_fall_2/EN306C_Professional_Writing_in_the_Discipline_Writing_and_Research_in_Your_Academic_Fi) | Professional Writing in the Discipline | 2023 Fall 2 |
| [MA120](./2023_fall_1/MA120_Basic_Concepts_of_Statistics) | Basic Concepts of Statistics | 2023 Fall 1 |
| [MA125](./2021_spring_1/MA125_Intermediate_Algebra) | Intermediate Algebra | 2021 Spring 1 |
| [BI101](./2022_spring_1/BI101_Biological_Concepts) | Biological Concepts | 2022 Spring 1 |
| [PY101](./2023_spring_1/PY101_Physical_World) | Physical World | 2023 Spring 1 |
| [LE300G](./2022_fall_2/LE300G_Integrative_Interdisciplinary_Learning_CapstoneTerrorism_the_Media) | Integrative Interdisciplinary Learning Capstone | 2022 Fall 2 |
| [PO200](./2022_summer/PO200_American_National_Government) | American National Government | 2022 Summer |

---

## Archive Structure

```
{year}_{term}_{session}/
  {COURSE_CODE}_{Course_Name}/
    README.md          ← navigation hub for the course
    syllabus.md
    grades.md
    announcements.md
    course_information/
    unit_01/ … unit_NN/
      *.md             ← one file per Canvas item (page/assignment/discussion/quiz)
    misc/              ← orphan assignments not attached to any module
```

Each course `README.md` lists every module and links to each item. Start there when browsing a course.

---

## Canvas Scraper

[`canvas_scrape/canvas_export.py`](./canvas_scrape/canvas_export.py) is the tool that generated this archive. It exports any Canvas LMS course to this Markdown format. Python 3.7+, zero external dependencies.

```bash
python3 canvas_scrape/canvas_export.py --list       # list available courses
python3 canvas_scrape/canvas_export.py --course CS377  # export one course
python3 canvas_scrape/canvas_export.py              # export all courses
python3 canvas_scrape/canvas_export.py --resume     # resume an interrupted export
```

Set your Canvas API token in `canvas_scrape/config.json` or via the `CANVAS_TOKEN` environment variable before running.
