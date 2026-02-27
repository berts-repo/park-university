# Unit 7: Assignment

**Due:** 2021-05-03T04:59:00Z
**Points Possible:** 20.0
**Submission Types:** online_upload

## Instructions

Introduction

This assignment lets you practice with reading from a file, writing to a file, and using dictionaries.

Preparation

This assignment must be done in a standalone Python environment, not the textbook. See the  [link: https://canvas.park.edu/courses/59577/pages/textbooks-and-materials] Textbooks and Materials page for instructions on installing the compiler on your local computer or using Park’s virtual desktop.

Download the data file  [link: https://canvas.park.edu/courses/59577/files/7735218/download?verifier=dQ6AWhKVWQi8p9wQH2VobnZSgPLJooXzzG9deKlB&wrap=1] state_crime.csv. This data file contains records of different types of reported crimes. The first line of the file contains a description of each column of data. 

Directions

Write a python program to read the file, and produce a summary of the total reported crimes for each state. The report will look something like this, though don't worry if your list is not in alphabetical order:

State            Reported Crimes      
Alabama                8,133,055
Alaska                 1,198,047
...
Wyoming                  834,588
United States        563,841,249

There are a lot of fields in the data file, but you can simplify your life by using subtotal fields, Totals.Property.All and Totals.Violent.All.

Once you  have the summary, change your program so it writes the summary to a file, crime_summary.txt.

Make sure you use a dictionary for this assignment. The obvious case is to use a key of state names and the value is the accumulated count of reported crimes. There might be a place for another dictionary as well, though you only need to use one.

Be sure to add a header comment to your program and any functions, and appropriate comments before other blocks of code.

Submission

Submit the file with .py extension.

Write a reflection in the comment box answering the following questions:

 In a sentence or two, what did you learn?

 In a sentence or two, what did you like about this project?

 In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

 In a sentence or two, if you had another hour or two, what would you like to add to the project or how would you do things differently?

---

## My Submission

**Score:** 20.0/20.0
**Grade:** 20
**Submitted:** 2021-04-29T08:51:35Z

### Submitted Files

- **unit7 assignment1.py**
  - Downloaded: `files/unit7 assignment1.py`

### Instructor Feedback

**Bert** (2021-04-29T08:51:35Z):

> 1) I learned to iterate through a nested dictionary, and write it to a file.
2) I like this project because I can begin to see my skills developing.
3) I don't know why I couldn't run a while loop to iterate through the original .csv file. I kept getting an error even if I stopped the iteration with .readline().
4) I would like to add some more search parameters, to be able to choose the year and get the totals through the year and state

**[INSTRUCTOR]** (2021-05-11T20:17:42Z):

> Assignment #7  20
comments          3
Read/Parse input  3
Create dictionary 4
Formats output    4
File Output       3
Reflection        3
Describe your added test cases and why you chose them.
what did you learn?
what did you like about this project?
what did you find confusing?
what would you like to add to the project
What questions or comments did you have?
