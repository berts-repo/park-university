# Unit 3 Lecture: Chapter 6

Foundations of Business Intelligence: Databases and Information Management

Information is becoming as important a business resource as money, material, and people. Even though a company compiles millions of pieces of data doesn’t mean it can produce information that its employees, suppliers, and customers can use. Businesses are realizing the competitive advantage they can gain by compiling useful information, not just data.

 [link: #fragment-1] 6.1

 [link: #fragment-2] 6.2

 [link: #fragment-3] 6.3

 [link: #fragment-4] 6.4

 [link: #fragment-5] 6.5

 [link: #fragment-6] Review Questions

6.1 What are the problems of managing data resources in a traditional file environment?

Why should you learn about organizing data? Because it’s almost inevitable that someday you’ll be establishing or at least working with a database of some kind. As with anything else, understanding the lingo is the first step to understanding the whole concept of managing and maintaining information. It all comes down to turning data into useful information, not just a bunch of bits and bytes.

6.1.1 File Organization Terms and Concepts

The first few terms, field, record, file, and database, are depicted in Figure 6.1, which shows the relationship among them.

Figure 6.1: The Data Hierarchy

An entity is basically the person, place, thing, or event on which you maintain information. Each characteristic or quality describing an entity is called an attribute. In the table below, each column describes a characteristic (attribute) of John Jones’ (who is the entity) address.

Attribute Table

First Name

Last Name

Street

City

State

Zip

Telephone

John

Jones

111 Main St

Center City

Ohio

22334

555-123-6666

Suppose you decide to create a database for your newspaper delivery business. In order to succeed, you need to keep accurate, useful information for each of your customers. You set up a database to maintain the information. For each customer, you create a record. Within each record you have the following fields: customer first name, customer last name, street address, city, state, zip, ID, and date last paid. Smith, Jones, and Brooks are the records within a file you decide to call Paper Delivery. The entities then are Smith, Jones, and Brooks, the people about whom you are maintaining information. The attributes are customer’s name (first and last), address (street, city, state, zip code), ID, and date last paid. This is a very simplistic example of a database, but it should help you understand the terminology.

 

6.1.2 Problems with the Traditional File Environment

Building and maintaining separate databases within an organization is usually the main cause of “islands of information.” It may begin in all innocence, but it can quickly grow to monstrous proportions. Let’s look at some of the problems traditional file environments have caused.

6.1.2.1 Data Redundancy and Inconsistency

Have you ever gotten two pieces of mail from the same organization? For instance, you get two promotional flyers from your friendly neighborhood grocery store every month. It may not necessarily be that you’re a popular person. It’s probably because your data was somehow entered twice into the business’s database. That’s data redundancy. Now, let’s say you change residences and, consequently, your address. You notify everyone of your new address including your local bank. Everything is going smoothly with your monthly statements. All of a sudden, at the end of the year, the bank sends a Christmas card to your new address and one to your old address. Why? Because your new address was changed in one database, but the bank maintains a separate database for its Christmas card list and your address was never changed in it. That’s data inconsistency. Just from these two simple examples you can see how data redundancy and inconsistency can waste resources and cause nightmares on a much larger scale.

6.1.2.2 Program-Data Dependence

Some computer software programs, mainly those written for large, mainframe computers, require data to be constructed in a particular way. Because the data are specific to that program, it can’t be used in a different program. If an organization wants to use the same data in a different program, it has to reconstruct it. Now the organization is spending dollars and time to establish and maintain separate sets of data on the same entities because of program-data dependence.

6.1.2.3 Lack of Flexibility

The sales and marketing manager needs information about his company’s new production schedule. However, he doesn’t need all of the data in the same order as the production manager’s weekly report. Too bad. The company’s database system lacks the flexibility to give the sales manager the information he needs, how he needs it, and when he would like to receive it.

6.1.2.4 Poor Security

Traditional file environments have little or no security controls that limit who receives data or how they use it. With all the data captured and stored in a typical business, that’s unacceptable.

6.1.2.5 Lack of Data Sharing and Availability

What if the CEO of a business wants to compare sales of Widget A with production schedules? That might be difficult if production data on the widgets is maintained differently by the sales department. This problem happens far more frequently in older traditional file environments that lack the ability to share data and make it available across the organization.

 

Bottom Line

Many problems such as data redundancy, program-data dependence, inflexibility, poor data security, and inability to share data among applications have occurred with traditional file environments. Managers and workers must know and understand how databases are constructed so they know how to use the information resource to their advantage.

6.2 What are the major capabilities of database management systems (DBMS), and why is a relational DBMS so powerful?

The key to establishing an effective, efficient database is to involve the entire organization as much as possible, even if everyone will not immediately be connected to it or use it. Perhaps they won’t be a part of it in the beginning, but they very well could be later on. Database management systems make it easy, fast, and efficient to relate pieces of data together to compile useful information.

6.2.1 Database Management Systems

You’ve heard the old saying, “Don’t put all your eggs in one basket.” When it comes to data, just the opposite is true. You want to put all your corporate data in one system that will serve the organization as a whole. Doing so makes it easier, cheaper, and more efficient to use the data across the entire organization. It makes it easier to use in applications and makes it available through many different delivery methods.

A database management system (DBMS) is basically another software program like Word or Excel or e-mail. This type of software is more complicated; it permits an organization to centralize data, manage data efficiently, and provide access to the stored data by application programs.

Physical views of data are often different from the logical views of the same data when they are actually being used.

For instance, assume you store tablets of paper in your lower-right desk drawer. You store your pencils in the upper-left drawer. When it comes time to write your request for a pay raise, you pull out the paper and pencil and put them together on your desktop. It isn’t important to the task at hand where the items were stored physically; you are concerned with the logical idea of the two items coming together to help you accomplish the task.

The physical view of data focuses on where the data are actually stored in the record or in a file. The physical view is important to programmers who must manipulate the data as they are physically stored in the database.

Does it really matter to the user that the customer address is physically stored on the disk before the customer name? Probably not. However, when users create a report of customers located in Indiana, they generally will list the customer name first and then the address. So, it’s more important to the end user to bring the data from its physical location on the storage device to a logical view in the output device, whether it’s on screen or on paper.

6.2.1.1 How a DBMS Solves the Problems of the Traditional File Environment

If you have just one database that serves the entire organization, you eliminate the islands of information and, in turn, most of the problems we discussed earlier. If you have only one database, you reduce the chances of having redundant and inconsistent data because each entity has only one record. You construct the data separate from the programs that will use them. The data are available to whoever needs them, in the form that works best for the task at hand. Securing just one database is much easier than controlling access to multiple databases.

6.2.1.2 Relational DBMS

A relational database stores data in tables. The data are then extracted and combined into whatever form or format the user needs. The tables are sometimes called files, although that is actually a misnomer, because you can have multiple tables in one file.

Data in each table are broken down into fields. A field, or column, contains a single attribute for an entity. A group of fields is stored in a record or tuple (the technical term for record). Figure 6.4 in the text shows the composition of relational database tables.

Each record requires a key field, or unique identifier. The best example of this is your social security number—there is only one per person. That explains in part why so many companies and organizations ask for your social security number when you do business with them.

In a relational database, each table contains a primary key, a unique identifier for each record. To make sure the tables relate to each other, the primary key from one table is stored in a related table as a foreign key. For instance, in the customer table below the primary key is the unique customer ID. That primary key is then stored in the order table as the foreign key so that the two tables have a direct relationship.

Customer Table

Customer Table

Order Table

Field Name

Description

Field Name

Description

Customer Name

Self-Explanatory

Order Number

Primary Key

Customer Address

Self-Explanatory

Order Item

Self-Explanatory

Customer ID

Primary Key

Number of Items Ordered

Self-Explanatory

Order Number

Foreign Key

Customer ID

Foreign Key

There are two important points you should remember about creating and maintaining relational database tables. First, you should ensure that attributes for a particular entity apply only to that entity. That is, you would not include fields in the customer record that apply to products in the customer orders. Fields relating to products would be in a separate table. Second, you want to create the smallest possible fields for each record. For instance, you would create separate fields for a customer’s first name and last name rather than a single field for the entire name. It makes it easier to sort and manipulate the records later when you are creating reports.

Wrong way:

Name

Address

Telephone number

John L. Jones

111 Main St Center City Ohio 22334

555-123-6666

Right way:

First Name

Middle Initial

Last Name

Street

City

State

Zip

Telephone

John

L.

Jones

111 Main St

Center City

Ohio

22334

555-123-6666

 

6.2.1.3 Operations of a Relational DBMS

Use these three basic operations to develop relational databases:

Select: Create a subset of records meeting the stated criteria.

Join: Combine related tables to provide more information than individual tables.

Project: Create a new table from subsets of previous tables.

The biggest problem with these databases is the misconception that every data element should be stored in the same table. In fact, each data element should be analyzed in relation to other data elements, with the goal of making the tables as small in size as possible. The ideal relational database will have many small tables, not one big one. On the surface that may seem like extra work and effort, but by keeping the tables small, they can serve a wider audience because they are more flexible. This setup is especially helpful in reducing redundancy and increasing the usefulness of data.

 

6.2.2 Capabilities of Database Management Systems

There are three important capabilities of DBMS that traditional file environments lack—data definition, data dictionary, and a data manipulation language.

 Data definition: Marketing looks at customer addresses differently from shipping, so you must make sure that all database users are speaking the same language. Think of it this way: Marketing is speaking French, production is speaking German, and human resources is speaking Japanese. They are all saying the same thing, but it’s very difficult for them to understand one another. Creating the data definitions sometimes gets shortchanged. Programmers who build the definitions sometimes say “Hey, an address is an address, so what.” That’s when it becomes critical to involve users in the development of the data definitions.

Data dictionary: Each data element or field should be carefully analyzed when the database is first built or as the elements are later added. Determine what each element will be used for, who will be the primary user, and how it fits into the overall scheme of things. Then write down all the element’s characteristics and make them easily available to all users. This is one of the most important steps in creating a good database. Each data definition is then included in the data dictionary.

Why is it so important to document the data dictionary? Let’s say Suzy, who was in on the initial design and building of the database, moves on and Joe takes her place. It may not be so apparent to him what all the data elements really mean, and he can easily make mistakes from not knowing or understanding the correct use of the data. He will apply his own interpretation, which may or may not be correct. Once again, it ultimately comes down to a persware problem.

Users and programmers can consult the data dictionary to determine what data elements are available before they create new ones that are the same or similar to those already in the data dictionary. This can eliminate data redundancy and inconsistency.

6.2.2.1 Querying and Reporting

Data manipulation language: This is the third important capability of a DBMS. It’s a formal language used to manipulate the data in the database and make sure they are formulated into useful information. The goal of this language should be to make it easy for users to build their own queries and reports. Data manipulation languages are getting easier to use and more prevalent. SQL (Structured Query Language) is the most prominent language and is now embedded in desktop applications such as Microsoft Access.

 

6.2.3 Designing Databases

Don’t start pounding on the keyboard just yet! That’s a common mistake that may cause you many headaches later on. You have a lot of work to do to design a database before you touch the computer.

First, you should think long and hard about how you use information in your current situation. Think of how it is organized, stored, and used. Now imagine how this information could be organized better and used more easily throughout the organization. What part of the current system would you be willing to get rid of and what would you add? Involve as many end users in this planning stage as possible. They are the ones who will prosper or suffer because of the decisions made at this point.

6.2.3.1 Normalization and Entity-Relationship Diagrams

We mentioned before that you want to create the smallest data fields possible. You also want to avoid redundancy among tables and not allow a relationship to contain repeating data groups. You do not want to have two tables storing a customer’s name. That makes it more difficult to keep data properly organized and updated. What would happen if you changed the customer’s name in one table and forgot to change it in the second table? Minimizing redundancy and increasing the stability and flexibility of databases is called normalization.

Your goals for creating a good data model are:

Including all entities and the relationships among them

Organizing data to minimize redundancy

Maximizing data accuracy

Making data easily accessible

Whichever relationship type you use, you need to make sure the relationship remains consistent by enforcing referential integrity. That is, if you create a table that points to another table, you must add corresponding records to both tables.

Determine the relationships between each data entity by using an entity-relationship diagram like the one below.

Figure 6.11 An Entity-Relationship Diagram

 

Determine which data elements work best together and how you will organize them in tables. Break your groups of data into as small a unit as possible (normalization). Even when you say it’s as small as it can get, go back through again. Decide what the key identifier will be for each record. See, you’ve done all this and you haven’t even touched the computer yet!

Give it your best shot in the beginning: It costs a lot of time, money, and frustration to go back and make changes or corrections or to live with a poorly-designed database.

6.2.3.2 Non-Relational Databases and Databases in the Cloud

Relational databases will serve your company well if all your data can be neatly tucked into rows and columns. Unfortunately, much of the data a business wants to access aren’t structured like that. Data are now stored in text messages, social media postings, maps, and the like. Non-relational database management systems are better at managing large data set on distributed computing networks. They can easily be scaled up or down depending on the particular needs of your business at a particular time.

6.2.3.3 Cloud Databases and Distributed Databases

Cloud computing service companies provide a way for you to manage your company’s data through Internet access using a web browser. At the present time, you may not be able to create a sophisticated relational database management system, but it won’t be long before it’s a standard service for organizations of all sizes. Pricing for cloud-based database services are predicated upon:

Usage—small databases cost less than larger ones

Volume of data stored

Number of input-output requests

Amount of data written to the database

Amount of data read from the database

Small- and medium-sized businesses can benefit from using cloud-based databases by not having to maintain the information technology infrastructure needed to establish a local database. Large businesses can benefit from the services by using it as an adjunct to their onsite database and moving peak usage to the cloud.

A distributed database is one that is divided among several storage and processing sites rather than having everything in one place. Specialized software ensures that the data are always synchronized and consistent regardless of where it’s physically located.

6.2.3.4 Blockchain

One of the newest technologies for creating and processing transactions across multiple users and storage locations is blockchain. It uses the distributed database concept that we mentioned above. The blockchain technology is especially useful when transactions are created and processed across a network of computers. Each time a transaction is updated or acted upon throughout the network, it is verified and time-stamped. The verification data is added to a ledger that follows the transaction through the network and ensures all users can follow the authenticity of the transaction.

Using blockchain technology is much simpler and cheaper than each user creating their own authentication processes. Smart contracts implement the rules governing transactions between firms who use blockchain for financial, supply chain, medical records and other types of data transactions.

Blockchain networks

reduce the cost of verifying users

reduce the cost of validating transactions

reduce the risks of storing and processing transaction information

Figure 6.12. How blockchain works

Bottom Line

Relational databases solve many of the problems inherent with traditional file environments. Database management systems have three critical components: the data definition, the data dictionary, and the data manipulation language. Managers should make sure that end users are fully involved in properly designing organizational databases using normalization and entity-relationship diagrams.

6.3 What are the principal tools and technologies for accessing information from databases to improve business performance and decision making?

Corporations and businesses go to great lengths to collect and store information about their suppliers and customers. What they haven’t done a good job of in the past is fully using the data to take advantage of new products or markets. They’re trying, though, as we see in this section.

 6.3.1 The Challenge of Big Data

Just a bit ago, we talked about how much of the data businesses want to collect, store, process, and use are no longer sorted neatly and easily into rows, columns, and tables.

E-mail messages, text messages, tweets, photos, videos and even output from large mainframe computers that process huge amounts of data, now contain information wanted by companies and managers. Postings to Facebook and LinkedIn contain data that can be useful to businesses if they are able to turn it into useful information.

The term big data is used to describe those kinds of data that cannot be stored and processed in typical database management systems. Big data generally refers to databases with millions to tens of millions of records, often exabytes of data.  Companies want and need to capture, store, process, and generate information from big data often in near real time, because it can identifypatterns in business transactions and processes that may be useful to executives and managers.

By 2020, big data and business analytics will be generating  [link: https://www.statista.com/statistics/551501/worldwide-big-data-business-analytics-revenue/] $188.8 billion in revenue worldwide. If you’d like a piece of this pie, now’s the time to get started. With more data available than ever before, why not get paid for your data?

Big data seems to be the term on everyone’s lips these days. But what exactly is big data, and why is it so important?

Big data describes the large volume of structured and unstructured data inundating businesses each day. Humans generate data with every page they visit online. They take their GPS-equipped phones everywhere and communicate through chat and social media apps.

Not to mention, machines are also generating more data than ever. This includes smart home devices, sensors on machines and in factories, and more. All this data leaves digital footprints everywhere.

It’s not the data itself that’s important. It’s what your business does with that data that matters the most. If big data isn’t analyzed, it’s useless. But when you use this data effectively, you’ll get insights that will lead to more strategic business decisions.

Police forces around the world are using data-driven strategies based on both public data and their own intelligence. This allows them to deploy their resources in the most effective way, and act as deterrents when necessary. 

Both man-made and natural disasters can be predicted with more accuracy than ever before. Scientists are using data from sensors to predict where earthquakes are most likely to hit next. They’re also using big data to safeguard and monitor the flow of refugees fleeing war zones across the globe. 

Patients are wearing smart devices which allow doctors to monitor them from a distance and pick up on trends. Doctors and scientists are also analyzing images and medical records for patterns. These help with the development of new medicines. This data also allows medical professionals to spot diseases earlier than ever before.

(How Companies Can Make Big Money with Big Data, www.emoneyindeed.com, Jain, Gaurav, July 11, 2018)

Big data is characterized by the “3Vs”:

Volume of data

Variety of data

Velocity at which data must be processed

 

6.3.2 Business Intelligence Infrastructure

Businesses collect millions of pieces of data. Using the right tools, a business can use its data to develop effective competitive strategies that we discussed in previous chapters. Rather than guessing about which products or services are your best sellers, business intelligence provides concrete methods of analyzing exactly what customers want and how best to supply them.

Three benefits of using business intelligence include:

Capability to amass information

Develop knowledge about customers, competitors, and internal operations

Change decision-making behavior to achieve higher profitability

Many times, businesses store data in separate systems even though they’ve made great strides in migrating everything into one large database. In some cases, the data are structured, semistructured, or unstructured. Somehow, all that has to come together at some point using appropriate tools and technologies. How to do that effectively and efficiently is what we’ll look at now.

6.3.2.1 Data Warehouses and Data Marts

As organizations want and need more information about their company, their products, and their customers, the concept of data warehousing has become very popular. Remember those islands of information we keep talking about? Unfortunately, too many of them have proliferated over the years and now companies are trying to rein them in by using data warehousing.

No, data warehouses are not great big buildings with shelves and shelves of bits and bytes stored on them. They are huge computer files that store old and new data concerning anything and everything about which a company wants to maintain information. Data come from a variety of sources, both internal and external to the organization. They are then stored together in a data warehouse from which they can be accessed and analyzed to fit the user’s needs.

Because a data warehouse can be cumbersome because of its size and sheer volume of data, a company can break the information into smaller groups called data marts. It’s easier and cheaper to sort through data marts that tend to be more focused on a particular subject. It’s still useful to have a huge data warehouse, though, so that information is available to everyone who wants or needs it. You can let the user determine how the data will be manipulated and used.

Using data warehouses and data marts correctly can give management a tremendous amount of information that can be used to trim costs, reduce inventory, put products in the right stores at the right time, attract new customers, or keep old customers happy.

6.3.2.2 Hadoop

For the kinds of data we discussed earlier that don’t fit neatly into rows, columns, and tables, a new technology called Hadoop is better for handling unstructured and semistructured big data. Hadoop is an open-source software framework that uses distributed parallel processing across a network of small computers.

The software divides huge data set problems into smaller subsets, sends the subsets to smaller computers for processing, and then gathers the results back into a data set that is analyzed.

There are two main components of the system:

Hadoop distributed file system used for data storage

MapReduce for high-performance parallel data processing

 

6.3.2.3 In-Memory Computing

Typically, database management systems rely on disk-based storage. When it comes time to process the data, they are accessed from the disk storage, brought into the computer’s main memory (RAM), and then moved back again. Not only does it take a long time to move the data back and forth and process it, bottlenecks often occur in the system.

In-memory computing eliminates the bottlenecks and the data movement time by moving all the data at once into the computer’s main RAM memory and processes it all at once. That’s only possible because of the advances in chip technology, multicore processing, and lower prices for main memory.

 

Interactive Session

Technology: Kraft Heinz finds a new recipe for analyzing its data (see page 230 of the text) describes how one of the biggest food and beverage companies in the world used big data technologies to identify opportunities for improving operational efficiencies to protect their profit margins.

6.3.2.4 Analytic Platforms

Preconfigured hardware–software systems specifically designed for query processing and analytics are now available for both relational and non-relational datasets. These analytic platforms include in-memory systems and non-relational database management systems. They are just one part of the overall business intelligence infrastructure shown in Figure 6.13 below

Figure 6.13 Contemporary Business Intelligence Infrastructure

6.3.3 Analytical Tools: Relationships, Patterns, Trends

Once all the data are captured, stored, and processed, hopefully a business will do something with it. The technologies in the following sections will tell you how to turn it into useful information.

6.3.3.1 Online Analytical Processing (OLAP)

As technology improves, so does our ability to manipulate information maintained in databases. Have you ever played with a Rubik’s Cube—one of those little multicolored puzzle boxes you can twist around and around to come up with various color combinations? That’s a close analogy to how multidimensional data analysis or online analytical processing (OLAP) works. In theory, it’s easy to change data around to fit your needs.

Figure 6.14: Multidimensional Data Model

6.3.3.2 Data Mining

Data mining technology allows a digital firm to get more information than ever before from its data. One danger in data mining is the problem of getting information that on the surface may seem meaningful, but when put into context of the organization’s needs, simply doesn’t provide any useful information.

For instance, data mining can tell you that on a hot summer day in the middle of Texas, more bottled water is sold in convenience stores than in grocery stores. That’s information managers can use to make sure more stock is targeted to convenience stores. Data mining could also reveal that when customers purchase white socks, they also purchase bottled water 62 percent of the time. We seriously doubt there is any correlation between the two purchases. The point is that you need to beware of using data mining as a sole source of decision making and make sure your requests are as focused as possible.

These are the five types of information managers can obtain from data mining:

Associations: Determine occurrences linked to a single event

Sequences: Determine events that are linked over time

Classification: Discover characteristics of customers and make predictions about their behavior

Clustering: Discover groups within data

Forecasting: Use existing values to forecast what other values will be

Many companies collect lots of data about their business and customers. The most difficult part has been to turn that data into useful information. Firms are using better data mining techniques to target customers and suppliers with just the right information at the right time.

For instance, based on past purchases, Chadwick’s clothing retailer determines that a customer is more likely to purchase casual clothing than formal wear at certain times of the year. Based on its predictive analysis, the retailer then tailors its sales offers to meet that expected behavior.

6.3.3.3 Text Mining and Web Mining

Much of the data created that might be useful to businesses is stored not in databases but in text-based documents. Word files, e-mails, call center transcripts, and services reports contain valuable data that managers can use to assess operations and help make better decisions about the organization. Unfortunately, there has not been an easy way to mine those documents until recently. Text mining tools help scrub text files to find data or to discern patterns and relationships.

It’s quite possible you’ve read comments left by others on Facebook pages, at the end of news stories, and even entire web sites dedicated to specific causes. Sometimes those comments and postings are favorable to a business and sometimes they aren’t. Either way, companies want to know how their customers feel about them, which is possible through sentiment analysis. Smart companies use the analysis to improve customer interfaces or solve problems they otherwise wouldn’t have known exist.

Because so much business is taking place over the web, businesses are trying to mine data from it also. There are three categories of web mining processes:

Web content mining: Extract knowledge from the content of web pages—text, images, audio, and video

Web structure mining: Data related to the structure of a web site—links between documents

Web usage mining: User interaction data recorded by web servers—user behavior on a web site

“Web mining is the process of using data mining techniques and algorithms to extract information directly from the Web by extracting it from Web documents and services, Web content, hyperlinks and server logs. The goal of Web mining is to look for patterns in Web data by collecting and analyzing information in order to gain insight into trends, the industry and users in general.

Web mining is a branch of data mining concentrating on the World Wide Web as the primary data source, including all of its components from Web content, server logs to everything in between. The contents of data mined from the Web may be a collection of facts that Web pages are meant to contain, and these may consist of text, structured data such as lists and tables, and even images, video and audio.” (Web Mining, https://www.techopedia.com, April 13, 2019)

6.3.4 Databases and the Web

Web browsers are far easier to use than most of the query languages associated with the other programs on mainframe computer systems. Companies realize how easy it is to provide employees, customers, and suppliers with web-based access to databases rather than creating proprietary systems. It’s also proving cheaper to create “front-end” browser applications that can more easily link information from disparate systems than to try to combine all the systems on the “back-end.” That is, you link internal databases to the web through software programs that provide a connection to the database without major reconfigurations. A database server, which is a special dedicated computer, maintains the DBMS. A software program, called an application server, processes the transactions and offers data access. A user making an inquiry through the web server can connect to the organization’s database and receive information in the form of a web page.

Figure 6.15 shows how servers provide the interface between the database and the web.

Figure 6.15 Linking Internal Databases to the Web

The benefits of using a web browser to access a database include:

Ease-of-use

Less training for users

No changes to the internal database

Allows a business to keep its old legacy system instead of replacing it

Cheaper than building a new system from scratch

Creating new efficiencies and opportunities

Provide employees with integrated firm-wide views of information

 

Bottom Line

There are many ways to manipulate databases so that an organization can save money and still have useful information. With technological improvements companies don’t have to continually start from scratch but can blend the old with the new when they want to update their systems. The Web is the perfect delivery vehicle for databases and is cheaper than building proprietary systems.

6.4 Why are information policy, data administration, and data quality assurance essential for managing the firm’s data resources?

At the beginning we said that as many users as possible should be brought together to plan the database. We believed it so much then that we’ll say it again here. By excluding groups of users in the planning stages, no matter how insignificant that group may seem, a company courts trouble.

 

6.4.1 Establishing an Information Policy

No one part of the organization should feel that it owns information to the exclusivity of other departments or people in the organization. A certain department may have the primary responsibility for updating and maintaining the data, but that department still has to share the information across the whole company if necessary. Well-written information policies outline the rules for using this important resource, including how it will be shared, maintained, distributed, and updated.

Ask any manager what her resources are and she’s likely to list people, equipment, buildings, and money. Very few managers will include information on the list, yet it can be more valuable than some of the others. A data administration function, reporting to senior management, emphasizes the importance of this resource. This function helps define and structure the information requirements for the entire organization to ensure it receives the attention it deserves.

Data administration is responsible for:

Developing information policies

Planning for data

Overseeing logical database design

Developing data dictionaries

Monitoring the usage of data by techies and nontechies

Data governance describes the importance of creating policies and processes for employing data in organizations. Making sure data are available and usable, have integrity, and are secure is one part. Promoting data privacy, security, quality, and complying with government regulations such as the Sarbanes-Oxley Act is the second part.

You need to get the nontechies talking and working with the techies, preferably together in a group that is responsible for database administration. Users will take on more responsibility for accessing data on their own through query languages if they understand the structure of the database. Users need to understand the role they play in treating information as an important corporate resource. Not only will they require a user-friendly structure for the database, but they will also need lots of training and hand-holding up front. It will pay off in the long run.

 

6.4.2 Ensuring Data Quality

Let’s bring the problem of poor data quality close to home. What if the person updating your college records fails to record your grade correctly for this course and gives you a D instead of a B or an A? What if your completion of this course isn’t even recorded? Because of the bad data, you could lose your financial aid or perhaps get a rather nasty e-mail from Mom and Dad. Think of the time and difficulty getting the data corrected.

Data quality audits verify data accuracy in one of three ways:

Survey entire data files

Survey samples from data files

Survey end users about their perceptions of data quality

It’s better for the company or organization to uncover poor quality data than to have customers, suppliers, or governmental agencies uncover the problems.

Whether a company creates a single data warehouse from scratch or puts a web-front on old, disparate, disjointed databases, it still needs to ensure data cleansing receives the attention it should. It’s too expensive, both monetarily and customer oriented, to leave bad data hanging around. A special type of software helps make this job easier by surveying data files, correcting errors in the data, and consistently integrating data throughout the organization.

 

Interactive Session

Organizations: Databases where the data aren’t there (see page 239 of the text) discusses the dangers to society and individuals when major gaps exist in federal criminal databases which rely on accurate and complete reporting from a variety of agencies.

 

Bottom Line

As with any other resource, managers must administer their data, plan their uses, and discover new opportunities for the data to serve the organization through changing technologies. If data quality suffers, it’s a sure bet the information obtained from that data will be of poor quality also.

6.5 How will MIS help my career? 

The chapter’s elements and information can help in securing a good job as an entry-level data analyst. This position will work with databases for a company that’s involved in the distribution, transmission, and generation of electricity as well as energy management and other energy-related services. These types of jobs are becoming more popular as information technology becomes more important in the workplace.

Review

Describe the three capabilities of database management systems: data definition, data dictionary, and data manipulation language. Discuss the importance of creating and using a data dictionary with a large corporate database.

Discuss the importance of business intelligence as it relates to databases.

What do you see as the benefits of using a web-like browser to access information from a data warehouse?

What advantage do non-relational databases and cloud databases provide to businesses?

Discuss management issues associated with databases like information policies, data administration, data governance, and data quality?

Compare your answers with  [link: https://canvas.park.edu/courses/57651/pages/unit-3-lecture-chapter-6-answers-to-review-questions] these.

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
