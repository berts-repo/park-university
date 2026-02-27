# Unit 4: Content Highlights - Physical Database Design and Database Application Development 

This page highlights the main points on this week’s readings, and complement some of the textbook explanations. It is recommended to first read this week’s assigned chapters from the textbook, and then come back to this document for further commentary.

The highlights of this week’s readings are:

Possible Data Types in a Real Database

Table 5.1 in the textbook (reproduced below) shows the most common data types to be used when creating fields on tables in a relational data model. Every field in the table must have a data type. This allows the database to allocate enough space for storage of the field contents.  Most of the types you will use in this class are NUMBER, DATE, and one not shown in the table, TEXT. In Microsoft Access, TEXT has the same function as VARCHAR2, but it is restricted to a length of 255 characters.  We will not need more on examples and exercises for this course.

 

 

Methods to Control Data Integrity.

The textbook mentions some ways in which a real database management system (DBMS) controls the integrity of the data in tables. These are:

The use of data types. It restricts inserting data of a different type on a field. It does not prevent all wrong data to be stored in a field, but at least the data will be of the same kind that is expected from that field.

Providing default values. This is useful if there is a value that is predominant for a field in the data. This is rare case. If that is the only value for that field, then we should not have that field, because it contains redundant information. Something may have to be re-designed to avoid this problem. On the other hand, if the value is not that common, it is an annoyance to have to delete the value most of the time.

Range control. Giving a field a range of possible values and allowing the database not to receive values outside this range will also prevent some data entry errors, but again, not all. A wrong value within the range will be taken by the DBMS.

Null value control. All reasonable DBMSs enforce Entity Integrity, so no primary key is allowed to have null values. Most databases also allow for other fields not to be null. This is useful when the contents of the field are always required.

Referential Integrity. Like Entity Integrity, reasonable DBMSs enforce this constraint, however, since any non-key field on a table may become a foreign key, the database developer must explicitly create the references needed for the DBMS to enforce them.

De-Normalization: When Redundancy is OK.

In a previous study unit we described the importance of normalization of tables to avoid data redundancy. This unit explains that de-normalization (adding redundant data) may be useful in some situations. The textbook explain some cases where it may be needed. All these cases involve a relationship that is described with multiple tables. Rather than using all these tables, de-normalization would store the data onto tables in the first normal form. This is done to be able to retrieve all the data about a relationship by just reading one record of the de-normalized data. This can be useful when the access to multiple tables at the same time is slow or inconvenient. However, we will need to compare the benefits of this approach against the time and effort that is needed to keep all redundant data being consistent.

Partitions

The textbook explains various scenarios in which tables may be broken horizontally (records are partitioned in separated files), vertically (fields are partitioned in separated files), or both. In a centralized DBMS these partitions may not be necessary at all. They become an alternative when we have a decentralized DBMS. A decentralized DBMS may serve large area, requiring the database to be broken geographically. Businesses working in various industries, may also want to break their databases per industry. Database developers should pay attention to the fact any broken database should include mechanisms to restore its unity, otherwise the separate partitions may become incompatible with the pass of time.

Reasons for Indexing

Most current DBMS these days allow for the indexing of any field or set of fields in a table. The textbook presents some situations when indexing is advisable. It is just good to remember that one must index wisely, because indexes take storage space in the database and consume time overhead when the index is created or when the indexed table is updated. Primary keys of all tables are usually indexed by default, or if not, should be set by the database developer to be indexed. Other candidate keys are also good fields to be indexed, since users may like to access data records using these alternate keys. Indexing of other non-field keys is advisable if they are also going to be used for the same purpose, as a point of entry in accessing data records.

Two-Tier Architecture and Three-Tier Architecture

Most business databases these days use the Internet for their deployment and to interface with the data they hold. These two activities are separated for efficiency, flexibility and security. In one side we want to protect the database by allowing access only to legitimate users of the systems. These may be distributed all over the world, but need to access the same database. User interface is slow, in comparison to data processing, since human interaction is the slowest activity in any computing cycle. This means that a central database may be able to satisfy many user requests in less time that takes one of them to make the request.

Because of this asymmetry, a database operation is usually broken in two or three tiers. One tier, close to the database’s user, will be involved with user interface. This piece usually resides or is partially deployed in the user’s computer.  Based in the user’s input, it handles the creation of requests to the DBMS. It also displays oncoming results from the DBMS for the user’s benefit. While the interface may be a program explicitly created for the DBMS, these days, most DBMS use Internet browsers as their main user interface.

A separate tier on the other side of the database system is the actual DBMS that takes care of the database itself. It includes a database server that receives requests from legitimate users and return results to them. The database itself may be centralized in the same system, or most common these days, decentralized among many devices. Regardless of the internal architecture of the database, the DBMS is in charge or finding the required data from wherever it is located in the database.

With these two clearly separated functions in a database, a system is defined as a two-tier or a three-tier system based on where each function begins and where it ends.

A two-tier system separates these functions in two: the user’s side, known as the client and the database’s side, known as the server. The following diagram from the textbook shows three variations on the two-tier system, each one differentiated by the amount of software and assignment of tasks assigned to them:

 

A fat client system incorporates some data processing in the client’s computer while a thin client does not include any data processing. A distributed two-tier system will split data processing between the client and the server side.

A similar approach is used in three-tier architectures, but the database system is now broken in three or more sections. The reason for this further split has to do with the design of the particular application that uses the database. A lot of systems these days perform multiple tasks for which they require big pieces of software and are part of a general computing strategy for a company. Databases and their DBMS are the back end of these applications, since they provide the data on which the applications may perform calculations. This layer of computing is between the final user of the system (the client) and the DBMS and it is the third tier of the three-tier architecture. Depending of the architecture of this new layer the system may in fact have more than three tiers, but regardless of the number, the generic name for all these systems is the three-tier architecture. The following a sample from the textbook on possible arrangements for this architecture:

 

 

Figures in this document were taken from the textbook material (Hoffer, Jeffrey A., Ramesh, V., Topi, Heikki, Modern Database Management, Twelfth Edition, Prentice Hall, 2016).
