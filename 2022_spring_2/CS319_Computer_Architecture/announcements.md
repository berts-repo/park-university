# Announcements - CS319DLS2A2022 Computer Architecture

## Week 8 work returned
*Posted: 2022-05-09T22:26:06Z*

Hi Class,

Your week 8 work has been graded and your course total grade is ready for your review. Please let me know of any questions by noon 12 pm CT tomorrow Tue, May 10th. After that, your grade will be submitted to the University and any dispute will need to follow the grade appeal procedure.  [link: https://catalog.park.edu/content.php?catoid=16&navoid=4840#academic-grievance] https://catalog.park.edu/content.php?catoid=16&navoid=4840#academic-grievance

Thank you very much for a fruitful term! It'd be great to hear from you once in a while even if I don't get to see you in other courses. Wish you the best in your future endeavors!

Thank you,
Crystal

---

## Student Opinion of Teaching Survey
*Posted: 2022-05-03T20:09:08Z*

Hi Class,

Could you complete the teaching survey by the end of Sunday, May 8th? You may access it through the link in Unit 7 or 8, or  [link: https://park.campuslabs.com/eval-home/] https://park.campuslabs.com/eval-home/  You will be prompted to login with your ParkIDnumber@park.edu and password.

All responses are anonymous. The compiled results will be shared with instructor after final grades have been submitted.

Your evaluation will be part of the formal record of this session with the University.

Your feedback will help me assess my teaching and improve this course.

Thank you for your support!

Thank you,
Crystal

---

## Week 7 work returned
*Posted: 2022-05-03T15:12:00Z*

Hi Class,

Unit 7 work has been graded and returned. I replied to some posts in Unit 7 discussion yesterday as I graded them. Review those, especially if it's a reply to your post.

Please read the grading comments on your assignment and let me know if you have any questions within 1 week of today via Inbox or the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page. Please review relevant lectures and examples as I suggested if you missed something.

Go through the x86 examples more if needed. The slides show how the stack of a program changes with the program execution. Walk through the stack change portion of the slides and run the program in the simulator. See how the slides illustrate the stack following what happens in the simulator.

You were asked to "Identify when the stack would be the fullest (with the most number of items from the bottom of the stack to where SP points) during the execution of the assembly program. "  The top of the stack is defined by SP. As an example, let's go through P4 from the Unit 7 discussion. The main() calls a 2-parameter function fun(). Function fun() has an if-else inside. I'll comment on the assembly instructions that affect the BP or SP.

int fun(int a, int b) {
  if (a > b)
    return a - b;
  else
    return a * b;
}

int main() {
  int x = 2, y = 4; 
  x = fun(x, y);
  return x;
}fun:
   PUSH    %BP    # save BP of main on the stack   
   MOV  %SP, %BP  # SP -> BP i.e. point BP to the current stack top. Stack frame of fun is established.
@fun_body:
@if0:
   CMP  8(%BP), 12(%BP)
   JLE  @false0
@true0:
   SUB  8(%BP), 12(%BP), %0
   MOV  %0, %13
   JMP  @fun_exit
   JMP  @exit0
@false0:
   MUL  8(%BP), 12(%BP), %0
   MOV  %0, %13
   JMP  @fun_exit
@exit0:
@fun_exit:
   MOV  %BP, %SP  # BP -> SP i.e. release space used by local vars of fun(). fun() uses no local vars, so no effect here.
   POP  %BP       # Pop out current stack top and copy it to BP i.e. release stack frame of fun() and restore BP of main
   RET            # Pop out the return addr and put it in PC i.e. return to caller of fun() (return to main)   
main:
   PUSH    %BP    # save old BP on the stack
   MOV  %SP, %BP  # SP -> BP i.e. point BP to the current stack top. Stack frame of main is ready
@main_body:
   SUB  %SP, $4, %SP # allocate space on the stack for var x
   MOV  $2, -4(%BP)
   SUB  %SP, $4, %SP
   MOV  $4, -8(%BP)
   PUSH    -8(%BP)   # Push y (value 4) as argument b for function to be called
   PUSH    -4(%BP)   # Push x (value 2) as argument a for function to be called
   CALL    fun       # jump to function fun; save return addr (addr of ADD instruction) on stack
   ADD  %SP, $8, %SP # (just returned from function call) release space used by two arguments
   MOV  %13, -4(%BP)
   MOV  -4(%BP), %13
   JMP  @main_exit
@main_exit:
   MOV  %BP, %SP    # BP -> SP i.e. release space used by local vars of main()
   POP  %BP         # Pop out current stack top and copy it to BP i.e. release stack frame of main and restore the old BP
   RET              # Return to the caller of main (OS) and send out the returned value

One stack frame will be created for each function call. main() is the entry point of a C program and invoked [by the operating system/OS] at the beginning. In general, the stack would be the fullest (stack pointer SP won’t go further down after this point) in the stack frame for the last function call of the program.

If such a function uses local variables, the stack would be the fullest right after the last var declaration in this stack frame. The last instruction the stack is fullest would be JMP @function_exit as the next instruction MOV %BP, %SP would "release" the stack space used by local variables of this function call.

If such a function doesn’t use any local variables, the stack would be the fullest right after PUSH %BP, the first instruction of this function when the old BP of the previous stack frame is saved. Consequently, the last instruction the stack is fullest would be MOVE %BP, %SP under @function_exit label. After that, POP %BP under @function_exit will pop out the old BP of the previous stack frame and SP will move up by one spot.   

Because function fun() doesn’t have any local variables, the stack would be the fullest right after instruction PUSH %BP (first instruction of fun function) is executed (i.e. this is the first instruction that the stack would be fullest):
  [ old BP         ]  <- BP  # stack frame of main() starts here
  [ x: 2           ] 
  [ y: 4           ]
  [ arg2: 4 (b)    ]
  [ arg1: 2 (a)    ]
  [ return address ]  return address is the ADD after CALL fun in main       
  [ BP of main     ]  <- SP. # stack frame of this call of fun() starts here 
The next instruction MOV $SP, $BP will move $BP to point to the spot $SP points before the body of fun() starts.
  [ old BP         ]   # stack frame of main() starts here
  [ x: 2           ] 
  [ y: 4           ]
  [ arg2: 4 (b)    ]
  [ arg1: 2 (a)    ]
  [ return address ]  return address is the ADD after CALL fun in main       
  [ BP of main     ]  <- BP, SP. # stack frame of this call of fun() starts here 
 Because function fun() doesn’t use any local variables, the last instruction the stack is fullest is MOV %BP, %SP under @fun_exit. 
  [ old BP         ]   # stack frame of main() starts here
  [ x: 2           ] 
  [ y: 4           ]
  [ arg2: 4 (b)    ]
  [ arg1: 2 (a)    ]
  [ return address ]  return address is the ADD after CALL fun in main       
  [ BP of main     ]  <- BP, SP. # stack frame of this call of fun() starts here 
Registers used by this point: 

R0 (stores 8, result of a*b in fun() ) and 

R13 (stores 8, as a*b result will be returned by fun()).

After that, POP %BP will "remove" the old BP of main from the stack (hence SP will move to the spot right above). While this old BP of main is not erased from the stack, it’s no longer part of this stack as SP always defines the top of the stack. This instruction releases the stack space used by old BP of main. Here is what the stack would look like after this POP %BP:    

  [ old BP         ]  <- BP # stack frame of main() starts here
  [ x: 2           ] 
  [ y: 4           ]
  [ arg2: 4 (b)    ]
  [ arg1: 2 (a)    ]
  [ return address ]  <- SP # return address is the ADD after CALL fun in main       
  [ BP of main     ]  # stack frame of this call of fun() starts here # content not erased, but not considered part of the stack anymore

Thank you,
Crystal

---

## Week 8
*Posted: 2022-05-02T13:07:46Z*

Hi Class,

Congratulations on reaching week 8, the last week of this term!  Week 8 is for you to review unit 1-unit 7 and prepare for the final exam.  The types of questions will be similar to the ones you've seen in discussions and assignments from unit1-unit7.  Use this week's discussion to ask questions and support each other prepare for the test.  

This week's assignments include:

Unit 8 Discussion: one initial post due Wednesday. Respond to at least one classmate by Sunday.

Fina Exam: due Sunday

Be aware that due dates in this course are at 11:59 pm CT on the specified dates.

Let me know if you have any questions.

Thank you,
Crystal

---

## "Draw" a stack by typing
*Posted: 2022-04-30T13:53:22Z*

Hi Class,

I figured out an easier way to "draw a stack". You may use this one for your unit 7 assignment, discussion, and the final exam. I've updated the final exam - additional information document.
[ old BP        ] # stack frame for main
[ ?: ?          ] <- BP (Your BP may not point to this spot)
[ ?: ?          ] 
[ ??            ] 
[ ??            ] <- SP
Thank you,
Crystal

---

## Week 6 work returned
*Posted: 2022-04-26T18:44:36Z*

Hi Class,

Unit 6 work has been graded and returned. I replied to some posts in Unit 6 discussion yesterday as I graded them. Review those, especially if it's a reply to your post.

Please read the grading comments on your assignment and let me know if you have any questions within 1 week of today via Inbox or the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page. Please review relevant lectures and examples as I suggested if you missed something.

Thank you,
Crystal

---

## Week 7
*Posted: 2022-04-25T13:13:03Z*

Hi Class,

We are at the last week of new material!!!

After learning von Neumann architecture, we will study an actual architecture, the x86 architecture this week. We will use an x86 simulator to help us understand the x86 architecture and how the architecture determines higher software layers. To wrap up our discussion of computer architecture, we will also examine how computers perform input/output.

You should start prepare for the final exam. Read the  [link: https://canvas.park.edu/courses/67161/pages/final-exam-additional-information] Final Exam - Additional Information page in Unit 7 module. Try the proctoring system through the practice quiz before next week and let me know if you run into any problems.

This week's assignments include:

Unit 7 Discussion: one initial post due Wednesday. Respond to at least two classmates by Sunday.

Unit 7 Assignment/Quiz: due Sunday. To prepare for the final exam, you should only type up your answer within the quiz, not work on paper and then upload a photo. Work in photos won't be accepted. 

Be aware that due dates in this course are at 11:59 pm CT on the specified dates.

Let me know if you have any questions.

Thank you,
Crystal

---

## Week 5 work returned
*Posted: 2022-04-21T02:29:46Z*

Hi Class,

Unit 5 work has been graded and returned. I replied to some posts in Unit 5 discussion on Monday as I graded them. Review those, especially if it's a reply to your post.

Please read the grading comments on your assignment and project and let me know if you have any questions within 1 week of today via Inbox or the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page. Please review relevant lectures and examples as I suggested if you missed something.

Thank you,
Crystal

---

## Week 6
*Posted: 2022-04-18T12:38:00Z*

Hi Class,

Now that we’ve learned about data representation, circuits, and memory hierarchy, we’re ready to look at computer architecture. This week we will study von Neumann architecture, an architecture model that all contemporary processors adhere to. We will use Little Man Computer (LMC), a software simulator to understand how processors operate. Feel free to use and share additional resources. We will learn assembly programming using the LMC. Get to the lectures and example exercises, practice through the discussion questions and then start on the assignment/quiz. 

This week's assignments include:

Unit 6 Discussion: one initial post due Wednesday. Respond to at least two classmates by Sunday.

Unit 6 Assignment/Quiz: due Sunday. To prepare for the final exam, you should only type up your answer within the quiz, not work on paper and then upload a photo. Work in photos won't be accepted. 

Be aware that due dates in this course are at 11:59 pm CT on the specified dates.

Let me know if you have any questions.

Thank you,
Crystal

---

## Week 4 work returned
*Posted: 2022-04-13T23:03:44Z*

Hi Class,

Unit 4 work has been graded and returned, discussions returned on Monday, assignments on Tuesday, and projects today. I replied to some posts in Unit 4 discussion on Monday as I graded them. Review those, especially if it's a reply to your post.

Please read the grading comments on your Unit 4 assignment and project. I left grading comments for every assignment/project in every unit on why pts were cut or how something may be improved. Let me know if you have any questions within 1 week of today via Inbox or the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page. 

I don't have any specific notes for this week's work other than that I'm very happy that we got more comfortable with circuits.  

Thank you,
Crystal

---

## Week 5
*Posted: 2022-04-11T05:00:00Z*

Hi Class,

This week we will study the memory hierarchy. We will learn how a memory device may be built using latches and how cache memory works. Feel free to use and share additional resources.

Sorry that I will add recordings for the 2nd and 3rd PPTs at the beginning of this week.

This week's assignments include:

Unit 5 Discussion: one initial post due Wednesday. Respond to at least two classmates by Sunday.

Unit 5 Digital Logic Project: due Sunday. Build a memory-reading circuit. You may start once you're done with the first PPT. This will be our last Logisim project.

Unit 5 Assignment/Quiz: due Sunday.

Be aware that due dates in this course are at 11:59 pm CT on the specified dates.

Let me know if you have any questions.

Thank you,
Crystal

---

## Week 3 work returned
*Posted: 2022-04-07T23:42:55Z*

Hi Class,

Unit 3 work has been graded and returned, discussions returned on Monday, assignments on Tuesday, and projects today. I replied to some posts in Unit 3 discussion on Monday as I graded them. Review those, especially if it's a reply to your post.

Please read the grading comments on your Unit 3 assignment and project. I left grading comments for every assignment/project in every unit on why pts were cut or how something may be improved. Let me know if you have any questions within 1 week of today via Inbox or the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page. 

Here are some notes on unit 3 work:

1. Is a group the biggest? As I said in the lecture, there is no good way to verify that. You have to double-check/triple-check your work. Groups can only include 1, 2, 4, 8, or 16 cells. Can you add more 1s or x's to a group? Can you extend your group to the other edge? We saw an extreme group in unit 3 project - the four corner cells can be grouped together.

2. Simplify a group:

A group of 2-cell will lead to a simplified term of three vars (i.e. one var will be removed). That's just an observation of the simplification process: each cell represents an input of V1V2V3V4. If you combine two cells, one var will be dropped.  
  \CD | 00 01 11 10
AB 00 |  0  1  x  0
   01 |  1  1  0  x
   11 |  1  x  1  1 
   10 |  x  0  0  0

1 is from input 0001 i.e. A'B'C'D
x is from input 0011 i.e. A'B'C DA'B'C'D + A'B'C D = A'B'D(C' + C) = A'B'D•1 = A'B'D
Similarly, a group of 4-cells will lead to a simplified term of two vars (i.e. two vars will be removed). 

A group of 8-cells will lead to a simplified term of one var (i.e. three vars will be removed).

A group of 16-cells (yes, they do exist) will lead to a simplified result of 1 (i.e. all vars will be removed).

Some extended observations:

If a group covers two adjacent rows, one var from the row labels will be dropped.

If a group covers two adjacent cols, one var from the col labels will be dropped. See the yellow group above.

If a group covers all four rows, both vars from the row labels will be dropped.

If a group covers all four cols, both vars from the col labels will be dropped. 

The green group in the k-map above covers two rows, so one var from the row label will be dropped:
rows 01 / A'B
 and 11 / A B 
A is dropped.

The green group also covers two cols, so one col var will be dropped:
cols 00 / C'D' 
     01 / C'D 
D will be dropped. The simplified term for this green group is B C'.

3. Circuit building. Please label each of your input/output pins and AND/OR gates. The circuit step of a project asks for documentation of testing. That's to remind you to check your work, like going through each input combination and see if the output pins show results as specified in the truth table. If not, either your wiring is wrong, or, your simplification is wrong. When a circuit involves many input and output variables, it helps to build and test the circuit incrementally, like one output portion at a time.

Thank you,
Crystal

---

## Week 4 Project
*Posted: 2022-04-06T20:28:27Z*

Hi Class,

Here is a tip for the project - you may start from step 2 and then work on step 1. Step 1 and 2 require you to build two independent circuits which will then be combined in step 3. Step 1 requires that you've gone through this week's lecture (all of them and with a focus on the third PPT), but step 2 is just k-map and combinational circuit.

Thank you,
Crystal

---

## Week 4
*Posted: 2022-04-04T05:00:03Z*

Hi Class,

Pad yourself on the back as some of us have noted that we're halfway through the 8-week term!

This week we will learn another type of digital circuit called sequential circuits. We will first understand how a circuit may be built solely with NAND gates and then will work with sequential circuits built with NAND gates. Feel free to use and share additional resources.

Sorry that I run out of time to record all the lectures. Will complete the remaining ones early this week.

This week's assignments include:

Unit 4 Discussion: one initial post due Wednesday. Respond to at least two classmates by Sunday.

Unit 4 Digital Logic Project: due Sunday. Build a digital circuit with a sequential sub-circuit and a combinational sub-circuit. Start as soon as you can. You have been warned!

Unit 4 Assignment/Quiz: due Sunday.

Be aware that due dates in this course are at 11:59 pm CT on the specified dates.

Let me know if you have any questions.

Thank you,
Crystal

---

## Thank you for your feedback on the practice tools!
*Posted: 2022-03-29T01:05:03Z*

Hi Class,

Thank you very much for your feedback! Here is my response to some of the questions/suggestions:

Zoom class time: it's hard to schedule a class time for an online class as everyone has a different schedule and we started with an expectation of asynchronous activities. I encourage you to take advantage of my Zoom office hours (Tuesdays and Thursdays 2 - 3 pm CT) or request additional 1x1 sessions if those slots don't work for you. Some of you have met me through Zoom.

"don't make the answers so big" in IEEE 754 32-bit to Decimal tool. You don't need to convert a big number to a final decimal result. All you need to do is to show the steps and a final decimal expression such as 2-80 + 2-78.

Allow users to type a number and see the result (i.e. calculator style). There are calculator-style tools out there. Some of you have shared your findings in the discussion. I built those tools to provide additional step-by-step examples and for your practice. If I add the calculator feature, the tools won't help much if I don't include the steps. With the steps, that would be a backdoor for assignments. I'm sure you understand. :)

Break down the steps even more, like color code some bits: an excellent idea! I will work on those in my next update.     

Thank you,
Crystal

---

## Week 2 work graded
*Posted: 2022-03-29T00:19:25Z*

Hi Class,

Unit 2 work has been graded and returned. I replied to some posts in Unit 2 discussion today as I graded them. Review those, especially if it's a reply to your post.

Please read the grading comments on your Unit 2 assignment. Let me know if you have any questions within 1 week of today via Inbox or the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page. 

Here are some notes on unit 2 work:

1. Please review examples from relevant lectures and unit discussions (and tips shared by others) if you missed some questions. Similar questions may show up on the final. If something is hard, take the time to go through the examples and practice before the final exam week.

2. Practice k-map more this week as we see how it's used in designing a simplified circuit.

3. Take advantage of my Zoom office hours (and you can request additional time) and Park's tutor.

Thank you,
Crystal

---

## Week 3
*Posted: 2022-03-28T05:00:06Z*

Hi Class,

After reviewing boolean algebra last week, we will learn how to build a combinational circuit and examine a few example combinational circuits: decoders, mux and demux, and adders. Feel free to use and share additional resources.

This week's assignments include:

Unit 3 Discussion: one initial post due Wednesday. Respond to at least two classmates by Sunday.

Unit 3 Digital Logic Project: due Sunday. Build a combinational circuit with 4 inputs and 7 outputs. It's not hard once you understand the lecture on building a combinational circuit, but time-consuming as you need to create 7 k-maps and build the whole circuit in the simulator. Start as soon as you can. You have been warned!

Unit 3 Assignment/Quiz: due Sunday. The last portion of the last question is extra credit i.e. optional.

Be aware that due dates in this course are at 11:59 pm CT on the specified dates.

Let me know if you have any questions.

Thank you,
Crystal

---

## Prepare for next week's circuit simulator
*Posted: 2022-03-24T21:41:40Z*

Hi Class,

Please complete the following to prepare for our study of combinational circuits next week:

1. Find out the JRE (Java Runtime Environment) you have on your computer. Complete this  [link: https://canvas.park.edu/courses/67161/quizzes/585759] JRE survey if you haven't.

2. Any JRE above 5 is good. If you don't have a JRE installed, download and install one from  [link: https://www.java.com] https://www.java.com

If you won't be able to install a JRE on your computer, use Park's virtual desktop (the Citrix system). JRE is already installed there. Make sure you can log into the system. Here is an ITS article on accessing Citrix through a web browser  [link: https://parkuniversity.freshdesk.com/support/solutions/articles/6000256686-citrix-how-to-use-light-version-web-browser-] https://parkuniversity.freshdesk.com/support/solutions/articles/6000256686-citrix-how-to-use-light-version-web-browser-  Once logged in, you will use the CS-Lab machine under the Desktops tab. It's a Windows virtual machine.

3. Download the Logisim simulator from our course:  [link: https://canvas.park.edu/courses/67161/files] Files > Logisim for Windows and Mac. One student with Windows has verified that both .jar and .exe work on his computer. Another student with Mac said at least .jar worked for him. 

.jar file, .exe file, and the gz files are the needed files for Windows or Mac. 

See the pdf file for directions on which files to use.

.mp4: a tutorial video to get you started.

If you use Citrix, download the .jar file to the virtual machine (just put it on the desktop).  

Make sure you can at least start the software before next week. Let me know if you have any questions.  

Thank you,
Crystal

---

## A quick survey for next week
*Posted: 2022-03-22T17:50:19Z*

Hi Class,

I need your help to complete this survey for next week.  [link: https://canvas.park.edu/courses/67161/quizzes/585759] JRE Survey Could you finish it asap by the end of tomorrow Wednesday? Let me know if you have any questions. Thanks a lot! 

Thank you,
Crystal

---

## Week 1 work graded
*Posted: 2022-03-21T23:45:10Z*

Hi Class,

Unit 1 work has been graded and returned. I replied to some posts in Unit 1 discussion today as I graded them. Review those, especially if it's a reply to your post.

Please read the grading comments on your Unit 1 assignment. Let me know if you have any questions within 1 week of today via Inbox or the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page. Do NOT leave comments on a graded assignment, as I don't receive notifications automatically on such comments, therefore, may not be able to respond in time.

Here are some notes on unit 1 work:

1. We did go through quite some math in unit 1. One unit in our online classroom covers two weeks' material in a 16-week face-to-face class. Take time to go through the lecture and examples, and try the online practice tools. We will see at least some of the problems again on the final.

2. We have to specify the # of bits when talking about two's complement representation. When the MSB is 1, it represents a negative value!

3. When a two's complement calculation generates a carry out of the MSB, that carry is recorded during calculation but discarded in the result. Such a carry is not overflow.    

4. Because our unit assignment is an untimed quiz, you may be able to open a unit assignment as many times as you want, as long as you don't submit it (there is only one submission allowed). Canvas may even save your work as you go along. However, there may be different versions of a question (but on the same subject).

Thank you,
Crystal

---

## Week 2
*Posted: 2022-03-21T05:00:04Z*

Hi Class,

Good job for completing week 1 work! We complete our study of data representation in week 2 learning how signed floating-point numbers are represented in IEEE 754 standard and the limitations of storing real numbers in binary. We will also have a quick review of Boolean algebra and Boolean function simplification. We say review because those have been covered in CS/MA208 discrete math. 

This week's assignments include:

Unit 2 Discussion: one initial post due Wednesday. Respond to at least two classmates by Sunday.

Unit 2 Assignment: due Sunday

[Extra Credit, optional] Survey on practice tools used in unit 1 and 2

Be aware that due dates in this course are at 11:59 pm CT on the specified dates.

Let me know if you have any questions.

Thank you,
Crystal

---

## Today's office hour
*Posted: 2022-03-17T20:28:02Z*

Hi Class,

Sorry that I forgot about today's office hour, even though I was working within Canvas. I've started Zoom and will be there until 4:30 pm to make it up.  [link: https://park.zoom.us/j/92298632120?pwd=dEE3c2Z4NG5pTmJTRE9qVXBQRi9ydz09] https://park.zoom.us/j/92298632120?pwd=dEE3c2Z4NG5pTmJTRE9qVXBQRi9ydz09

Thank you,
Crystal

---

## My office hour and tutor
*Posted: 2022-03-15T18:10:40Z*

Hi Class,

My  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office (Contact/Response Time) page.

My office hours are T/Th 2 - 3 pm via Zoom. Just use this Zoom link: 

Join Zoom Meeting 
 [link: https://park.zoom.us/j/92298632120?pwd=dEE3c2Z4NG5pTmJTRE9qVXBQRi9ydz09] https://park.zoom.us/j/92298632120?pwd=dEE3c2Z4NG5pTmJTRE9qVXBQRi9ydz09

Meeting ID: 922 9863 2120 
Passcode: 065510

I am also available outside that window through requests. Let me know through Canvas inbox and include two-three slots that work for you. We will then meet through the same zoom link listed above.  

Park's tutoring service should have at least one CS319 tutor, Stephanie Kugle, an ICS senior. She has a 4.0 GPA. Just use the "Park Tutoring and Success Services" link from the course menu (on the left) and find her under "Virtual Tutors + Mentors + Study Groups" module -> "Search tutors and mentors by name".     

Let me know if you have any questions.

Thank you,
Crystal

---

## Week 1
*Posted: 2022-03-14T04:08:14Z*

Hi Class,

Here comes our first week of class, which will open at 12 am CT on Monday 3/14.

If you haven't done so already, please introduce yourself to the class by posting in  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406736] Introductions. This will help us build this online classroom and give us a little idea of your background. What's more, it's counted towards your course total.

The focus of week/Unit 1 is an overview and then data representation in binary. We will explain how numeric data is represented in computers in general and introduce Two’s Complement representation, the representation for signed integers. We will learn how arithmetic is carried out on signed integers in Two’s Complement representation. Do go through the lecture slides and scripts. Feel free to use and share additional online resources.

This week's assignments include:

Unit 1 Discussion: one initial post due Wednesday. Respond to at least two classmates by Sunday.

Unit 1 Assignment: due Sunday

Be aware that due dates in this course are at 11:59 pm CT on the specified dates. Be sure to read the late submission policy of this course, in the  [link: https://canvas.park.edu/courses/67161/assignments/syllabus] syllabus and on the  [link: https://canvas.park.edu/courses/67161/pages/grading-and-assignments] Grading and Assignments  page.

Let me know if you have any questions.

Thank you,
Crystal

---

## Welcome to CS319 DL
Hi Everyone,

Welcome to CS319 DL! You should have access to our course on Canvas beginning Monday, Feb 28th. Be sure to read our  [link: https://canvas.park.edu/courses/67161/assignments/syllabus] syllabus and go through items listed under the  [link: https://canvas.park.edu/courses/67161/modules/702160] Course Information Module. 

Please introduce yourself at the  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406736] Introductions discussion.  This will help the whole class to know you a little and build this online classroom. This introduction discussion is graded and due by Wed March 16th.

Our class starts on Monday, March 14th. Feel free to let me know of any questions. I look forward to meeting you in this online class!

Thank you,
Crystal

P.S. connect to peers and alumni via CSIS Dept LinkedIn Page:  [link: https://www.linkedin.com/in/csis-department-park-university-2a690216b/] https://www.linkedin.com/in/csis-department-park-university-2a690216b/

Bin "Crystal" Peng, Ph.D.
Associate Professor of Computer Science
Department of Computer Science and Information Systems
Park University
Parkville, MO 64152

Office Hour: see  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406737] Instructor's Office page

---
