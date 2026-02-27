# Unit 4: Assignment

**Due:** 2021-04-12T04:59:00Z
**Points Possible:** 20.0
**Submission Types:** online_upload

## Instructions

Introduction

This assignment lets you practice with writing and using conditional statements, boolean functions, and while loops.

Preparation

Download the program  [link: https://canvas.park.edu/courses/59577/files/7735226/download?verifier=NBQ3MMMEcW0KgputEHXp9p3okqp6zSo5juZyLcDG&wrap=1] RandomTurtle-book-main.py which is the program from the book, but with a main function and better variable and parameter names. Make sure you can run the program before you do anything else.

Directions

Modify the program in the following ways:

Write appropriate comments for this program and function. Include:

A header comment for the program

A header for the function describing the parameters and return value.

Comment the blocks of code. 
The text has descriptions of all this, so reread that if necessary.

Following the process in the previous unit’s assignment, write a function to randomly move a turtle. The function should have at least one parameter, the turtle to move. Call this function in your main program instead of the code that is already there. If you do this correctly, your program will behave the same.

Create a second turtle, make it a different color, and start it at a different location than the current one. The location should be 100 units away, either horizontally or vertically.

The second turtle should move randomly 5 times for every time the first turtle does. It should also move 1/5 the distance as the original turtle each time. This is where having a function with proper parameters comes in handy.

After the loop, write a message, in the center of the window, indicating which turtle was higher up. Use the turtle that is higher (more toward the top of the screen) to do the writing. Be sure your message specifies the turtle. See the write() function in the turtle module for writing text messages in the window.

Once your program works the way you want, rewrite the if statement in the function isInScreen, so it still implements the same logic, but does it a different way. For example, maybe you can use an elif, or maybe you can write several statements and eliminate the use of or. You should probably do this step last, or else if you make a mistake, you'll never be able to debug the rest of your code.

 Submission

Submit the file with .py extension.

Write a reflection in the comment box answering the following questions:

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

In a sentence or two, if you had another hour or two, what would you like to add to the project or how would you do things differently?

Write a few sentences about why you think your new if statement(s) for step 6 are correct.

---

## My Submission

**Score:** 20.0/20.0
**Grade:** 20
**Submitted:** 2021-04-12T00:56:47Z

### Submitted Files

- **unit4 assignment1.py**
  - Downloaded: `files/unit4 assignment1.py`

### Instructor Feedback

**Bert** (2021-04-12T00:56:47Z):

> 1) I learned a bit about calling functions and debugging.
2) I liked how challenging it was
3) I still don't understand why I had to call the return of the stillin function, when in the while statement.
4) I would of not asked for help and worked on it figuring it out.
5) The elif works becuase it can only exit on 2 plates x and y. If the turtle were draw a line at a 45 degree angle, and leave at a corner this might cause an error

**[INSTRUCTOR]** (2021-04-24T01:50:01Z):

> Program   
turtle shapes  4
for loop 3
in line comments 2
header comments 1
variables/constants 2

Reflection 3
What did you learn?
What was easy/hard?
