# Unit 5: Unit Lab Assignment

**Due:** 2021-11-22T05:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Introduction

The purpose of this assignment to explore Queries in a Relational Database.

Directions

This unit, you are provided with a small  [link: https://canvas.park.edu/courses/64263/files/8477203/download?verifier=JtDlESGpXaceuJ38D2x3WDl5EUXUXJkXwuqC6aPS&wrap=1] Microsoft Access database that contains data about a book seller with the following characteristics:

The book seller keeps track of the ISBN, title, category (“Science”, “Art”, etc.), number of copies in stock, price and the indication if the book is used or not, for all books they had.

Names and unique AuthorID codes of book’s authors are also stored in the database in an Author table and the Wrote table makes the connection between authors and books. The field AuthorRank in the Wrote table indicates the rank of an author among all authors of the book. For example a book with three authors will give rank number 1 to the first author, 2 to the second, and 3 to the third. Books with one author always will give a rank number of 1 to this author.

Table Customer contains the name, address and a unique identifier for each customer.

Customers may order books. Dates when the order was made and when it was delivered are stored in the Order table, together with the CustomerId. The Order table is related by the field OrderNo with the OrderLine table. The OrderLine table contains a record per each book title ordered. The field OrderRank indicates the rank of the Book within the Order. The pair of fields OrderNo and OrderRank are the primary key for the OrderLine table. A record in the OrderLine table also contains the ISBN of an ordered book, the quantity ordered and the percentage of discount over the original price that is given for this book.

You must use the Access database and create queries that will answer the requests below. You may use Query by Example (QBE) or direct SQL to create the queries. Store them using the number of the question (Q1, Q2, etc.).

Q1. Obtain the names and addresses of all customers who ordered a book by Susan Colley. Avoid repetitions.

Q2. Obtain the average, minimum and maximum prices of all “Mathematics” books that were ordered

Q3. Obtain the Last and First Names of all second authors whose books were ordered. Print these names next to their book titles. Show also the total amount sold of each of these titles. The total amount sold is the quantity of books in a orderline multiplied by their price and added for all orders of the same author. Order the results in descending order of the total amount sold (Hint: Use the SUM function to add the multiplications and GROUP BY to make these additions per author and title).

Q4. Obtain the CustomerIDs and the names of the customers that have made more than one order (actually orderlines) of any given title. List next to the customer name also the title of a book and the number of all orders made of that title by the customer. Order the results in descending order of the number of orders.

Q5. Obtain the average price before discount of all books that were delivered after May 5, 2016.

Q6. Obtain the minimum, maximum and average price of all ordered books per category. Use prices before discounts. Sort the list in descending order of average price. Do not include average prices smaller than S20.00.

Q7. Obtain the names of all customers that bought the most expensive book(s). Sort the names alphabetically. Hint: Use subqueries to find the ISBN(s) of the most expensive book(s).

Q8. Obtain the total of all discounted prices of all books ordered by the Customer “Jerry Seinfeld”. The discounted price is calculated by multiplying the Quantity sold of a title by its Price and by (1-PercentageDiscount/100).

Q9. Obtain the book titles, the last name of their first authors, and the sum of all copies of the book sold. Include only the titles with more than 5 copies ordered by customers in total. Sort the list in descending number of books sold.

Q10. Obtain the ISBN, title and author last names of all books that were not ordered ever. Hint: Use a subquery to find a list with the ISBNs of all ordered books. The ones that were not ordered should not be in that list.

Microsoft Access Relationship Map

Deliverables

Submit the Microsoft Access database containing all required stored queries.

Due Date

Due by 11:59 p.m., Sunday, CT.

---

## My Submission

**Score:** 8.1/10.0
**Grade:** 8.1
**Submitted:** 2021-11-21T19:07:00Z

### Submitted Files

- **Database for Assignment 5.accdb**
  - Downloaded: `files/Database for Assignment 5.accdb`

### Instructor Feedback

**[INSTRUCTOR] Ph.D.** (2021-11-23T23:28:58Z):

> Q01: OK
Q02: OK
Q03: Results were not sorted as requested. [-0.1]
Q04: Query should select Title and COUNT(*) also. It should also declare the Book table and link it. Missing GROUP BY and HAVING clauses. ORDER BY should be by COUNT(*) [-0.7]
Q05: OK
Q06: Results were not sorted as requested. [-0.1]
Q07: Wrong location of subquery. It should be used in the WHERE conditions, not the SELECT clause. GROUP BY clause was not needed (no aggregate functions used). Results were not sorted as requested. [-0.4]
Q08: Formula in SELECT should multiply the discounted Price by Quantity before SUM.[-0.1]
Q09: Wrong location of subquery. It was not needed. SUM(Quantity) alone should be used GROUP BY and HAVING clauses missing. Ordering should be by SUM(Quantity). [-0.5]
Q10: OK
