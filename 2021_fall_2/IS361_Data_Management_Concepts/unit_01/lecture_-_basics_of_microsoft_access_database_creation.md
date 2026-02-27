# Unit 1: Lecture - Basics of Microsoft Access Database Creation

This page shows some basic activities that can be performed inside Microsoft Access. This will refresh students’ memories on some basic operations needed to complete Assignment 1 in Unit 1. This course will use Microsoft (MS) Access as a medium to apply database concepts in assignments. Students are expected to be familiar with this software from pre-requisite courses like CS140, Introduction to Computers, or from other personal experiences. It is the responsibility of students to remember or familiarize her/himself with MS Access.

The images presented in this document come from using Microsoft Access from Microsoft Office Version 14. Students may have to search for similar features in their software if different versions of this product are used.

Creating a Table

After opening Microsoft Access, one can create a blank database by double-clicking on the icon with labeled “Blank Database”:

 

A MS Access database contains sets of tables. Tables contain the database’s information. Each table contains columns with attributes. Every row on the table is a collection of values for each one of these attributes, hopefully representing data from the same entity. When the database is empty, MS Access will prompt users to enter information for a table named “Table1”, like this:

 

The best action to take will be first to define completely the table columns, before entering data. To do so we need to change the view above (known as the Datasheet View) to a Design View. We do this by right-clicking over the name of the table tab above and select “Design View” on the Drop-Down Menu, like this:

This will prompt the user to enter a name for the table to be saved:

 

Enter a name for the table. The design view will display as follows:

 

In the Design View we need to define all columns (fields or attributes) for this table Every column must have at the minimum a unique Field name within the table (this should be typed) and a Data Type (Text, Number, Date/Time, Currency, Yes/No, Calculated, etc.),  that can be selected from a Drop Down Menu. The following image shows sample of integer values, currency, text, and Boolean (Yes/no) data types:

 

When selecting a data type, MS Access will give the many options to customize the data type. For example when selecting a Numeric data type, we can select to make it an Integer by choosing this keyword in the Field Size General attribute as shown below:

 

Notice the ID field in the table above has a small icon of a yellow key on its left side. This indicates that this field is the primary key of the table. You will learn more about primary keys in the course, but if one needs to change a primary key, one should right-click the space left to the field name of the new primary key, and select the “Primary Key” option, as shown below, where the TextField is being chosen to become the new primary key:

 

If a primary key is made of more than one field one must select all fields that make the primary key at once. This is done by clicking the space left to each of the field names while holding the Ctrl-button. Once all required fields are selected, right-clicking one of the selected spaces while still holding the Ctrl-button will show the “Primary key” than can be selected. For example, the following is selecting ID and TextField as the composite primary key:

 

Once all fields are defined we can save the table by once again, right-clicking over the name of the table tab above and select “Save” on the Drop-Down Menu, as follows:

 

Records with data for all fields in the table can be added if we select the “DataSheet View” again, using the same procedure as we did above to save the table, but selecting the “Datasheet View” this time. Data is added to the table, the same way as data is added in a spreadsheet. The following shows two records that were added to the table:

 

Do not forget to save the table after any change has been made. Values will be lost if they are not saved.
