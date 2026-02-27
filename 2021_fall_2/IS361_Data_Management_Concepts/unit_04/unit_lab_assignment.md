# Unit 4: Unit Lab Assignment

**Due:** 2021-11-15T05:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Introduction

The purpose of this assignment is create a real Relational Database from a Relational Data Model.

Directions

Last unit, you produced a Relational Data Model from and ER Diagram. This unit, we will finally create a real Relational Database using Microsoft Access. You are given a new Relational Data Model at the end of this assignment. Once again it represents a slightly different scenario from last week. In particular, the differences are as follows:

A major change is that the course Offerings table has been de-normalized and it incorporates the contents of the Records Table. The Offerings table now keeps the StudentID and grade of all students who took an offering.

For brevity, the field for Initials was eliminated in Faculty and Student tables.

Faculty table contains numeric fields for Years-of-tenure and Salary instead of Office and Phone-No.

Student Associations went back to be advised by a Faculty member, but only one Faculty Member.

Use the given Relational Data Model below to create a Microsoft Access database with the following considerations:

Within the Microsoft Access database, create one table for each of the tables in the Relational Data Mode. Use the same names for tables and fields as prescribed in the Relational Data Model. Declare all text fields as TEXTs, and use integer or decimal values when appropriate. You have discretion on the sizes of the fields. Give every table their corresponding primary key.

Define every foreign key relation between tables as prescribed by the Relational Data Model.

After defining all the tables and relationships, fill the tables with complete and valid records. You are free to use real or invented data that make sense for the tables. The Faculty and Student tables should include information for at least 7 faculty members and 7 students. The Course table should include information for at least 10 courses. All courses should be offered at least once in some combination in Fall, Spring and Summer semesters. All courses should have at least one student and every student should have registered in at least 1 course every semester and have a grade for the course. There are at least 2 Student Associations and each student should belong to at least one of them.

Deliverables

Submit your Microsoft Access database containing all tables described in the given Relational Data Model and their relationships. The tables should contain the requested minimum number of records.

Due Date

Due by 11:59 p.m., Sunday, CT.

---

## My Submission

**Score:** 6.1/10.0
**Grade:** 6.1
**Submitted:** 2021-11-14T00:14:35Z

### Submitted Files

- **unit4lab.accdb**
  - Downloaded: `files/unit4lab.accdb`

### Instructor Feedback

**[INSTRUCTOR] Ph.D.** (2021-11-15T20:13:27Z):

> Faculty table should have at least 7 records. It has none [-0.4]
Student table should have at least 7 records. It  has none [-0.4]
Course table should have at least 10 records. It only has 1 [-0.4]
Offerings table should have at least 10 records. It has none. [-0.4]
StudentAssociation table should have at least 2 records. It only has 1. [-0.4]
MemberList table should have at least 7 records. It has none. [-0.4]
There are no offerings for at least 3 semesters [-0.3]
Not all courses are offered in the Offerings Table [-0.3]
Offerings does not have at least one record per student in each of 3 semesters [-0.4]
Not all students belong to an Association [-0.4]
MemberList has the wrong primary key. It should be a composite (AssociationID, StudentID) [-0.1]

**Bert** (2021-11-17T09:51:13Z):

> Ouch, I don't know how I missed the entire part where it told me to input data. Know I didn't do it on purpose. I just didn't double check my work well enough.
