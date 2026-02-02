# Unit 3: Overview

## Basic SQL for Queries

Introduction: This unit will give practical experience to students on the use of the SELECT command from SQL to retrieve information from a database in MariaDB. Also known as queries. The information retrieved will be in the form of tables. Queries will involve one or multiple tables, and they will use the three most basic clauses in the command: SELECT, FROM, and WHERE.
Unit Learning Outcomes

At the conclusion of the unit, the learner will be able to:

Formulate basic SQL queries to a relational database management system (CLO2).

## Assignments

Discussion (10 points): First post due 11:59 p.m., Thursday, CT.  Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Lab Activity/Homework (100 points): Due by 11:59 p.m., Sunday, CT.

Course Project Part 1 - SUBMISSION: (100 points - Includes 10 points for topic selection): Due by 11:59 p.m., Sunday, CT.

---
# Unit 3: Lab Assignment

## Purpose

The purpose of this assignment is to explore Queries in a Relational Database.
Activities

Click here to download a file you will need to work on this assignment.

Download Click here to download a file you will need to work on this assignment.

In this assignment students are provided with a small MariaDB database with data from a transport company:

- The company has a number of vehicles and drivers that transport various loads for clients under contract.

- The Vehicle table contains the following data per vehicle: NumberPlate, (unique) Make, Model, Year, Weight (vehicle’s weight in pounds), VolumeCapacity (in cubic meters), and MaxWeightLoad (maximum weight of a load for the vehicle in pounds).

- The Driver table contains the following data per driver: DocumentID (usually a driver’s license), FirstName, Initials, LastName, BasicSalary (in Dollars), and CommissionPerTrip (a percentage number).

- The Client table has the following fields: ClientID (a unique value per client), Name, LegalAddress, and Phone (phone number).

- All contracts have a unique number (ContractNo), a ClientID and they could be long term or short term. Short-term contracts are made for only one trip, while long-term contracts contain multiple trips for the same Client. The boolean field IsLongTerm will be TRUE if the contract is LongTerm, FALSE otherwise. Based on this field, all contracts in the Contract table have a record in either the LongTermContract table or the ShortTermContractTable.

- A record in the LongTermContract table contains the ContractNo that originates it and the following two fields: PricePerMile (dollars to be charged per mile traveled), and InsurancePerPound (dollars to be charged for insurance per pound of weight being transported).

- A record in the ShortTermContract table also contains the ContractNo that originates it, but it has many more fields: Origin (the place where the trip starts), Destination (the place where the trip ends), Price (total cost of the trip in dollars), InsuranceValue (total insurance cost for the trip in dollars), DateSigned (Date the contract was signed), VehicleAssigned (NumberPlate of the Vehicle who made the trip), and DriverAssigned (DocumentID of the Driver who made the trip). To clarify, all this is information is in this table because short-term contracts are only written for one trip only.

- In contrast, long-term contracts may produce many trips. Each of these trips generates a record in the Trip table with the following fields (some of them similar to the ones in the ShortTermContract table): TripNo (a unique number for the trip), ContractNo, Origin (place where the trip starts), Destination (the place where the trip ends), Distance (miles traveled in the trip), Weight (number of pounds transported for the client in this trip), DateSigned (Date the contract was signed), VehicleAssigned (NumberPlate of the Vehicle who made the move), and DriverAssigned (DocumentID of the Driver who made the move). Once again, to clarify, the Trip table contains information only for trips in long-term contracts.

Students must use the MariaDB database provided in the MySQL dump file named “ForAssig03-dump.sql”. After importing the database, students must create queries (SELECT commands) that will answer the following questions:

Q1: List the last name and first name of all drivers who drove for a short-term contract together with the client’s name. Sort the results in ascending order of the driver’s last name. 

Q2: List the trip numbers, their origin, and destination together with the names of clients with long-term contracts. List only records of clients whose name begins with the letter ‘C’. Sort the results per the client’s name and trip number.

Q3: List the last name and first name of all drivers together with the number plates of the vehicles they have driven for long-term contracts. Sort the list in ascending order of the driver’s last name. Avoid duplication of records.

Q4: List the last name and first name of all drivers together with the number plates of the vehicles they have driven for short-term contracts. List only drivers whose basic salary is greater than 115000. Sort the list in ascending order of the driver’s last name. Avoid duplication of records.

Q5: List the number plates of all vehicles and the last and first names of all drivers that have been used by the client “Chris Rock” in his long-term contract. Sort the list in ascending order of number plate. Avoid duplications of records.

Q6: Count the number of trips and the total number of miles driven (in the Distance field) made by all drivers in long-term contracts whose LastNames begin with either of the letters “A”, “B”, “C” or “D”.

Q7: List the total weight, average weight, minimum weight, and maximum weight of all trips made in a long contract signed by all clients whose Firstname begins with the letter “J”.

Q8: List the average insurance value, the total price charged, and the total driver commission of all short-term contracts per driver’s LastName. Sort the listing in descending order of the total commission.

Q9: List the total distance and total weight of all long-term contracts per client’s name and vehicle’s number plate. Sort the list by the ascending client’s name. Show only records where the total weight is larger than 5000.

Q10: List the total price charged to clients and the average insurance value in long-term contracts per client. The total price is calculated by adding all costs per trip. A cost per trip is the price per mile multiplied by the distance in every trip. The average insurance value is the average of the insurance per pound after it is multiplied by the weight of the trip. Exclude from the report all records with less than 4000 in average insurance value. Sort the listing by descending order of total price charged.

## Deliverables

Students must write a text document (.txt) using a Text Editor like NotePad, WritePad, or TextPad for submission. This document will contain the SQL-SELECT commands that answer the queries in this assignment, all of them properly numbered. To be able to grade the assignment, only text (.txt) documents will be accepted.
Deadline

This assignment is worth 100 points and it is due Sunday, Week 3, at midnight (24:00 pm) CST.
Unit Learning Outcomes Reflected in Assignment

Formulate basic SQL queries to a relational database management system (CLO2).

 

![Relational Database Model](/IS362-DiagramForAssign03.jpg) 

---
# Unit 3: Course Project Part 1 - SUBMISSION

## Activities

Students must make their Class Project Part 1 submissions by the end of this unit, Sunday, Unit 3, at midnight (24:00 pm) CST. A reminder of the narrative for this class project is given below.

Remember to present:

- A written description in English of the aspects of the business that the student’s project is addressing and the rules that are going to be described by the ERD.
- An ERD for the student’s project.
- A translation of the presented ERD into a relational database model.

All submissions must be written and drawn professionally and can be created using Microsoft Word, Excel, or Powerpoint. PDF files are also welcomed. No other file type will be accepted.

Submissions will be graded during Unit 4 and returned to students so that they can proceed with requested modifications to be implemented for Class Project –Part 2 (due at the end of Unit 5).

### Unit Learning Outcomes Reflected In Assignment

Formulate basic SQL queries to a relational database management system (CLO2).

## Unit 2 – Class Project Part 1 – Description  (Reminder)

### Objective

The purpose of the first part of the class project is to design a database for a business, chosen by students, using the principles of relational database design. Students will create an ERD and a relational database model for their project.

### Guidelines

In the first unit of classes, students selected (or were assigned) one title for their class project. All titles for projects corresponded to generic names for small/local businesses. In this part 1 of the class project, students must describe their projects and draw an Entity Relationship Diagram (ERD) that represents some aspects of their assigned business. There is no direct description provided for any of the businesses. Students must come up with their own written descriptions of some aspects of the business and translate these descriptions into an ERD.

Even though no description is given for the businesses, all of them share a common set of areas that can be used to describe most businesses. Namely, all businesses must deal with clients or customers, suppliers or providers of services, products or services produced by the businesses, processes or operations, capital resources (like machinery, equipment, installations, offices, buildings, etc.), personnel of many kinds (part-time, full time, contractors) organized in departments of different kinds. Students may select one or more of these areas and/or others that they consider relevant for their business. These areas should be described in written English and produce an ERD with entities, attributes, and relationships between these entities, under the following requirements:

- The ERD must include at least 6 strong entities describing some areas of the business. Strong entities do not require other entities to be represented, but they rely on their attributes to define them. Each of these strong entities must have an identifying attribute. They also must have at least other 4 attributes of any kind, except multivalued attributes. If you want to have a multivalued attribute it should be represented as a relationship with another table.

- The ERD must include at least 4 associative entities. These entities represent relationships between various other entities in the diagram. The identifying attribute for each associative entity should be the composite of all the identifying attributes of the other entities associated with the associative entity. Alternatively, the identifying attribute could be a surrogate key. Each associative entity should also have at least one additional attribute describing the relationship.

- All entities should be connected. This means that one can navigate from any entity to any other entity in the diagram by traversing the relationships between them.

Once an ERD is completed it must be translated into a relational database model with the following requirements:

 - All entities (including strong and associative) are represented by tables with the same name as their original entity and columns for all attribute names. Every table has a primary key that is underlined by a solid line.

 - All tables are connected with primary key-foreign key links. This means that one can navigate from any table to any other table in the relational database model by traversing these primary key-foreign key links between them. Foreign keys that are not also primary keys themselves should be underlined with a segmented line.

### Deliverables

Every submission must include three things:

- A written description in English of the aspects of the business that the student’s project is addressing and the rules that are going to be described by the ERD.
- An ERD for the student’s project.
- A translation of the presented ERD into a relational database model.

All submissions must be written and drawn professionally and can be created using Microsoft Word, Excel, or Powerpoint. PDF files are also welcomed. No other file type will be accepted.

An example of what is expected is given in Unit 02 - Assignment 02. This assignment shows a description in English, an ERD, and a relational database model for a small airline company.

### Deadline

Students have two weeks to prepare and submit their work for this project. (Unit 2 and Unit 3). Submissions are due on Sunday, Unit 3, at midnight (24:00 pm) CST.

### Questions

Students may use this discussion thread to share ideas and ask questions about the project. Please share ideas and not the actual projects.
