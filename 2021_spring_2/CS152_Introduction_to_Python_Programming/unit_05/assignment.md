# Unit 5: Assignment

**Due:** 2021-04-19T04:59:00Z
**Points Possible:** 20.0
**Submission Types:** online_upload

## Instructions

Introduction

This assignment lets you practice manipulating strings, including slices, justification, and other string methods. You'll revisit this program again in the next unit.

Preparation

Review the string functions in section 9.5 of the text. You'll also find the function isdigit() useful, which is documented at  [link: https://docs.python.org/3/library/stdtypes.html#string-methods] Python.org: String Methods. 

 Download the starter program,  [link: https://canvas.park.edu/courses/59577/files/7735077/download?verifier=K1lVj8cs5jGKTeRMeI5uZmDOrLRo6wxzRs2SS8Xg&wrap=1] Courses.py, compile and run. This gives you the list of data to use to test your program.

Directions

Your assignment is to take a list of strings representing (Department code, course number, title, enrollment) and print them in nice tables, one per line.  Data looks like

'CS152Introduction to Python Programming21'

or

'CS352Data Structures19'

The department code and course number are always the same size, but the course titles contain different numbers of words and are different lengths. The enrollment numbers will always be between 1 and 999. Unfortunately, when the data was generated, the programmer forgot to add a space between each of the components, so you will have to deal with that in your program. 

Look at the string methods in section 9.5 for how to do this. You may want to look on the web for some additional examples. You do not have to use the .format() method in order to accomplish this lab, nor do you  need any techniques from Chapter 10.

For Table 1, print just the department code and course number, separated by a space

Table 1

CS 152
CS 369
...
MG 315

For Table 2, print all the data in the string, with a single space between each piece.

Table 2

CS 152 Introduction to Python Programming 21
CS 369 Operating Systems Administration 8
CS 352 Data Structures 19
CS 208 Discrete Mathematics 124
CS 319 Computer Architecture 14
MA 221 Calculus and Analytical Geometry for Majors I 12
MA 311 Linear Algebra 7
MA 150 Precalculus Mathematics 27
CS 335 Introduction to Cybersecurity 20
IS 361 Data Management Systems 22
MG 315 Advanced Business Statistics 6

For Table3, truncate the titles to the number of characters shown, but watch out for short titles. Make sure the enrollments all line up as shown. Add up all the enrollments and print the total.

Table 3

CS 152 Introduction to Pyth  21
CS 369 Operating Systems Ad   8
CS 352 Data Structures       19
CS 208 Discrete Mathematics 124
CS 319 Computer Architectur  14
MA 221 Calculus and Analyti  12
MA 311 Linear Algebra         7
MA 150 Precalculus Mathemat  27
CS 335 Introduction to Cybe  20
IS 361 Data Management Syst  22
MG 315 Advanced Business St   6
                     Total: 280

For Table 4, sort the list (this is one statement in Python), and print the complete title, but make sure all the enrollments line up as shown.

Table 4

CS152 Introduction to Python Programming             21
CS208 Discrete Mathematics                          124
CS319 Computer Architecture                          14
CS335 Introduction to Cybersecurity                  20
CS352 Data Structures                                19
CS369 Operating Systems Administration                8
IS361 Data Management Systems                        22
MA150 Precalculus Mathematics                        27
MA221 Calculus and Analytical Geometry for Majors I  12
MA311 Linear Algebra                                  7
MG315 Advanced Business Statistics                    6

For Table 4, make sure your program actually prints the table based on the length of the longest title. You will have to write code to find the length of the longest title, then use that number. For instance, if the data only had CS 208 and MA 311, the table would look like

CS 208 Discrete Mathematics   24
MA 311 Linear Algebra          7

Once your program works with the provided data,

a) add a record to the list to demonstrate your code still computes a total correctly,

b) add a second record to the list to demonstrate your code still sorts the list correctly,

c) add a third record to the list to show that your program always creates a neat table, no matter how long or short the titles are.

Notes

The tables increase in complexity, so work on them in order.

Be sure to document your program with an appropriate header comment, including your name, date, and description of what the program does. Also add comments before blocks of code, rather than at the end of a line.

Some students think the way to solve this problem is to retype the original data to fix the spacing problems. Don't try that approach - you won't receive any credit if you do that.

Submission

Submit the file with .py extension.

Write a reflection in the comment box answering the following questions:

Describe your added test cases and why you chose them.

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

In a sentence or two, if you had another hour or two, what would you like to add to the project or how would you do things differently?

---

## My Submission

**Score:** 20.0/20.0
**Grade:** 20
**Submitted:** 2021-04-18T12:37:28Z

### Submitted Files

- **unit5 assignment1.py**
  - Downloaded: `files/unit5 assignment1.py`

### Instructor Feedback

**Bert** (2021-04-18T12:37:28Z):

> 1) I think you are talking about the added data entry's for question one? I chose some random names to test the length and sort function.
2) I learned a bit on this assignment, it was a lot of trail and error.  I specifically learned about spacing and separating white space.
3) This project tested my skills and it seemed like it could be a real world problem
4) I feel like some of the requirements are not fully covered through the chapter  but that is probably part of the debugging and learning proces.
5) I want to work with strings longer
