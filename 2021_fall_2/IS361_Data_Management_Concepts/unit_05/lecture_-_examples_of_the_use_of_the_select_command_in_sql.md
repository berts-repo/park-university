# Unit 5: Lecture - Examples of the Use of the SELECT Command in SQL

All database queries in SQL are performed by the SELECT command. In its simplest form this command has the following format (Square brackets [] indicate optional parameters):

 

SELECT  Field1  [ , Field2 , … ]   
         FROM  Table1  [ , Table2 , … ] 
         [ WHERE  Condition1 [ ,Condition2, … ]  ]  ;

 

The words SELECT, FROM and WHERE are keywords and must be written as seen. Even though the format displayed above is written in three lines for clarity, the commands themselves are free-format and can be written all in one line or in multiple lines. Blank spaces can be added wherever the programmer thinks is appropriate for readability.

The purpose of this command is to create a table “on-the-fly” and display it. This table will contain all fields specified in the first line (SELECT) in the specified order. The fields will be obtained from the tables mentioned in the second line (FROM). If no other parameter is given the command will retrieve all the requested fields from all records of these tables The records can be filtered further under some criteria specified in the parameters of the optional third line (WHERE). Only the records that satisfy the conditions impose in the third line will end-up in the final output of the command.

Notice that a semicolon at the end of the command indicates the end of the statement. Omitting this semicolon, or locating it in the wrong place, will produce a syntax error.

To show examples of how this command works we will use a database with the following design and relationships:

 

It is recommended that students review these commands directly under the SQL View of queries in Microsoft Access, using the database provided for the Assignment.

To access the SQL View, students may open the MS Access database and select the Query Design button, as shown:

 

After clicking this button a panel will appear, prompting you to select tables. Close that panel without selecting any table:

 

A query tab will appear. If you right-click the name of the query tab you will get a drop-down menu. Select the “SQL View” menu item to enter the SQL View mode where you can enter SQL commands:

 

 

After writing a SQL command, it can be tested by clicking the Run button that shows and exclamation mark in the menu above (! Run). To go back to the SQL View you can always right-click the query tab. The SQL command can also be saved by right-Clicking the query tab and selecting Save and giving a name to the query.

For every query we have to construct, the first thing we need to find out is which fields we want to obtain, locate them in the database design and use their correct field name in the SELECT portion of the query, in any order we prefer. We also need the names of the tables in which the fields are located. These names will be some of the table names that should appear in the FROM clause, also in any order.

 

Examples Using Only One Table

 

1. List all the book titles

The title of a book is to be found in the Book table in our design. Only one field and one table are needed. The following command will provide all book titles:

 

SELECT Title FROM Book ;

 

2. List the ISBN, title and price of all books in the database

All three fields are to be found in the Book table, therefore we have:

 

SELECT ISBN, Title, Price FROM Book ;

 

The following example shows the use of  ‘*’. This is a wildcard for fields that means “all fields in the table”:

 

3. List all data for all books

The following command will produce all fields for all records in the Book table:

 

SELECT *  FROM Book ;

 

The examples below shows the use of  ‘DISTINCT’.

 

4. List the AuthorID for all Authors who wrote a book:

The following command will produce all fields for all records in the Book table:

SELECT AuthorID FROM Wrote ; 

The problem with this command is that it generates duplicate records when an author has written more than one book. 

To eliminate any duplicate record in the output table we may use the DISTINCT keyword after the SELECT command:

SELECT DISTINCT AuthorID FROM Wrote ;

This does not generate duplicate records.

Use of Conditionals in The Where Clause

5. List the titles of all ‘ART’ books in the database

The WHERE clause is added to the command to select all records that have the Category field containing the value of ‘ART’:

SELECT Title FROM Book WHERE Category = ‘ART’ ;

When writing TEXT values for fields, one can use single or double quotes, but one must write them directly in the MS Access environment. The symbol may not be accepted if copied and pasted from other text editors/processors, and may produce a syntax error.

6. List the titles of all used ‘ART’ books in the database

This time there is an added condition to the previous query. We should include it in the WHERE clause using the AND connector. Since the Used field is already a boolean, it will stand on its own as a condition:

SELECT Title FROM Book WHERE (Category = 'Art') AND (Used) ;

Added parentheses to the conditional expressions where optional, but they are recommended because they clarify the order of evaluation of the expressions.

 

More Examples

 

7. List all customer names living in New York
 
 

SELECT CustomerName FROM Customer WHERE State = ‘New York’ ;

 

8. List all the book titles with prices between $10.00 and $15.00

Describing a range of prices requires conditionals with the AND clause:

SELECT Title FROM Book WHERE Price >10.00 AND Price < 15.00 ;

9. List all the book titles in Physics or Management

On the other hand, to describe conditions that are mutually exclusive we may use the OR clause:

SELECT Title FROM Book WHERE  Category = ‘Physics’ OR

      Category = ‘Management’ ;

 

10. List all the book titles not in Physics or Management

Inequality in conditional expressions is expressed with the symbols <> :

SELECT Title FROM Book WHERE Category <> 'Physics' OR Category <> 'Management' ;

 

Examples Using More Than One Table

In the majority of queries where more than one table is used, tables need to be connected using their foreign keys. The process of query construction is the same: finding out the fields we want to obtain, locating them in the database design, and using their correct field name in the SELECT portion of the query, in any order we prefer. Sometimes, however, we may need to prefix the field name by the table name and a dot (reason why this is called the dot notation). For example, the field ISBN from the Book table could be listed as Book.ISBN. The reason for this action is to avoid ambiguity when fields have the same name in different tables. If we were to use the table Book and the table Wrote at the same time, we need to specify the provenance of the ISBN field. The dot notation previously described will indicate that Book.ISBN is the ISBN field coming from the Book table.

In the FROM clause of the SELECT, besides the names of the tables in which the fields are located, we will need to list also the names of all tables in a path between them.

In the WHERE clause, besides all required conditions for the problem at hand we will need to add conditions to link the tables in the above mentioned path. The linkage, or “join”, as it is known in SQL parlance will happen when we make conditions that check for the equality of foreign keys. This can be better explained in the following examples.

 

11. Show the customer’s name with the number of the orders they made

The Customer Name is located in the Customer Table, while the Order numbers are all in the Order table. Both fields (CustomerName and OrderNo) must be included in the SELECT clause and both tables (Customer and Order) must be included in the FROM clause. Because both tables are connected by a foreign key relation, the WHERE clause should include the condition that checks that the CustomerID in the Customer table matches the CustomerID in the Order table.

SELECT CustomerName, OrderNo

                                    FROM Customer, [Order]

                                     WHERE Customer.CustomerID = Order.CustomerID ;

Notice also that the name Order has to be surrounded by square brackets ([ ]) because the word ORDER is a reserved word in SQL (as the words SELECT, FROM and WHERE are). Every time we use a keyword as a field name or table name we may need to differentiate it from keywords by surrounding the name with square brackets.

If we omit the WHERE clause what we obtain is a table in which every CustomerName is paired with every OrderNo. Mathematically this is a Cartesian product of both fields, and it is seldom needed.

         SELECT CustomerName, OrderNo

                    FROM Customer, [Order];

12. Show the book titles with the order numbers where they were ordered an the quantity being ordered

The book title is located in the Book Table, while the Order numbers and quantities are all in the OrderLine table. The three fields (Title, OrderNo, and Quantity) must be included in the SELECT clause and both tables (Book and OrderLine) must be included in the FROM clause. Because both tables are connected by a foreign key relation, the WHERE clause should include the condition that checks that the ISBN in the Book table matches the ISBN in the OrderLine table.

 

SELECT Title, OrderNo, Quantity

                FROM Book, OrderLine

                WHERE Book.ISBN = OrderLine.ISBN; 

 

13. List all the book titles with their authors’ last names

The book title is located in the Book Table, while the authors’ last names are in the Author table. As before, these fields and tables must be included in the SELECT and FROM clauses respectively. This time the connection between Book and Author tables involve a third table, Wrote. This table must also be included in the FROM clause and this time we have to connect the Book table with the Wrote table by checking the equality of their foreign key (ISBN). We must also connect the Wrote Table with the Author table by checking the equality of their corresponding foreign key (AuthorID).

SELECT Title, LastName 
                 FROM Book, Wrote, Author

                WHERE Book.ISBN = Wrote.ISBN AND

                               Wrote.AuthorID =  Author.AuthorID ;

The conditions to join tables along the path of multiple tables is the most common condition that is going to found in practice. SQL provides commands to perform various kinds of joints between tables, but rather than learning them all, students should use the conditions as shown here, because when used wisely, they cover all possible joins other commands may perform.

Use of joints using conditions in the WHERE clause will be the required joints in this course and the use of all other forms of joints are discouraged.

Field Creation and Sorting

In occasions is necessary to perform calculations on the data fields before display. The formulas for all these calculations can be added in the SELECT clause as part of the field list.

14. List all titles and their corresponding prices and taxes (8%)

The tax for a book can be calculated by multiplying the Price field by 0.08. This can be expressed as follow in the SELECT clause:

       SELECT Title, Price, [Price]*0.08 FROM Book ;

In the previous example, taxes will appear in a separate column field with a automated name for the expression. If we wish to add a column name like “Tax” we could add the parameter “AS Tax” after the calculated expression, as follows:

 

SELECT Title, Price, [Price]*0.08 AS Tax, [Price]*1.08 AS Total FROM Book ;

 

Records in the output table can also be sorted by certain field or set of fields in ascending (default) or descending order using a new clause: ORDER BY. This clause usually located at the end of the query, after the WHERE clause and any other clause we will see in the future. After the keywords “ORDER BY”, a list of fields indicated the sorting order. The output table will sort the records based on the first field, and if there are duplicate values in this field, they will be sorted by the second field, and so on. After each of these fields in the ORDER BY clause, we can specify the keyword DESC to select descending order on that field, or ASC to select ascending order on that field. All fields in the ORDER BY clause must have been mentioned for display at the beginning of the SELECT clause.

 

15. List all the book titles in Mathematics or Art sorted by Price

The added ORDER BY clause at the end of this example will sort all output records by Price, in ascending order (the default) from the least expensive title to the most expensive title:

        SELECT Title, Category, Price FROM Book

                      WHERE Category = 'Mathematics' OR Category = 'Art'

                      ORDER BY Price;

The same query could be sorted in descending order, from the most expensive title to the least expensive using the parameter DESC after the Price field in the ORDER BY clause:

        SELECT Title, Category, Price FROM Book

                      WHERE Category = 'Mathematics' OR Category = 'Art'

                       ORDER BY Price DESC;

16. List all the book titles in Mathematics or Art sorted by Price in descending order and Title in ascending order

The ORDER BY clause in the following query will sort the records in the table first by Price in descending order (most expensive first) and when more than one record have the same price, they will be sorted in ascending order of Title (this means A-Z).

          SELECT Title, Category, Price FROM Book

                          WHERE Category = 'Mathematics' OR Category = 'Art'

                           ORDER BY Price DESC, Title ASC;

Ascending is the default sorting order, therefore the following will do the same:

          SELECT Title, Category, Price FROM Book

                           WHERE Category = 'Mathematics' OR Category = 'Art'

                            ORDER BY Price DESC, Title;

Aggregate Functions

Sometimes rather than displaying the records of a query we want to know a value that represents all those records, for example we may need to know how many records we have. This can be obtained if instead of just selecting the field, we surrounded the field with the Count function. The Count function is one of a set of functions called Aggregate Functions. They produce a number that represents the collection of records found in a query. 

 

17. How many customer do we have?

The * wildcard may obtain the data for all Customers in the Customer table. If we want to count them, all we need to do is surround the wildcard with the Count function:

          SELECT Count(*) AS NumberOfCustomers FROM Customer ;

This will produce a table with only one field (NumberOfCustomers) containing the number of Customers in that Table.

Notice that instead of using the * wildcard we could also count the number of Customer IDs:

         SELECT Count(CustomerID) AS NumberOfCustomers FROM Customer ;

18. How many customer do we have in New York? 

Adding a WHERE condition to the query limits the number of records in the output. The remaining records can be equally counted with the Count function.

         SELECT Count(*)AS NumberOfCustomers FROM Customer

                         WHERE State = 'New York' ;

19. How many Used books in Management and Physics do we have?

 

         SELECT Count(*) AS NumberOfBooks FROM Book

                         WHERE Category = 'Management' OR Category = 'Physics' ;

 

20. What is the average price for all the books? 

Another aggregate function we can use is the Avg function to obtain the average of a number field.

 

         SELECT Avg(Price) AS Average FROM Book  ;

21. What is the total number of all books sold?

The Sum function is used to add the values of a number field. Be aware this is different than counting, because here we are adding the contents of the field.

 

         SELECT SUM(Quantity) AS TotalBooksSold FROM OrderLine ;

 

22. What is the total number of all ‘Art’ books sold ? 

 

         SELECT SUM(Quantity) AS TotalBooksSold FROM OrderLine, Book

                         WHERE OrderLine.ISBN = Book.ISBN AND

                                         Category = 'Art' ;

 

23. Which are the least and the most expensive titles in the database?

Minimum and Maximum values in a number field can be obtained with the Min and Max functions respectively.

 

         SELECT Min(Price) AS MinPrice, Max(Price) AS MaxPrice FROM Book ;

 

24. What is the average price of all ordered books after discount?

Aggregate functions may also be used in temporary fields created by expressions:

 

         SELECT Avg(Price*(1.0-PercentageDiscount/100)) AS AveragedDiscountedPrice 
                          FROM Book, OrderLine

                         WHERE Book.ISBN = OrderLine.ISBN;

 

Grouping

Aggregate functions obtain representative values for the whole set of records. For example the following query obtain the average price for all books in the Book table.

25. What is the average price for used books?

         SELECT Avg(Price) AS AveragePriceUsedBooks 
                          FROM Book

                         WHERE Used;

 

However, sometimes we may need to have representative values for specific subsets of records. For example, we may need to obtain the same average price as we did before, but per category. For this situations we can use the GROUP BY clause. This clause will indicate the field that contain the values used to separate the records into different groups. In our case, we could use the field Category in the GROUP BY clause. Notice that we also need to add this field in the set of selected fields for the SELECT clause. 

 

26. What is the average price of books per category?

The query adds the Category field to the SELECT clause and uses this same field in the GROUP BY clause. The output of this query will be a table showing all categories and the average price for each of these categories.

 

         SELECT Category, Avg(Price) AS AveragePrice

         FROM Book

         GROUP BY Category;

 

We can also filter the groups we want to display. The GROUP BY clause generates all groups available in the field selected (all categories in the previous example). Adding the HAVING clause may eliminate from display some of these groups. The HAVING keyword should be follow by a condition that uses the aggregate functions in the SELECT clause. For example, we may need to obtain the average price of all books per category, but only if the average price is larger than $20.00.

 

27. What is the average price of books per category? List only averages that are bigger than $20.00

The previous query is further filtered by adding the HAVING clause with the condition that uses the same Avg(Price) used in the SELECT clause.

 

         SELECT Category, Avg(Price) AS AveragePrice

         FROM Book

         GROUP BY Category

         HAVING Avg(Price) > 20.0;

 

Be aware that the HAVING clause is only used if the GROUP BY clause is used. Do not confuse the HAVING clause with the WHERE clause. The WHERE clause puts conditions to include records in a table. The HAVING clause puts conditions to include groups in a table.

 

The following example shows the use of the GROUP BY and HAVING clauses combined with created fields, aggregate functions, and the ORDER BY clause.

 

28. List all the order numbers in ascending order number with their total value after discount.

 

         SELECT OrderNo, SUM(Price*Quantity*(1.0-PercentageDiscount/100.0))

                           AS Total

             FROM Book, OrderLine

             WHERE Book.ISBN = OrderLine.ISBN
              GROUP BY OrderNo

             HAVING SUM(Price*Quantity*(1.0-PercentageDiscount/100.0)) > 10.00 
              ORDER BY OrderNo ;

Subqueries

The SELECT command generates a table as a result. If the table contains one record and one field, the value for this field in that record can be used as a value anywhere where a value is needed. 

 

29. List all titles with price greater than the average of all books

To perform this query we first need to know the average price for all books. We could perform this query first:

 

      SELECT Avg(Price) FROM Book;

 

and then use whatever value we obtain for the average in the following query (assume the average price is $29.09) :

 

      SELECT Title, Price FROM Book WHERE Price >  29.09;

 

However, we could use the first query to replace the number directly:

 

      SELECT Title, Price FROM Book WHERE Price > 

            (SELECT Avg(Price) FROM Book)

 

The query inside the parentheses is a subquery, a query made to obtain a value and used in another query.

 

30. List all titles of all the books with the same category as the book ‘Design Basics’

In this example we can make a subquery to first obtain the category of the “Design Basics’ book.

 

SELECT Title FROM Book WHERE Category = 

                        (SELECT Category FROM Book WHERE Title = ‘Design Basics’)  ;

 

31. List the name of all customers in the same State as ‘Jay Leno’

The subquery will look for the State name for ‘Jay Leno’.

 

SELECT CustomerName FROM Customer WHERE State = 

                        (SELECT State FROM Customer WHERE CustomerName = ‘Jay Leno’); 

 

Subqueries may be nested as needed. Namely, a subquery may contain other subqueries 

 

32. List the names of all customers who bought a book from the same first author who has the most expensive book in the database

An initial subquery must be made to obtain the maximum price of the books in the database:

 

            SELECT MAX(Price) FROM Book;

With this information a second subquery will search for the AuthorID of the first author of this book:

 

SELECT AuthorId FROM Book, Wrote

WHERE Book.ISBN = Wrote.ISBN AND

               AuthorRank = 1 AND

               Price = (SELECT MAX(Price) FROM Book) ;

 

The final query will contain both of the previous subqueries and obtain the names of all customers who bought books from that author”

 

SELECT CustomerName FROM Customer, [Order], OrderLine, Book, Wrote

      WHERE Customer.CustomerID = [Order].CustomerID AND

                     [Order].OrderNo = OrderLine.OrderNo AND

                     OrderLine.ISBN = Book.ISBN AND

                     Book.ISBN = Wrote.ISBN AND

                     Wrote.AuthorID =

(SELECT AuthorId FROM Book, Wrote

WHERE Book.ISBN = Wrote.ISBN AND

                                    AuthorRank = 1 AND

                                                      Price = (SELECT MAX(Price) FROM Book) ) ;

 

In the previous query the search for the AuthordID of the first author who has the most expensive book may have produced more than one AuthorID. This would happen if more than one book have the most expensive price. In situations like that rather than testing the equality of the AuthorID field, it will be best if we can check if the values for the attribute can be found in a table. The way it will work is at follows. The first and second query will remain the same. If they produce more than AuthorID, that will be a table. Now, in the final overall query instead of checking if Wrote.AuthorID is equal to the second subquery we check if that field is inside the table for the second subquery using the keyword IN.  This keyword will take the values of the field Wrote.AuthordID, and it will check if they are inside the table created in the second subquery. If they are, they will be accepted. The query so transformed will be:

 

SELECT CustomerName FROM Customer, [Order], OrderLine, Book, Wrote

      WHERE Customer.CustomerID = [Order].CustomerID AND

                    [Order].OrderNo = OrderLine.OrderNo AND

                    OrderLine.ISBN = Book.ISBN AND

                    Book.ISBN = Wrote.ISBN AND

                    Wrote.AuthorID IN

(SELECT AuthorId FROM Book, Wrote

WHERE Book.ISBN = Wrote.ISBN AND

               AuthorRank = 1 AND

               Price = (SELECT MAX(Price) FROM Book) ) ;

 

33. List all author names with more than one written title

The first subquery must find all AuthorIDs who have written more than one title. A subquery using the GROUP BY clause can count the number of books written per author and the HAVING clause may filter this table to include only the ones for which the count is bigger than 1.

SELECT AuthorID, Count(*) FROM Wrote

             GROUP BY AuthorID HAVING Count(*) >1 ;

 

A second subquery will get just the AuthorID from the table generated above. We need to eliminate the Count(*) field because we only want to compare the AuthorID:

 

SELECT AuthorID FROM

              (SELECT AuthorID, Count(*) FROM Wrote

                             GROUP BY AuthorID HAVING Count(*) >1) ;

 

Finally, we use the table generated in this second subquery to select the records from the Author table we want with the IN clause:

 

SELECT AuthorID, FirstName, Initials, LastName

     FROM Author  WHERE AuthorId IN

               (SELECT AuthorID FROM

                             (SELECT AuthorID, Count(*) FROM Wrote

                                                    GROUP BY AuthorID HAVING Count(*) >1) ) ;

 

34. How many customers ordered more than 3 titles in an order?

SELECT Count(*)  AS NoCustomers FROM (

              SELECT DISTINCT Customer.CustomerID FROM Customer, [Order]

                       WHERE Customer.CustomerID = [Order].CustomerID AND

                                  OrderNo IN

                                  (SELECT OrderNo FROM

                                            (SELECT OrderNo, COUNT(*) FROM OrderLine

                                                            GROUP BY OrderNo

                                                                   HAVING  COUNT(*) > 3) ) ); 

 

35. List the last names of all authors who wrote a book with the author of ‘Linear Algebra’

SELECT DISTINCT Lastname FROM Author, Wrote

          WHERE Author.AuthorID = Wrote.AuthorID AND

                    Wrote.ISBN IN  

                    (SELECT ISBN FROM Wrote WHERE AuthorID  = 

                                                    (SELECT AuthorID FROM Wrote, Book

                                                              WHERE Wrote.ISBN = Book.ISBN

                                                                        AND Title='Linear Algebra' ));

 

The same way we use the IN clause to search for values inside a table generated by a subquery, we can use the NOT IN clause to find values that are not inside the table.

 

36. Get the last name of all authors who have books as single authors.

A subquery is needed to generate a table of ISBNs all books that have more than one author.

 

SELECT ISBN FROM Wrote, Author

                  WHERE Wrote.AuthorID = Author.AuthorID AND AuthorRank<>1 ;

 

The books that have only one author are NOT IN the table created in the previous query, so we can use that table to filter authors:

 

SELECT DISTINCT LastName FROM Author, Wrote      

                        WHERE Author.AuthorID =Wrote.AuthorID AND

                           ISBN NOT IN

                                    (SELECT ISBN FROM Wrote, Author

                                    WHERE Wrote.AuthorID = Author.AuthorID AND

                                               AuthorRank<>1) ;

 

Wildcards and Date Operations

Besides the * wildcard being used in the SELECT clause, we can also use it inside a string in the LIKE condition. The LIKE condition is used when a text field should follow certain format. 

 

37. Give all info from Book table of all books which title begins with the letter ‘C’.

SELECT * FROM Book WHERE Title LIKE 'C*';

38. Give all info from Book table of all books which title ends with the letter ‘A’.

SELECT * FROM Book WHERE Title LIKE '*A';

39. Give all info from Book table of all books which title has the letter ‘K’ anywhere.

SELECT * FROM Book WHERE Title LIKE '*K*';

 

The NOT LIKE clause will obtain the reverse of the LIKE clause

40. Give all info from Book table of all books which title has the letter ‘K’ nowhere.

SELECT * FROM Book WHERE Title NOT LIKE '*K*';

Another useful wildcard is the question mark (?). In a string it represents any character. It is the placeholder for one and only one character that must be presented.

 

41. Give all info from Book table of all books which title has 5 letters exactly.

SELECT * FROM Book WHERE Title LIKE '?????';

 

Dealing with Date fields may be accomplished if we transform the Date datat type into TEXT. To do that we use the function Format. Rather than using the date-typed field directly in our query we should surround the field by the Format function. The Format function requires two parameters, the first is the data-typed field and the second is String showing a format that uses DD, MM, and YYYY as proxies for the days, months and years. For example the following Format function will transform the Date field into a String with format “MM-DD-YYY”: Function (Date, “MM-DD-YYYY”).

 

42. Find all order numbers that were ordered in April 13, 2016.

If we compare the OrderDate directly with the string ‘04/13/2016’, SQL will complain that there is a type mismatch. We should use the Format Function instead, as follows:

 

SELECT OrderNo FROM [Order]

WHERE Format(OrderDate, "MM/DD/YYYY") = '04/13/2016';

 

We can also obtain the numeric value of a day, month or year using the Day, Month and Year functions on a Date-typed field.

 

43. Find all order numbers that were ordered in any April.

SELECT OrderNo FROM [Order]

WHERE Month(OrderDate) = 4;

 

44. Find all order numbers that were ordered in April 13 of any year.

SELECT OrderNo FROM [Order]

WHERE Month(OrderDate) = 4 AND Day(OrderDate) = 13 ;

 

Full-Fledged SQL-Select Command Format

            SELECT  Field1  [ , Field2 , … ]   FROM  Table1  [ , Table2 , … ] 

[ WHERE  Condition1 [ ,Condition2, … ]  ]  ;

[ GROUP BY  Field1 [ ,Field2, … ] 

[HAVING GroupCondition1[ ,GroupCondition2, … ]  ]

]

[ ORDER BY  FieldA [ASC | DESC][ ,FieldB [ASC | DESC], … ]  ]  ;

 

Field could be any field on the tables or an aggregate field and their names can be changed with the use of the clause AS.

Tables should be joined together in the WHERE section by a condition. If this is not done, the result will produce the Cartesian product of the tables.

WHERE-Conditions refer to the fields requested and must be tied together with the use of the clause. Use these conditions to specify row selection and join of Tables.

GROUP BY Fields must be requested at the beginning of the SELECT and they should include all non-aggregate fields.

HAVING clause is used only to declare conditions on the groups when GROUP BY is used.

ORDER BY fields must be requested at the beginning of the SELECT and the order of the fields indicate the precedence for sorting. The clauses ASC and DESC indicate if the sorting should be ascendant or descendent on those fields. ASC is the default.
