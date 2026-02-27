# Unit 7: Content Hightlights - Data and Database Administration 

This page highlights the main points on Data and Database Administration, and complement some of the textbook explanations. It is recommended to first read this week’s assigned chapters from the textbook, and then come back to this document for further commentary.

The highlights of this week’s readings are:

A Data Administrator Does Not Necessarily Administer The Database.

There is a difference between being a data administrator and a database administrator. The data administrator is concerned with the data itself. Her/his main concerns are that data is accurate and well-defined, as well as protected and in compliance with norms and regulations for the industry. However, s/he could do that without having to manage the database itself. The database administrator is the one who manages the database itself. S/he is in charge to create, maintain and report on the files that make up the database and their relationships. Data and database administrators could be the same person, but they are two distinct roles. The textbook pinpoints traditional tasks for each one of these roles:

A data administrator is concerned with:

Data policies, procedures and standards

Leadership on planning databases for growth

Resolution of conflicts relating to data and data ownership

A database administrator is concerned with:

Analyzing, designing and implementing the database

Selecting the DBMS and all related software

Installing and maintaining the DBMS

Tuning database performance including query performance

Managing physical data security, privacy and integrity

Creating backups and recovery of data when needed.

Security Treats

The following is a list of common threats to computer systems in general, and databases in particular, Data and database administrators should be prepared to fight the following threats:

Errors and accidents:

Human errors

Procedural errors

Software errors

Electromechanical problems

“Dirty data” problems

Natural hazards

Computer Crimes

Theft of hardware and/or software

Theft of data content

Theft of time and service

Internet related fraud

Data kidnapping and/or ransom

Provoked system crashes

Computer Criminals

Individuals or groups outside the company

Disgruntled employees

Outside partners or suppliers

Corporate spies

Foreign intelligence services

Organized crime

Terrorists

Views

One of the tools database administrators have to prevent unauthorized access to data is the use of Views. Views are pre-coded queries in the DBMS. They are executed every time the View is invoked. Database administrators may assign Views to users that require their information for display and nothing more. This prevents granting unnecessary access to sections of files outside the view.

Integrity Controls

Entity and Referential Integrity are examples of integrity rules that DBMSs are expected to enforce. Many databases these days allow for the enforcement of more integrity controls, if the design of a database calls for them. Simple rules like the type of information that can be entered in certain fields and their range are common place and easy to make them enforceable by the database itself. Larger DBMSs may also allow more sophisticated rules, called Assertions. These rules specify conditions that should always be enforced in a database and they may involve many tables and fields. DBMSs that support assertions prevent changes in the database contents that would make the assertion to become false.

 

Backup and Restore

When databases get corrupted, the best way to fix them is by using previous backups. Therefore it is important to perform regular backups. In between backups, all modifications made to the data must be journalized into log files. Log files should include dates and times when modifications were made, the location of the modified fields and the extent of their modification. Also, the status of these fields and their tables before and after the modification should also be recorded. This way, when repairing a corrupted database, we may begin from the last backup and perform the modifications in the log files until we get to a good state (process known as roll forward), or we could begin from a corrupted database and undo transactions from a log until a good state in the database is reached (process known as backward recovery).

Concurrency and Deadlocks

In a multi-user database system, various users may require access to a field, a record or a table (known as resources) at the same time. This is called concurrency. To avoid inconsistencies that may affect the database, most systems use locks to avoid access to users when a resource is currently used by another user. After the source is released, the lock is opened and any other user can access the resource. A common problem with these locks happens when each of two users may need the same two resources. One user might have locked the first resource and the second user may have locked the second one. Each one of the users will be waiting for the other user’s locks to be opened, but neither resource will be released. This is called a deadlock. The textbook explain some strategies to deal with deadlocks.
