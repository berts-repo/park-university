# Unit 3: Content Highlights - From ERDs to Relational Data Model

This page highlights the main points on the conversion of Entity-Relationship Diagrams (ERDs) into Relational Data Models, and complement some of the textbook explanations. It is recommended to first read this week’s assigned chapters from the textbook, and then come back to this document for further commentary.

The highlights of this week’s readings are:

Converting Entities onto Tables

The relational data model is an intermediate model between ERDs and an actual database. We must convert ERDs into a database model and from then we can create the real database in a database management system.

One could certainly ask: why don’t we design the database directly onto the relational data model? Why do we need ERDs? The reason is that relational databases are not the only kind of databases around, but they are the most widely used, that is why we study them in detail. If we had to deal with other database model, we could convert the ERD into that model before implementation. We are creating ERDs first, to have a model that defines the data in our system independently of the data model in which is going to be implemented. This gives flexibility to our approach. In the future, if other kinds of databases are the norm, we still use ERDs to describe the data, but we would use the models of the new databases.

The basic unit of the relational data model is the table. Most students should be familiar with the concept of a table as a set of rows with columns. This is the same in the relational data model. All data in the database will be stored in tables like this. A table is also known as a relation. Do not confuse the term relation with relationship. The term relation is synonym with the term table in the relational data model. The term relationship is only used when dealing with ERDs, to indicate interaction between various entities.

Each entity in an ERD must be converted onto a table in the relational data model. The way to do this is as follows: every attribute in the entity is converted onto a column in a table. Columns in this table are also known as fields. Every entity instance from the entity will become a row in the table. Rows in this table are also known as records. A simple example of this procedure is shown below. In a previous unit we had the following Book Entity:

 

This entity will be transformed in a table represented by the following structure in the relational data model:

 

Each attribute on the Entity is converted onto a box with the name of the attribute inside the box. Each box represents a column (a field). The attributes that make the identifying attribute are all underlined, just like with the entity. The name of the entity is located above the table over the left corner. Even though we only see a line of headings, it is assumed that all entity instances with specific values for the attributes (the records) will be listed below the fields in this representation. We should think of this representation as a table on which we are only looking at the headings.

Well-defined tables in the relational data model have the property that they do not have duplicate records. Two records in the table could have the same values for some fields, even have most of the field values being the same, but at least one the fields must have different values between them. This property allows recognition of individual records within a table. We previously discussed that it was important that entities have an identifying attribute. The reason why we required this identifying attribute is now evident. It guarantees that, after conversion, the records in the tables we obtain have fields with different values, at least on the identifying attributes. In the relational data model, the identifying attributes are known as the keys. There could be more than one identifying attribute in an entity, however, for the relational data model, we chose one of them to become what is called the primary key. All other keys are known as the candidate keys. For example, in a Person entity, that represents people, there could be attributes for SSN, Driver’s License Number, and Passport Number. All of them are keys on their own, but we must select one of them to become the primary key for the table. The other two that were not chosen would be the candidate keys. A composite attribute may also become a primary key. The key is made up of the combination of the attributes in the composite, and it is the combination that should be unique.

To further guarantee that we can recognize and retrieve every record in a table using the primary key, relational database management systems enforce a property known as the “Entity Integrity”. This property requires that the primary key in every table cannot be null. At any time we must be able to recognize and retrieve a record by using its primary key.

Converting Composite Attributes

When converting entities in ERD to the relational data model, composite attributes are separated and each attribute that makes up the composite gets a box on its own. The name of the complete composite is lost and it is not translated onto the table at all. If the composite attribute is an identifying attribute, all attributes that make up the composite in the entity will have their corresponding fields underlined in the table. The book shows an example with the following ERD:

 

 

In the relational data model, the composite CustomerAddress attribute is represented by fields with the names of the attributes that make up the composite:

 

No mention of the original CustomerAddress field remains.

Converting Multivalued Attributes

The relational data model requires that every cell on the table (an attribute in a record) should have only one value. No multivalued attributes are allowed (known in the relational data model as Repeating Groups). We need to convert all multivalued attributes onto single value attributes.

Rather than producing only one table, the conversion of entities with multivalued attribute to the relational data model produces two or more tables. One with all attributes, except the multivalued ones, and the other tables with independent multiple value attributes and the identifying attribute. For example, suppose we have the following ERD with only one multivalued attribute (Skills), as shown in the textbook:

 

This ERD shows that an employee may have many Skills. To convert this entity onto the relational data model, we create two tables: one table containing all attributes, except the multivalued one, and a second table with only the multivalued attribute and the identifying attribute of the Entity. In the second table, the multivalued attribute is no longer multivalued, but a single valued attribute. All Employee’s Skills are now single records of this table. The identifying attribute of the Entity is added to this table to know which Skill belongs to which Employee. The primary key for the first table is the identifying attribute. The primary key for the second table is the composite of the identifying attribute with the Skill attribute, because the identifying attribute of the entity will be repeated. The resulting tables look like this:

 

 

A sample of the second table may include values like the ones shown below:

 

What the textbook does not show is that if the Employee entity would have not only one multivalued attribute, but two independent multivalued attributes, like Skills and Degrees, then the relational data model would include, not two, but three tables: the ones shown above and a third one like this:

 

This third table will also have a relation with the first table, because their EmployeeID attributes should match, therefore a solid arrow should point from the third to the first table, as the second table does. More on these relations will be explained in the next point.

At this point I want to call your attention to an example in the textbook. It shows how to eliminate the multivalued attributes that does not break the entity onto multiple tables. It shows a table of orders, in which each table has multiple products per order:

 

Take note that the previous table is not considered to be a table yet, as required by the relational data model, because each order contains many products. Let us call it a listing instead. To convert this listing onto a relational table, rather than creating separate tables, the textbook repeats all common data about an order for each one of the products within the order. Therefore a single record for an order having multiple products is converted into multiple records with the same common data for the order (OrderID, Date, and Customer data), but each one containing only one different product and its related information (ProductID, Description, Finish, Standard Price, and Ordered Quantity):

 

 

In terms of our relational data model that does not show records, this table would be represented by the following:

 

This table has many attributes, so to display it better, it has broken in three rows, but each row is part of the same table. The breakage is indicated by the uncompleted boxes at the end of each row.

The problem with this example is that no good designer would create a table like the one shown. If one follows the process of writing an ERD fist, the entity that produces this table would have to be something like this:

 

This entity is having 5 multivalued attributes, but they are all related to each other, they are not independent. When we talk about certain ProductID, we are also talking about its description, finish, and price. These indicate that Product is a source of data, and it should be an entity on its own. The same would happen to Customer, even though it has no multivalued attributes. Any knowledgeable person drawing ERDs like ourselves would know to have something like we had last week instead:

 

The ERD shown above lacks multivalued attributes, making the design easer to translate. The point of this observation, is that this example in the textbook is not a good example to follow when converting multivalued attributes. The best method is to produce multiple tables, not one. The book’s authors included this example, not to show how to convert multivalued attributes, but they wanted to show an example that later they can use when explaining normalization, a topic we will talk later in this unit. Do not follow this example in your conversions.  

Converting Relationships

 

Relationships between tables in the relational data model are implemented by having fields in one table making reference to fields with similar values in other tables. For example, if we go back to the example on employees’s skills and degrees from the previous point, we saw that after converting the ERD into tables, the field EmployeeID was added onto the EmployeeSkills table and the EmployeeDegrees table. The field EmployeeID in these tables is making reference to the Employee identified by this EmployeeID in the Employee table. The EmployeeID field in the EmployeeSkills table and EmployeeDegrees table do not necessarily contain all employees in the database. They only have the ids of employees with skills or degrees. These fields are not unique either, because an employee may have multiple skills or degrees. However, their values must match one of the values inside the EmployeeID field in the Employee table. Otherwise we are having a skill or a degree for an employee that does not exist in our database. Fields like EmployeeID that reference primary fields in other table are known as foreign keys. EmployeeID in the EmployeeSkills and EmployeeDegrees tables are foreign keys, because they must match their values with a value inside the primary key EmployeeID for the Employee table. A foreign key may or may not be part of the primary key in its own table. That is not required. In this example, the EmployeeID field in both, EmployeeSkills and EmployeeDegrees tables, are part of their primary keys, but this does not have to be the case all the time. The name of the field does not have to match either. The field could be called EmployeeID in the Employee table and have different name in the other two tables. What is important is the reference made from the foreign key to a primary key in another table. This reference is represented by an arrow going from the foreign key in one table to the primary key in the other table.   This can be seen in the relational data model shown in above, with the Employee and EmployeeSkills tables. Foreign keys may be represented by underlining the key with a segmented line.

The fact that foreign keys must match their values with the primary key of another table is enforced on real relational databases by what is known as the referential integrity constraint, a second constraint imposed by the relational data model to make them work properly. The referential integrity constraint states that a foreign key must match a value within the primary key of another table or it must be null. In the example above, the EmployeeID field on the EmployeeSkills and EmployeeDegrees tables should match a value on the EmployeeID field in the Employee table, otherwise their value should be null. In our example with employees, the value EmployeeID on the EmployeeSkills and EmployeeDegrees tables will never be null, because the field is part of the primary key for these table. Entity Integrity constraint guarantees that the primary key is never null. In other situations where the foreign key is not part of the primary key for a table, the value of the foreign key could be null, indicating that among this particular record has no value among all possible values in the referenced table.  Entity Integrity and Referential Integrity constraints are the pillars over which real relational databases are built. 

The following cases will show how to convert various kinds of relationships into relational data models. Most of them follow the same principles described in the previous example: we create a relationship by adding or selecting an attribute in a table that will be a foreign key referencing a primary key in another table.

 

Strong Entity-Weak Entity Relationships. 

This relationship is as simple to convert as the one for multivalued attributes. All we need to do is to have a field in the Weak Entity to be a foreign key for the identifying attribute of the Strong Entity. We also make this foreign key part of the primary key for its table. The textbook shows the following relationship as an example:

This can be converted onto the following tables. Notice that an EmployeeID field was added to the Dependent table as a foreign key and as part of its primary key. It references EmployeeID, in the Employee table.

 

 

One-to-One Relationships. 

This kind of relationship means that there is only one possible entity instance in one entity that can be associated with another entity instance in the other entity. The textbook provides the following example of the Nurse entity in charge of a Care Center. Only one Nurse can be in charge of a Care Center at any given time:

The way to convert this relationship onto tables is by adding a field in the CareCenter table that contains the identifying attribute of the Nurse entity, as follows:

One-to-Many Relationships. 

Converting this relationship is similar to converting dependent relationships. The primary key in the table on the “one” side of the relationship becomes the foreign key in the table for the “many” side of the relationship. The example from the textbook is:

Converted onto tables we have:

The CustomerID attribute was added to the Order table to become a foreign key in the Customer table.

Relationships with Associative Entities. 

Associative entities will be converted onto tables, the same way other entities are also converted. Their relationships are mostly one-to-many relationships with other tables, in which they are in the “many” side of the relationship. For each of this relationships, the identifying attribute of the table with the “one” side of the relationship will be added as a field in the table for the associative entity. Each one of these added fields is a foreign key for the associative entity. If the associative entity does not have already an identifying attribute, then the composite of all these added fields will become the primary key for the associative entity. The textbook shows the example of an order of products. The order has many order lines, and each order line contains a product, as follows:

When this ERD is converted onto tables it will look like this:

The OrderLine entity has for primary key the composite of the attributes OrderID and ProductID. Each one of them is a foreign key for the table.

Many-to-Many Relationships. 
The textbook shows how to convert a many-to-many relationship, but if you follow the advice given in the previous unit, it would be better to convert a many-to-many relationship onto a set of one-to-many relationships. Having done that in the ERD, we will only deal with conversions of associative entities.

Ternary Relationships. 
Similarly to many-to-many relationships, if ternary relationships were converted onto one-to-many relationships in an ERD we would need to deal only with these relationships in the same way as we do with associative entities.

Unary Relationships. 
Unary relationships are a particular class of conversion to tables, because there is only one table in the ERD, and the relationship is established from this entity to itself. Based on the cardinality, this relationship could be a one-to-one, one-to-many or many to many. The procedure to deal with one-to-one and one-to-many relationships is the same as described for the cases with the same names, above. The only difference is that the added fields to represent the relationships are added to the only table we have. For example, the textbook shows the example of the relationship “employee manages employee”:

To convert it to a table, we add the field ManagerID that contains the EmployeeID of the manager for that particular employee. This is a foreign key that references the primary key within the same table:

The textbook also shows an example of a many-to-many unary relationship of an item containing other items in various quantities, for example, the item rack of spices, containing spices of various kinds, each one an item on its own:

Even though the book shows a way to convert this relationship onto tables, I would remind you that it is best to convert many- to-many relationships onto one-to-many relationships first before doing the conversion to tables. You may do this transformation yourself and then convert the new ERD onto tables. You will see that the tables generated are similar to the ones show in the textbook conversion:

Surrogate Keys

It maybe time consuming to have to deal with the fields that make up a composite primary key, especially if this primary key is made up of three or more fields. To avoid this problem, database designers may add an extra field to the table, known as the surrogate key. The purpose of this field is to become the primary key for the table, taking over this role from the composite primary key. As any other primary key, the surrogate key will have a unique value for every entity instance in the table, and it will identify records uniquely. Every other field remains the same, even the fields that made up the composite.

You may see an example of the application of these ideas in the Lecture  [link: https://canvas.park.edu/courses/64263/files/8477713/download?verifier=LmSPnIQiNMDqjMHNGpgPrxoezrUtEmu6Rp2lwNpK&wrap=1] Unit 3: Example of Conversion ERD to Tables.

Some figures in this document were taken from the textbook material (Hoffer, Jeffrey A., Ramesh, V., Topi, Heikki, Modern Database Management, Twelfth Edition, Prentice Hall, 2016).
