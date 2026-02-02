# Unit 7

# Purpose

The purpose of this assignment is to explore Bulk Importing Data onto a MariaDB database.

# Activities

In this assignment, students are provided with a csv file named “ClementsList.csv" This file contains one of the famous Clements checklists of birds from the Cornell Lab of Ornithology that is mentioned in the textbook. A csv file is basically a text file that contains one record in every line, each one with the same number of fields separated by commas. The first line of this file is not an actual record, but it contains the names of the fields, also comma-separated. Students may view the file, if they decide to do so (not needed), using a text editor like TextPad, NotePad, or WritePad, and they can also upload it into Excel. Excel knows how to upload csv files, so students will have to do nothing for the file to be loaded in Excel. However, Excel will take away the commas and display each field in separate columns.  The student's task is to import some fields of this file into a table in MariaDB. From this table, students will later extract certain records and submit them to a final table. This is what students must do:

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

# Deliverables

Submit the SQL dump file of this database with the correct name when completed.

## Unit Learning Outcomes Reflected In Assignment

Bulk import data into a relational database management system (CLO 3, CLO 4)