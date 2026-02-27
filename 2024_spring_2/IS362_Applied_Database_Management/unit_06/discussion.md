# Unit 6: Discussion

Introduction

Dear Students:

Participation in discussion threads is a unit assignment that will test your reading process and critical thinking.  You can participate in these discussion threads from 00:00 CST on Monday to 24:00 CST on Sunday in the corresponding Unit. These threads will be locked before and after the final date and time.

This unit’s reading from the course shell is:

Data Warehousing

Directions

After reading the assigned material, you must make an initial posting to the Discussion thread that satisfies the following requirements (no later than Thursday, 11:59 p.m. CT):

You are presented with the database design of two related Data-Marts and a set of questions, most of which should be answered with queries using the SELECT SQL command, or with an explanation on why a query cannot be used. You must choose one of these questions (one that has not been responded to yet) and answer it using the + Reply. Always start your text by indicating the number and the text of the query you are answering.

There is the possibility that more than one student selects the same question without each other knowing it. Since every student must work on different a question, a system of pre-claiming questions is enforced in this discussion thread. A student may post a complete answer to a question first. S/he may also make a post until Thursday in which the only s/he will do is to claim the question s/he will be working on, without any more development. This will serve as a warning to anybody else in the class that this question is not selectable until the first deadline on Thursday. The student who made the claim must make a posting answering the question by the Thursday deadline in order to keep her/his questions. All other students must select (claim and develop) other questions, however, if they chose a pre-claimed one, their contribution will not count. If a student claims a question but does not attempt to answer it by the deadline on Thursday, the question is up for grabs and anyone can select it. All students must check the selected questions in the postings their classmates make to avoid duplications. First come first served. Posts with claims do not count towards the minimum postings to be made by a student unless they also answer the question.

Use only one thread for your personal contribution. After you have made your first posting, claiming or answering a question, make all other postings about this question within the same thread. Even if you decide to change the question, use the same thread. One thread per student, please. This will avoid your contribution from being improperly graded.

Make a second posting by Sunday, 11:59 p.m. CT with the following requirements:

A second posting with comments on each other works is also expected by the end of the unit. These comments may point out if there is any problem with the responses, maybe some possible corrections or suggestions on how to do better. Students may also point out strong points in their fellow student’s work. Lively participation and engagement are good for learning.

In unit assignment 2, you were presented with a database design for a small airline company. This database was a transactional database for the company.

 [link: https://canvas.park.edu/courses/80245/files/11005438/download?verifier=7SJwA7VAle1amL7CxqHu4HBZIzMokXUJC2G3bo9Q] Click here to enlarge the transactional database for the company. 

The company decided to create two Data-marts to analyze flight trends on the licensing of their pilots. The design of both data marts is as follows:

 [link: https://canvas.park.edu/courses/80245/files/11006147/download?verifier=Mz5jD4U0ziVQv3hExE3WkM7rpVRoBbn86RCc5QyJ] The design of both data marts is shown below - Click here to enlarge. 

The diagram describes two fact tables: a Flights-Fact-Table and a License-Fact-Table. The Flight-Fights-Table contains information about all flights performed by the airline. It is related to five dimension tables: Flight Concession, Passenger, Pilot, Airplane, and Time. Each record in the dimension tables describes a unique concession, passenger, pilot, airplane, and time, respectively. They are differentiated by the primary keys in the tables, which are FlightNo for the Concession, DocumentID for the Passenger, PilotID for the Pilot, AirplaneID for the Airplane, and FlightDate for Time. Together, these attributes also make up the primary key for Flights-Fact-Table. The only additional information stored in this fact table is the seat number a particular passenger took.

The second fact table is the License-Fact-Table which contains information about the licensing of pilots. It is related to some of the same dimensions as the Flights-Fact-Table, like Pilot and Time, but it is also related to the AirplaneType dimension with TypeID as its primary key. This TypeID, together with PilotID, the DateGranted, and the ExpiryDate attributes make up the primary key for the License-Fact-Table. There are no additional attributes in this fact table.

Questions

Please select and answer one of the following questions.

The following are questions regarding the construction of the tables for this data warehouse from the transactional database:

Write a SQL SELECT command that will create the table and all its records for the Flights-Fact-Table from the transactional database.

Write a SQL SELECT command that will create the table and all its records for the License-Fact-Table from the transactional database.

Write all the SQL SELECT commands that will provide the records for the Time Dimension table from the transactional database.

Write a SQL SELECT command that will create the table and all its records for the Pilot Dimension table from the transactional database. List the names of all destination cities for the passenger named “George Lopez”.

The following questions are to be solved with SQL queries to the data warehouse tables. If you do not think they can be solved with such queries, please argue why not.

List the names of all destination cities for the passenger named “George Lopez”.

List the name of the most requested destination city.

List the name of the most used origin city.

List the name of the most used airplane type.

List the name of the pilot with the most flights made.

List the name of the passenger who made the most flights.

List the name of the day with the most flights made.

List the most used seat on flights.

List the specific date with the most flights made.

List the AirplaneID of the plane with most flights.

Indicate how many seats are empty in the FlightNo 12345 that happened on “July 27, 2016”.

List the FlightNo of the plane with the least occupied seats on “May 15, 2015”.

List the FlightNo of the least scheduled flight.

List the average number of flights on any given day.

List the average number of flights that happened on Tuesdays.

List the average number of passengers that takes FlightNo 2325.

List the average number of flights made by any pilot.

List the name of the pilot with the most licenses on “April 2, 2014”.

List the name of the pilots who have a license to fly a TypeID = “DC10” on “January 18, 2013”.

List the name of the pilots who did not even have a license to fly a TypeID = “Airbus 100”.

Unit Learning Outcomes Reflected In Assignment

Write simple programs to query a relational database management system (CLO 3).

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-04-16T14:44:17Z

#1

Write a SQL SELECT command that will create the table and all its records for the Flights-Fact-Table from the transactional database.

---


### Feedback

**[INSTRUCTOR]:** Bert, you portrayed a well-structured SELECT statement that showcases how to ccreate the table and all its records for the Flights-Fact-Table from the transactional database - Great Work!
