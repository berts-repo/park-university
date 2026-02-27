# Unit 3: Unit Lab Assignment

**Due:** 2021-11-08T05:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Introduction

The purpose of this assignment is to practice on the creation of a Relational Data Model from an Entity -Relationship Diagram.

Directions

Last unit, you were given the task to create an ER Diagram for the entities and relationships found in a small college.

This unit, you will convert an ER diagram for a similar situation into a Relational Data Model. The ER Diagram is shown at the end of the directions and represents a slightly different scenario from last week. In particular, the differences are as follows:

Schools and Departments are not considered to be entities on their own, but just attributes in other tables.

Course offerings are an associative relationship between Faculty and Course entities. A Faculty member teaches a course that is being offered. An offering has a unique OfferingID that is never repeated. The offering relationship keeps track of the Semester in which the Offering took place, the name of the section and the classroom where it was taught. As before, when a semester ends, student’s grades are reported to a file of Official Records. Every student with grades as references to the Official Records where all her/his grades are saved.

Student associations may now be advised by none, one or more than one Faculty member.

You must convert the given ER Diagram into a Relational Data Model following the guidelines of the textbook and the course shell. Be sure to create rows of boxes for every required table, each box should contain a field within the table. Primary keys should be properly underlined and foreign key relations should be clearly indicated with arrows.

Deliverables

Create and submit a Relational Data Model Design with a diagram showing all tables, primary keys, and foreign key relationships that describe the given ER Diagram.

To draw the diagram, students may use Microsoft Office software like Word (.docx), Excel (.xlsx), or PowerPoint (.pptx) and submit them. Students may also use any other software that creates diagrams available to them, as long as they produce a PDF file to be submitted. Alternatively, diagrams may also be drawn by hand, and a picture may be taken (.jpg) for submission. Therefore, only the following file types will be accepted: .docx, .xlsx, .pptx, .pdf and .jpg. In all cases, be sure that the diagram is neatly organized and readable.

Due Date

Due by 11:59 p.m., Sunday, CT.

---

## My Submission

**Score:** 9.6/10.0
**Grade:** 9.6
**Submitted:** 2021-11-06T05:35:37Z

### Submitted Files

- **lab3.xlsx**
  - Downloaded: `files/lab3.xlsx`

### Instructor Feedback

**[INSTRUCTOR] Ph.D.** (2021-11-09T23:02:33Z):

> StudentID should not be part of Offerings table. It means that only one Satudent is assigned to the Offering. [-0.1]
Official Records table should have the OfferingId instead of the Course attribute. The Grades are per Offering, not per Course. [-0.1]
The following relationship(s) was (were) not properly captured: 
•	There are Official Records per Offering. Arrow should join OfferingID fields in both tables. [-0.2]
