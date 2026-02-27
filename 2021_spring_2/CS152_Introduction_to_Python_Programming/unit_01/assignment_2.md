# Unit 1: Assignment 2

**Due:** 2021-03-22T04:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_text_entry, online_upload

## Instructions

Introduction

This assignment lets you practice with writing a program that accepts user input and performs some simple calculations.

Directions

Write a Python program that prompts the user to enter a number of quarts, and then calculates the number of barrels and remaining quarts, as well as the number of ounces, and then prints the results.

Notes

There are 32 ounces in a quart and 168 quarts in a barrel. Your program must declare and use several variables, like for the number of quarts and number of ounces. You should choose appropriate names based on your reading.

Your output should look like the examples. Be sure to print text and numbers without extra spaces.

Submission

Copy your program from the ActiveCode window in the text book and paste it into the text entry box. Be sure to use pre-formatted mode, like in the discussion. See the video  [link: https://canvas.park.edu/courses/59577/files/7735087/download?verifier=Z4MDGdgnBFXJsKymoQFaGzv7EmtQMCF4j3BvLwpj&wrap=1] Pasting Python Programs

Write a reflection in the text entry box answering the following questions:

What did you learn?

What was easy/hard? 

What questions or comments did you have on the exercise?

Example 1

Enter a positive number of quarts: 300

You entered 300 quarts, which is:
1 barrels and 132 quarts
or
9600 ounces

Example 2

Enter a positive number of quarts: 12

You entered 12 quarts, which is:
0 barrels and 12 quarts
or
384 ounces

---

## My Submission

**Score:** 10.0/10.0
**Grade:** 10
**Submitted:** 2021-03-17T22:15:54Z

Assignment 2:

number_quarts = int(input("Enter total amount of quarts"))
total_barrels = number_quarts // 168
remain_barrels = total_barrels % 168
total_oz = total_barrels * 32
print(total_barrels,"barrels and",remain_barrels,"quarts")
print("or")
print(total_oz,"ounces")

### Instructor Feedback

**Bert** (2021-03-17T22:15:55Z):

> 1)What did I learn: The lessons did a good job preparing me for the assignment.
2)Was it easy or hard: I had a little bit of issues on the first print function, I just had to clear the line and retype it.
3)Questions and Comments: I want to know if I am pasting and formatting the code properly. I fallowed the instructions, but it does not appear like the other students discussion post.

**[INSTRUCTOR]** (2021-03-27T01:23:44Z):

> Program   
input 2
barrels calculation 3
ounces calculation 2
variables 1

Reflection 2
What did you learn?
What was easy/hard?
What questions or comments did you have on the exercise?
