# Unit 3: Summary of Normalization

Unit 3 – Normalization – Summary of Steps

The following is a summary of the steps involved in the normalization of a database to Third Normal Form. This summary will also shows an example of the application of the normalization steps on a database design. This sample database design has the following ERD and relational database model:

 

               

The functional dependency diagram for this relational database model is also:

 

The normalization steps are as follows:

Normalization Steps

Outcome

Example

1. Eliminate multivalued attributes by correct translation to a relational database model.

The relational database will be in First Normal Form (1NF).

The relational database model presented above is already in 1NF, because the multivalued attribute G correctly spawned a table with primary key made out of A and G fields and the foreign key A is pointing to the original Entity1 table.

2. Eliminate partial dependencies in each separated table. This step has various sub-steps:

a.   If all non-key fields depend fully of the primary key in their tables, there are no partial dependencies

The table will be in Second Normal Form (2NF).

In table Entity2, there are no non-keys, both A and G are part of the primary key, therefore the table Entity2 is already in 2NF.
On the other hand in the table Entity1, the field C only depends of B, not A (part of the primary key). Similarly, the field D only depends of A, not B. These are partial dependencies to be eliminated. It is assumed that the remaining non-key fields E and F are fully dependent of both, A and B.

 

b.   For every table with partial dependencies, break their primary keys in as many non-empty subsets as possible. 

The initial seed for normalized tables in 2NF.

The primary key for the table Entity1 that has partial dependencies is AB. All possible non-empty subsets of AB are:A, B and AB. Each one will be the seed for new tables that will replace Entity1. Please notice that if the primary key had 3 fields, like ABC, the number of subsets will be larger: A, B, C, AB, AC, BC, and ABC.

 

c.    For every subset created in b, starting from the smallest to the largest, we must attach all non-keys fields that depend exclusively on that subset of primary keys and the fields that depend of these attached non-keys. 

The table will be in Second Normal Form (2NF).

The set A will attach the field D that depends directly from it. It will also attach the field F that depends on D.

The set B will attach the field C that depends directly from it.

The set AB will attach the remaining field E that does not depend individually from A or B, but it is then assumed to depend of the whole set AB.

The final new tables that replace Entity1 will be ADF, BC, and ABE.

 

Note: if the sets with only one element do not attach any other field, that table should be eliminated. For example if C did not depend of B, the subset with B alone should have been eliminated.

3. Eliminate transitive dependencies in each table. If a table has a transitive dependency, separate the fields involved in this dependency into a new table. The primary key in this new table will be the field that determines the dependency. This same field will be a foreign key pointing to the old table. To make this possible, a copy of this field will also remain in the original table.

The table will be in Third Normal Form (3NF).

 

 

 

 

 

 

 

The table ADF has a transitive dependency between D and F fields. To eliminate this dependency we create the table DF with D as the primary key. D will also be the foreign key, so a copy of D must remain with the original table. The original table is therefore converted onto AD.

The following diagrams show the transition of the original tables in the example, already in first normal form, towards second and third normal forms.
