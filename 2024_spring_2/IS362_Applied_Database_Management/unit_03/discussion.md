# Unit 3: Discussion

Introduction

Dear Students:

Participation in discussion threads is a unit assignment that will test your reading process and critical thinking.  You can participate in these discussion threads from 00:00 CST on Monday to 24:00 CST on Sunday in the corresponding Unit. These threads will be locked before and after the final date and time.

This unit’s readings from the course shell are:

Textbook Chapter 7: Selecting Data (pages 119-132)

Textbook Chapter 9: Joining and Subquerying Data (pages 153-166)

Using the Select Command in SQL for Simple Queries

Directions

 [link: https://canvas.park.edu/courses/80245/files/11005861/download?verifier=O8fUdJlh245DkVssCUNCG8Uh6e9nOxgaY5rPojmQ&wrap=1] Click here to download a file you will need to respond to this Discussion.

After reading the assigned material with an emphasis on the SELECT command, you must make an initial posting to the Discussion thread that satisfies the following requirements (no later than Thursday, 11:59 p.m. CT):

You are presented with a Database Design and a set of queries to be solved with the SELECT SQL command. You must choose one of these queries (one that has not been responded to yet) and answer it using the + Reply. Always start your text by indicating the number and the text of the query you are answering.
There is the possibility that more than one student selects the same query without each other knowing it. Since every student must work in different a query, a system of pre-claiming queries is enforced in this discussion thread. A student may post a complete answer to a query first. S/he may also make a post until Thursday in which the only thing s/he will do is to claim the query s/he will be working on, without any more development. This will serve as a warning to anybody else in the class that this query is not selectable until the first deadline of Thursday. The student who made the claim must make a posting answering the query by the Thursday deadline in order to keep her/his query. All other students must select (claim and develop) other queries, however, if they chose a pre-claimed one, their contribution will not count. If a student claims a query but does not attempt to answer it by the deadline on Thursday, the query is up for grabs and anyone can select it. All students must check the selected queries in the postings of their classmates to avoid duplications. First come first served. Posts with claims do not count towards the minimum postings to be made by a student unless they also answer the query with a SQL command.

Use only one thread for your personal contribution. After you have made your first posting, claiming, or answering a query, make all other postings about this query within the same thread. Even if you decide to change the query, use the same thread. One thread per student, please. This will avoid your contribution from being improperly graded.

Make a second posting by Sunday, 11:59 p.m. CT with the following requirements:

After some of your fellow students had also the chance to post their own SELECT queries, you must also comment on at least one of these responses. review each other’s work, and point out if there is any problem with them. Maybe show out possible corrections or suggestions on how to do better. We could also point out strong points in our fellow student’s work. Lively participation and engagement are good for learning. Be engaged in online discussions. Do this by replying directly to the selected response.

 [link: https://canvas.park.edu/courses/80245/files/11005404/download?verifier=38c5sZRa4wKE8brMSZVcZOUkenc2a2KaQdhJOKNP] Click here to enlarge the database design for this Discussion.

The diagram describes a simple database for a small Investigative Report Agency. It includes tables with information about journalists, printed articles, articles published on the web, and special private reports for companies. The Journalist table has personal information about the journalists who write all articles in the Article table. More than one journalist may be the author of a given Article, so they are ranked with the field AuthorRank in the WrittenBy table. For example, if the Article “Here we go again” was written by Jane Smith and Han Solo, there will be two records for this Article in the WrittenBy table, one with the JournalistID of Jane Smith and AuthorRank number 1, because she is the first author, and another for the JournalistID of Han Solo and AuthorRank number 2 because he is the second author.

Each article could be printed, published on the web, or sold privately to another company. If it is sold to another company, it is not printed or published on the web. The Private table keeps track of which company bought the article and the price they paid. The Company table has information about the companies buying articles. If an article is printed, it may or may not be published on the web. If it is published on the web, the URL where it was published is stored in the table WebPublished. An article is printed in an issue of a journal within given start and end pages. Every issue has a number, volume, month, and year of publication.

A SQL dump file containing a database with this design is provided for you to practice answering the queries in this discussion thread (ForDT03-dump.sql)

Write SQL SELECT commands to make the following queries:

List the names of all companies who had bought an Article written by the Journalist “Luis Alva”. Avoid company name duplications with DISTINCT.

List the first and last names of all journalists who published a ‘Geopolitics’ article on the web.

List the last and first names of all journalists who printed an article in February 2016. Sort the list in ascending order of the journalist’s last name.

List the last and first names of all journalists who have written private reports articles on ‘Finances’. Sort the list in descending order of the last name. Avoid duplications in journalist names with DISTINCT.

List the last and first names of all journalists who wrote private reports, together with the names of the company that hired them. Sort the list by the last name of the journalist. Avoid duplications of records with DISTINCT.

List the last and first names of all journalists whose last names begin with the letter ‘C’ and have printed articles. Sort the list in ascending order of the journalist’s last name. Avoid journalist duplications with DISTINCT.

List the titles of all articles on “General Economy’ that were published on the web, next to the last and first names of its author-journalists.

List the titles of all articles with two authors that were printed and published online together with the last name of the second author-journalist. Avoid duplications using DISTINCT.

List the title, issue number, month, and year of publication, and start and end page of all articles in printed issues by a journalist whose last names begin with the letter ‘D’.

List the title and subject of all private articles with their author-journalist’s last and first names of their first author and their price. Sort the articles alphabetically by subject and title.

List the titles and numbers of pages of all printed articles together with the last name of its first author-journalists. Sort the articles by the last name of the authors.

List the titles and number of words per page of all printed articles that were also web-published. Sort the title by the number of words per page in descending order.

List the title and subjects of the private articles with a price higher than or equal to $ 20,000.00. List and sort these titles next to the names of the companies in alphabetical order.

List all private titles, their subject, and their price per word. Sort these titles alphabetically by subject, and within a subject by the price per word in descending order.

List the names of the journalists who had written printed articles either in ‘GeoPolitics’ or ‘General Economy’. Avoid listing journalists twice. Sort the journalist alphabetically

The following questions require the use of SQL aggregate functions COUNT, SUM, MAX, MIN, and/or AVG. Some of them may also require the use of the GROUP BY clause and perhaps also the HAVING clause:

Count the number of printed articles in ‘GeoPolitics’ or ‘General Economy’.

Count the number of articles that were published on the web written by “Maria De los Angeles”.

List the total number of words of all web-published List also their average, minimum, and maximum number of words.

List the total number of words of all private articles per company name. List also their average, minimum, and maximum number of words. Sort the listing in descending order of the total of words.

Count the total number of printed articles separated by subjects. List only subjects with more than 1 article. Order the list from the one with more articles to the one with the least.

List the total number of words of all private articles per company name and subject. Exclude all records that have less than or equal to 2000 words per article in total. List also their average, minimum, and maximum number of words. Sort the listing by company name and subject.

List the average, minimum, and maximum number of pages of all printed articles per subject. Exclude all subjects with less than 20 pages on average. Sort the listing by subject.

List the total number of words, the total number of pages, and the average number of words per page of all printed articles per volume of issues. Order the list by volume.

List the total amount of money collected on private articles per journalist. Identify each journalist by JournalistID and LastName. Sort the list in descending order of money collected

List the average, minimum, and maximum prices per word of all private articles per subject. Order the list in descending order of average.

List the average number of words, and the total amount of money collected from all private articles that were written by the Journalist “Boccelli”.

List the total number of pages and the average number of words in published issues per month and per subject. Order the list per subject.

ULOs Reflected in Discussion

Formulate basic SQL queries to a relational database management system (CLO2).

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-03-29T18:36:47Z

24. List the total number of pages and the average number of words in published issues per month and per subject. Order the list per subject.

 

Class,

Sorry I'm a little late to this conversation. I have been sick and slept a ridiculous amount, and on top of that my brother visiting from out of state. I believe that I have done this correctly.

 

SELECT issue.Month, article.Subject,
SUM(printed.EndPage - printed.StartPage) AS TotalPages,
AVG(article.NoOFWords) AS AvgWords
FROM issue, printed, article
WHERE issue.IssueNo = printed.IssueNo AND printed.ArticleID = article.ArticleID
GROUP BY issue.Month, article.Subject
ORDER BY article.Subject;

---


### Feedback

**[INSTRUCTOR]:** Bert, very structured query utilizing the WHERE clause to answer for Q24.  Your structured query answered the request precisely by listing the total number of pages and the average number of words in published issues per month and per subject. Order the list per subject. Nicely orchestrated!
