# Unit 1: Discussion

Introduction 

Participation in discussion threads is a weekly assignment that tests your reading process and critical thinking. You may participate in these discussion threads for this unit between 12:00 a.m., Monday, CT through 11:59 p.m., Sunday, CT. of the corresponding week.

 

Requirements

Your initial post must answer both of your chosen questions by 11:59 p.m., Thursday, CT. If your program is still not fully functional, post what you have, explaining what is missing and how you plan to complete it. If you have problems, describe them so that the class can try to help you in fixing them.

You must complete your own posting and respond to at least one other student thread (different than your own) by 11:59 p.m., Sunday, CT.

Throughout the week, you must respond, to the best of your knowledge, the questions or requests made by Instructor and/or students, especially the Instructor’s requests for corrections.

Due Date

Initial post by 11:59 p.m., Thursday, CT

Respond to one or more classmates by 11:59 p.m., Sunday, CT

Directions 

This discussion thread has two parts. After reading the assigned course material, this is what you must do:

Part 1

Think and write any arithmetic expression that uses the following 5 basic operations in C at least once: +, -, * /, and %. The expression may or may not have parentheses. Evaluate the operations and produce a final result for the expression following the C order of precedence for operations. The posting must show the order in which operations were performed.

 

Examples (do not use these for your response):

54 % 5 + 3 / 2 - 3 * 2 = 
4+1-6 = -1 
   OR

54 % ((5 + 3) /2) – 3 * 2 = 
56 % (8/2) - 6 = 56 % 4 - 6= 0 - 6 = -6

Part 2

Select a mathematical formula that calculates something you have studied or used before, and that requires at least two input variables. However, do not select any formula given in any Programming Assignment. Programming Assignments are personal and should not be shared with anybody but the instructor.

Write a C/C++ program to calculate your selected formula. The program must include the following:

Appropriate selection of data types for all variables. Declare all of them correctly.

Commands to read values for your input variables from the user. These values must be printed after received with appropriate labels to identify them. This will confirm that the values were properly read.

Perform of calculations into output variables to obtain the formula.

Printing of the values for output variables with appropriate labels.

You must use the scanf and printf C commands for Input/Output. The program must compile and run in Microsoft Visual Studio.

Post the contents of your C/C++ program in this environment. Do not attach the code, but copy and paste the entire source file onto the discussion thread. When you do that, you may lose some indentation. You need to restore this indentation manually to make the program readable. Attach a screenshot of the program completely running in a console window as a proof that the program compiled and run. 

Please read what other students are posting and post all different formulas. Do not repeat previous postings. Be Original. There are plenty of formulas around our daily life if we pay enough attention. Also, do not write programs about the formulas you have to calculate in Programming Assignments.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-08-19T07:11:43Z

Part 1

(4 + 2 - 3 * 2 / 2) % 2

(4 + 2 - 6 / 2) % 2

(4 + 2 - 3) % 2

(4 - 1) % 2

3 % 2

1

 Part 2 
#include /*testpercent.cppBert8/19/2021This program ask the user to input a test score,and it calculates the percent they recieved.*/int main() {    float score_received;    float total_points;    printf("how many points is the test worth?\n");    scanf_s("%d", &total_points);    printf("how many points did you get?\n");    scanf_s("%d", &score_received);    printf("you got a %.2f percent!\n", score_received / total_points);}

---
