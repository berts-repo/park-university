# Unit 4: Discussion

Introduction

Dear Students:

Participation in discussion threads is a unit assignment that will test your reading process and critical thinking.  You can participate in these discussion threads from 00:00 CST on Monday to 24:00 CST on Sunday in the corresponding Unit. These threads will be locked before and after the final date and time.

This unit's readings are:

Textbook Chapter 9: Joining and Subquerying Data (pages 166-173)

Textbook Chapter 10: String Functions

Textbook Chapter 11: Date and Time Functions

Textbook Chapter 12: Aggregate and Numeric Functions (pages 241-247)

Using Select for Advanced Queries

Directions

 [link: https://canvas.park.edu/courses/80245/files/11005417/download?verifier=2492M74OkPdU7y0fu9lpJCWpVAjD7ha3L3J8Cdqm&wrap=1] Click here to download a file you will need to respond to this Discussion.

After reading the assigned material you must make an initial posting to the Discussion thread that satisfies the following requirements (no later than Thursday, 11:59 p.m. CT):

You are presented with a Database Design that is similar to the one we reviewed in the Discussion Thread for the previous unit. The design has been modified to add attributes with DateTime types. You must study the diagram and propose three SQL SELECT commands using the + Reply. Do not repeat other students’ commands. Be original! The three commands should include:
One SQL command containing a subquery

One SQL command containing a Date or Time Function

One SQL command containing a String or a Numeric function

Use only one thread for your personal contribution. After you have made your first posting, make all other postings about this topic within the same thread. One thread per student, please. This will avoid your contribution from being mis-graded.

Make a second posting by Sunday, 11:59 p.m. CT with the following requirements:

After some of your fellow students had also the chance to post their own SELECT queries, you must also comment on at least one of these responses. Review each other’s work, and point out if there are any problems. Maybe show out possible corrections or suggestions on how to do better. We could also point out strong points in our fellow student’s work. Lively participation and engagement are good for learning. Be engaged in online discussions. Do this by replying directly to the selected response. 

 [link: https://canvas.park.edu/courses/80245/files/11006138/download?verifier=BuZHX36F25C6b9dd1VLQfqmxivmbPz5AbwjyWFvb] Click here to enlarge the database design for this unit's Discussion queries.

The diagram describes the same database for a small Investigative Report Agency as presented in the discussion thread in a previous Unit. The only changes made are that tables WrittenBy, Journalist, WebPublished, and Private tables have the SubmissionDate HiringDate, PublishedDate, and DateSold fields respectively added. All these fields are DateTime types.

ULOs Reflected in Discussion

Formulate advanced SQL queries to a relational database management system (CLO2).

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-04-04T18:45:46Z

Class,

•  One SQL command containing a subquery

This subquery retrieves a list of articles that were published on the website:

SELECT Title
FROM article
WHERE ArticleID IN (SELECT ArticleID FROM webpublished);

 

•  One SQL command containing a Date or Time Function

This subquery finds the web posted articles in December of 2015:

SELECT Title
FROM article
WHERE ArticleID IN (
SELECT ArticleID
FROM webpublished
WHERE YEAR(PublishedDate) = 2015 AND MONTH(PublishedDate) = 12
);

 

•  One SQL command containing a String or a Numeric function

This query calculates the average read time for the web published articles in December of 2015:

 

SELECT Title, ROUND(NoOFWords / 240, 2) AS AverageReadTime
FROM article
WHERE ArticleID IN (
SELECT ArticleID
FROM webpublished
WHERE YEAR(PublishedDate) = 2015 AND MONTH(PublishedDate) = 12
);

---


### Feedback

**[INSTRUCTOR]:** Bert,

Great work in developing the 3 specific SQL commands outlined in the discussion directions.    You showcased a prominent understanding of the Date/Time, String/Numeric function in addition to a Subquery. Well, done!
