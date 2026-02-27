# Unit 6: Assignment 2

**Due:** 2021-04-26T04:59:00Z
**Points Possible:** 25.0
**Submission Types:** online_upload

## Instructions

Introduction

This assignment lets you practice with reading from a file and manipulating lists.

Preparation

This assignment must be done in a standalone Python environment, not the textbook. See the  [link: https://canvas.park.edu/courses/59577/pages/textbooks-and-materials] Textbooks and Materials page for instructions on installing the compiler on your local computer or using Park’s virtual desktop.

Download the following all to the same folder:

The program  [link: https://canvas.park.edu/courses/59577/files/7735206/download?verifier=MObYy13eIdJa1ik13RpcpKprqK2h26W6iOxx55yU&wrap=1] Lab9-start.py 

The data files  [link: https://canvas.park.edu/courses/59577/files/7735247/download?verifier=9YFbUie31zE6ZQgQJJGX42X94tNbcZO9FAu4x951&wrap=1] health-no-head-sample.csv and  [link: https://canvas.park.edu/courses/59577/files/7735202/download?verifier=A7hdKfDadgdRGgdJoWtybtdnNzmerwS4hBLYjpxu&wrap=1] health-no-head.csv 
 [link: https://canvas.park.edu/courses/59577/files/7735202/download?verifier=A7hdKfDadgdRGgdJoWtybtdnNzmerwS4hBLYjpxu&wrap=1] The big data file contains records of some infectious diseases from 1928 to 2011. The  small one only includes data from 3 years from 5 states. Run the python program. It should print something like this

MEASLES,206.98,COLORADO,2099,1014000,1928

['MEASLES', '206.98', 'COLORADO', '2099', '1014000', '1928\n']
MEASLES,634.95,CONNECTICUT,10014,1577000,1928 

['MEASLES', '634.95', 'CONNECTICUT', '10014', '1577000', '1928\n']
MEASLES,256.02,DELAWARE,597,233000,1928

['MEASLES', '256.02', 'DELAWARE', '597', '233000', '1928\n']
...

Make sure that you get output like this before starting the assignment or writing any additional code.

Directions

Modify the program in the following ways:

Write each line as part of a table, include a header before the table, and a summary line at the end. Use a fixed width for each column (don’t try to find the largest width like you did in the previous unit). You should end up with something like

State                 Disease        Number      Year

COLORADO              MEASLES         2,099      1928
CONNECTICUT           MEASLES        10,014      1928
DELAWARE              MEASLES           597      1928
…
DELAWARE              SMALLPOX            0      1930
DISTRICT OF COLUMBIA  SMALLPOX            0      1930
FLORIDA               SMALLPOX           28      1930
                      Total          52,307  
Not every field of the original line is used in the output. You will have to do some research about the .format() function to print the number of cases with a comma. If you can’t get the comma in the number column, move on and come back to that once you have more of the program written. The key is to have all the columns line up.  

Use some if statements to add three filters to your program that let the user select exactly one state, disease and year to include in the report. Prompt the user to enter these values.

Enter state: Colorado
Enter disease: smallpox
Enter year: 1928
State                 Disease        Number      Year

COLORADO              SMALLPOX          340      1928
                      Total             340   
Unfortunately, this isn’t very flexible.

Change your program so that if the user just hits return for a prompt, the program includes all the data for that field. For example:

Enter state (Empty means all): Colorado
Enter disease (Empty means all):
Enter year (Empty means all): 1928
State                 Disease        Number      Year
 
COLORADO              MEASLES         2,099      1928
COLORADO              POLIO              71      1928
COLORADO              SMALLPOX          340      1928
                      Total           2,510    
Your program should run as expected using this small data set

Change the open statement in the program to use the full data set, health-no-head.csv.

Write down the answers to the following queries:

How many cases of Hepatitis A were reported in Utah in 2001?

How many cases of polio have been reported in California?

How many cases of all diseases were reported in 1956?

Add another feature to your program. 
This could be something like printing the highest and lowest numbers for each query, or allowing the user to just type the first part of value, so that entering 20 for the year generates a table for years 2000, 2001, 2002, … 2011, or entering D for a state gives information on Delaware and the District of Columbia. Or maybe leverage your previous assignment and make the column only as wide as they need to be for the data. Try to make it something useful.

Comment your code.
Be sure to add a header comment to your program and any functions, and appropriate comments before other blocks of code.

Submission

Submit the file with .py extension.

Write a reflection in the comment box answering the following questions:

Show the answers from Step 5.

Describe your added feature from Step 6. Show the code that accomplishes this.

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

In a sentence or two, if you had another hour or two, what would you like to add to the project or how would you do things differently?

---

## My Submission

**Score:** 25.0/25.0
**Grade:** 25
**Submitted:** 2021-04-25T06:25:05Z

### Submitted Files

- **unit6 assignment2.py**
  - Downloaded: `files/unit6 assignment2.py`

### Instructor Feedback

**Bert** (2021-04-25T06:25:05Z):

> 1) 59 and 47,743 and 631,797
2) My feature allows you to enter part of a year, another lets you enter a location without capitalization.
3) I learned some interesting things about if statements in a list
4) I enjoyed this projected because it felt like I was actually was getting to practical skills.
5) I struggled on a few things, the if statements especially.
6) I would like to experiment with putting a range of years into the input.

**[INSTRUCTOR]** (2021-05-11T19:09:33Z):

> Assignment #6-2  25 
comments   3
table header and summary  4
data neat columns   4
input filters    3
empty input filter  3
new functionality  3
reflection   5
Describe your added test cases and why you chose them.
what did you learn?
what did you like about this project?
what did you find confusing?
what would you like to add to the project
What questions or comments did you have?
