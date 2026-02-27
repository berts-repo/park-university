# Unit 7: Discussion

Introduction

Dear Students:

Participation in discussion threads is a unit assignment that will test your reading process and critical thinking.  You can participate in these discussion threads from 00:00 CST on Monday to 24:00 CST on Sunday in the corresponding Unit. These threads will be locked before and after the final date and time.

This unit’s reading from the course shell is:

Textbook Chapter 13: User Account and Privileges

Textbook Chapter 15:Bulk Importing Data

Directions

After reading the assigned material, you must make an initial posting to the Discussion thread that satisfies the following requirements (no later than Thursday, 11:59 p.m. CT):

You are presented again with the database design for a small airline company used in previous units. 
 [link: https://canvas.park.edu/courses/80245/files/11005435/download?verifier=C7rTxjwOsYzH1aOZaIOQrD4BpmJqfcUKxZv2tbIH] Click here to enlarge the database design for the airline company. 

Assume you are in charge of this database and you need to create a user account and privileges for a contractor to perform some activities with some specific tables in the database. For the contractor’s name, use your favorite artist (any well-known artist in any discipline will do). Using the + Reply link, you must provide a response that will show the following set of SQL commands in order:

Commands to create your favorite artist’s user account

Commands to grant three or more privileges to some table in the database.

Commands to revoke some of the privileges previously granted, after the artist supposedly used the account.

Commands to destroy the user account, after the artist supposedly used the account.

Use only one thread for your personal contribution. After you have made your first posting, claiming or answering a question, make all other postings about this question within the same thread. Even if you decide to change of favorite artist, or write only one command in every response, please use the same thread. One thread per student, please. This will avoid your contribution from being improperly graded.

Make a second posting by Sunday, 11:59 p.m. CT with the following requirements:

After some of your fellow students had also the chance to make their posting, you must also comment on at least one of these responses. The comments may point out if there is any problem with the responses, maybe some possible corrections or suggestions on how to do better. Students may also point out strong points in their fellow student’s work. Lively participation and engagement are good for learning.

ULOs Reflected in Discussion

Manage a relational database management system through commands (CLO 4)

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-04-22T21:26:40Z

Class,

1. Commands to create your favorite artist’s user account

CREATE USER 'WattersonBill'@'localhost'
IDENTIFIED BY PASSWORD '';

2. Commands to grant three or more privileges to some table in the database.

GRANT SELECT, INSERT, UPDATE, DELETE ON ForDT07.* TO 'WattersonBill'@'localhost';

3. Commands to revoke some of the privileges previously granted, after the artist supposedly used the account

REVOKE UPDATE, DELETE ON ForDT07.* FROM 'WattersonBill'@'localhost';

4. Commands to destroy the user account, after the artist supposedly used the account.

DROP USER 'WattersonBill'@'localhost';

---


### Feedback

**[INSTRUCTOR]:** Bert, you have demonstrated a well-rounded understanding of how to apply various MariaDB Account Management commands. Excellent work!
