# Unit 5: Overview

## Programming for the DBMS

Introduction: After having explored most SQL commands to create and manipulate tables and their contents, students will learn how to write a program to execute these operations automatically. The languages that can be used in this course are Java or Python. Chose the language you are most familiar with and proceed to the respective readings.  They will explain to you how to establish connections from your program to the DBMS and how to use these connections to create and manipulate tables. Also, this chapter will explain how to perform automatic queries into a database from a program and handle the results obtained.
Unit Learning Outcomes

At the conclusion of the unit, the learner will be able to:
- Write simple programs to access a relational database management to create and populate a database (CLO 3).

## Assignments

Discussion (10 points): First post due 11:59 p.m., Thursday, CT.  Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Lab Activity/Homework (100 points): Due by 11:59 p.m., Sunday, CT.

Course Project Part 2 - SUBMISSION: (100 points): Due by 11:59 p.m., Sunday, CT.

---
# Unit 5: Lab Assignment

## Purpose

The purpose of this assignment is to explore Java or Python Programming to access MariaDB Databases. Students will choose only one of these languages to write their programs for this assignment.
Activities

In this assignment, students will work with the same design for a transport company given in the previous unit (shown again at the end of this document). You are not giving a sql-dump this time, but rather a text file containing the commands that can be used to create the database Preparation Commands

Download Preparation Commands. Students may use these commands as a reference for this assignment. Students must do the following:

- Select two tables within the design that are related by a primary key-foreign key relation.
- Create an empty database named assig05 in MariaDB.
- Write a Java or Python program with a name that contains the student’s last name, first name, and the word “Assig05”. For example, if the student’s name is Jane Doe, her program must be named “DoeJaneAssig05.java” (or “DoeJaneAssig05.py”). This program will create the two tables selected in 1 inside the database from 2. The program should create all fields in both tables with appropriate types. It should also populate fully both tables with all the records shown in the text file with the instructions. Students must also create the primary key-foreign key relationship between tables.

## Deliverables

Students will submit the “.java” file or the “.py” file with their program. The program should compile and produce the required tables in the required database when run.
Deadline

This assignment is worth 100 points and it is due Sunday, Unit 5, by 11:59 pm CST.

Unit Learning Outcomes Reflected In Assignment
- Write simple programs to access a relational database management to create and populate a database (CLO 3).

![Relational Database Model](/IS362-DiagramForAssign05.jpg)

---
# Unit 5: Course Project Part 2 - SUBMISSION

## Activities

Students must make their Class Project Part 2 submissions by the end of this week, Sunday, Week 5, at midnight (24:00 pm) CST. A reminder of the narrative for this class project is given below.

Remember to present:

- A corrected version of the relational database model that describes the MariaDB database presented in this part of the project.
- A sql-dump file containing a backup of the implemented database in this part of the project.

All submissions must include diagrams drawn professionally. These can be created using Microsoft Word, Excel, or PowerPoint. PDF files are also welcomed for the diagrams. The sql-dump file is by nature a text file.

Submissions will be graded during Unit 6 and returned to students, so that they can proceed with requested modifications to be implemented for Class Project –Part 3 - Final (due at the end of Unit 7).
Unit 4 – Class Project Part 2 – Description  (Reminder)

## Objective

The purpose of the second part of the class project is to create a MariaDB database based on the revised design from the first part.

## Guidelines

Students must do the following:

- Review and implement the corrections indicated by the instructor in the grading of part 1. These may include:

- Addition, modification, or elimination of tables and or relations.
- Name changes for fields, tables, and relationships
- Change of cardinality in relationships

    + Implementation of these corrections should be reflected in the construction of a new relational database model to be included in the deliverables for the submission of part 2.

- Create a MariaDB database that reflects the corrected relational database model. Names of tables and fields must agree with the names given in the relational database model. All tables and primary key-foreign key relations must be implemented.

- Populate the tables in the created database. Each table representing a strong entity must contain at least 20 records. Any table for a weak entity may contain a lesser amount of records, but they should be enough to make the database look realistic. Each table representing an associative relationship should include at least one record per each of the records of the entities that participate in the relationship. Since every strong entity may have 20 unique records, this means that associative entities that reference them may also contain 20 or more records.

- Be sure that Entity and Referential integrities are preserved in the database, meaning that no primary key may accept duplicate values and every foreign key should reference a proper primary key (no null foreign keys should be present in this database).

## Deliverables

Every submission must include:
- A corrected version of the relational database model that describes the MariaDB database presented in this part of the project.
- A sql-dump file containing a backup of the implemented database in this part of the project.

All submissions must include diagrams drawn professionally. These can be created using Microsoft Word, Excel, or PowerPoint. PDF files are also welcomed for the diagrams. The sql-dump file is by nature a text file.

### Deadline

Students have two weeks to prepare and submit their work for this project. (Unit 4 and Unit 5). Submissions are due on Sunday, Week 5, at midnight (24:00 pm) CST.
