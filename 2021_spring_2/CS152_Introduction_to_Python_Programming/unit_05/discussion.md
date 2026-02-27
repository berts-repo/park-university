# Unit 5: Discussion

String Functions

This discussion will let you code and use different functions that accept a string as a parameter. In addition to the required posts involving code, you will probably have other interactions requesting clarifications or explanations. You should respond to any of these posts addressed to you or help another student who is having issues.

Directions

Initial Post: Post your initial post by 11:59 p.m., Thursday, CT. 

Reply Post: Reply to one or more classmates as per the specific instructions by 11:59 p.m., Sunday, CT.

Discussion Prompt

Initial Post:

Choose one of these functions to code:

Write a fruitful function with at least one string parameter that returns an integer. This could be something like counting the number of commas in the string or returning half the length of the string. For example:

def half_length(aString):

""" Returns the length of the string parameter aString divided by 2 """

return len(aString) / 2

Write a fruitful function with at least one string parameter that returns another string. This could be something like returning a new string with every other character from the original string or returning the first half of the string. For example:

def half_off(aString):

""" Returns a string which is the first half of the string parameter aString """

       halflen = len(aString) / 2

       return aString[:halflen]

Write a fruitful Boolean function with at least one string parameter. This could be something like returning  True  if the string has a length that is a multiple of 3, or if the first letter is capitalized. For example:

def first_cap(aString):

""" Returns True if the first character of the string parameter aString is a capital letter """

       return isUpper(aString[0])

Be sure to document what your function does and what the parameters are!!!!

Do NOT give an example of how to call the function. Other students have to figure it out from your detailed description of the parameters being passed.

Reply Post:

Respond to another student’s code by writing a program that calls the function at least 2 times with different parameters.

Show the results of running the program. Since it is a fruitful function, print the returned value.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-04-15T22:55:49Z

Hey class,

### checks the number of white spaces in a sentence

# counts the number of white spaces
def count(string):
    white = 0
    for index in string:
        if index.isspace():
            white += 1
    return white

# calls the function to check white spaces        
theString = 'time for lunch'        
print(count(theString))

---


### Feedback

**[INSTRUCTOR]:** Discussion  10 pts
Initial Post   5
Reply Post   5
