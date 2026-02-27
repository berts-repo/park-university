# Unit 3: Digital Logic Project

**Due:** 2022-04-04T04:59:59Z
**Points Possible:** 35.0
**Submission Types:** online_upload

## Instructions

Warning: this project is time-consuming. The final circuit has 7 outputs. You should start as soon as you're done with the "Build a Combinational Circuit" lecture.

Purpose

The purpose of this project is to use a digital logic simulator and build a moderate combinational circuit.

Project Description

We will build a BCD to decimal 7-segment circuit. The input will be the BCD code of a decimal digit (4-bit input. Name them ABCD, with A being the most significant bit). The output will be a decimal value in a 7-segment display (with 7 outputs for the 7 segments a~g).

Step 0

Download the digital logic simulator called Logisim. See the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1428089] Prepare for next week's circuit simulator announcement in Canvas.

Step 1

Start Logisim and work through the Beginner’s Tutorial, accessible from the Help menu > Tutorial. A video showing steps 1 – 3 of this tutorial is provided in  [link: https://canvas.park.edu/courses/67161/files] Files > Logisim for Windows and Mac. After completing this tutorial, add your name, Park ID, and date to your circuit using the Text tool (the A tool on the toolbar). Now take a screenshot of your circuit and include the screenshot in your project document.

If those resources are not enough, watch the first 4:20 of this YouTube video:  [link: https://www.youtube.com/watch?v=dYZ-Hwbcnq4] https://www.youtube.com/watch?v=dYZ-Hwbcnq4 

Step 2

Start from the design step.
a. Read ch8.2 Seven-Segment Displays of our Tarnoff textbook. 
b. Instead of a circuit to display hexadecimal digits (0~9 and A~F), we will build a circuit to display decimal digits 0~9 only. 
c. Truth table: we will only use the first 10 rows of Fig 8-14 from ch8.2. The last 6 rows (for hex A-F) become invalid/don’t cares. Include a copy of the revised truth table in your project document. Include 16 rows but mark the don’t care conditions. 
d. Provide a simplified expression for each of the 7 outputs a ~ g (must use the don’t care cells). You may use whatever simplification method you like, but show your work with steps (such as k-map).

Step 3

Create a circuit (a new file) in Logisim to implement these simplified functions. Add your name, Park ID, and date to your circuit using the text tool. Save your circuit as Unit3_YourLastName.circ. It should have four inputs and 7 outputs. Test your circuit to make sure it works properly before proceeding to the next step. Document your testing in the project document.

Step 4

Now attach a 7-segment display to your a~g outputs. Figure 1 shows where 7-segment display is listed in Logisim. Figure 3 shows the mappings between a~g segments (and the dot) and the 8 pins of the 7-segment display component. The right most pin in the bottom (the dot) is connected to a constant 0 as we don’t need this dot. Use a Constant component (Figure 2) and change its value attribute to 0. 

    
        

            
Figure 1
            
Figure 2
            
Figure 3
        

    

Do not delete the a~g output pins when attaching the 7-segment display. Add additional wire before each output component as shown below. Save your circuit as Unit3_YourLastName_7seg.circ. Test your circuit and document your testing in the project document.

Step 5

Project feedback:

a. What’s the hardest part of this project for you? Please explain.

b. How’s your understanding of simplification and combinational circuits after this project? Please explain. Feel free to comment on other aspects of this project.

Notes

In Logisim, the wires of a properly connected circuit should only be light green (1) or dark green (0). 
  
Use one AND gate for each ANDed term no matter how many variables the term uses. Use one OR gate to OR terms at the same level. You can change the number of input pins an AND/OR gate has. 

Be sure to label items in your circuit. Labels are like comments for a program. I label the AND gates with the terms generated and the OR gates with the function name, like W. 

You may want to build and test the circuit of each segment of a~g (Project menu > Analyze Circuit) before adding more gates and wires. You may even save a copy of your work after each segment is tested (Unit3_a.circ, Unit3_b.circ, …) in case you need to go back to an earlier working version.

Submission

Submit three files: two circuit files and one project document (a Word/PDF file that includes all other required items). See the rubric for the required items.

    
You may do your work on paper and scan or take a picture. Insert the pictures into your project document.

    
When submitting multiple files, you may turn in separate files as listed (preferred) or combine everything into a single .zip archive. Do NOT use any other archive format, as the instructor won’t be able to open them.

Rubric

    
        

            Step 1. A screenshot of your test circuit with name, Park id, and date
            1 pts
        

        

            Step 2.c Truth table for BCD to decimal digits 
            1 pts
        

        

            Step 2.d. Simplification and simplified Boolean expression for each segment. Must show your steps, otherwise zero credit.
            14 pts (2 pts for each segment)
        

        

            
                
Step 3. Circuit file (no 7-seg display. With name, Park id, and date) and testing description.

                Your circuit must match your simplification work, otherwise zero credit.
            
            15 pts: 14 pts (Circuit. 2 pts for each segment portion) + 1 pts (testing) 
        

        

            Step 4. Circuit file (with 7-seg display) and testing description
            2 pts: 1 pts (Circuit) + 1 pts (testing)
        

        

            Step 5. Project feedback
            2 pts
        

        

            Total: 

            35 pts

---

## My Submission

**Score:** 30.0/35.0
**Grade:** 30
**Submitted:** 2022-04-04T03:49:11Z

### Submitted Files

- **Unit3_bbert_7seg.circ**
  - Downloaded: `files/Unit3_bbert_7seg.circ`
- **Unit3_Bert.circ**
  - Downloaded: `files/Unit3_Bert.circ`
- **k-maps and SOP 1.jpg**
  - Downloaded: `files/k-maps and SOP 1.jpg`
- **k-maps and SOP 2.jpg**
  - Downloaded: `files/k-maps and SOP 2.jpg`
- **Seven Segment Display Truth Table.xlsx**
  - Downloaded: `files/Seven Segment Display Truth Table.xlsx`
- **written documentation.docx**
  - Downloaded: `files/written documentation.docx`

### Instructor Feedback

**Bert** (2022-04-04T03:49:11Z):

> I am really concerned that I didn't add a mux when I should of. I ran out of time or I would of played with adding the mux in my 7seg.circ

**[INSTRUCTOR]** (2022-04-07T22:58:33Z):

> Total: 30 pts = 35 - 5. Good job! 

[1 pts. Step 2.c. truth table]
+ correct

[14 pts. Step 2.d simplification. 2 pts each seg.]
+ All 1s and x's are filled in correctly in each k-map.
+ Grouping covered all 1s, but a few can be bigger.

-0.5 pts. a seg should be simplified to two 8-cell groups and two 4-cell groups. The two 8-cell groups are the last two columns and the last two rows (missed). The two 4-cell groups are the four cells in the center and the four corner cells (missed). 

-0.5 pts. b. You got an extra group (the 1st term/the one simplified to term A/written in pencil). All 1s in that group have already been covered by other groups (i.e. this group doesn't have its unique 1s). 
-0.5 pts. b. [mistake] Correct grouping but wrong simplification. The simplified term for the 2nd group/term (in your expression) should be B'. That messed up your b segment in the circuit 
-0 pts. b. You wrote down CD' for the last group/term. Should be CD. Your circuit does show CD.

-0.5 pts. c. should be simplified to three 8-cell groups. The groups are: the first 2 cols, the middle 2 cols (missed), and the middle 2 rows (missed).
-0.5 pts. c. [mistake] correct grouping but wrong simplification: the 1st group/term should be C'. This messed up your c segment in the circuit. 

-0.5 pts. d should be simplified to one 8-cell group, three 4-cell groups, and one 2-cell group. The four corner cells can form a 4-cell group (missed). The last two cells in the top row and in the bottom row can form another 4-cell group (missed).

-0.5 pts. e should be simplified to two 4-cell groups. The four corner cells form a 2nd group (missed). Your 2nd group/term is not needed, as all 1s in that group have been covered by other groups. 
 
-0.5 pts. f should be simplified to one 8-cell groups and three 4-cell groups. Your third term can be expanded to a 4-cell group covering the 1st col. Your last term can be a 4-cell group (the middle two cells in the first and last columns).

-0.5 pts. g. Your last group (the two 1's in the top row) can be grouped with the two x's from the bottom row i.e. the last two cells in the top row and in the bottom row. 


[15 pts. Step 3. Circuit w/o 7-seg]
+ Your circuit is well aligned and super easy to read!
+ Matched your simplification result (even though the simplification can be improved)
 
-0 pts. b seg: incorrect outputs for input values 5 and 6 due to a mistake from simplification (incorrectly simplified a term)
-0 pts. c seg: incorrect outputs for input values 2, 8, and 9 due to a mistake from simplification (incorrectly simplified a term).

-0 pts. Testing: you should gone through each input combinations 0000~1001 to see if a~g generates the right outputs.

-0 pts. extra AND gates used. This circuit only needs 9 AND gates. Aside from simplification issues, a term using a single variable (like your A, A', C) doesn't need an AND gate and can be directly connected to the OR gate. 


[2 pts. Step 4. Circuit w 7-seg]
-0.5 pts. The wiring for f and g, when connected to the 7-seg display is reversed. That affected 0, 2, 3. The testing here should run through each input combinations 0000~1001 and see if the 7-seg display actually displays the number. This is supposed to be a clear indicator that you need to check your connection or even go back to the simplification step.


[2 pts. Step 5. Project feedback]
* Keep practicing. You got all the 1s in k-maps and just need to double-check "can this group be bigger"?
* No, we don't need a mux here. It's not mentioned anywhere in the project description.
