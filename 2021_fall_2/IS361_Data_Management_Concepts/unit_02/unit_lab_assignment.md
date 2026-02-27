# Unit 2: Unit Lab Assignment

**Due:** 2021-11-01T04:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Introduction

The purpose of this assignment is to practice on the creation of Entity -Relationship Diagrams (ER Diagrams).

Directions

Create an ER Diagram for the scenario described below.

You are commissioned to design a database to keep records of a small college. You talked with various key members of this community and obtained the following information: 

The college keeps information about students and student performance. Every student is known by her/his first name, initials and last name. They are also identified by a unique StudentID provided by the University. Every student also belongs to one of five Schools (Arts & Sciences, Education, Management, Music and Engineering), and has a Major within that School (History, Chemistry, etc.). All programs of study require 4 years of study, and students are classified as freshmen, sophomore, junior, or senior, depending of the year that are currently attending. Each student is assigned and advisor from Faculty.

The college also keeps track of Faculty information. Besides their first name, initials and last name, Faculty menbers are also issued a unique FacultyID for the institution. Each one is also given an official title for their position in the University, an office number and a telephone number.

Every school within the college has a number of different departments. Each department may offer courses identified by a unique CourseID (i.e. IS361). They also have a course name, and a number of credits hours they are worth for.

Every semester the departments offer some of the courses associated with them. These offerings are uniquely identified by a Semester and a List number. There are 3 semesters per year (Fall, Spring and Summer) and they are given a name that includes the year, i.e.: Fall 2016 or Spring 2017. A List Number is unique within a semester, but it may be repeated from semester to semester and assigned to different courses between semesters. Different sections of the same course within a semester are assigned different List Numbers. Besides referencing a course, every offering also identifies the faculty member who will teach the course, and the classroom number.

When a semester ends, student’s grades are stored in a file of Official Records that references the student, the semester, the list number, and the final grade (A, B, C, D, F or I).

The college also wants to keep track of student associations that are advised by a Faculty member. To this effect they give each of these associations a unique AssociationID and an official name. Each association must have only one advisor, but any student may belong to as many associations as they want. A list of all student members of each association is also kept up-to-date.

Deliverables

An ER Diagram showing all entities and relationships that describe the scenario above. Diagrams must follow the guidelines given by the textbook and the course shell on how to create them.

To draw the diagram, students may use Microsoft Office software like Word (.docx), Excel (.xlsx), or PowerPoint (.pptx) and submit them. Students may also use any other software that creates diagrams available to them, as long as they produce a PDF file to be submitted. Alternatively, diagrams may also be drawn by hand, and a picture may be taken (.jpg) for submission. Therefore, only the following file types will be accepted: .docx, .xlsx, .pptx, .pdf and .jpg. In all cases, be sure that the diagram is neatly organized and readable.

Due Date

Due by 11:59 p.m., Sunday, CT.

---

## My Submission

**Score:** 8.5/10.0
**Grade:** 8.5
**Submitted:** 2021-10-31T23:36:28Z

### Submitted Files

- **IMG_20211031_183050__01-1.jpg**
  - Downloaded: `files/IMG_20211031_183050__01-1.jpg`

### Instructor Feedback

**Bert** (2021-10-31T23:36:28Z):

> Hello Professor, 
I found this easiest to do on a white board. If you would like me to recreate it in paint, please let me know I can find the time to do that. 
I had a few issues in the offial grades section. Any tips would be appreciated. 
thank you

**[INSTRUCTOR] Ph.D.** (2021-11-03T03:01:56Z):

> Offerings (Semester) entity misses the Classroom attribute. [-0.1]
Official Records entity misses the listNumber and Grade attribnutes. [-0.2]

The following relationships are represented incorrectly:
Student to Official Records should be a 1-to-many relationship with 1 in the Student side. [-0.2]
Course to Offerings (semester) should be a 1-to-many relationship with 1 in the Course side. [-0.2]
Faculty to Student Association should be a 1-to-many relationship with 1 in the Faculty side. [-0.2]
Faculty to Student as Advisor should be a 1-to-many relationship with 1 in the Faculty side. [-0.2]

The following relationships are missing:
Faculty to Offerings. [-0.4]
