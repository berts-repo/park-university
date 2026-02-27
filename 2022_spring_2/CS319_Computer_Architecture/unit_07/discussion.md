# Unit 7: Discussion

Due Dates:

First post due 11:59 p.m., Wednesday, CT. 

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Guidelines: see  [link: https://canvas.park.edu/courses/67161/discussion_topics/1406742] Unit 1 Discussion

Discussion questions:  [link: https://canvas.park.edu/courses/67161/files/9152257?verifier=dNq9b5z1TDHb8tvJYWQ7RIu8rbWhIX97CpkKWIYm&wrap=1] Unit7_Discussion.docx

For readability, show Assembly code in the "Preformatted" style. If needed, see the "Change Text Style" section of this Canvas Student Help article  [link: https://community.canvaslms.com/t5/Student-Guide/How-do-I-add-and-modify-text-in-the-Rich-Content-Editor-as-a/ta-p/322] https://community.canvaslms.com/t5/Student-Guide/How-do-I-add-and-modify-text-in-the-Rich-Content-Editor-as-a/ta-p/322

(Update 4/30/2022) Use this template when "draw a stack":
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

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-04-27T11:33:10Z

4. Pick one program from P1 – P5. Given this C program and its assembly code, comment each line of 
the assembly code. Your comment should explain an assembly statement in the context of the given C 
program, such as "allocate memory on the stack for local variable x" or "initialize x to 1". Do not use a 
general description like "push a value onto stack" or "move the value in first operand to second 
operand".

 

P2:

int main() {
  int x;
  int y = 2, z = 4;
  if ( y > z || z % 2 == 0 )
    x = y;
  else
    x = z - y;
  return x;
}
main:
   PUSH %BP                     //initializes stack
   MOV %SP, %BP                 //moves source pointer to the top of stack
@main_body:
   SUB %SP, $4, %SP             //allocates x by moving down the stack, 4bytes
   SUB %SP, $4, %SP             //allocates y
   MOV $2, -8(%BP)              //initializes y, y=2
   SUB %SP, $4, %SP             //allocates z
   MOV $4, -12(%BP)             //initializes z, z=4
@if0:
   CMP -8(%BP), -12(%BP)        //compare address locations, y to z
   JGT @true0                   //jumps if y < z
@false0:
   DIV -12(%BP), $2, %0         //divides address location z by 2 and store in register 0
   CMP %12, $0                  //checks if there is a remainder
   JNE @false1                  //jumps if remainder is 1
@true0:
   MOV -8(%BP), -4(%BP)         //stores y in x
   JMP @exit0                   //jumps
@false1:
   SUB -12(%BP), -8(%BP), %0    //else statement, z-y, store in register 0
   MOV %0, -4(%BP)              //store result in x
@exit0:
   MOV -4(%BP), %13             //stores x in register 13
   JMP @main_exit               //jumps
@main_exit:
   MOV %BP, %SP                 //moves SP to the top of the stack
   POP %BP                      //removes address location for stack
   RET                          //exits program

---


### Feedback

**[INSTRUCTOR]:** Good job with this week's discussion and supporting others!

The micro tab of the simulator http://ctoassembly.com/microc.html  lists syntax examples and pointers and arrays are there.
