# Unit 2: Lecture - C/C++ Control Statements

In this Unit we will complete the review of the basics commands in C/C++ with the study of Boolean expressions and control statements:  conditional and repetition statements.

As with other units, to highlight the main security points, in this document you will see paragraphs prefaced by the initials SPR. They indicate an important Secure Programming Rule that you must keep in mind when programming. This will be particularly important when a code and a number follows the initials SPR. They are the code and number assigned to this recommendation by the Software Engineering Institute at Carnegie Mellon University, a source of authoritative information on the discipline ( [link: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard] SEI CERT C Coding Standard). You will also be directed to more information from the textbook and course material in paragraphs marked as Read more. References to companion C/C++ programs will also be prefaced by: “You may review the attached program(s).”

 [link: #fragment-1] Boolean Expressions

 [link: #fragment-2] Conditional Statements

 [link: #fragment-3] Repetition Statements 

 [link: #fragment-4] Assignment Equality 

Boolean Expressions

In many programming languages, Boolean expressions (a.k.a. conditional expressions) are computations that produce one of two values: either true or false. These are known as Boolean values and they are the base for the Boolean data types.

C++ fully adopted the concept of Boolean data types, so Boolean variables can be declared as  bool, and can have values of  true or  false, all of which are language keywords. For example, the following declares some Boolean variables and assign values to them.   

bool ok = false;       
bool finish;     
finish = true;

Boolean values can also be obtained from Boolean expressions. Basic Boolean expressions are usually written to compare two things, like two variables or two numbers. If one compares an integer variable x with a number 8, there are 6 possible ways to compare them:

 (x == 8)     Symbol  ==  means “is equal to”

 (x != 8)   Symbol  !=   means “is not equal to”   

 (x < 8)   Symbol  <    means “is less than”   

 (x <= 8) Symbol  <=  means “is less than or equal to”   

 (x > 8)  Symbol  >    means “is greater than”    

 (x >= 8) Symbol  >=  means “is greater than or equal to”    

The symbols used in these comparisons are known as logical operators. The results of the comparisons will be true or false, and can be assigned to any bool variable. For example:

bool complete = ( x > 8 );

Larger Boolean expressions involve additional operations on basic Boolean expressions using relational operators. They may combine more than one basic Boolean expression, as follows:

(x>8)&& (x <=10)      Symbol  && means “AND”   

(x<=8)||(x>10)        Symbol  ||  means “OR”   

!(x>8)                                                 Symbol  !  means “NOT”

The original C language did not have a specific data type to handle Boolean values. Therefore, expressions that produced a value of zero were considered to be the Boolean false value. Any other value was considered to be true. Although this is considered a more primitive way to handle Boolean operations, because this course is about C, we will stick to this convention.

Review the Code

You may review on the attached program  [link: https://canvas.park.edu/courses/62124/files/8205360/download?verifier=3c7pG755f2q53gn9r82Ubbss9VMrcusZfXjH0kKY&wrap=1] ABooleanInCpp.cpp how boolean expressions are used in C++. For a glimpse on how C handles Boolean expression you may also review the attached program [link: https://canvas.park.edu/courses/62124/files/8205361/download?verifier=tLd7MQ17yftyfjtSszbVEPo649iu4xMqvpjV6WIm&wrap=1]  BBooleanInC.cpp. The attached program  [link: https://canvas.park.edu/courses/62124/files/8205113/download?verifier=GARCBIQ4vOa1wahdF90q3a1di2kgVPcZm9aX9G1y&wrap=1] CRelationalOperators.cpp shows the use of these operators while creating truth tables.

Conditional Statements

Conditional statements use Boolean expressions to determine the actions a program will take among various alternatives. C/C++ primarily uses the if-statement as its main conditional statement in all its forms as described below:

Single if-statement. Used when some action must be taken only when a conditional expression is true. Its structure is as follows:

if (conditional_expression) {
 // actions to be taken only if conditional_expression is true
} 

For example:

if (x > 7) {
 // actions to be taken only if x is bigger than 7
} //end of if (x > 7)

if-else-statement. 

Used when a different set of actions is to be taken depending if a conditional expression is true or false. Its structure is as follows:

if (conditional_expression) {
 // actions to be taken if conditional_expression is true
}
else {
// actions to be taken if conditional_expression is false
} 
For example:

if (x > 7) {
 // actions to be taken if x is bigger than 7
}
else {
 // actions to be taken if x is NOT bigger than 7
} //end of if (x > 7)

Sequential if-else-statements. 

Used when the program needs to decide among more than two sets of actions that are related. Structurally is as follows:

if (conditional_expression1) {
 // actions to be taken if conditional_expression1 is true
}
else if (conditional_expression2) {
// actions to be taken if conditional_expression1 is false
//  and if conditional_expression2 is true
}
    // ... add as many similar else-if statements as needed
}
else {
// actions to be taken if all previous conditional 
// expressions are false
} 

For example:

if (x>=100) {
 // actions to be taken if x is bigger than or equal to 100
}
else if (x>50) {
 // actions to be taken if x is bigger than 50,
 // but less than 100
}
else if (x >=7) {
 // actions to be taken if x is bigger than or equal t0 7,
 // but less than or equal to 50
}
else {
 // actions to be taken if x is smaller than 7
} //end of if (x >= 100)

Notice that all forms above have the following characteristics:

All conditional expressions are surrounded by parentheses.

The use of curly brackets is compulsory if there are more than one action in a set of actions, and it is recommended in all cases, because it adds readability to the code,

Based on the values computed for the conditional expressions, a running program may go thru zero or one of all sets of actions, but no more. Namely, these set of actions are mutually exclusive. Once a set of actions is chosen, all other sets are ignored.

No semicolon is required after any of the curly bracket endings, but all actions inside the curly brackets should end in semi-colon, unless they end other curly brackets themselves.

Indentation is required for all sets of actions in between curly brackets. Even if curly brackets are omitted in cases where there is only one action, this single action must be indented.

The comment at the end of each if statement is optional but may add readability, especially if the conditional statement contains many actions.

If statements may be placed inside other if-statements in what is called nested if-statements. This usually happen when a set of actions may include decisions to be made on an unrelated Boolean expression. For example:

if (x>=100) {
 // actions to be taken if x is bigger than or equal to 100
}
else if (x>50) {
    // actions to be taken if x is bigger than 50,
    // and less than 100, including the following
    if (y>30) {
     // actions to be taken if y is greater than 30
    }
    else { 
     // actions to be taken if y is less than or equal to 30
    } //end of (y>30)
}
else {
 // actions to be taken if x is smaller than or equal to 50
} //end of if (x >= 100)

 

Another form of conditional statement in C/C++ is the switch-statement. The switch-statement is a shorthand command, used to reduce the amount of writing in cases where all the conditional expressions in a sequential if-statement are equality comparisons against a single value or variable that is of an integer type (char or int). For example, if a program has to decide the actions to take based on the integer variable step, the following could be written:

if (step == 1) {
    // actions to be taken if step is 1
}
else if (step == 2) {
    // actions to be taken if step is 2
}
else if (step == 3) {
    // actions to be taken if step is 3
}
else {
 // actions to be taken if step is neither 1, 2, or 3
} //end of if (step == 1)

 

The same example can be written using a switch-statement like this:

switch(step) {
   case 1:
     // actions to be taken if step is 1
     break;
       case 2:
     // actions to be taken if step is 2
     break;
       case 3:
     // actions to be taken if step is 3
     break;
   default:
     // actions to be taken if step is neither 1, 2, or 3
} //end of switch(step)

A switch-statement has the following characteristics in C/C++:

The switch command would take any expression that produces a char or integer value.

The switch will compare the value of the expression in between parentheses after the keyword switch with every value after each case keyword in order. The first case in which both values are the same will be the one chosen and all its actions performed.

A break statement indicates the end of the actions to be taken. After a break, the program will go to the first statement after the switch. However, break statements are optional and if omitted, all actions that follow within the switch will be performed until the switch ends or until a break statement appears, even if they pass beyond a case. For example, in the switch above, if the break inside case 1 is deleted, every time the switch enters this case, will perform the actions for steps 1 and 2. When the break in case 2 is found, the switch will end.

Cases can be stacked together if all actions will be the same for the cases involved. For example, the following indicates that cases 1, 2 and 3 will perform the same steps:

case 1: case 2: case 3:
         // actions to be taken if step is 1, 2 or 3
break;

The default case is optional and can be omitted. If present, it should be the last one, otherwise the cases below it will never be tested.

 

SPR DCL41-C

Do not declare variables inside a switch statement before the first case label.  In general, no actions should be taken outside switch cases.

 

Review the Code

You may review on the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205104/download?verifier=zH33kjodKrCTBWwwH70cdE6MkHRFpxHic86GgsQA&wrap=1] DIfSample.cpp and [link: https://canvas.park.edu/courses/62124/files/8205086/download?verifier=bRggFeIEVOQseb4lOdzLyConB6L8MO7853tGXWiP&wrap=1]  ESwitchSample.cpp, the use of conditional statements.

 

Repetition Statements

Repetition statements are also known as loops. They also use Boolean expressions, like the conditional statements, but rather than using them to decide among various possibilities, they are used to decide if the actions on the repetition statement should be indeed, repeated, or if the loop should stop. There are three basic repetition statements in C/C++:

while-statement. This is the most generic of all repetition statements and it has the following structure:

while (conditional_expression) {
  // actions to be taken if conditional_expression is true
} //end while
It has the following characteristics in C/C++:

The following example shows a working while loop that prints “Hello” 7 times:

The conditional expression is checked first. If it is true, the actions inside the curly brackets are performed. Because the conditional expression is evaluated before the actions, this repetition statement is classified as a pre-check loop.

After finishing the actions inside the curly bracket, the conditional expression is checked again and if true, the actions are repeated. This process continues until the conditional expression becomes false when checked, at which point the program goes to the first line after the end of curly brackets.

If the conditional expression is not true the first time is checked, the program never enters the loop. After entering the loop, if the conditional expression never becomes false, the program never leaves the loop, in what is considered an infinite loop.

Infinite loops should be avoided, and to do so, the program must do something inside the loop for the conditional expression to become false at some point in the future.

There are no commas after the end of curly brackets, and the actions inside the loop should be indented for readability.

The following example shows a working while loop that prints “Hello” 7 times:

int count = 0;
while (count < 7) {
    printf(“Hello World!\n”);
    count = count +1;
} //end of while (count < 7)

do-while-statement. This repetition statement allows for at least one execution of the actions inside the loop. This is achieved by checking the results of its conditional expression after the actions have been performed. This is what is called a post-check loop. It has the following structure:

do {
  // actions to be repeated by the loop
} while (conditional_expression);

It has the following characteristics in C/C++:

The actions inside the loop are executed first. At the end, the conditional expression is checked. If true, the actions inside the curly brackets are repeated. This process continues until the conditional expression becomes false when checked, at which point the program goes to the first line after do-while.

If the conditional expression is not true the first time is checked, the program only executes the actions inside the loop once.

Infinite loops are still a possibility and should be still be avoided, by doing something inside the loop for the conditional expression to become false at some point in the future.

The do-while ends with a semicolon after the conditional expression.

The following example shows a working do-while loop that asks the user to guess a number between 1 to 10:

int goal = 7;
int number;
do {
    printf(“Guess an integer number between 1 thru 10: ”);
    scanf(“%d”,&number);
} while (number!=goal);

for-statement. This is the most widely used repetition statement. It was designed as a shorthand for the while statement. It has the following structure:

for (initializations;conditional_expression;updatings){
  // actions to be taken if conditional_expression is true
} //end for

It has the following characteristics in C/C++:

The main idea for the for-loop is to place together in one line of command all the elements that create an actual loop. A while loop usually requires some variables to be initialized and updated to move the loop along. Rather than be placed before or inside the loop, they are put together with the conditional expression. As an example, let us review the one given for the while loop. If written as a for-loop, it can look like the following:

for (int count=0; count < 7; count=count+1) {
    printf(“Hello World!\n”);
} //end of for

The original while loop had a variable count initialized at zero before the while loop and incremented at the end of the loop. In the for loop, both activities were moved next to the conditional expression. The flow of the program is now as follows: when it arrives to the for-loop, it first executes the initializations (only once). In the example above it declares the variable count and initializes it to zero. The conditional expression is evaluated next ( count<7 in the example above), and if true, all actions inside the curly brackets at the for-loop are executed (the printf command in the example above). When these actions are completed, the flow of the program goes back to beginning of the for-loop and executes the updatings (count=count+1 in the example above). Only then, it checks again the conditional expression to see if it continues with the loop. When the conditional expression is false, the loop stops and the program goes to the first sentence after the loop, like any other repetition statement.

The initializations could involve more than one variable separated by commas and it may not involve the declaration of the variables. The following could be proper initializations:

int i,j,k;
for (i=1,j=2,k=3;/// ... and so on
OR
for (int i=1,j=2,k=3;/// ... and so on

The updatings may also involve more than one operation. Something like the following may be allowed:

for (int i=1,j=2,k=3;k<10;i++,j+=3,k=i*j){

Each of these three sections is optional, but the semicolons must always be present. The following statements may be valid:

for (;k<10;k++) {      // no initializations
for (int k=0;k<10;) {  // no updatings
for (;k<10;) {       
 // no initializations or updatings
for (;;) { // an infinite loop to be avoided      

The for-loop is also classified as a pre-check loop

There are no commas after the end of curly brackets, and the actions inside the loop should be indented for readability.

Even though all three repetition statements in C/C++ look different, they are in fact interchangeable. One can convert a while-loop into a for-loop, or into a do-while loop, and vice versa.

A basic terminology used in all loops include the terms loop body and loop step. A loop body is the set of actions to be repeated, namely, all the sentences inside the curly brackets. A loop step is one single run of the loop body.

Some repetition statements are so common in the language that they have specific names and structures. These are some of the most used:

Counter Loop. This loop uses a variable to count every time the program performs a loop step. This variable is known as the counter and it usually marks the progress of the loop by starting at certain value, incrementing at every loop step, and stopping the loop when it reaches certain value. The loops to print “Hello World” seven times shown above are examples of a counter loops in both of their forms, using the while-statement or using the for-statement. The variable count would be the counter. This loop is categorized as a definitive loop because one may know how many times the program will run the loop step before it is actually executed.

Sentinel Loop. This loop runs loop steps until the user enters a specific value, known as the sentinel, at which point it stops the loop. The example given on the do-while statement shows a sentinel loop, in which the sentinel is the value of the goal This loop is categorized as an indefinitive loop because one may not know how many times the program will run the loop step until it actually finishes.

Review the Code

You may review on the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205363/download?verifier=au8S9qweqAhHcsCu91fNbcSmQs4k4uUAyoXjRGQH&wrap=1] FGradeCounter.cpp,  [link: https://canvas.park.edu/courses/62124/files/8205364/download?verifier=JMcH9z4on21OjaSYF41M49TMsM5GUE7KJH8cdKGb&wrap=1] GSentinelGrader.cpp and [link: https://canvas.park.edu/courses/62124/files/8205112/download?verifier=40z0f2x2l4AAEf8SaelpnftXoEMhG6LxC5Ve9rje&wrap=1]  HForAndDoLoops.cpp the use of repetition statements.

Assignment and Equality

A common mistake using Boolean expressions in C is to confuse the assignment operation (performed with the symbol =) with the equality comparison (performed with the symbols ==).  For example, the following constructs will compile and run, but fail to perform correctly in C:

if (x = 0) {// steps if true }
for (int i=0,k=1;(i<10) && (k=0); i++) {//loop steps }

The conditional statement is supposed to run some steps if the value of variable x is zero. Instead, it is assigning the value of zero to variable x. The zero value of x is then considered to be false for the conditional expression, and the steps are never executed. Similarly, the for-statement will never run its steps. When the conditional expression is evaluated before the loop, the variable i will be zero, that is less than 10 (i<10 is true), but variable k will be assigned the value of zero. This means that (k=0) will be considered false, and the whole conditional statement will evaluate to false (true && false is equal to false).

Sometimes, using assignments in conditional expressions may help the programmer to write less steps. For example, the following may be intentional, and will be acceptable expressions in C:

if (x = y) {// steps if true }
for (int i=10; k = i; i--) {  // loop steps }

The conditional statement is not comparing the value of variable x with the value of variable y, instead, it is assigning the value of variable y to variable x. If that value is zero, the conditional expression is false and the “steps if true” will not be executed. Any other value different than zero for y will perform these steps. The conditional statement will compile and the program will run, but the intent of the programmer is dubious. S/He may be aware of the implications of these actions, but they may appear suspicious to other programmers, who may consider it to be a mistake.

The for-statement will run exactly 10 times, because the value of variable i will start at 10 and decrement one by one until it becomes zero. Before each loop step the value of variable k is updated to the current value of variable i, and it is used to decide when the loop steps end. When variable i becomes zero, so the variable k and the loop will end. Once again, the loop works, but the intent is dubious.

To avoid the uncertainty that these and similar codes provide, the following secure programming rule forbids the use of assignments in conditional or repetition statements:

SPR EXP45-C

Do not perform assignments in selection statements.

The previous dubious examples could be re-written to satisfy this rule as follows:

x=y;
if (x) {// steps if true }
k=10;
for (int i=10;i>0;i--,k=i) {  // loop steps }

Read more

 Read more about the topics of this lecture in sections 3.1 thru 3.7 of the textbook.

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
