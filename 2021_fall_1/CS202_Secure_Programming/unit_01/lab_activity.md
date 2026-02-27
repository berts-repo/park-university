# Unit 1: Lab Activity 

**Due:** 2021-08-23T04:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Introduction 

The purpose of this assignment is to practice the creation of simple C/C++ programs that follow the input-process-output paradigm.

 

Requirements for the program include:

Name the C/C++ file with the following format: LastNameFirstNameUnit1cpp. For example the Instructor may create a file with the following name: [INSTRUCTOR]Unit1.cpp.

Select appropriate identifiers and data types for all variables. Declare all of them correctly.

The input variables are top radius of the spherical segment (a), the bottom radius of the spherical segment (b), and the height of the spherical segment (h). All input values for these variables must be read from the user using scanf. These values must be printed after received, with appropriate labels to identify them. This will confirm that the values were properly read.

Evaluate the requested formulas and store their results in output variables.

Print the values for output variables after evaluation, with appropriate labels.

Include appropriate comments. In particular include a header for the main function and description of all variables.

The program should compile and run.

Deliverables

Submit only the C/C++ program file when completed. Do not submit anything else. This file is the .cpp file you created with the right name.

Due Date

by 11:59 p.m., Sunday, CT

Directions 

Write a C/C++ program to calculate the following formulas that describe the dimensions of a spherical segment (shown):

 

Some formulas require the value of . You may use the value of 3.14159265359 for this constant. Other formulas include a power of two of a variable, for example h2. To evaluate this, all you must do is to multiply the variable by itself (h*h). On the other hand, to evaluate the square root of a variable, you may use the sqrt function. This function requires you to include the math.h C library at the beginning of the program, like this:

#include <math.h>

 To calculate the square root of variable h you should write; sqrt(h)

Do not use Arrays or any other advanced concept that was not reviewed in the class yet to solve this assignment. Assignments that use these concepts will only be granted 1 point for presentation.

Example

The program should reproduce the following input-output session:

What is the size of the top radius of the spherical segment?
10
What is the size of the bottom radius of the spherical segment?
20
What is the size of the height of the spherical segment?
10
The data your entered is:
The top radius of the spherical segment is 10.00.
The bottom radius of the spherical segment is 20.00.
The height of the spherical segment is 10.00.
With this data you have the following results:
The volume of the spherical segment is 8377.58.
The top surface area of the spherical segment is 314.16.
The bottom surface area of the spherical segment is 1256.64.
The sphere radius of the spherical segment is 22.36.
The lateral surface area of the spherical segment is 1404.96.

---

## My Submission

**Score:** 10.0/10.0
**Grade:** 10
**Submitted:** 2021-08-24T09:02:02Z
**Late:** Yes

### Submitted Files

- **BertUnit1-1.cpp**
  - Downloaded: `files/BertUnit1-1.cpp`

### Instructor Feedback

**Bert** (2021-08-23T03:02:59Z):

> I have not been able to get my variables to store in memory. I have spent 10hrs trying to get it to work and really could use another hint. I even tried just assigning them without an input 'int a = 10;' and had no luck.

**Bert** (2021-08-24T09:02:03Z):

> Hello Professor,
I do not expect to get extra points because I am resubmitting the assignment. I just figured out what I was doing wrong and wanted to resubmit the assignment. I was using placeholders in the print function block, so removing those fixed my issue with my variables. I also was able to see what my calculations were outputting and I fixed my calculation for volume.
Thanks and sorry for a wasted response if you don't see this in time.

**Luke Donoho** (2021-08-25T01:38:31Z):

> Bert - Welcome to the world of programming! These things happen and this is how we learn.
