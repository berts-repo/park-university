# Unit 2

## Purpose

The purpose of this assignment is to create and populate a complete relational database in MariaDB from its relational data model.

## Activities

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

## Suggestions

The easiest way to make this work is to write all commands in order in a text file. Students should use some text editor like NotePad or TextPad to write the text file. Do not use Word or any other word processor because they may introduce characters you may not want in your commands. If this happens, then it will be extremely difficult to work with that command. Use a Text Editor. Once students have a text with all commands, they can be copied and pasted in order from the text file onto the MariaDB Client to be executed in order. There is only one problem you may find when copying and pasting the command, and that is the use of single or double quotes (‘’,”). Some Text Editor may use an ASCII symbol that is not compatible with the one used in MariaDB. In those cases is best to type the command completely in MariaDB.

Every time a command is entered, the user can verify if the command worked correctly. If not, the user should analyze the reason why modify the text file where is needed and try the command again.

When writing the commands, students should begin with the CREATE TABLE commands to create all tables in the database. Students should indicate in these commands all PRIMARY KEYs, but not to worry about the FOREIGN KEYs yet.

Once all tables are created, students should write ALTER TABLE commands to add the FOREIGN KEYs with ADD CONSTRAINTs clauses. Students may use ON DELETE RESTRICT and ON UPDATE CASCADE options. 

Next students may INSERT rows in the various tables. Remember that all tables that contain primary keys that are referenced by foreign keys must be populated first, so for example the tables Pilot, AirplaneType, FlightConcession, Passenger, and Licensed should be populated first.

Finally, students should dump the database in the SL file for submission.
