# Unit 2: Discussion

Graphics

This discussion will let you look at different ways of drawing the same shape

Directions

Initial Post: Post your initial post by 11:59 p.m., Thursday, CT. 

Reply Posts: Reply to two or more classmates as per the specific instructions by 11:59 p.m., Sunday, CT.

When pasting code into Canvas, be sure to use the pre-formatted mode. See the video  [link: https://canvas.park.edu/courses/59577/files/7735087/download?verifier=Z4MDGdgnBFXJsKymoQFaGzv7EmtQMCF4j3BvLwpj&wrap=1] Pasting Python Programs

Discussion Prompt

Initial Post:

Write a python program that draws a closed a shape. Your shape doesn’t have to be fancy, but draw something besides a square, triangle or rectangle. Don’t duplicate a program that is already in the discussion.

For example:

import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex

alex.forward(100)
alex.left(90)
alex.forward(10)
alex.left(90)
alex.forward(20)
alex.right(90)
alex.forward(80)
alex.left(90)
alex.forward(60)
alex.left(90)
alex.forward(80)
alex.right(90)
alex.forward(20)
alex.left(90)
alex.forward(10)  

First Reply Post:

Respond to another student’s code by drawing the same shape in a different way. Maybe you use variables, maybe change the order of drawing, maybe use a loop, just do it differently. Explain what you changed.

Second Reply Post:

Respond to a different student by comparing two solutions. State which solution you think is better and why, or state why neither is significantly better than the other.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-03-25T00:02:13Z

Hello Class,

I noticed I couldn't speed up the turtle, because he was only moving 1 place per loop on the range. There might be a more efficient way of doing this but I was just playing around.

import turtle                    #turtle library
import math                      #used for pi
wn = turtle.Screen()
franklin = turtle.Turtle()

franklin.color('black')          #coloring in half the circle
franklin.begin_fill()
for circle in range(180):        #range of half circle
    franklin.forward(1)
    franklin.left(1)
franklin.left(90)
franklin.forward(360/math.pi)    #math import
franklin.end_fill()

franklin.right(90)               #second half of circle
for circle in range(180):
    franklin.forward(1)
    franklin.right(1)
franklin.right(90)
franklin.forward(360/math.pi)    #math import

wn.exitonclick()

---


### Feedback

**[INSTRUCTOR]:** Very good!
Discussion  10 pts
Initial Post   5
Reply Post   5
