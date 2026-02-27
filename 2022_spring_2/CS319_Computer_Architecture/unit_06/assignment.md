# Unit 6. Assignment

**Due:** 2022-04-25T04:59:59Z
**Points:** 43.0

The assignment is in the format of a Canvas quiz. The quiz is untimed but only allows one attempt.

In all problem-solving problems, you must show your work or explain your answers. No credits will be given for a result without any steps or explanations, even if the result is correct. 

To prepare for the final exam, you should only type up your answer within the quiz, not work on paper and then upload a photo. Work in photos won't be accepted. 

For readability, it's a good idea to use the "Preformatted" format on your LMC code, like the table shown below. If needed, see the "Change Text Style" section of this Canvas Student Help article  [link: https://community.canvaslms.com/t5/Student-Guide/How-do-I-add-and-modify-text-in-the-Rich-Content-Editor-as-a/ta-p/322] https://community.canvaslms.com/t5/Student-Guide/How-do-I-add-and-modify-text-in-the-Rich-Content-Editor-as-a/ta-p/322

Reference

Mnemonic  | Numeric| Purpose (AC for Accumulator)
----------------------------------------------------------------- 
INP       | 901    | AC <- input                
ADD addr  | 1xx    | AC <- AC + mem[addr]
SUB addr  | 2xx    | AC <- AC - mem[addr] 
STA addr  | 3xx    | AC -> mem[addr]
LDA addr  | 5xx    | AC <- mem[addr] 
BRA addr  | 6xx    | Branch to an instruc
BRZ addr  | 7xx    | Branch if AC == 0
BRP addr  | 8xx    | Branch if AC >= 0
OUT       | 902    | AC -> output
OTC       | 922    | Output AC as a char (treat AC as ASCII code)
HLT       | 000    | Halt program execution
DAT value | -      | Initialize the mem loc to a specific value

**My Score:** 34.5/43.0

### Feedback

**[INSTRUCTOR]:** Good job!

Q2. 
a. -0.5 pts. The machine code for LDA 10 is 510. 
b. -3 pts. Not meeting the requirement "Your description must include all relevant LMC components and registers (such as PC, Arithmetic Unit, instruction register, address register, and RAM) and their content at specific moments."
See one example discussion question and my reply from unit 6. 

Q3. -2 pts. Missed the print step and that the loop would print out from input n down to 4 (while n-3>0 i.e. while n>3) 

Q5. Some logic errors. 
* Should STA x before SUB ten, not after. That's why your program would print out wrong values. You want to store x, not x-10. 
* The testing (BRP) should be set before any print. 
-1 pts: should not produce any print for input > 10.
-1 pts: should not produce any print for input 10.
-1 pts. correct # of prints for input<10, but the values are wrong. Should be x, x+2, ... until a 8 or 9 (the last value needs to be <10).

Q6. Sorry that your schedule was tight. Otherwise, you could have performed better in this assignment quiz.
