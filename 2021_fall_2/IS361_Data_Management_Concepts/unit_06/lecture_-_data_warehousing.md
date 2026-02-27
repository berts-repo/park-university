# Unit 6: Lecture - Data Warehousing

Introduction 

The purpose of this document is to highlight some of the important issues in Data Warehousing with some practical applications.

Data Warehousing

  A discipline within databases concerning on organizing historical data in a way that can be used to spot trends and guide managerial decisions.

All databases we have been reviewing in this course so far are known as transactional databases. These databases are in charge of handling day-to-day operations on businesses and other applications. If they are designed as relational databases, they are optimized to avoid data redundancy, by careful analysis of their attributes and relationships, and normalization of their tables. With time, these databases accumulate a large amount of records that may not be used in current operations. Take for example the following database:

If the database has been used for a number of years it may accumulate a large number of records: books, authors, customers and orders. It probably does not use old records frequently. It seldom reviews or modifies past transactions, unless an historical search is implemented, and when it does, it may take some time to retrieve its data, because it may be dispersed among multiple files. When this situation arisen in the first database systems, it was considered important to look for other ways to archive and organize historical data to facilitate analysis and retrieval.

A new kind of databases was created and named as data warehouses because, like brick-and-mortar warehouses do, they would store large amount of products, in this case, a company’s data. The data in the warehouse will never be modified, because it would be historical and it would be cleaned before storage to guarantee its veracity. In the design of these new kind of databases, avoiding redundancy was not a priority. Since the data would be cleansed of inconsistencies, this database may use repetition as a way to optimize data retrieval.

Data warehouses offer an overall view of the historical records of a company. In large organizations, the data warehouse may include a large number of tables, fields and attributes describing all aspects of the business. This may offer managers a grand view of their affairs and may allow then to spot trends and quantify performance. If they notice that a specific area needs to be better study, they may also focus on this area for further analysis.

Sometimes, companies may not want to invest in such wide and detailed view of their business, because it may require a lot of resources they are not able or willing to invest. However, in some situations, managers in these companies may see the need to analyze historical data from a specific area, and may want to have a small data warehouse for only one sector or aspect of their business. These smaller data warehouses, concentrated in a particular business area are known as Data Marts. Companies may start to build these data marts in areas of their business they want to study, at a reduced cost for the company. With time, companies may create data marts for other business areas and eventually they could join all of them to obtain a greater view of the company as a whole. This is in fact one way in which full-grown data warehouses are built. For the rest of this discussion and the rest of the course, we will use the generic term data warehouse to refer also to data marts, since they are basically the same idea at different scale. If the term data mart is used will be to emphasize their characteristic of a smaller size.

A data warehouse will have a different design that transactional databases. The most common design for these databases is known as the star-schema. The star-schema organizes all information around a single table known as the fact table. The fact table contains most of the data to be stored. The data is classified according to various dimensions. A dimension can be any attribute in the database system that may partition data along various categories. A partition is a technical name from set theory that indicates that all members of a set are assigned to one and only one of some given categories. Each dimension will generate a dimension table that is connected to the fact table with primary key-foreign key relations. These will be expressions of a one-to-many relations with the cardinality of 1 in the dimension table and the cardinality of many in the fact table. A record in the dimension table may be related to many records in the fact table. An important characteristic of the dimensions that classify records in a fact table is that they are usually orthogonal, meaning that they are independent of each other. Let us see an example to clarify these concepts.

Suppose that managers at the bookstore want to answer questions like these: which books are our best sellers? or, who are our best customers? or, what is the average value of an order? These questions may be answerable with a transactional database, but to answer them may involve the access of many tables in this database and a lot of computer time performing queries. This may lock up resources that could better be used to handle day-to-day operations that produce daily revenue for the company. This is the main reason why we want to have a separated database where trends in the business can be observed and managerial queries can be answered. A data warehouse will be created for this purpose.

The fact table in this data warehouse could include attributes like CustomerID, name and address of customers; ISBN, title, category, and author names of books; and order number, ordering date, delivery date, price, quantity and discount of orders. In our case all these attributes are obtainable from the original transactional database. In some other cases, external information may also be gathered to complete the data warehouse, if the administration sees that data as important for their operations. If we create a big table with all these attributes from all historical records of the transactional database, we may have a crude data warehouse, made up of only one big fact table as shown below:

However, this design can be improved. Although we are not concerned with redundancy, we still may eliminate unnecessary repetition of values by partitioning the attributes in this table along various dimensions. In this particular case, there are three attributes that can be used as dimensions:  ISBN, CustomerID, and OrderNo. All three attributes satisfy the definition of dimension: they partition all data in the fact table in various categories. Every record in the fact table will identify with one ISBN, because every book ordered by a customer has an ISBN. Every record in the fact table will identify with one CustomerID, because every book was ordered by a customer with a CustomerID. Every record in the fact table will also identify with one OrderNo, because every book was ordered via an order from a customer. Not only that, but every record in the fact table must have an ISBN, a CustomerID and a OrderNo, or such transaction would not have been possible

Furthermore, these three attributes chosen as dimensions are orthogonal: this means that they are independent of each other. An ISBN for a book does not determine or does not tell us anything about a customer or an order. Neither a CustomerID determines a particular book or an order. And while knowing an OrderNo may determine who the customer is, it may not determine a particular book in an order, since an order may comprise of many titles.  

Each of these dimensions will generate a dimension table in our data warehouse design. The dimension tables will have attributes that describe the dimension values singularly. For example, The Customer Dimension may include information that will never change about individual customers. This information may include attributes like CustomerID, customer name and address. The following is table shows these attributes grouped around the Customer Dimension and using CustomerID as their primary key:

Each record in this table describes a unique customer. Notice that in the transactional database we have different names for the customer name and address attributes. They do not have to match. The data warehouse is created independently of the transactional database and the designer is free to use information any way they think it is appropriate. The non-key attributes in this table will be taken out of the fact table. Namely, name and address will be eliminated from the fact table and only the CustomerID field will remain. CustomerID will be a foreign key in the fact-table referencing the attribute with the same name in the Customer Dimension. This way we eliminate unnecessary duplication in the fact table.

Similarly, the Order Dimension may include information that is common to all Orders, like OrderDate and DeliveryDate. Having the OrderNo as the primary key in this table, the Order Dimension will look like this:

Each record in this table describes a unique order. As it was done for the Customer Dimension, the attributes OrderDate and DeliveryDate are taken out from the fact table and grouped with the OrderNo field in this Order Dimension table. The attribute OrderNo is the primary key on this table. The fact table retains the OrderNo as a foreign key to relate to the Order Dimension table.

The Book Dimension is obtained with a similar process. Every book can be described by its ISBN, title, category, price, discount, used status, authors’ ranks, and authors’ names as follows:

However, notice this time that, to make the Book Dimension a proper relational table we need to join the ISBN attribute with the AuthorRank attribute as the primary key. This is because each book may have more than one author. Unfortunately, adding AuthorRank as part of the primary key destroys the concept of a dimension for this table. A book may have two authors. When this happen, the same book in the fact table will be associated with two records in the Book Dimension, one for each of the two authors. This will not partition the fact table (a condition of the star-schema), because the same record will be associated to two different categories in the Book Dimension.

This problem is produced by the fact that the tentative Book Dimension table is trying two describe two independent entities: The Book and its Authors. Separating these two entities is the logical solution to this problem, as the following diagram shows:   

In this new diagram, each record in the Book Dimension describes a single book in the database only once, with its unique attributes of ISBN, title and category. Title and category attributes can now be taken out from the fact table and grouped with the ISBN field in this Book Dimension table. ISBN is the primary key on this table. The fact table retains the ISBN attribute as a foreign key to relate to the Book Dimension table. AuthorRank and AuthorName attributes are also eliminated from the fact table, and placed in the Author table. The Author table is not a dimension, just a table that describes better some attributes of the Book Dimension (the authors of a book). However, the information in the Author table is no longer needed in the fact table, since it can be found thru the relation it holds with the Book Dimension.

An aside note for the acute reader: the conversion from a single table to the two related tables above is just an example of normalization from a second normal form to a third normal form, where all transitive dependencies are eliminated.

Another less crucial modification, could be made to the Book Dimension. Given that category names will be repeated a lot, we could give a code to each category and have a separate table with their description. This way we only use the code in entries for the fact table. This modification may look like this:

As it was said, this is not such important modification, but it may save some time when dealing with these fields. What readers may notice is that category could have been used as a dimension on its own in the data warehouse, like any other attribute that causes a partition may have.  We could have left the category as part of the fact table and link it directly to a Category Dimension that looks pretty much like the Category table shown above. However, category is an attribute of books, and therefore, dependent of the ISBN: each ISBN determines a particular book and each book should belong to a single category, if category is a dimension. If we keep category in the fact table, we would have to eliminate ISBN from this table, because they are not orthogonal. ISBN determines a category. Since we cannot eliminate the Book Dimension, we put category as one of its attributes.   

Finally, notice that the attributes Price and Used were not carried along with the Book Dimension. This, in fact, points to a flaw in the design of the original transactional database. Notice that in the original database, the Book table contains these two attributes. What it means is that books would only have one price at all times and they will be either “new” or “used”. This design did not allow to have books in different conditions and at different prices, depending of these conditions. They also make impossible to track the price of a book thru time, because the current price is the only one being stored. The transactional database should be corrected and updated. Mistakes like that are bound to appear when, in the process of creating a data warehouse, the design of a database is inspected. Also, in general, the team in charge of the data warehouse is different to the one in charge of the transactional database. When a mistake like that is found, the team working on the data warehouse may inform the team working in the transactional database, but they will not correct the actual transactional database. What they will do is to design around the problem and incorporate solutions that will work in the future with their own data warehouse design. In this case, the solution is to leave the Price and Used on the fact table, which means that every order by a customer of a book will carry its own price and its own “used” condition. When actual records are loaded in the data warehouse, some decision will have to be made regarding which prices and “used” conditions are going to be loaded on these attributes. Maybe historical records can be obtained from sources other than the transactional database, or some assumptions can be made that would produce more truthful values. However, the important part is that the data warehouse would have a ready-made solution that will improve the quality of the information.

With all these considerations, the final design for the Book Store Data Warehouse will be as follows:

A database created with this design can be populated mainly with information from the transactional database. For example, the Fact-table could be constructed with the following command applied to the transactional database:

 CREATE TABLE Fact-Table
SELECT Customer.CustomerID, Book.ISBN, OrderList.OrderNo, 
                Quantity, Price, PercentageDiscount, Used
       FROM Customer, OrderList, OrderLine, Book  
      WHERE Customer.CustomerID = OrderList.CustomerID AND
                 OrderList.OrderNo = OrderLine.OrderNo AND
                 OderLine.ISBN = Book.ISBN;

This commands shows how a SELECT command can be used to generate a new table when using it in conjunction with the CREATE TABLE command.

There may be external sources that can complement or add information to the data warehouse, but they will need to be incorporated as attributes, fields and tables, following the same process of analysis and design.

Once the data warehouse is implemented, its data can be analyzed with multiple techniques and under various points of view, independently of the transactional database. There is usually specialized and dedicated software to perform this analysis, but at a minimum, we can still extract information from the database using the same SQL commands we use in transactional databases. For example, as indicated earlier, managers may be interested on knowing: which books are our best sellers? If we define as best sellers the books that have sold the most copies, this can be answered with the following query to the data warehouse:

SELECT FACT-TABLE.ISBN, Title, SUM(Quantity) as CopiesSold
     FROM FACT-TABLE, [BOOK DIMENSION]
     WHERE FACT-TABLE.ISBN = [BOOK DIMENSION].ISBN
     GROUP BY FACT-TABLE.ISBN, Title
     ORDER BY SUM(Quantity) DESC;

The first records produced in this query will be the ones with most copies sold.

If on the other hand we define as best sellers the books that produced the most revenue, we can query the data warehouse as follows:

SELECT FACT-TABLE.ISBN, Title,
SUM(Quantity*Price*(1.0-PercentageDiscount/100.0)) as Revenue
     FROM FACT-TABLE, [BOOK DIMENSION]
    WHERE FACT-TABLE.ISBN = [BOOK DIMENSION].ISBN
    GROUP BY FACT-TABLE.ISBN, Title
    ORDER BY SUM(Quantity*Price*(1.0-PercentageDiscount/100.0)) DESC;

Once again, the books that produced the most revenue will be in the first records produced by this query.

Managers may want to know which are the categories that are the best sellers. To find this out, we need to incorporate the Category table in our query. Once again, we have two ways to define the best seller categories. If we use the number of books sold in a category, a query that may provide the answer would be:

SELECT Code, Description, SUM(Quantity) as CopiesSold
      FROM FACT-TABLE, [BOOK DIMENSION], CATEGORY
     WHERE FACT-TABLE.ISBN = [BOOK DIMENSION].ISBN AND
                   [BOOK DIMENSION].CategoryCode = CATEGORY.Code
     GROUP BY Code, Description
     ORDER BY SUM(Quantity) DESC;

The first records produced in this query will be the ones of categories with most copies sold.

Again, if instead we define as best sellers the categories that produced the most revenue, we can query the data warehouse as follows:

SELECT Code, Description,
SUM(Quantity*Price*(1.0-PercentageDiscount/100.0)) as Revenue
     FROM FACT-TABLE, [BOOK DIMENSION] , CATEGORY
     WHERE FACT-TABLE.ISBN = [BOOK DIMENSION].ISBN AND
                   [BOOK DIMENSION].CategoryCode = CATEGORY.Code
     GROUP BY Code, Description
     ORDER BY SUM(Quantity*Price*(1.0-PercentageDiscount/100.0)) DESC;

Here again, the categories that produced the most revenue will be in the first records produced by this query.

Managers may also want to know who are our best customers? This could be defined as the customers which produce the most revenue. If that is the case, a query similar to the last one can be used, except that now the grouping attribute is the CustomerID and Name:

SELECT FACT-TABLE.CustomerID, Name,
            SUM(Quantity*Price*(1.0-PercentageDiscount/100.0)) as Revenue
     FROM FACT-TABLE, [CUSTOMER DIMENSION]
     WHERE FACT-TABLE.CustomerID = [CUSTOMER DIMENSION] .CustomerID
     GROUP BY FACT-TABLE.CustomerID, Name
     ORDER BY SUM(Quantity*Price*(1.0-PercentageDiscount/100.0)) DESC;

Finally, if managers ask “what is the average value of an order?” The following can be done: First create a table that contains the value of each Order as follows:

CREATE TABLE OrderValues
     SELECT OrderNo, SUM(Quantity*Price*(1.0-PercentageDiscount/100.0)) as Revenue
          FROM FACT_TABLE
          GROUP BY OrderNo;

Having created that table, we can now query it with the following:

SELECT AVG(Revenue) as AverageRevenue FROM OrderValues;

This will produce the average revenue per all orders. This also shows another use of creating tables directly from a select.

All these queries could also be similarly composed in the transactional database, but they would have compromised operational resources. It is best if we have a separate database to perform ad-hoc queries and operations.

A final point regarding data warehouses. They are created to give an historical perspective on data. Because of that, they generally involve a time dimension. This can be done explicitly with a table that contain dates, time, or temporal events. These attributes would be described in the time dimension table and used as foreign keys in the fact table. However, the time dimension can also be implicitly incorporated in the data warehouse design. This is what we did in the design of the data warehouse for the book store. The temporal dimension is implicitly given by the Order Dimension. This dimension marks the pass of time with its OrderDate and DeliveryDate attributes. The OrderNo attribute is therefore a proxy for time.

An important point to notice in this discussion is that, if implemented as relational databases, data warehouses can also be treated as any other transactional table. They will respond to the same SQL commands and produce results like any other relational database. Data warehouses may also be created in other environments, but they go beyond the scope of this course.
