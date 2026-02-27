# Unit 3: Discussion

Functions

This discussion will let you code and use different types of functions. In addition to the required posts involving code, you will probably have other interactions requesting clarifications or explanations. You should respond to any of these posts addressed to you or help another student who is having issues.

Directions

Initial Post: Post your initial post by 11:59 p.m., Thursday, CT. 

Reply Post: Reply to one classmate as per the specific instructions by 11:59 p.m., Sunday, CT.

Discussion Prompt

Initial Post:

For your initial post, modify one of the two templates below to define and then call a function. Your function can be like the examples, or more complicated if you want the challenge. The focus is on keeping the template structure and using one or more parameters correctly.

Some ideas for a fruitful function are:

Perform another mathematical operation, like subtract 17, or multiply by 5.25

Add up all the odd numbers from 1 to some limit

Add up all the even numbers from 2 to some limit

Add up all numbers in some range (needs two parameters)

Some ideas for a non-fruitful function with a turtle are

Draw another regular polygon (pentagon, hexagon, octagon)

Draw a right triangle

Draw a filled circle that changes colors (see .dot() function)

Draw a target design with different colored bands

Be sure to change the comments to say what your function does and what the parameters are!!!!

Reply Post:

Respond to another student’s code with modifications that

Change the function to have one additional parameter. You will also have to change the call in the main function. Be sure to use the value of the parameter in the function. Also document your additional parameter and function behavior.

Call the function at least three times with different values. If the original program already did this, use different values than the original.

Fruitful function example:

# Illustrate calling a function and printing the result
# John Cigas, 2/10/2019

# Define functions
def addeight(n):
    """Returns the numerical value of n + 8, where n is an integer or float"""

    return n + 8

def main():
    """This is where you define your variables and do input and output"""
    
    anum = int(input("Enter a number: "))
    print("Your number plus 8 is", addeight(anum))
    
# Call main function - should be last statement in your file
main()

Non-fruitful turtle function example:

# Illustrate calling a turtle function 
# John Cigas, 2/10/2019

import turtle

# Define functions
def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    """This is where you set up the window and its attributes,
       define your variables, and create your turtle(s)."""

    wn = turtle.Screen()         
    wn.bgcolor("lightgreen")

    # Draw a square
    alex = turtle.Turtle()       
    drawSquare(alex, 50)         

    wn.exitonclick()
    
# Call main function - should be last statement in your file
main()

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-04-01T04:31:46Z

Hello class,

### adds all even numbers in a range (inclusive)
def add_even(x):
    some_num = 0
    for counter in range(0,x+1,2):
        some_num = some_num + counter
    return some_num

def main():
    what_num = int(input('pick a number to add all even numbers up to and including'))  #input add_even function
    result = add_even(what_num)
    print(result)

if __name__ == '__main__':  #checks if program is being imported into another program
    main()

---


### Feedback

**[INSTRUCTOR]:** Good work, Bert
Discussion  10 pts
Initial Post   5
Reply Post   5
