# Unit 6: Overview

## Database Warehousing

## Introduction:

This unit will also complete the practical experiences with programming for a DBMS. Data Warehousing concepts and how SQL can be used in this area will also be reviewed.
Unit Learning Outcomes

At the conclusion of the unit, the learner will be able to:

- Write simple programs to query a relational database management system (CLO 3).

## Assignments

Discussion (10 points): First post due 11:59 p.m., Thursday, CT.  Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Lab Activity/Homework (100 points): Due by 11:59 p.m., Sunday, CT.

Course Project Part 3 - DESCRIPTION: Description of Course Project Part 3 will be posted in this Unit as a Discussion Thread to answer students' questions about the project. Students are not required to participate or submit any results in this unit.

---
# Unit 6: Lab Assignment

## Purpose

The purpose of this assignment is to explore Java or Python Programming to query MariaDB Databases. Students will choose only one of these languages to write their programs for this assignment.

## Activities

In this assignment, once again, students will work with the same design for a transport company previously given (with the design shown again at the end of this document). You may use the MySQL dump file named “ForAssig06-dump.sql

Download ForAssig06-dump.sql”. You must import this file into a database named “ForAssig06”. This way your program can be evaluated for grading. After importing the database, students must do the following:

- Design a query command (SELECT) that involves at least three tables within the design that are related by primary key-foreign key relations. This command should display most (if not all) fields in the tables involved and should limit the number of records to 5 or more by the use of conditional statements in the WHERE clause. Test the query in the database.
- Write a Java or Python program with a name that contains the student’s last name, first name, and the word “Assig06”. For example, if the student’s name is John Doe, his program must be named “DoeJaneAssig06.java” (or “DoeJaneAssig06.java”). This program will perform the query designed in 1. The program should produce (display) a report table with all the fields obtained in the query. The report table should label correctly each of its columns at the top and report all requested records generated in the query.

## Deliverables

Students will submit the “.java” file or the “.py” file with their program. The program should compile and produce the required tables in the database provided when run.
Deadline

This assignment is worth 100 points and it is due Sunday, Unit 6, by 11:59 pm CST. 

Unit Learning Outcomes Reflected In Assignment

Write simple programs to query a relational database management system (CLO 3).

![Relational Database Model](/IS362-DiagramForAssign06.jpg)

---
# Unit 6: Course Project Part 3 - DESCRIPTION
Objective

The purpose of the third and last part of the class project is to create application programs that interact with the MariaDB database that was implemented in the second part.

### Guidelines

Students must do the following:

- Review and implement any corrections to the database given by the instructor in the grading of the second part.

- Write 3 Java or Python programs that will display the information related to tables from 3 of the 4 associative entities in the project design. Each program will display a report table with all important and descriptive information regarding a relationship. For example, if the database design includes an associative entity that describes the orders made by a Client entity from a Supplier entity, then all attributes in the associative entity must be displayed in the report table, but also the full names of the Client and the Supplier. These names will probably not be inside the table for the associative entity, but they can be pulled from related tables. Students must show their good own criteria in deciding which attributes are important or descriptive enough to be displayed in their report tables. It is recommended that for every program, students should formulate a SQL query that would display the required report. Once this is defined, it would be easier to write a Java or Python program that will execute the query and handle the output to produce the report table. The report table should label correctly each of its columns at the top and report all records in the associative entities.

- Name each of your programs starting with the student’s last name, followed by the student’s first name, and the word “ProgX”, where X will be the number 1, 2, or 3, for each of the three programs. For example, if the student’s name is Jane Doe, her programs must be named “DoeJaneProg1.java”, “DoeJaneProg2.java”, and “DoeJaneProg3.java” (or “DoeJaneProg1.py”, “DoeJaneProg2.py”, and “DoeJaneProg3.py”).

### Deliverables

Every submission must include:

- A final version of the ERD and the relational database model for the project with all corrections requested by the instructor.
- A sql-dump file containing the corrected and final version of the MariaDB database for the project.
- Three “.java” or “.py” files containing the requested programs in this final part of the project. The programs should compile and produce the required report tables when run.

### Deadline

Students have two weeks to prepare and submit their work for this project. (Unit 6 and Unit 7). Submissions are due on Sunday, Unit 7, at midnight (24:00 pm) CST.
Questions

Students may use this discussion thread to share ideas and ask questions about the project. Please share ideas and not the actual projects.
