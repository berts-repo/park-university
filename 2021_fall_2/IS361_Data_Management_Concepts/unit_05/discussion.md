# Unit 5: Discussion

Introduction

This discussion is different than most discussions...Please carefully read the entire discussion post!

In this discussion, you are presented with a Database Design and a set of queries to be solved with the SELECT SQL command. You will be asked to choose one of these queries (one that has not been responded yet) and answer it. 

There is the possibility that more than one student may select the same topic without each other knowing it. Since every student must work in different topics, a system of pre-claiming topics is enforced in discussion thread. Be sure to read the instructions below carefully.

Since this unit, we are creating specific SQL commands, there is no requirement for students to comment on each other works. However, it would be good if we review each other’s work, and point out if there is any problem with the responses. Maybe show out possible corrections or suggestions on how to do better. We could also point out strong points on our fellow student’s work. Lively participation and engagement is good for learning.

Directions

Read the following chapters from the textbook prior to responding to the discussion:

Chapter 6: Introduction to SQL

Chapter 7: Advanced SQL

Review the sections below under This Unit's Discussion Questions:

Database Design

List of Queries from which to Choose

Pre-claim your topic:

Review all prior claims of topics.

Make a post to claim the topic. Always start your text by indicating the number and the text of the query you are answering. A student may post a complete topic first, but s/he may also make a post until Thursday of any given week in which s/he will only claim the topic they are working without any more development. This will serve as a warning to anybody else in the class that the topic is not selectable until the first deadline of Thursday. The student who made the claim must make a posting by the Thursday deadline in order to keep her/his topic. All other students must select (claim and develop) other topics, however, if they chose a pre-claimed one, their contribution will not count. If a student claims a topic but does not produce a complete posting on the topic by the deadline on Thursday, the topic is up for grabs and anyone can select it. All students must check the selected topics in the discussion thread to avoid duplications. First come first served. 
Note: Word count from claiming queries to be solve with the SELECT SQL command do not count towards the minimum postings to be made by a student, unless they also answer the query with a SQL command.

Complete your initial  post by 11:59 p.m., Thursday, CT. Make sure your post:

Begins by indicating the number and the text of question you are answering

Reflects your understanding of the assigned readings for the week.

Uses of your critical thinking.

Uses only one thread for your personal contribution. After you have made your first posting, answering the original question of the discussion thread, make all other postings about this topic within the same thread. Even if you decide to change topic, use the same thread. One thread per student, please. This will avoid your contribution being mis-graded. Your initial post must include the following:

Write SQL commands to make queries from the list below.

After posting an answer for one of the requested SQL queries:

Create and post a non-SELECT SQL command on your own that can be applied to this database. This could be any SQL command to create, modify, or delete a table, to insert; update, or delete data in a table; or create an index in a table. Do not repeat other student’s commands. Be original!

Respond to your classmates (optional).

This Unit's Discussion Questions

Database Design

 

The diagram describes a simple database for a small clinic. It includes tables with information about Physicians, Patients, Consultations, Medicine, Clinical Testing and Follow Up. Every Physician, Patient, Medicine, and Clinical Testing in the system contains a record within their corresponding Table. Every time a patient visits a physician, a unique consultation record is created. After the consultation ends, a set of RequestedClinicalTests may be ordered, Medication for Patients may be filled and FollowUp records may also be created. Assume that the fields named Salary, Dosage, Quantity, and UnitCost are the only numeric fields in the database. All other fields are strings (TEXT).  The fields Date and DOB can be transformed to the format MM-DD-YYYY (‘01-31-1950’, for example) by using the function Format(<Date-Field>,” MM-DD-YYYY”). A particular month could also be obtained as a number using the function MONTH(<.Date-Field>). The design also shows the 1-to-many relationships that govern this application.

A Microsoft Access database is included for you to test your queries:  [link: https://canvas.park.edu/courses/64263/files/8477310/download?verifier=9JqCkr6Z3yJUdt3m7qAdaFHKEJRUBf93u4739WXu&wrap=1] Database for Discussion 5.accdb

List of Queries from which to Choose:

Write SQL commands to make the following queries:

List the first and last names of all patients who had a Clinical Test named ‘X-Ray’. Avoid patient duplications.

List the first and last names of all physicians with specialty of ‘Geriatrics’ who prescribed the medicine called ‘Aspirine’. Avoid physician duplications.

List the SSN, first and last names of all patients who have ever had a consultation with Dr. George Lopez. Sort the list in ascending order of the patient’s last name. Avoid patient duplications.

List the MedicationId and the names of all medicine ever prescribed to the patient named Jennifer Lopez. Sort the list in ascending order of the medicine’s name. Avoid medicine name duplications.

List the first and last names of all physicians together with the first and last names of all their patients. Sort the list by the last name of the physician, and the last name of the patient. Avoid listing duplications of pairs of physician and patients names.

List the SSN, first name and last name of all patients whose last names beginning with the letter ‘N’ and a Diagnosis of ‘Allergies’. Sort the list in ascending order of the patient’s last name. Avoid patient duplications.

List the first and last names of all patients who visited a doctor and had a clinical test the same date. It also happens to be during the month of the patient’s birthday. Avoid patient duplications. Hint: use the function MONTH(x) to get the number of the month from a date type.

List the first names, last names and insurance number of all patients who require a treatment of ‘Rest’ and the Medicine ‘Sleeping Pill’. Avoid patient duplications.

List the names of all medicine with the contraindications of ‘Avoid aspirin’ that was ever prescribed to a patient with diagnosis of ‘Angina’. Avoid medicine name duplications.

List the insurance numbers of all patients that received medications with total cost greater than $100.00. List the total cost next to the insurance number. The total cost of medication is the product of Quantity by UnitCost.

List the MedicationID, name, quantity, unit cost, and total cost of all medication prescribed on February 11, 2017 (the day of the consultation) with a dosage of 100 mg (Dosage 100, DosageUnit is ‘mg’). The total cost is the product of Quantity by UnitCost. Avoid medicine duplications. Hint: Use the function Format(Date,”MM/DD/YYYY”) to get a String to be compared with “02/11/2017”.

List the first and last names of all physicians and the patients who have the same last name. Sort the list by the last name of the physician. Avoid name duplications in the final list.

The following questions require the use SQL aggregate functions COUNT, SUM, MAX, MIN and/or AVG. Some of them may also require the use of the GROUP BY clause and perhaps also the HAVING clause:   

Count the number of patients with a diagnosis of ‘Migraine’ that had a clinical test named ‘White cell count’ ever. Avoid counting patients twice.

Count the number of times a consultation prescribed a ‘MRI’ test at the same time that it prescribed the medication named ‘Ontobion’. Avoid counting consultations twice.

List the total number of consultations taken by all physicians separated by specialties. List only specialties with more than 1 consultation. Order the list from the one with more consultations to the one with the least.

List the total cost of medication per patient SSN and consultation. The total cost is the product of Quantity by UnitCost. Order the list first by the Patient’s SSN and within the SSN, per descending total cost of consultation.

List the number of medications prescribed and the average unit cost of these medications, per treatment. Order the list in ascending order of treatment and then the average unit of cost.

List the number of requested clinical tests and the average unit cost of these tests, per diagnosis. Order the list in descending order of diagnosis and then the number of requested clinical tests.

List the number of medications prescribed with the minimum and maximum unit costs of these medications, per specialty and physician. Order the list in ascending order of specialty, physician ID, and number of medications.

List the number of requested clinical tests and the minimum and maximum unit cost of these tests, per patient. Order the list in ascending order of the number of requested clinical tests.

List physician’s IDs next to the total number of distinct patients who consulted that physician in March, 13, 2017. The list should be in descendent order of the number of patients seen, and it should include only the physicians who saw more than 1 patient. Hint: Use the function Format(Date,”MM/DD/YYYY”) to get a String to be compared with “03/13/2017”.

List the Medication id, name and the average unit cost of medication ordered by Dr. Richard Kimball sorted in ascending by MedicationId.

List the Test ID, name and the average unit cost of all distinct ClinicalTests taken by patients with a diagnosis of ‘Flue’ sorted by TestID.

List the total cost of medications and their average costs grouped per patients with the same diagnosis. Show the diagnoses next to their costs. Sort the list in ascending order of Diagnosis. The total cost is the product of Quantity by UnitCost.

List physician’s specialties next to the average, minimum and maximum salaries of all physicians in that specialty, and the number of distinct physicians in that specialty. The list should be sorted in descending order of specialty name, and include only the specialties with more than 1 physician.

For the adventurous students, the following questions require the use of subqueries, a topic of Advance SQL that you are not required to know in this course, but could be useful in real life for complicated queries.

List the first name, Last name, specialty and salary of all physicians that ordered Clinical Tests that have unit costs higher than the average. You will need a subquery to find the average first. Avoid physician duplications.

List the first names and last names of all patients that took the test named ‘Urine Battery’ but were not diagnosed with “Stress”. Hint: use a subquery to find the SSN of all Patients with “Stress”. The requested patients should not be in the results of this subquery (NOT IN). Avoid patient duplications.

List the first name and last name of all patients who had a diagnosis of ‘Exhaustion’ and did not have any clinical test done due to this consultation. Avoid patient duplications.

List the first name and last name of all physicians who prescribed a treatment of ‘Low Sodium Food’ but did not prescribed any medication to a patient on that consultation. Avoid physician duplications.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-11-19T03:37:23Z

10. List the insurance numbers of all patients that received medications with total cost greater than $100.00. List the total cost next to the insurance number. The total cost of medication is the product of Quantity by UnitCost.

---


### Feedback

**[INSTRUCTOR] Ph.D.:** Good participation. It satisfies requirements.
