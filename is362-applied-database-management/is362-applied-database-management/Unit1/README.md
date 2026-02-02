# Unit 1: Overview
Entity Relationship Diagrams and Access to a Database Management System

Introduction: In this unit we will review Entity Relationship Diagrams (ERDs) from Data Management Concepts. We will also access the course’s database management system (DBMS). Topics included in this unit are:

Description of elements in an Entity Relationship Diagram.
Construction of Entity Relationship Diagrams from a narrative.
Accessing of MariaDB and creation of simple tables in this DBMS.

## Unit Learning Outcomes

At the conclusion of the unit, the learner will be able to:

Access and inspect a relational database management system (CLO 4).
Create a simple database with one table in a relational database management system (CLO 1)

## Assignments

Discussion (10 points): First post due 11:59 p.m., Thursday, CT.  Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Lab Assignment (100 points): Due by 11:59 p.m., Sunday, CT.

Course Project Introduction and Pre-Selection (10 points included in the next course project delivery in Unit 3): Student must select a topic for the Course Project. Due by 11:59 p.m., Sunday, CT.


---
# Unit 1: Lab Assignment
Due: Sun Mar 17, 2024 11:59pmDue: Sun Mar 17, 2024 11:59pm
---

## Purpose

We will be using MariaDB, a Database Management System (DBMS) to create and use databases in this course. The purpose of this unit’s assignment is for the student to start using MariaDB and produce a simple database with one table.

## Activities

After reading and practicing MariaDB commands from Chapter 3 of the textbook in your working environment, you will create a simple database on your own with one table and the following characteristics:

- Create Database: The name of your database should be your last name, followed by your first name, followed by the word assig01. For example, if your name is John Doe, your database must be named doejohnassig01. Do not worry about having the name all written in lowercase, that is how MariaDB deals with file names.
- Create a table named Pilot inside the database created above. This table must contain three TEXT fields with exactly the following names: LicenseNo, FirstName, and LastName (be sure to use the correct upper and lower cases).
- Fill the pilot table with 10 records with all the data being completed. Namely, you should add 10 first and last names for pilots with appropriate license numbers (7 characters in each license). You may use real or fictitious data.
- Once you finished, export the database into a SQL dump file with the same name as your database followed by the suffix “-dump.sql”. For example, the database named doejohnassig01 will be dumped into the file named doejohnassig01-dump.sql. You may review the document “How to Export and Import Databases in MariaDB” under Unit 1 for an explanation of how to do this.

## Deliverables

Submit the SQL dump file with the correct name when completed.