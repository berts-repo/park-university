# Unit 3: Assignment 2

**Due:** 2021-04-05T04:59:00Z
**Points Possible:** 20.0
**Submission Types:** online_upload

## Instructions

Introduction

This assignment lets you practice with writing and using functions. You are rewriting existing code to use functions so the behavior of the program should not change throughout this exercise.

Preparation

Download and run the program  [link: https://canvas.park.edu/courses/59577/files/7735215/download?verifier=AxXmCaYD7M2pfBQM64wLN9RWvwD7rDh4yVUZu2hZ&wrap=1] PracticeFunctions.py. Look at what it does and look at the code to get an idea of the program structure.

Directions

The programming assignment for this unit has two functions.

Use these two functions as models for the functions you are to write.  
You will be removing code from main() and putting it in several separate functions. The behavior of the program will not change throughout the exercise, so you can always tell if your program is correct.

Use the non-fruitful function drawRect as a model. Write another non-fruitful function that moves a turtle forward without drawing a line. The function is defined as

def skipForward(t, len):

    """ Moves the turtle t forward len units without drawing anything. """

and called with a statement like

skipForward(alex, 20)

The contents of the function are to lift the pen, move the turtle, then lower the pen.

Write another non-fruitful function skipTo, which is defined as

def skipTo(t, x, y):

    """ Moves the turtle t to coordinates (x,y) without drawing anything. """

and is called with

skipTo(alex, xpos, ypos)

Make sure to use the parameters x and y in the body of this function.

Next, you'll work with fruitful functions. Look at the function to calculate the next y-position for drawing a set of shapes. This function is called near the bottom of the program:

ypos = next_y_position(ypos, width)

Using this function as a model, add a fruitful function to calculate the perimeter of a rectangle. The function is defined with

def perimeter(len,wid):
    """ Returns the perimeter of rectangle with sides len and wid. """

and  it is called with the statement

p = perimeter(length, width)

Make sure you use the parameters len and wid in the body of the function.

Again, using this function as a model, add a fruitful function to calculate the value math.sqrt(length*width/math.pi) which appears near the end of the program. The function should be defined as

def circ_rad(len, wid):
    """ Returns the radius of a circle with
an area of len * wid """

Mimic the call from what you did in the previous step.

Make sure that your main function is calling skipForward and skipTo in at least two different statements. This is one of the benefits of using functions is that you can call them multiple times, often with different parameters. Ask if you are unsure what this means.

Make sure your functions have the same parameters and the same comment as in the assignment description. Write a complete header comment.

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
**Submitted:** 2021-04-02T06:43:17Z

### Submitted Files

- **unit3 assignment2.py**
  - Downloaded: `files/unit3 assignment2.py`

### Instructor Feedback

**Bert** (2021-04-02T06:43:17Z):

> 1)The unit assignment did a good job preparing me again. Although I learned I learned I have to spend alot of time just staring at the screen, trying to wrap my head around something.
2)I like how I saw some of the features screen properties. I also liked seeing more advanced code related to my own current skill level.
3)I think the project was good, although I didn't quite understand what was going on with the screen parameters. 
4)I would spend more time staring at the screen, trying to get a little bit more understanding of what's going on, although I do have a good idea.

**[INSTRUCTOR]** (2021-04-17T01:06:20Z):

> Assignment #2
skipForward  2
skipTo 3
perimeter  3
circ_rad  3
function use  4
structure 3
Reflection  2
