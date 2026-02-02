# Unit 3

## Purpose

The purpose of this assignment is to explore Queries in a Relational Database.

## Activities

Download file you will need to work on this assignment.

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


## Unit Learning Outcomes Reflected in Assignment

    Formulate basic SQL queries to a relational database management system (CLO2).
