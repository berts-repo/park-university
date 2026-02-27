# Unit 3: Lecture - Example of Conversion of ERD onto a Relational Data Model

In a previous unit we showed an example of the creation of an ERD. The analysis of the case produced the following diagram:

 

To convert this ERD onto the relational data model, we have two general steps: converting all entities into tables with their own primary keys, and then convert relationships into foreign key fields on the tables.

Converting Entities into Tables

The first step is to create tables from the entities by assigning a field in every entity to a column in a table, as seen below. All entities generate a table, even the associative entities. The last table in the design below (Customer) has many attributes, so to display it better, it has broken in three rows, but each row is part of the same table. The breakage is indicated by the uncompleted boxes at the end of each row. Notice that names of composite attributes are omitted in all tables and only the names of the attributes inside the composite were added to the tables. The identifying attributes are underlined in the tables and they become the primary keys for their corresponding table. Some of the tables are missing a primary key. To complete this step we must create foreign keys for them.

 

The Author table misses a primary key. We have two options to fix the problem. We either make the whole name of an author the primary key. This may fix the problem, unless there are authors who have the same full names. To avoid this situation, it would be best to add a code attribute that uniquely identify authors in the database. Let us call this new attribute AuthorID. This will be the primary key for the Author table.

The Wrote table also misses a primary key. This table is an Associative table. The primary key for an associative table can be a composite attribute made of the primary keys of the entities to which it is associated. In this case, the table Wrote is associating the Author and Book Tables, therefore the Wrote table should include as fields the primary keys of the Author and Book tables, AuthorID and ISBN, respectively. The composite of these two attributes in the Wrote table will be its primary key.

With these changes, the tables after Step 1 look as follow:

Converting Relationships Into Foreign Key Fields

The second and final step is to translate the relationships in the ERD into Foreign Relationships links. Because this diagram has only 1-to-many relationships, it is easy to perform this step. All we need to add is an arrow from every table with the “many” side of a relationship to a table with the “1” side of the relationship. This arrow has to end in a field that contains an identifying attribute. This will become the foreign key. The arrow should begin in a field that will match the type of data the foreign key contains. For example, the 1-to-many relationship between the Author and Wrote entities will be translated onto an arrow leaving the AuthorID field in the Wrote table (the “many” side of the relationship) and arriving at the AuthorID field in the Author table (the ‘1’ side of the relationship). AuthorID will be the foreign key for this relationship. After this procedure is completed, the final set of tables for the relational data model would look like this:
