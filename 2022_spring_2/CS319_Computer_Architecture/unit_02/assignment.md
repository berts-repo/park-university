# Unit 2: Assignment

**Due:** 2022-03-28T04:59:59Z
**Points:** 30.0

The assignment is in the format of a Canvas quiz. The quiz is untimed but only allows one attempt.

In all problem-solving problems, you must show your work and explain your answers. No credits will be given for a result without any steps or explanations, even if the result is correct.  A calculation that you can figure out the result directly in your head doesn't need any more steps/explanations. For example, one may directly go from "2^4 + 2^3" to "24", but need more than one step to convert an 8-bit 2's complement number to decimal.

You may do your work on paper, scan or take a picture, and then attach the picture to your response to a specific question. Make sure the pictures are legible. Nonetheless, keep in mind that similar questions may show up on the final exam, during which you can only type up your work on screen. 

Rubric

Q1 and Q2, 5 pts each
0.5 pts. sign bit
1 pts. absolute value to binary
1 pts. normalize
1 pts. True exp to biased exp
0.5 pts. drop leading 1. of the fraction part
1 pts. Final result in 32 bits.

Q3 and Q4, 5 pts each
1 pts. Hex to 32-bit binary
0.5 pts. sign bit
1 pts. biased exp to true exp in decimal
0.5 pts. Fraction part with leading 1.
1 pts. Sign, true exp, fraction assembly together in the form of 1.xxx2 x 2y  
1 pts. Final decimal result

Q5, 4 pts
2 pts each.

Q6, 6 pts
1 pts. 4-var k-map, the labels must be correct
1 pts: 1-cells filled correctly
3 pts: correct groups
1 pts: simplified boolean expression result

**My Score:** 29.0/30.0

### Feedback

**Bert:** I realized I didn't get the last question right after I worked through a response in the discussion

**[INSTRUCTOR]:** Good job!

Q1. When working manually, I write the bits for the fraction portion in 4-bit groups even in the intermediate steps. The bits would be easier to read, especially if I need to trace back my work. The practice tool doesn't show the bits in 4-bit groups that as it requires additional coding and I haven't got to that yet. :)

Q5. I wasn't thinking about special values, but values like 0.1 for a and a huge number for b (beyond 10^38). 

Q6. -1 pts. 
* Your group 3 is the same as your group 2. I assume you made a typo.
* As you already realized, your reduced result is wrong.
