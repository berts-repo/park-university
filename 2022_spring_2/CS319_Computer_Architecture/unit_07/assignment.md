# Unit 7: Assignment

**Due:** 2022-05-02T04:59:59Z
**Points:** 38.0

The assignment is in the format of a Canvas quiz. The quiz is untimed but only allows one attempt.

When a problem involves multiple steps, you must show your work steps. No additional explanation is needed if your steps are clear and complete. No credits will be given for a result without any steps (or explanations), even if the result is correct.

To prepare for the final exam, you should only type up your answer within the quiz, not work on paper and then upload a photo. Work in photos won't be accepted. 

For readability, show Assembly code in the "Preformatted" style. If needed, see the "Change Text Style" section of this Canvas Student Help article  [link: https://community.canvaslms.com/t5/Student-Guide/How-do-I-add-and-modify-text-in-the-Rich-Content-Editor-as-a/ta-p/322] https://community.canvaslms.com/t5/Student-Guide/How-do-I-add-and-modify-text-in-the-Rich-Content-Editor-as-a/ta-p/322

Update 4/20/2022: An easier way to "draw a stack":

[ old BP        ] # stack frame for main
[ ?: ?          ] <- BP (Your BP may not point to this spot)
[ ?: ?          ] 
[ ??            ] 
[ ??            ] <- SP

Use this template when illustrating a stack:

   ---------------
  | old BP        | # stack frame for main
   ---------------
  | ?: ?          | <- BP (Your BP may not point to this spot)
   ---------------
  | ?: ?          | 
   ---------------
  | ??            | 
   ---------------
  | ??            | <- SP
   ---------------

**My Score:** 29.5/38.0

### Feedback

**[INSTRUCTOR]:** Good job!

Q1. -2 pts. "Be sure to explain how CPU is involved in each technique". 

Q2. 
2. -0 pts. 
"MOV  %BP, %SP" at the end of the program is to copy the value in BP to SP. This instruction releases space used by local vars created in main(). 
"POP  %BP" pops out the current stack top and copies it to BP. This instruction releases stack frame of main() and restore the old BP.   

3. -1 pts. The first instruction that the stack would be fullest is "SUB  %SP, $4, %SP # allocate mem space for var n". The last instruction that the stack would be fullest is "JMP  @main_exit".

4. -2 pts. You need to identify BP and SP. 
The stack at the last such instruction would be:
  [ old BP (636) ] <- BP  # stack frame for main 
  [ n: 3    ] <- SP
 
The content of R0 and R13 is correct.


Q3. 
2. -0.5 pts. Missing comments on some instructions. Some comments too general. See Q2. 

Responses to your questions: 
DIV  8(%BP), 12(%BP), %0  # a / b -> R0 . Remainder of the division is in R12. 
You asked why the remainder is in R12 instead of R13. R12, like R0, is used by the CPU [of this simulator] to store intermediate results during calculation. R12 is dedicated to remainder of any division calculation. R13 is used exclusively to store a value to be returned to implement "return xx" in C language.

ADD  %SP, $8, %SP  # release space used by two arguments
MOV  %13, -8(%BP)  # R13 -> n, value returned from fun saved in n (C code "n = fun(...)")
MOV  -8(%BP), %13  # n -> R13. To be returned by main (C code "return n")

3. -1 pts. The first instruction that the stack would be fullest is "SUB  %SP, $4, %SP # allocate mem space for var t". The last instruction that the stack would be fullest is "JMP  @fun_exit" (right before the @fun_exit portion code).
  
4. -2 pts. You need to identify BP and SP. 
The stack at the last such instruction would be:
  [ old BP        ] # stack frame for main
  [ m: 11         ] 
  [ n: ?          ] 
  [ arg b: 4      ] 
  [ arg a: 11     ] 
  [ return addr 92] address of ADD instruction right after CALL fun 
  [ BP of main    ] <- BP  # stack frame for this call of function fun
  [ t: 2          ] <- SP 

The content of R0, R12, and R13 is correct.

Q4. Feel free to explore how pointers work. We won't be able to cover that in this course as some students only have had Python.
