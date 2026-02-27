# Unit 6: Content Highlights - Data Quality and Integration and Data Warehousing 

This page highlights the main points on this week’s readings, and complement some of the textbook explanations. It is recommended to first read this week’s assigned chapters from the textbook, and then come back to this document for further commentary.

The highlights of this week’s readings are:

Data Warehouses

As we explained in week 1, based on their use, there are two kinds of databases we will study in this course. So far, we have only studied Transactional Databases, used for the daily management of an enterprise. These databases provide a view of the current situation of data within the organization. This week we are going to study Data Warehouses. They are created with the sole purpose of helping a company’s management in making decisions about their business. They provide historical information, rather than current information. They obtain their data by periodic extraction of information from transactional databases.  The extracted information is stored in a manner that makes easier their retrieval and analysis. Data stored in data warehouses never change, since information from the past does not either. It is only augmented, every time new information is extracted.

Data Marts

As you can read in the textbook, there is more than one way to implement data warehouses. The biggest data warehouses contain historical data that comprises all aspects and databases used in an enterprise. Their aim is to be able to answer any question management may have about any historical aspect of their business. By contrast, Data Marts are smaller data warehouses, containing information about a specific aspect of a business. Their aim is to be able to answer specific questions of limited scope within the business. For example, a data mart may be created to contain client’s information exclusively, with the aim of analysis customer trends. Another data mart may contain information about payroll, with the aim to analyze employee’s compensations. A data mart is a data warehouse, but is smaller in size and scope.

The Star Scheme

The most widely used architecture in data warehouses is the star-scheme. In this architecture, there is one big table containing all historical information in the data warehouse. This is called the Fact table. Besides this table, there are a number of other ones, called dimension tables. Dimension tables are tables that contain the values of attributes that classify data in the fact table. The most typical dimension is time. Time can be expressed in many ways depending on time interval in which data is going to be stored. For example, if data is going to be stored in the fact table at the end of every month, the time dimension table should include entries for all possible months were data will be stored: February 2016, March 2016, etc. Any attribute could be made a dimension. The data warehouse designer must select the attributes that will better group data   in categories that will help to find trends for management to explore. Those attributes should become dimensions.  The fact table will contain fields for each of these dimensions. They primary key for records in the fact table will be the composite of the attributes that are dimensions.  Every dimension table will maintain a 1-to-many relationship with the fact table, indicating that every record in the fact table has a value for each of the dimensions and that some records in the fact table may share some of the values in dimensions, but not all (otherwise there will be duplicates in the primary key of the fact table). All other non-key fields in the data table contain the archived data to be stored and used for analysis by management.

 

 

Data Quality

Chapters this week stress the importance of data quality. Wrong data leads to wrong decisions; therefore, it is important that the data represented inside databases be as accurate as possible. Being vigilant about data accuracy is a task that data managers and database managers must perform continuously, since errors and inconsistencies may invade databases from many sources. This is especially true when there is regulation that requires enterprises to abide by certain norms of conduct with regard to data storage and manipulation. The chapter on Data Quality and Integration talks about some of these regulations. It also presents a table of reasons for deteriorated data quality.

The ETL Process

The chapter on Data Quality and Integration also shows the process of converting data inside transactional databases and data warehouses. This process is known as the ETL process: Extract, Transform and Load. Data extracted from a transactional database needs to be vetted to assure that is correct, that is complete and that will produce the required fields in the data warehouse. Once “cleansed”, the data needs to be transformed to obtain the values to be stored in the data warehouse. This may mean simply to copy the values we have in the appropriate fields, but in some cases it may mean transforming the data onto something else:  maybe we need to obtain an average, or we need to sort the data, or we need to convert the units of the data. All these transformations should produce the entries that will load the fields in the data warehouse files.

 

Figures in this document were taken from the textbook material (Hoffer, Jeffrey A., Ramesh, V., Topi, Heikki, Modern Database Management, Twelfth Edition, Prentice Hall, 2016).
