# Unit 6: Unit Lab Assignment

**Due:** 2021-11-29T05:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Introduction

The purpose of this assignment is to practice the design, construction, and use of Data-marts using the Star-Schema.

Based on the original transactional database for a small college in Assignment 4 (copied below at the end) that depicts data transactions in a small college, a data-mart was designed to compare the average grades of classes. This data-mart includes the following tables:

Course Dimension: This table includes generic information about every course. It does not include information about offerings, only courses.

Time Dimension: This table uses semesters to mark the pass of time. Because semesters may have names that are not sequential (the database may not know that “Spring 2020” comes before “Fall 2020”), a surrogate TimeID attribute is created with consecutive values to mark the sequence (first semester is 1, second 2, etc.). Assume this table was already created for you and it exists.

Faculty Dimension: This table includes all relevant information about a Faculty member.

Fact table: contains all primary keys of the dimensions tables and the average grades of all courses offered with the same CourseID during the same semester by the same faculty member

The star-schema for this data-mart is as follows:

Directions

Answer the following questions:

Write a SQL SELECT command to create the Faculty dimension table for the data-mart. You may only use the tables from the original transactional database for the small college.

Write a SQL SELECT command to create the Course dimension table for the data-mart. You may only use the tables from the original transactional database for the small college.

Write a SQL SELECT command to create the Fact-Table for the data-mart. You may only use the tables from the original transactional database for the small college and the Time dimension from the data-mart (assume it was already created).

Design and draw a star-schema for a new data-mart that will keep track of the grades made by students in courses, This data-mart will have the same Time and Course Dimensions that the first data-mart shows, but it will also have a new Student dimension with information about a Student instead of the Faculty dimension. This information includes StudentID, names, major, and school. The Fact-Table will also change and it will hold the grade obtained by a student in a course in a semester.

Write a SQL SELECT command to create the Student dimension table for the new data-mart you designed. You may only use the tables from the original transactional database for the small college.

Write a SQL SELECT command to create the Fact-Table for the new data-mart you designed. You may only use the tables from the original transactional database for the small college and the Time dimension from the data-mart (assume it was already created).

Deliverables

Submit an Office document (Word, Excel or PowerPoint) or a PDF file containing the answers to the questions above, including the design for the new data-mart about students.

Due Date

Due by 11:59 p.m., Sunday, CT.

---

## My Submission

**Score:** 8.6/10.0
**Grade:** 8.6
**Submitted:** 2021-11-27T08:01:45Z

### Submitted Files

- **IS361 Lab6.docx**
  - Downloaded: `files/IS361 Lab6.docx`

### Instructor Feedback

**[INSTRUCTOR] Ph.D.** (2021-11-29T23:44:50Z):

> Q1: Correct
Q2: Correct
Q3: Command is CREATE TABLE. No WHERE conditions or GROUP BY clause presented. [-0.8] 
Q4:  The arrowheads in the diagram should be pointing to the dimension tables. [-0.3]
Q5: Correct
Q6: Command is CREATE TABLE. Missing WHERE clause condition connecting the tables in FROM. [-0.3]
