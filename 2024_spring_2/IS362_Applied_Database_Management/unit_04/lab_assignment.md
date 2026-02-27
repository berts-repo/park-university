# Unit 4: Lab Assignment

**Due:** 2024-04-08T04:59:00Z
**Points Possible:** 100.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this assignment is to explore Advanced Queries Relational Databases.

Activities

 [link: https://canvas.park.edu/courses/80245/files/11006080/download?verifier=kb39tqKtynM74bCaRPGEsp3Ra3HQVlAIxzzoZ3IO&wrap=1] Click here to download a file you will need to work on this assignment.

In this assignment, students are provided with a modified version of the MariaDB database for a transport company given in the previous unit. The modifications made to the database are:

The LongTermContract table includes now a DateTime type field named DateSigned that contains the date and time when the contract was signed.

The ShortTermContract table includes now a DateTime type field named DeliveryStamp that contains the date and time when the transportation service was completed for that contract.

The Trip table no longer has the field DateSigned, but it includes now a DateTime type field named DepartureDate that contains the date and time the trip started. It also includes a new DateTime type field named DeliveryStamp that contains the date and time when the particular trip ended.

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

Unit Learning Outcome Reflected in Assignment

Formulate advanced SQL queries to a relational database management system (CLO2).

 [link: https://canvas.park.edu/courses/80245/files/11006157/download?verifier=8qvjkU3H2Mwvbeo4SNriW8ctgrJW4cj5hAUa05p6] Relational Database Model - Click here to enlarge the image

---

## My Submission

**Score:** 100.0/100.0
**Grade:** 100
**Submitted:** 2024-04-07T23:46:05Z

### Submitted Files

- **Bertassig04.txt**
  - Downloaded: `files/Bertassig04.txt`

### Instructor Feedback

**[INSTRUCTOR]** (2024-04-09T21:19:54Z):

> Bert, Exceptional work! You have developed a series of diverse SQL queries with each fulfilling the request. See Rubric comments for detailed feedback.
