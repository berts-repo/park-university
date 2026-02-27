# Unit 4: Lecture - Creating Relations within Microsoft Access Database

A previous document showed how to create tables in a Microsoft Access database, and how to add/modify its primary key. This document will show how to create relations between 2 tables in the Microsoft Access database. Relations in the relational database model are established by creating foreign keys between tables.

The images presented in this document come from using Microsoft Access from Microsoft Office Version 14. Students may have to search for similar features in their software if different versions of this product are used.

Establishing a Relation between tables using a Foreign Key

Suppose a database has two tables related by a foreign key, as shown in a relational data model:

If both tables are created separately in a Microsoft Access database, their relation with a foreign key can be established by selecting the “Relationships” menu icon under the “Database Tools” tab, as shown below:

After clicking the “Relationships” menu icon, MS Access may prompt you to select the tables for the relation from a list. If it does not do that, you must select the tables individually by clicking and dragging them from the “Tables” panel on the left to the “Relationships” panel of the right, like this:

To create the foreign key relationship we click-and-drag the field that is going to be the foreign key in one table towards the field in the other table that is related to this foreign key. In our case we should click and drag the AuthorID field from the Author table (this field is the “one” part in the one-to-many relationship) towards the AuthorID field in the Wrote table (the “many” part in the one-to-many relationship). Doing that will produce the following panel:

The panel will show both fields to be connected and it will show the Relationship type to be “One-To-Many”. Here we need to click the option to “Enforce Referential Integrity” if we want to have standard database relationships. One also could select among two options: “Cascade Update Related Fields”, that will modify related tables or indexes when the value of one of the fields in the relation is modified, and “Cascade Delete Related Fields”, that will nullify fields in related tables when a foreign key is deleted. It is advisable to select all three of these options as shown:

Clicking the “Create” button will establish the foreign key relation as shown:

After all relations have been created, one can save them by clicking the “Close” button and answering “Yes” to a request to save changes to the layout of “relationships”:
