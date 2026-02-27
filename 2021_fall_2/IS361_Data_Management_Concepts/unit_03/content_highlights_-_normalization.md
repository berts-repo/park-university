# Unit 3: Content Highlights - Normalization

Normalization is all about avoiding redundancy. When tables are normalized, they avoid duplicating data in their fields. Most redundancy is introduced in databases because they were not designed as normalized tables from the start. Some of these tables come from legacy traditional file processing systems and they have not been re-designed according to current database creation principles. The textbook explain the advantages of normalizing tables in our database designs and show the steps to achieve normalization up to what is known as the Third Normal Form. This is the most widely used normalization form.

The key of normalization is what is called functional dependency. The value of an attribute or field in a database system may depend of one or many other attributes or fields. This is what functional dependency means. Examples are evident in tables we created from ERDs in this unit. Let us take a look to the Book table we had:

 

If we defined the Book Entity correctly and translated it into a table correctly, there is a field in the table from which all other fields are functionally dependent. This attribute is the primary key. All fields in a table should be functionally dependent of the primary key. What does this mean? It means the following: if somebody tells us the ISBN (the primary key) of a book, that value alone identifies a unique book record from which the values of all other fields are completely defined: title, category, copies and price. If on the other hand, somebody gives us the category of the book, we could not pinpoint a unique book instance with certainty, because, in general, there are may be more than one book on the same category. The same goes for the other fields. If somebody gives us the price, or the number of copies, or even the title of the book, we will not be able to pinpoint a unique book record with certainty, because, in general there maybe more than one book with the same price, same number of copies or same title. We occasionally may find an actual table in which a value for a category, a title, a number of copies or a price are the only ones in their respective field. This may be so, but it does not mean that these values functionally define all other fields, because one cannot say at all possible times, that if one knows the price, one knows which book one is talking about. 

Let me also point out that if the primary key is a composite field, all other fields in the table are not functionally dependent of the individual fields that make up the composite primary key, but they are functionally dependent of the composite primary key as a whole.

If the table has other candidate keys, we will also say that they are functionally dependent from the primary key. The opposite is also true, that the primary key is functionally dependent of each one of the candidate keys. We could even say that all non-key attributes are also functionally dependent of all these candidate keys. However, since we already selected the primary key as the most representative of all possible keys for the table, we can dismiss all dependencies to the candidate keys and consider only that all fields in a table should be functionally dependent of the primary key.

Functionally dependency in a table may be represented by arrows coming from the field (or the fields in a composite primary key) that determine the functional dependency and arriving to each one of the dependent fields. The book table showing functional dependencies will look something like this:

 

Caution: Please do not confuse the arrows in functional dependencies with the arrows used in foreign key relations. As a norm, both kinds of arrows never appear together in a diagram. Further on, arrows for functionally dependencies always go between fields in a same table. Arrows used in foreign key relations always go from a field in one table to another field in another table.

If all fields in tables in a relational data model are dependent only of their primary key, then the design could be considered to be at least in Third Normal Form and redundancies of data in the design have been eliminated. As said before, if we follow the process of writing ERDs and translating them to relational tables correctly, chances are that all our tables will contain fields that are functionally dependent of their primary keys, but we need to check that. And in checking them we may find certain anomalies that need to be corrected in order to avoid redundancies. 

The textbook presents an example of a listing with repeating groups. We have previously used this listing to explain conversion onto the relational data model. This is the listing again:

 

As we previously said, this listing is not presented by the textbook as a model of the kind of tables we should design. It is not even a table in the spirit of tables in the relational database model. Actually, the purpose of this listing is to show us how to go about normalization. Let us consider this listing a typical file we would find in a legacy file processing system. We should attempt to modify this file into a set of normalized tables in third normal form that will eliminate data redundancy.

As before, the first problem with this listing is that is not a table, because it contains repeating groups. We eliminated this problem before by repeating all common data about an order for each one of the products within the order. This converts the listing into a table in first normal form in the relational database model. A table is in first normal norm (1NF) if it does not contain repeating groups (multivalued attributes). Here is our table in 1NF:

 

Having the table in 1NF, the next step is the analysis of functional dependencies among all fields in the table. Such analysis may provide the following functional dependencies:

The dependencies found in the previous figure can be described as follows:

 

Given the OrderID we are able to determine which was the Order Date, what is the CustomerID, her/his name and her/his address. The opposite is not truth. There could be many orders in a given date, and a customer may have placed multiple orders the same day. OrderDate, CustomerId, CustomerName and CustomerAddress are all functionally dependent from OrderID.

Although the OrderID may determine the CustomerID, her/his name and her/his address, we could also determine the name and address of a customer just by knowing the CustomerID. Therefore Customer’s name and address are functionally dependent from the CustomerID.

Knowing the ProductID alone may tell us the description of the product, its finishing, and its standard price. ProductDescription, ProductFinish, and StandardPrice are functionally dependent of ProductID.

Given an OrderID and a ProductID, it is possible to know how many products of this kind were requested in this particular order. The opposite is not true. Given an ordered quantity it may not be possible to tell neither the ProductID, nor the OrderID.

It is noticeable that not all fields in the table are only functionally dependent from the composite primary key (OrderID-ProductID). There are two other kinds of dependencies that we should eliminate to have the table properly normalized.

 

Partial Dependencies

The first kinds of dependency that need to be eliminated are partial dependencies. Partial dependencies are the functional dependency a field has to a partial key. A partial key is only a part of a composite primary key. By definition, it only occurs when the table has a composite primary key. In our example, the fields ProductDescription, ProductFinish, and StandardPrice are functionally dependent of the composite primary key OrderID-ProductID, but also of ProductID on its own. These are partial dependencies. The way to eliminate these dependencies is as follows:

 

Create as many tables as can be created with the all possible combinations of the fields that make up the primary key.  In our case, we have two fields in the primary key: OrderID and ProductID, so we create a table that only contains the OrderID field, another table that only contains the ProductID field and finally a table that contains both the OrderID and The ProductID. Three tables in total.

A good strategy is to create first all tables with only 1 field from the primary key. Then, we can create tables with two fields from the primary key, and so on, until the last table contains all fields from the primary key. If the composite primary key is made out of n fields, the number of tables to be created will be 2n -1. The primary key in each of these tables is made of all the fields they contain so far. 

Starting with the created tables with smaller number of fields, towards the ones with more fields, assign all the remaining fields in the original table to the table that contains the smallest number of fields to which they are fully functionally dependent. Assign each field only to one of the newly created tables.

In our example, The new tables with small number of fields are the one containing OrderID, and the one containing ProductID. We should assign to the OrderID table all fields that are functionally dependent only of that field and not of ProductID. These are: OrderDate, CustomerID, CustomerName, and CustomerAddress. Similarly, we should assign to the ProductID table all fields that are functionally dependent only of that field and not of OrderID. These are: ProductDescription, ProductFinish, and StandardPrice. Finally, the remaining fields will necessarily be functionally dependent of both OrderID and ProductID. The only field like this is QuantityOrdered, so it is added to the last table. There should be no more fields to be added from the original table into the new tables at the end of this process. If by some chance, any new table does not have fields that were added to them, we should discard this table, because there is no field that is functionally dependent from it.

The sets of tables we obtain after this process is in second normal form (2NF). Our example in 2NF looks like this now:

 

Transitive Dependencies

The first of the three tables we obtained in the previous step still has fields that are not only dependent of the primary key, but they are also dependent of a non-key field: CustomerID. Notice an error in the textbook with a similar diagram (titled “Removing partial dependencies”): it does not include the dependencies of CustomerName and CostumerAddress from the primary key, OrderID, even though they were present in the diagram of the same example in 1NF (titled “Functional dependency diagram for INVOICE”).

 

A transitive dependency is a dependency to a non-key field. This is what is shown in the first table on the previous figure. To eliminate transitive dependencies, we need to move all fields that are functionally dependent of a non-key field into their own separate table, including a copy of the non-key field. This copy of the non-key field becomes the primary key in the new table. The original non-key field that is left in the original table becomes a foreign key for the new table. There will be one additional new table for each non-key and the variables that functionally depend of it. The following is the diagram for our example without any transitive dependency. Notice that all fields in all three tables now depend uniquely of their respective primary keys. This design is now considered to be in third normal form (3NF):

 

Remember that the previous table is only showing the functional dependencies. A proper representation of this design in 3NF will not include the functional dependencies because in 3NF it is given that all fields in a table are functionally dependent of their primary key. What we have to show instead are the links to foreign keys. The final design in 3NF that includes these links will be something like this:

 

There are other higher normal forms, but they are beyond the scope of this course. For most common databases, 3NF is enough to avoid most redundancies.

Some figures in this document were taken from the textbook material (Hoffer, Jeffrey A., Ramesh, V., Topi, Heikki, Modern Database Management, Twelfth Edition, Prentice Hall, 2016).
