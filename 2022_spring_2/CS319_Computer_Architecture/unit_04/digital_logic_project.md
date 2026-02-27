# Unit 4: Digital Logic Project

**Due:** 2022-04-11T04:59:59Z
**Points Possible:** 35.0
**Submission Types:** online_upload

## Instructions

Warning: this project is time-consuming. You need to build a sequential circuit and a combinational circuit separately, and then combine them into a final circuit. 

Purpose

The purpose of this project is to use a digital logic simulator and build a moderate circuit with a sequential sub-circuit and a combinational sub-circuit.

Project Description

We will build a 4-bit counter with two Hex Digit displays to show the corresponding decimal values 0 ~ 15 (and back to 0). The circuit uses a counter sub-circuit (step 1) to generate BCD code automatically. The output of the counter sub-circuit will then be fed to a second sub-circuit (step 2) and connected to two Hex Digit displays.  

Step 1

Build the counting-up counter described in Fig 10-17 (ch10.5) of our Tarnoff textbook in Logisim. This is a sequential circuit. Use one D flip-flop for each of the four latches and set their trigger attribute to “Rising Edge”.

The clock signal is in the Wiring folder [of Logisim]. If you need an example of how to connect a clock signal to D flip-flops, review the screenshot of a Logisim circuit in the 3rd PPT of this unit. That circuit is for Fig 10-16 of our Tarnoff textbook. Be aware that wirings in that circuit, except for the clock signal wiring, are different from what we need here.   

Connect the output Q of each D flip-flop to an output pin named Q3 (latch A, MSB), Q2, Q1, and Q0 (latch D, LSB) Q0 (latch A, LSB), Q1, Q2, and Q3 (latch D, MSB) respectively. You may want to lay the Q3 output pin on the top, next Q2, Q1, and Q0 at the bottom (Q3 Q2 Q1 Q0 together represent a 4-bit binary number).

Poke the clock to run your circuit. The outputs should cycle through 0000~1111 and then restart from 0000.  

Add your name, Park ID, and date to your circuit using the Text tool. Save your circuit as Unit4_YourLastName_Step1.circ. Test your circuit to make sure it works properly before proceeding to the next step. Document your testing in the project document.

Step 2

Now design and build a combinational circuit to convert BCD code (4-bit input) to its decimal value expressed in two sets of BCD codes (8-bit output Y7 ~ Y0). Even though it has 8 outputs, this circuit is simpler than the project we built in the previous unit.

a. The truth table is provided below. The intention is to convert input ABCD (0000 ~ 1111) to outputs Y7~Y0 which represent decimal values 0 ~ 15. The decimal values will be expressed in two sets of BCD codes, Y7~Y4 for the ten’s digit (0000 for values 0~9 and 0001 for values 10~15) and Y3~Y0 for the one’s digit (0000~1001 for values 0~9 and 0000~0101 for values 10~15). 

b. Provide a simplified expression for each of the 8 outputs Y7 ~ Y0. You may use whatever simplification method you like, but show your work with steps (such as k-map). Hint: Y7, Y6, and Y5 will be the same and end up being 0. 

c. Create a new circuit in Logisim to implement these simplified functions. Only use AND, OR, and NOT gates. Label items (every input/output pin and every AND/OR gate) in your circuit. Labels are like comments in a program and can help us track our work, especially if we need to check our work or trace back. Label the AND gates with the terms generated and the OR gates with the function name, like W. 
Hint: use a constant 0 wire for Y7, Y6, and Y5. 

Add your name, Park ID, and date to your circuit using the Text tool. Save your circuit as Unit4_YourLastName_Step2.circ. Test your circuit to make sure it works properly before proceeding to the next step. Document your testing in the project document.

Step 3

Now we’re ready to put the two parts together. The overall connection (see the visual below) will be: Step 1 circuit (counter) -> Step 2 circuit -> two splitters -> two Hex displays. It’s a good idea to save your work following each sub-step. 

a. Save a copy of your counter circuit from Step 1 as Unit4_YourLastName_Step3.circ (i.e. don’t destroy your Step 1 file). We will work in this file to combine our Step 1 and Step 2 circuits. 

b. Load your Step 2 circuit (BCD to 2-digit decimal) into this Step 3 file. First, make sure your Step 2 circuit file is in the same folder on your computer as this Step 3 file. Next use Project menu -> Load Library -> Logisim Library … to add your Step 2 circuit. The loaded circuit will become a new folder under the Explorer Pane, as shown in Figure 1. Click open that folder and add the main component to the current file (the same way you add a built-in component). It will be displayed as a black box with four input pins and 8 output pins. We’ll use the loaded circuit like a Logisim component, the same way we set up a function in programming and then call the function instead of repeating the code. 

Figure 1. The loaded circuit in the Explorer Pane

c. Connect each of the four outputs of your Step 1 counter to the corresponding input pin of the black box (your step 2 circuit). Make sure they’re paired correctly. The Step 1 MSB output should be connected to the MSB input pin of the black box. Do not delete the output pins. Just add additional wire before each output of your Step 1 counter circuit.

d. Add two Hex Digit Displays to the right side of the black box and align them side by side (Figure 2). The Hex Digit Display component is listed under the Input/Output folder. Be sure to use the “Hex Digit Display”, not the 7-seg display we used last week.

  

Figure 2. Two Hex Digit Displays Side by Side Showing an Output of 15.

A Hex display takes a single input line carrying 4 bits, not 4 lines of 1-bit input. Because of that, we need to combine Y7~Y0 into two 4-bit lines before connecting the outputs of the black box to the two Hex displays. We will use two splitters. Splitter is the first component listed under the Wiring folder. Figure 3 shows how a splitter combines four 1-bit lines into a 4-bit line before a Hex Digit Display. If it helps, build a test circuit as in Figure 3 to understand the connection before adding splitters to your Step 3 circuit. Use the following attributes for the splitter:

Facing: North
Fan Out: 4
Bit Width In: 4

Figure 3. Use Splitter to combine four 1-bit lines into a 4-bit line

Now add two splitters to your Step 3 circuit between the black box and the two Hex displays. One splitter will combine Y7~Y4 into a 4-bit line before sending them to the Hex display on the left (for the ten’s digit). The other splitter will combine Y3~Y0 for the Hex display on the right (for the one’s digit).  

Save your circuit and test it. Document your testing in the project document.

Step 4

Project feedback:

a. What’s the hardest part of this project for you? Please explain.

b. How’s your understanding of combinational circuits and sequential circuits after this project? Please explain. Feel free to comment on other aspects of this project. 

Notes

In Logisim, the wires of a properly connected circuit should only be light green (1) or dark green (0).

Use one AND gate for each ANDed term no matter how many variables the term uses. Use one OR gate to OR terms at the same level. You can change the number of input pins an AND/OR gate has.

Submission

Submit four files: three circuit files and one project document (a Word/PDF file that includes all other required items). See the rubric for the required items.

You may do your work on paper and scan or take a picture. Insert the pictures into your project document.

When submitting multiple files, you may turn in separate files as listed (preferred) or combine everything into a single .zip archive. Do NOT use any other archive format, as the instructor won’t be able to open them.

Rubric

Step 1. A circuit file containing a working sequential circuit as specified

6 pts:

1 pts: the clock is connected properly to other components;

4 pts: 1 pts for each D flip-flop that is connected properly;

1 pts: output components properly connected and numbered 

Step 2.b. Simplification and simplified Boolean expression for each output. Must show your steps, otherwise zero credit.
11 pts: 1 pts for Y7~Y5, 2 pts each for Y4~Y0 (2 pts x 5)

Step 2.c. A circuit file containing a working combinational circuit as required.

Your circuit must match your simplification work, otherwise zero credit.
9 pts: 8 pts (1 pts for each of the 8 output variables. The point covers any necessary input/output pin connection, wiring, and gates for that output variable) + 1 pts (all items properly labeled) 

Step 3. A circuit file containing a working circuit as required.

Your circuit must be based on your Step 1 and Step 2 work, otherwise zero credit.

7 pts:

1 pts: 3.b loading step 2 circuit

2 pts: 3.c connecting outputs of step 1 to input pins of step 2

2 pts: 1 splitter (to combine Y7~Y4) and a Hex display for the ten’s digit, including proper attributes and connections.

2 pts: 1 splitter (to combine Y3~Y0) and a Hex display for the one’s digit, including proper attributes and connections.

Steps 1, 2, and 3: testing description for circuits from each step 
1 pts

Step 4. Project feedback
1 pts

Total: 

35 pts

---

## My Submission

**Score:** 32.5/35.0
**Grade:** 32.5
**Submitted:** 2022-04-08T19:09:17Z

### Submitted Files

- **Unit4_Bert_Step1.circ**
  - Downloaded: `files/Unit4_Bert_Step1.circ`
- **Unit4_Bert_Step2.circ**
  - Downloaded: `files/Unit4_Bert_Step2.circ`
- **Unit4_Bert_Step3.circ**
  - Downloaded: `files/Unit4_Bert_Step3.circ`
- **Logism documentation.docx**
  - Downloaded: `files/Logism documentation.docx`
- **Unit4_Bert_Step2_test.circ**
  - Downloaded: `files/Unit4_Bert_Step2_test.circ`

### Instructor Feedback

**[INSTRUCTOR]** (2022-04-13T22:55:44Z):

> Total: 32.5 pts = 35 - 2.5 pts. Good job!

[6 pts. Step 1. Counter. Sequential circuit] 
+ correct. Good job labeling the latches

[11 pts. Step 2.b. Simplification w steps] 
+ correct


[9 pts. Step 2.c. A circuit based on step 2.b work]
+ The circuit works properly
-2 pts. Y7~Y5 doesn't match your step 2.b work.
-0.5 pts. The requirement is "Only use AND, OR, and NOT gates. "
-0 pts. The AND gate and NAND gate connecting D to Y0 are not needed as each gate has only one input. Just directly connect D to Y0. 
-0 pts. Similarly, just directly connect the AND gate for AB'C' to Y3.
  

[7 pts. Step 3. Combine step 1 and step 2 work]
+ correct

[1 pts. Step 1, 2, and 3 Testing description]
+ Good

[1 pts. Step 4. Project feedback]
* Good job completing the project, but you do need to read the project description and specific requirements. :)
