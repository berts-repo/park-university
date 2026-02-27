# Final Exam - Additional Information

If you haven't, read  [link: https://canvas.park.edu/courses/67161/pages/final-exam-general-information] Final Exam - General Information first.

What will be on the exam?

10~15 questions. Questions will be similar to the ones in discussions and assignment quizzes from Unit 1 ~ Unit 7. The Unit Learning Outcomes (ULOs) generally define what's expected from a unit:

Unit 1

Describe the main functions and structural components of a computer. (CLO 1)

Convert unsigned integers and fractions between decimal, binary, and hexadecimal number systems. (CLO 1)

Convert signed decimal integers to/from two's complement representation. (CLO 1)

Perform two's complement arithmetic (negation, addition, and subtraction) (CLO 1)

Unit 2

Convert decimal to/from IEEE 754 floating-point 32-bit. (CLO 1)

Name some special values under IEEE 754 and explain why IEEE 754 needs to define special values. (CLO 1)

Convert between: Boolean expression <-> truth table. (CLO 2)

Simplify a Boolean expression. (CLO 2)

Unit 3

Convert between: Boolean expression <-> truth table <-> combinational circuit.  (CLO 2)

Build a decoder/mux/demux (truth table, circuit) with a specified number of inputs or outputs. (CLO 2)

Build a 1-bit half adder and/or a 1-bit full adder. (CLO 2)

Explain how a multi-bit adder is built and the purpose of carry look ahead. (CLO 2)

Unit 4

List two reasons why a digital circuit may be built solely with NAND gates. (CLO 2)

Explain how a sequential circuit differs from a combinational circuit. (CLO 2)

Given the circuit of an S-R latch/D latch/S-R flip-flop/D flip-flop, produce the truth table and explain how it works on a series of inputs. (CLO 2)

Given a circuit built with D flip-flops, draw its timing diagram on a clock input and analyze its behavior. (CLO 2)

Unit 5

Compare different types of devices in the computer memory hierarchy and describe an example use of ROM, SRAM, and DRAM. (CLO 3)

Describe how a memory hierarchy with cache, main memory, and disk works. (CLO 3)

Solve addressing problems in a direct mapping/fully-associative/set-associative cache. (CLO 3)

Unit 6

Describe the three key concepts of von Neumann architecture. (CLO 4)

Describe how CPU processes instructions. (CLO 4)

Trace the execution of Assembly/machine language programs. (CLO 4)

Write LMC assembly language programs involving input/output/if-else/loops. (CLO 4)

Unit 7

Show the address space of a program and trace the execution of its assembly code. (CLO 4)

Explain at least three ways the CPU design impacts the higher software layers. (CLO 4)

Contrast different input/output techniques. (CLO 3)

 

Additional Requirements and Tips

When a problem involves multiple steps, you must show your work steps. No additional explanation is needed if your steps are clear and complete. No credits will be given for a result without any steps (or explanations), even if the result is correct. For example,

Q. Given a memory space of 8 Mega, how many address lines are needed?

An answer of "23 address lines" will receive no credits due to a lack of work steps.

An answer of "8 Mega = 8 x 2^20 = 2^23, so 23 address lines" will be enough for full credit as it shows clearly how the given information 8 Mega is transformed to 2^23 which leads to the final result 23.

Practice typing up your work within a quiz. You can also practice via a discussion post since they use the same editor. In general, work out a strategy of how to do something in the Canvas editor before the exam and stick to it so you don't waste time trying to figure that out during the exam.

This template will be provided on the exam for timing diagram-related questions.

   initial|cycle|cycle|cycle|cycle|cycle|cycle|
   state  |#1   |#2   |#3   |#4   |#5   |#6   |    
           __    __    __    __    __    __
Clock    _|  |__|  |__|  |__|  |__|  |__|  |__

 

Those templates will be provided for k-map related questions.

  \ C | 0 1
AB ?? | - -
   ?? | - -
   ?? | - - 
   ?? | - -
  \CD | ?? ?? ?? ??
AB ?? |  -  -  -  -
   ?? |  -  -  -  -
   ?? |  -  -  -  -
   ?? |  -  -  -  -

It may be easier to mark groups using multiple copies of a k-map. For example, given this k-map:

  \CD | 00 01 11 10
AB 00 |  -  1  -  -
   01 |  1  x  -  -
   11 |  1  x  -  -
   10 |  -  -  -  -

We can have two groups:

Group 1:

  \CD | 00 01 11 10
AB 00 |  -  1  -  -
   01 |  1  x  -  -
   11 |  1  x  -  -
   10 |  -  -  -  -

Group 2:

  \CD | 00 01 11 10
AB 00 |  -  1  -  -
   01 |  1  x  -  -
   11 |  1  x  -  -
   10 |  -  -  -  -

 

This table will be provided for LMC-related questions. If you need to write LMC code, format your code in the "Preformatted" style for readability.

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

 

(Updated 4/30/2022) This template will be provided for x86 simulator-related questions.

[ old BP        ] # stack frame for main
[ ?: ?          ] <- BP (Your BP may not point to this spot)
[ ?: ?          ] 
[ ??            ] 
[ ??            ] <- SP
