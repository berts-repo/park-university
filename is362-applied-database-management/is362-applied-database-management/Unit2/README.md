# Unit 2: Overview
Relational Database Models and Manipulation of Tables in a DBMS

## Introduction: This unit will review how to understand a relational data model and how to create one based on a pre-existing Entity-Relationship Diagram. We will also learn how to create and manipulate tables in MariaDB. Topics included in this unit are:

Conversion of ERDs into relational database models.
Creating and Altering Tables in MariaDB.
Inserting, Updating, and Deleting Data in Tables in MariaDB.

## Unit Learning Outcomes

At the conclusion of the unit, the learner will be able to:

Design and creation of a relational database from an Entity-Relationship Diagram (CLO1).

## Assignments

Discussion (10 points): First post due 11:59 p.m., Thursday, CT.  Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Lab Assignment (100 points): Due by 11:59 p.m., Sunday, CT.

Course Project Part 1 - DESCRIPTION: Description of Course Project Part 1 will be posted in this Unit as a Discussion Thread to answer student questions about the project. Students are not required to participate or submit any results in this unit.

---
# Unit 2: Lab Assignment

## Purpose

The purpose of this assignment is to create and populate a complete relational database in MariaDB from its relational data model.
Activities

Students are given an ERD and a relational data model at the end of this document. They describe some data relationships among the entities of a small airline company.  In particular, these diagrams describe the following business rules:
- The small airline company has a number of airplanes, each one described by an AirplaneID and a TypeID (both VARCHAR (7) types). The TypeID is one of a set of predetermined possible values. Each airplane type has its name (TEXT), description (TEXT), and the number of seats (an INT type). For example, an airplane type may have a TypeID of “DC10”, named “Boeing DC-10”, described as “Standard transatlantic passenger carrier” and 400 seats. The small airline usually will have a number of each airplane type, each one with its own ID.
- Pilots are described by their PilotID (VARCHAR(7)), first name, initials, and last name attributes (all TEXT). They also have a salary (a FLOAT type). Each pilot is licensed to fly one or more Airplane types. Each license has a date on which it was granted and a date on which it will expire (both DATE types).
- Flights are officially given by authorities to the airline as concessions. The airline can only flight the concessions given. A concession is specified by a Flight Number (VARCHAR(7)), the origin and destination airports for the flight (both TEXT), the day of the week in which the flight operates (BIT(7) type), and the time when the flight will usually depart (TIME type) on those days. The day of the week is a bit-field of 7 because we only need one bit to indicate if a flight is licensed for a given day. For example, if the value is set to “1010111”. This means that the flight may operate on Monday (the first bit), Wednesday (the third bit), Friday, Saturday, and Sunday (the last 3 bits).
- With a flight concession, the airline may schedule flights for specific Flight Dates (a DATE type). A scheduled flight is assigned one airplane and one pilot.
- Each scheduled flight has a set of seats (VARCHAR (3), a number, and a letter, like “23B”). Each seat may be taken by only one properly documented passenger (a VARCHAR(7) type for the document) or it may be empty (null entries are allowed for this attribute). Besides a DocumentID, a passenger’s first name, initials, and last name should also be recorded (all TEXT types).

Use the description above and the relational data model below to create a MariaDB database and populate it, following these considerations:

- The name of the database should be the student’s last name, followed by the student’s first name, followed by the word assig02. For example, if the student’s name is Jane Doe, the database must be named doejaneassig02.
- Within the MariaDB database, students must create one table for each of the tables in the relational data model. The same names for tables and fields shown in the relational data model must be used in the MariaDB database. Students must also use the correct data types for each field as described in the narrative above. When the size is not indicated for data types, students have the discretion to decide on the sizes of the fields. Every table must have the correct primary key as described in the relational data model.
- Every foreign key relationship between tables as prescribed by the relational data model must be defined and created.
- After defining all the tables and relationships, tables must be filled with complete and valid records. Students are free to use real or invented data that make sense for tables. Pilot, Airplane, and Passenger tables should include complete information for at least 10 entity instances (10 Pilots, 10 Airplanes, and 10 Passengers). The database should have airplanes of at least 2 Airplane types and all pilots must be licensed to fly them all. The database should also have at least 5 Flight Concessions and 5 corresponding Scheduled Flights. Each scheduled flight should have at least 2 seated Passengers.
- Once students have finished, they must export the database into a SQL dump file with the same name as the database followed by the suffix “-dump.sql”. For example, the database named doejaneassig02 will be dumped into the file named doejaneassig02-dump.sql. Students may review the document “How to Export and Import Databases in MariaDB” under Unit 1 for an explanation of how to do this.

## Deliverables

Submit the SQL dump file with the correct name when completed.

### Suggestions

The easiest way to make this work is to write all commands in order in a text file. Students should use some text editor like NotePad or TextPad to write the text file. Do not use Word or any other word processor because they may introduce characters you may not want in your commands. If this happens, then it will be extremely difficult to work with that command. Use a Text Editor. Once students have a text with all commands, they can be copied and pasted in order from the text file onto the MariaDB Client to be executed in order. There is only one problem you may find when copying and pasting the command, and that is the use of single or double quotes (‘’,”). Some Text Editor may use an ASCII symbol that is not compatible with the one used in MariaDB. In those cases is best to type the command completely in MariaDB.

Every time a command is entered, the user can verify if the command worked correctly. If not, the user should analyze the reason why modify the text file where is needed and try the command again.

When writing the commands, students should begin with the CREATE TABLE commands to create all tables in the database. Students should indicate in these commands all PRIMARY KEYs, but not to worry about the FOREIGN KEYs yet.

Once all tables are created, students should write ALTER TABLE commands to add the FOREIGN KEYs with ADD CONSTRAINTs clauses. Students may use ON DELETE RESTRICT and ON UPDATE CASCADE options. 

Next students may INSERT rows in the various tables. Remember that all tables that contain primary keys that are referenced by foreign keys must be populated first, so for example the tables Pilot, AirplaneType, FlightConcession, Passenger, and Licensed should be populated first.

Finally, students should dump the database in the SL file for submission.

![ERD](/IS362-DiagramForAssign02a.jpg)

![Relational Data Model](/IS362-DiagramForAssign02b.jpg)

---
# Unit 2: Class Project Part 1 - DESCRIPTION

## Objective

The purpose of the first part of the class project is to design a database for a business, chosen by students, using the principles of relational database design. Students will create an ERD and a relational database model for their project.
Guidelines

In the first unit of classes, students selected (or were assigned) one title for their class project. All titles for projects corresponded to generic names for small/local businesses. In this part 1 of the class project, students must describe their projects and draw an Entity Relationship Diagram (ERD) that represents some aspects of their assigned business. There is no direct description provided for any of the businesses. Students must come up with their own written descriptions of some aspects of the business and translate these descriptions into an ERD.

Even though no description is given for the businesses, all of them share a common set of areas that can be used to describe most businesses. Namely, all businesses must deal with clients or customers, suppliers or providers of services, products or services produced by the businesses, processes or operations, capital resources (like machinery, equipment, installations, offices, buildings, etc.), personnel of many kinds (part time, full time, contractors) organized in departments of different kinds. Students may select one or more of these areas and/or others that they consider are relevant for their business. These areas should be described in written English and produce an ERD with entities, attributes, and relationships between these entities, under the following requirements:
- The ERD must include at least 6 strong entities describing some areas of the business. Strong entities do not require of other entities to be represented, but they rely on their attributes to define them. Each of these strong entities must have an identifying attribute. They also must have at least other 4 attributes of any kind, except multivalued attributes. If you want to have a multivalued attribute it should be represented as a relationship with another table.
- The ERD must include at least 4 associative entities. These entities represent relationships between various other entities in the diagram. The identifying attribute for each associative entity should be the composite of all the identifying attributes of the other entities associated with the associative entity. Alternatively, the identifying attribute could be a surrogate key. Each associative entity should also have at least one additional attribute describing the relationship.
- All entities should be connected. This means that one can navigate from any entity to any other entity in the diagram by traversing the relationships between them.

Once an ERD is completed it must be translated into a relational database model with the following requirements:

- All entities (including strong and associative) are represented by tables with the same name as their original entity and columns for all attribute names. Every table has a primary key that is underlined by a solid line.
- All tables are connected with primary key-foreign key links. This means that one can navigate from any table to any other table in the relational database model by traversing these primary key-foreign key links between them. Foreign keys that are not also primary keys themselves should be underlined with a segmented line.

## Deliverables

Every submission must include three things:

- A written description in English of the aspects of the business that the student’s project is addressing and the rules that are going to be described by the ERD.
- An ERD for the student’s project.
- A translation of the presented ERD into a relational database model.

All submissions must be written and drawn professionally, and can be created using Microsoft Word, Excel or Powerpoint. PDF files are also welcomed. No other file type will be accepted.

An example of what is expected is given in Unit 02 - Assignment 02. This assignment shows a description in English, an ERD, and a relational database model for a small airline company.