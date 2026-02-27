# Unit 5: Discussion

Introduction

Dear Students:

Participation in discussion threads is a unit assignment that will test your reading process and critical thinking.  You can participate in these discussion threads from 00:00 CST on Monday to 24:00 CST on Sunday in the corresponding Unit. These threads will be locked before and after the final date and time.

In this unit, students may choose the language they will prefer to program on, either Java or Python. 

If the student selects Java, the readings from the course shell are:

Java Programming to Access MariaDB Databases.

Installing Java, TextPad, and the Java API for MariaDB

Compiling and Running Java Programs

Textbook Chapter 16: Application Programming Interfaces (optional)

If the student selects Python, the readings from the course shell are:

Python Programming to Access MariaDB Databases.

Installing Python for MariaDB

Compiling and Running Python Programs

Textbook Chapter 16: Application Programming Interfaces (optional)

Directions

After reading the assigned material, you must make an initial posting to the Discussion thread that satisfies the following requirements (no later than Thursday, 11:59 p.m. CT):

You are presented with the same database design for a small Investigative Report Agency we used in the previous unit, and a list of activities to be implemented by a Java program that will interact with MariaDB. You must choose one of these activities (one that has not been selected yet) and answer it using the + Reply. Always start your text by indicating the number and the text of the activity you will be working on.

There is the possibility that more than one student selects the same activity without each other knowing it. Since every student must work in a different activity, a system of pre-claiming activities is enforced in this discussion thread. A student may post a complete answer to an activity first. S/he may also make a post until Thursday in which the only s/he will do is to claim the activity s/he will be working on, without any more development. This will serve as a warning to anybody else in the class that this activity is not selectable until the first deadline on Thursday. The student who made the claim must make a posting answering the activity by the Thursday deadline in order to keep her/his activity. All other students must select (claim and develop) other activities, however, if they chose a pre-claimed one, their contribution will not count. If a student claims an activity but does not attempt to answer it by the deadline on Thursday, the activity is up for grabs and anyone can select it. All students must check the activities their classmates selected in postings to avoid duplications. First come first served. Posts with claims do not count towards the minimum postings to be made by a student unless they also answer the activity with a Java program.

Use only one thread for your personal contribution. After you have made your first posting, claiming, or answering an activity, make all other postings about this activity within the same thread. Even if you decide to change activity, use the same thread. One thread per student, please. This will avoid your contribution from being improperly graded.

Make a second posting by Sunday, 11:59 p.m. CT with the following requirements:

After some of your fellow students had also the chance to make their posting, you must also comment on at least one of these responses. The comments may point out if there is any problem with the responses, maybe some possible corrections or suggestions on how to do better. Students may also point out strong points in their fellow student’s work. Lively participation and engagement are good for learning.

 [link: https://canvas.park.edu/courses/80245/files/11006165/download?verifier=BUdSlTI8V0oL9dpPmXfhR38BQpTkYVIXFcungZoO] Click here to enlarge the relational database model.

This is the same relational database model for a small Investigative Report Agency we used the last unit. This time, rather than a SQL dump file for this database, a text file containing the commands used to create the database is provided  [link: https://canvas.park.edu/courses/80245/files/11006017/download?verifier=dGxfe6rQ5sNOp7xIbjeC9b0oMj4fAaLwGU8b4RNe&wrap=1] Preparation Commands. You may use these commands as a reference when creating your Java program for your answer to the discussion thread. Also, if the activity you chose tells you to assume a table was created or populated, you can try your program by creating and/or populating the table directly in the database with the commands provided in the document.

Your task is to create a Java or Python program that performs one of the following activities for the given database:

Create the structure of the Issue table.

Create the structure of the Journalist table.

Create the structure of the Company table.

Create the structure of the Article table.

Create the structure of the WebPublished table.

Create the structure of the WrittenBy table.

Create the structure of the Printed table.

Create the structure of the Private table.

Assuming it was already created, populate the Issue table with records.

Assuming it was already created, populate the Journalist table with records.

Assuming it was already created, populate the Company table with records.

Assuming it was already created, populate the Article table with records.

Assuming it was already created, populate the WebPublished table with records.

Assuming it was already created, populate the WrittenBy table with records.

Assuming it was already created, populate the Printed table with records.

Assuming it was already created, populate the Private table with records.

Assuming it was already created and populated, modify all the attributes of one record in the Issue table, except for the primary key.

Assuming it was already created and populated, modify all the attributes of one record in the Journalist table, except for the primary key.

Assuming it was already created and populated, modify all the attributes of one record in the Company table, except for the primary key.

Assuming it was already created and populated, modify all the attributes of one record in the Article table, except for the primary key.

Assuming it was already created and populated, modify all the attributes of one record in the WebPublished table, except for the primary key.

Assuming it was already created and populated, modify all the attributes of one record in the WrittenBy table, except for the primary key.

Assuming it was already created and populated, modify all the attributes of one record in the Printed table, except for the primary key.

Assuming it was already created and populated, modify all the attributes of one record in the Private table, except for the primary key.

Assuming it was already created and populated, drop all attributes in the Issue table, except for the primary key.

Assuming it was already created and populated, drop all attributes in the WebPublished table, except for the primary key.

You must write, compile, and test your program. To complete your posting you may show or attach your program and an image or images showing the contents before and after the program is executed. For example, if you wrote the program to create the Customer table from the reading material, you could show the program you used and the following image (minus the arrows):

Unit Learning Outcomes Reflected In Assignment

Write simple programs to access a relational database management to create and populate a database (CLO 3).

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-04-11T16:18:26Z

Assuming it was already created and populated, modify all the attributes of one record in the WebPublished table, except for the primary key.

 

Code:

''' 
ForDT05.py
Bert

Assuming it was already created and populated, 
modify all the attributes of one record in the WebPublished table,
except for the primary key.
'''
import mariadb

userAux = input ("Enter user: ")
passwordAux = input("Enter password: ")

conn = mariadb.connect (
    user = userAux,
    password = passwordAux,
    host = "localhost",
    database = "ForDT05"
    )
cur = conn.cursor()

# Article (row) to update
articleID = 'AB00931'

# Modified values for article
newWebsite = 'https://www.newsite.com'
newPublishedDate = '2024-04-11 12:34:56'

# Modify mysql statement
stmt = "UPDATE webpublished SET Website = ?, PublishedDate = ? WHERE ArticleID = ?"

# Run SQL statement
try:
    cur.execute(stmt, (newWebsite, newPublishedDate, articleID))
    print("Record updated successfully.")
except mariadb.Error as e:
    print(f"Error: {e}")

conn.commit()
conn.close()

 

Output variations:

---


### Feedback

**[INSTRUCTOR]:** Bert,

Great work in creating a code for activity #21outlined in the discussion directions. You showcased a prominent understanding of Python to MariaDB connection and modied all the attributes of one record in the WebPublished table, except for the primary key.

Great Work!
