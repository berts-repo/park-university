# Unit 4: Discussion

Dear Students,

Please read carefully the directions for this discussion thread since it is different from any other we had in the course. The Rubric is also different and it is displayed at the end of this narrative.

Directions

After reading the assigned material, students must present three (3) postings according to the directions below:

Initial Post – The purpose of the initial post is to present an example to illustrate one of the following topics:

A concrete example (not from the textbook) of one of the possible ways in which a company may handle missing data for a field in a database entry. Show tables and fields as part of the explanation.

A concrete example (not from the textbook) of a situation in which de-normalization could be advantageous to handle a database. Show tables and fields as part of the explanation.

A concrete example (not from the textbook) of a situation in which partition could be advantageous to handle a database. Show tables and fields as part of the explanation.

A concrete example (not from the textbook) a situation in which indexing a table by a field (or fields) that are not part of the primary key could be advantageous to handle a database. Show tables and fields as part of the explanation.

A concrete example (not from the textbook) of a company that decided to use a Two-Tier Architecture. Explain how this architecture is implemented in your example and the advantages that it provides. Show diagrams of this architecture.

A concrete example (not from the textbook) of a company that decided to use a Three-Tier Architecture. Explain how this architecture is implemented in your example and the advantages that it provides. Show diagrams of this architecture.

The initial posting must be made by 11:59 p.m., Thursday, CT. More than one student may select the same topic, but each one must present a different example as an answer. The initial post must:

Be about 100 words or more.

Begin by indicating the number and the text of question being answered (not part of the 100-word count)

Reflect the student’s understanding of the assigned readings for the week.

Use critical thinking to describe how the example fits the topic selected.

First Response Post – Student must respond to at least one of the initial postings from your fellow student’s posts by 11:59 p.m., Sunday, CT. This reply should:

Contain a critical question over the example presented in an Initial Post by another student (students may not have a first reply for their own Initial Posting). A critical question is intended to go deeper into the substance of the example and the topic to reveal new knowledge, establish relations between important concepts, and/or suggest possible new uses in other contexts. For example, critical questions may help to:

Analyze or break down the information provided into its component parts (What are the most important/significant ideas of…? What assumptions/biases underlie in …? What part of … are similar/different to …?).

Synthesize or connect separate pieces of information (How can this be combined with… to create …? How can these different ideas be grouped into a more general category?).

Evaluate or judge the validity of data, ideas, data, etc. (How would you judge the accuracy or validity of…? How would you evaluate the ethical implications of…?).

Deduct or draw conclusions about examples that are logically consistent with other situations (What conclusions can be drawn from …? If this is true, what is the logical conclusion of …? What practices would be consistent with …?).

Engage balanced thinking to consider arguments and evidence for or against a particular position (What are the strengths and weaknesses of…? What evidence supports/contradicts …?).

The first response may not include any possible answer, just a question.

Second Response Post – Student must respond to at least one of the questions posed by another student in their first response posts by 11:59 p.m., Sunday, CT. This reply should:

Be about 100 words or more.

Use critical thinking to answer the question posted in the first reply.

Students may select to answer the questions posed to their own initial posting or to another student’s initial posting.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-11-11T07:26:29Z

Hello class,

I will be answering prompt 3: A concrete example (not from the textbook) of a situation in which partition could be advantageous to handle a database. Show tables and fields as part of the explanation.

The first thing I thought of when trying to find a good example of reasons to partition a database would be for a nation wide census. It could be optimized with horizontally partitioning of people in different zip codes. This would help with efficiency, instead of dealing with hundreds of millions of people, one could query a much smaller group of people per county.  This would help with load balancing, if you wanted to compare the parallel partitions. It could help with backup and storage as each database would be much smaller, and it would also help with maintenance as each database could be managed by each individual county.

SSN
FirstName
MiddleInit
LastName
Address
State
Zipcode

111-11-1111
Abby
L
Gablin
322 w 9th
Missouri
64153

222-22-2222
Brett
M
Holland
4252 Francis
Pennsylvania 
15106

333-33-3333
Carl
N
Indigo
2 Fall Dr.
Missouri
64153

444-44-4444
Donald
O
Joy
3117 Baker
Missouri
64153

555-55-5555
Francis
P
Kip
342 158th St
Pennsylvania
15106

If I understood the book correctly, once the partitions are established you will have to use a partition key to represent the relationship between the databases. You if my reading comprehension is correct, you can select to have fields included or excluded from he partition.

SSN
FirstName
MiddleInit
LastName
PartitionKey/Zipcode

222-22-2222
Brett
M
Holland
15106

555-55-5555
Francis
P
Kip
15106

---


### Feedback

**[INSTRUCTOR] Ph.D.:** Participation satisfies requirements.
