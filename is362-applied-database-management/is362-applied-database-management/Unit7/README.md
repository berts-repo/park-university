# Unit 7: Overview
Database Administration and Bulk Importing

Introduction: This unit explores bulk importing, or how data can be uploaded into a database from external sources. This task is often performed when a database is initially created and needs to be populated with external information. Another possible scenario requiring bulk importing may be the creation of a Data Warehouse where information needs to be uploaded from a staging area. Because of the latter, some Data Warehousing concepts will be reviewed.
Unit Learning Outcomes

At the conclusion of the unit, the learner will be able to:

- Manage a relational database management system through commands (CLO 4)
- Bulk import data into a relational database management system (CLO 3, CLO 4)

## Assignments

Discussion (10 points): First post due 11:59 p.m., Thursday, CT.  Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Lab Activity/Homework (100 points): Due by 11:59 p.m., Sunday, CT.

Course Project Part 3 (100 points): Due by 11:59 p.m., Sunday, CT.
Student Opinion of Teaching Survey

---
# Unit 7: Lab Assignment

## Purpose

The purpose of this assignment is to explore Bulk Importing Data onto a MariaDB database.

## Activities

In this assignment, students are provided with a csv file named “ClementsList.csv

Download ClementsList.csv”. This file contains one of the famous Clements checklists of birds from the Cornell Lab of Ornithology that is mentioned in the textbook. A csv file is basically a text file that contains one record in every line, each one with the same number of fields separated by commas. The first line of this file is not an actual record, but it contains the names of the fields, also comma-separated. Students may view the file, if they decide to do so (not needed), using a text editor like TextPad, NotePad, or WritePad, and they can also upload it into Excel. Excel knows how to upload csv files, so students will have to do nothing for the file to be loaded in Excel. However, Excel will take away the commas and display each field in separate columns.  The student's task is to import some fields of this file into a table in MariaDB. From this table, students will later extract certain records and submit them to a final table. This is what students must do:

- Create a MariaDB database with a name that contains the student’s last name, first name, and the word “Assig07”. For example, if the student’s name is Jane Doe, her database must be named “DoeJaneAssig07.java”.

- The file “ClementsList.csv” should be placed in a location that is accessible to MariaDB. Students using the Citrix Park Virtual Lab, do not have to do anything here. The system administrator has already placed a copy of this file in the following folder: C:\Program Files (x86)\MariaDB 10.2\data. Students will be given instructions below on how to reach this destination. It is recommended that students using their own platforms should place the file in the data folder for their MariaDB installation. This could also be the C:\Program Files (x86)\MariaDB 10.2\data if MariaDB was installed in the default directories.

- Create a table in the database for this assignment that contains the following TEXT fields:

    + category
    + englishName
    + scientificName
    + aRange
    + aOrder
    + family
    + extinct
    + extinctYear

- Upload the contents of the “ClementsList.csv’ file into the table created in step 3, using the INFILE command in MariaDB. To write this command correctly consider the following:
    + The path to reach the file is ‘../data/ClementsList.csv’. This path is correct as long as the file was installed in the data folder of the MariaDB installation, as previously prescribed.
    + Fields in the “ClementsList.csv’ are terminated by commas (,), and some fields (not all) are enclosed with double quotes (“).
    + Fields in the “ClementsList.csv’ are terminated by carriage return and new line characters (\r\n).
    + The first line in the file should be ignored because it contains the fields’ names.
    + The first three (3) fields from each line should be ignored using a @dummy variable.
    + The last two (2) fields from each line should also be ignored using a @dummy variable.
    + All fields in between should be uploaded to the table in the order that was presented in step 3 above.

- If uploading was successful, the table will contain 32419 records. From all these records, students must extract only the ones that have the category = “subspecies” and that have a scientificName that begins with the first letter of the student’s last name. For example, Jane Doe will extract all records that have “subspecies” in the category and have a scientificName that begins with the letter “D”. Students may produce this result in two possible ways: 1. Deleting all undesired records from the table obtained in steps 4, or, 2. By creating another table from the first one, containing only the required records. In either case, in the end, the database should contain only one table with the requested records. It is not recommended for students to try to edit the csv file itself. It is too large and unsorted to be handled properly by Excel or the Text Editors. It is possible, but it is more work than following the instructions given here, and it is prone to produce many mistakes.

- Once students have finished, they must export the database with only one table into a SQL dump file with the same name as the database followed by the suffix “-dump.sql”. For example, the database named doejaneassig07 will be dumped into the file named doejaneassig07-dump.sql. Students may review the document “How to Export and Import Databases in MariaDB” under Unit 1 for an explanation of how to do this.

## Deliverables

Submit the SQL dump file of this database with the correct name when completed.
Deadline

This assignment is worth 100 points and it is due Sunday, Week 7, at midnight (24:00 pm) CST.
Unit Learning Outcomes Reflected In Assignment

Bulk import data into a relational database management system (CLO 3, CLO 4)

---
# Unit 7: Course Project Part 3 - SUBMISSION

## Activities

Students must make their Class Project Part 3 submissions by the end of this unit, Sunday, Unit 7, at midnight (24:00 pm) CST. A reminder of the narrative for this class project is given below.

Remember to present:

- A final version of the ERD and the relational database model for the project with all corrections requested by the instructor.
- A sql-dump file containing the corrected and final version of the MariaDB database for the project.
- Three “.java” or “.py” files containing the requested programs in this final part of the project. The programs should compile and produce the required report tables when run.

## Objective

The purpose of the third and last part of the class project is to create application programs that interact with the MariaDB database that was implemented in the second part.

## Guidelines

Students must do the following:

- Review and implement any corrections to the database given by the instructor in the grading of the second part.

- Write 3 Java or Python programs that will display the information related to tables from 3 of the 4 associative entities in the project design. Each program will display a report table with all important and descriptive information regarding a relationship. For example, if the database design includes an associative entity that describes the orders made by a Client entity from a Supplier entity, then all attributes in the associative entity must be displayed in the report table, but also the full names of the Client and the Supplier. These names will probably not be inside the table for the associative entity, but they can be pulled from related tables. Students must show their good own criteria in deciding which attributes are important or descriptive enough to be displayed in their report tables. It is recommended that for every program, students should formulate a SQL query that would display the required report. Once this is defined, it would be easier to write a Java or Python program that will execute the query and handle the output to produce the report table. The report table should label correctly each of its columns at the top and report all records in the associative entities.

- Name each of your programs starting with the student’s last name, followed by the student’s first name, and the word “ProgX”, where X will be the number 1, 2, or 3, for each of the three programs. For example, if the student’s name is Jane Doe, her programs must be named “DoeJaneProg1.java”, “DoeJaneProg2.java”, and “DoeJaneProg3.java” (or “DoeJaneProg1.py”, “DoeJaneProg2.py”, and “DoeJaneProg3.py”
    ).

## Deliverables

Every submission must include:

- A final version of the ERD and the relational database model for the project with all corrections requested by the instructor.
- A sql-dump file containing the corrected and final version of the MariaDB database for the project.
- Three “.java” or ".py" files containing the requested programs in this final part of the project. The programs should compile and produce the required report tables when run.

## Deadline

Students have two weeks to prepare and submit their work for this project. (Unit 6 and Unit 7). Submissions are due on Sunday, Unit 7, at midnight (24:00 pm) CST.
