# Unit 1: Assignment

**Due:** 2022-03-21T04:59:59Z
**Points:** 24.0

The assignment is in the format of a Canvas quiz. The quiz is untimed but only allows one attempt.

In all problem-solving problems, you must show your work and explain your answers. No credits will be given for a result without any steps or explanations, even if the result is correct.  A calculation that you can figure out the result directly in your head doesn't need any more steps/explanations. For example, one may directly go from "2^4 + 2^3" to "24", but need more than one step to convert an 8-bit 2's complement number to decimal.

You may do your work on paper, scan or take a picture, and then attach the picture to your response to a specific question. Make sure the pictures are legible. However, keep in mind that similar questions may show up on the final exam, during which you can only type up your work on screen.

**My Score:** 17.9/24.0

### Feedback

**[INSTRUCTOR]:** Good job!

Q1. -0.1 pts. Correct work, but missed the 1st division step when converting int part to binary

Q3. -0.5 pts. -120: need to show how you went from 7 bits to the final result 8 bits.  

Q4. -1 pts. negative number: steps don't match up your result. 

Q5. -0.5 pts. 16 bits can represent 2^16 different values. Your smallest value is off by 1.

Q6. -1 pts. There is an overflow. The result is negative but we're adding two positive numbers.

Q7. -1 pts. Incorrect. 
* You missed the add 1 step when negating the subtrahend. The result of the subtraction should be (1)0101 0100 
* It's incorrect to say "There is an overflow in the MSB". There is a carry out of the MSB. Such a carry doesn't indicate an overflow. 
* There is an overflow due to sign of the result. Overflow happened, as the operands of subtraction have different signs (operands of addition have the same sign), and the result has a different sign from the 1st operand, the minuend.

Q8. -2 pts. Incomplete.
* Overflow happens in 2's complement addition when two operands have the same sign but the result is in a different sign.
* Missed: overflow in subtraction
* Missed: Illustrate with a specific example in 5-bit 2’s complement for each type of calculation. 

Q9. You set a high bar for yourself (and I applaud for that!). You have time to practice more in the coming weeks before seeing them on the final. Let me know if I can be of any support. Take advantage of the tutor.
