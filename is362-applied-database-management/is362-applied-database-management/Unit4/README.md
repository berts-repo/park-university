# Unit 4: Overview

## Advanced SQL for Queries

Introduction: In this unit, we will continue with the exploration of the capabilities of the SELECT command to retrieve information from a database in MariaDB. We will review the GROUP BY, HAVING, and ORDER BY clauses. We will also study various types of functions for queries: numeric, aggregate, String, Date, and Time functions. 
Unit Learning Outcomes

At the conclusion of the unit, the learner will be able to:

Formulate advanced SQL queries to a relational database management system (CLO2).

## Assignments

Discussion (10 points): First post due 11:59 p.m., Thursday, CT.  Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Lab Activity/Homework (100 points): Due by 11:59 p.m., Sunday, CT.

Course Project Part 2: Description of Course Project Part 2 will be posted in this Unit as a Discussion Thread to answer students' questions about the project. Students are not required to participate or submit any results in this unit.

---
# Unit 4: Lab Assignment

## Purpose

The purpose of this assignment is to explore Advanced Queries Relational Databases.
Activities

[Click here to download a file you will need to work on this assignment.](/ForAssig04-dump.sql)

Download Click here to download a file you will need to work on this assignment.

In this assignment, students are provided with a modified version of the MariaDB database for a transport company given in the previous unit. The modifications made to the database are:

- The LongTermContract table includes now a DateTime type field named DateSigned that contains the date and time when the contract was signed.
- The ShortTermContract table includes now a DateTime type field named DeliveryStamp that contains the date and time when the transportation service was completed for that contract.
- The Trip table no longer has the field DateSigned, but it includes now a DateTime type field named DepartureDate that contains the date and time the trip started. It also includes a new DateTime type field named DeliveryStamp that contains the date and time when the particular trip ended.

Students must use the MariaDB database provided in the MySQL dump file named “ForAssig04-dump.sql”. After importing the database, students must create queries (SELECT commands) that will answer the following questions:

Q1: List the contract number and the name of all clients with short-term contracts with an Insurance value larger than their average.

Q2: List the contract number and the name of all clients with short-term contracts who paid above-average prices and below-average Insurance values.

Q3: List the numbers of all trips with their total price and total insurance value for long-term contracts with prices above the average and insurance below the average. Hints: in trips for long-term contracts, the total price is calculated by multiplying the PricePerMile in a contract by the Distance driven in the trip. The total insurance value is calculated by multiplying the InsurancePerPound in a contract by the Weight of the trip.

Q4: List the last name of the drivers together with their total amount of commissions for long-term trips of all drivers who made the average basic salary. Hints: The commissions are obtained by calculating the percentage the driver gets from the total price for a trip. All these commissions should be added per driver (SUM). A subquery is needed to get the average basic salary of all drivers.

Q5: List the driver’s document, total distance (Sum), and the average weight of all trips made for long-term contracts by the driver(s) with the highest basic salaries.

Q6: For every record in the Trip table, list the concatenation of the first three letters of the Origin field, with the first three letters of the Destination of the trip, the name of the month in the DepartureDate field, and the name of the day in the DeliveryStamp field. Each section should be separated by a dash (-). The concatenation should be all in uppercase. Example: For a trip from Chicago to New Orleans starting on 2018-05-12 and ending on 2018-05-14, the concatenation will be: “CHI-NEW-MAY-MON”.

Q7: List the last names of all drivers who made a trip for a long-term contract that began by or after June 20, 2017, and ended by or before June 30, 2017.

Q8: List the client’s name, contract number of all short-term contracts which have a delivery stamp that is not more than two days from the date the contract was signed. List also the date the contract was signed and the delivery date.

Q9: List trip number and the number of days between the departure date and the delivery stamp of all trips for long-term contracts that departed in June 2017.

Q10: List the number of trips (count how many) made per month for long-term contracts. Sort the listing in descending order of the month. 
Deliverables

Students must write a text document (.txt) using a Text Editor like NotePad, WritePad, or TextPad for submission. This document will contain the SQL-SELECT commands that answer the queries in this assignment, all of them properly numbered. To be able to grade the assignment, only text (.txt) documents will be accepted.
Deadline

This assignment is worth 100 points and it is due Sunday, Unit 4, by 11:59 pm CST.

### Unit Learning Outcome Reflected in Assignment

Formulate advanced SQL queries to a relational database management system (CLO2).

![Relational Database Model](/IS362-DiagramForAssign04.jpg)

---
# Unit 4: Course Project Part 2 - DESCRIPTION

## Objective

The purpose of the second part of the class project is to create a MariaDB database based on the revised design from the first part.
Guidelines

Students must do the following:

Review and implement the corrections indicated by the instructor in the grading of part 1. These may include:

- Addition, modification or elimination of tables and or relations.
- Name changes for fields, tables and relationships
- Change of cardinality in relationships

Implementation of these corrections should be reflected in the construction of a new relational database model to be included in the deliverables for the submission of part 2.

- Create a MariaDB database that reflects the corrected relational database model. Names of tables and fields must agree with the names given in the relational database model. All tables and primary key-foreign key relations must be implemented.

- Populate the tables in the created database. Each table representing a strong entity must contain at least 20 records. Any table for a weak entity may contain a lesser amount of records, but they should be enough to make the database look realistic. Each table representing an associative relationship should include at least one record per each of the records of the entities that participate in the relationship. Since every strong entity may have 20 unique records, this means that associative entities that reference them may also contain 20 or more records.

- Be sure that Entity and Referential integrities are preserved in the database, meaning that no primary key may accept duplicate values and every foreign key should reference a proper primary key (no null foreign keys should be present in this database).

### Deliverables

Every submission must include:

- A corrected version of the relational database model that describes the MariaDB database presented in this part of the project.
- A sql-dump file containing a backup of the implemented database in this part of the project.

All submissions must include diagrams drawn professionally. These can be created using Microsoft Word, Excel, or PowerPoint. PDF files are also welcomed for the diagrams. The sql-dump file is by nature a text file.
Deadline

Students have two weeks to prepare and submit their work for this project. (Unit 4 and Unit 5). Submissions are due on Sunday, Unit 5, at midnight (24:00 pm) CST.
Questions

Students may use this discussion thread to share ideas and ask questions about the project. Please share ideas and not the actual projects.
This topic is closed for comments.