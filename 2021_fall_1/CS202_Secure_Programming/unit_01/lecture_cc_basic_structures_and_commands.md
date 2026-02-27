# Unit 1: Lecture: C/C++ Basic Structures and Commands

Introduction

This course requires that students be already familiar with programming in a language other than C/C++ (preferably Java or Python). A student with such experience is equipped to recognize the basic programming structures all programming languages should contain. During the first two units of this course we will briefly review these basic structures and the way they are implemented in C/C++.

While this course teaches specifically the C/C++ programming language, the main goal of the course is to provide you with secure programming rules that you may apply to your programming career in general. To highlight these security points, from time to time, in this and other course documents, you will see paragraphs prefaced by the initials SPR. They indicate an important Secure Programming Rule that you must keep in mind when programming. This will be particularly important when a code and a number follows the initials SPR. They are the code and number assigned to this recommendation by the Software Engineering Institute at Carnegie Mellon University, a source of authoritative information on the discipline ( [link: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard] SEI CERT C Coding Standard). You will also be directed to more information from the textbook and course material in paragraphs marked as Read more. References to companion C/C++ programs will also be prefaced by: “You may review the attached program(s).”

 [link: #fragment-1] About C and C++

 [link: #fragment-2] Structure of C/C++ Programs

 [link: #fragment-3] A Basic Program in C/C++

 [link: #fragment-4] Compilation of C/C++ programs 

 [link: #fragment-5] Identifiers

 [link: #fragment-6] Variables

 [link: #fragment-7] Assignments

 [link: #fragment-8] Arithmetic Operations and Data Type Conversions

 [link: #fragment-9] Constants

 [link: #fragment-10] Basic Input / Output (I/O) with C

 [link: #fragment-11] Comments and Indentation

 [link: #fragment-12] Practical Example

About C and C++

C is a programming language developed by Dennis Ritchie (one our textbook’s authors) in 1972 to program UNIX machines. Its flexibility to adapt to various other platforms, as well as the directness in which it allows programmers to control all sort of hardware devices made it an important language to learn, even today, more than 40 years after its initial release. During these years it had had various incarnations and improvements, more importantly, the advent of C++. This extension of C was created by Bjarne Stroustrup in 1979 with two main goals: to incorporate Object Oriented Programming ideas onto C and to improve the user interface with the inclusion of new libraries for input and output.

Documents in this course will mention C/C++ when talking about the language in general, but will be more specific when dealing with topics that are pertinent to C or C++ in particular. Even though we will talk in this course about C/C++ as a unit, we will concentrate in the study of the C language and its structures, because they provide the best opportunities to explore security programming issues. 

Structure of C/C++ Programs

The basic logical unit of programming in C/C++ is known as the function. Functions can be thought as mini-programs used to build up larger applications. Fully operational programs in C/C++ are therefore sets of functions organized in one or more files. Some files are provided by the language itself, and others are written by programmers like you. These files are divided into two kinds: C/C++ files with extension .cpp (or .c for old C programs), and header files with extension .hpp (or .h for old C programs).

C/C++ files will contain the functions a programmer writes for an application. There can be one or more of these files in a single application with one or many functions inside each of them, but what is important to remember is that one of these files (and only one of them), must contain a function named main. A C/C++ application will start and end in the main function. This function is the one that controls the behavior of all other functions. The main function may call other functions to perform from the available C/C++ files or from the header files included in the application. A header file is similar to a C/C++ file, but it usually contains a library of general purpose functions that are thematically related. For example, C provides the header file named math.h that contains mathematical functions, and another one named stdio.h that contains functions for standard input and output. Either of these files may be useful in more than one application, therefore they are stored as header files rather than .cpp files. Programmers may also add their own libraries of functions if they save them in files with names ending in the .hpp extension.

A Basic Program in C/C++

Like any other programming language, the purpose of C/C++ is to provide instructions for computers to perform calculations. This set of instructions is what is known as a program. Even though these instructions may have a very sophisticated organization, in essence, computers today perform these calculations via the traditional model of computing: input-process-output. Programs may receive input from some source, apply process operations to this input and produce some output results.

One of the most basic examples of a C/C++ program is the classic HelloWorld code. This program receives no external input, process nearly nothing, and prints only one message: “Hello World!”. The following is the HelloWorld program written in C (with line numbers on the left):

1: #include <stdio.h>
2:
3: int main() {
4:   printf("Hello World!\n");
5:   return 0;
6: }

Instructions in C/C++ are contained within functions. As indicated before, a function is the most basic logical unit of programming in C/C++. It provides a mechanism to identify some input for a program, it contains a set of instructions to be performed sequentially from top to bottom, and it allows a way to produce results from calculations. In the example above, the HelloWorld program contains only one function. This function was given the name of main in line 3. This main function begins in line 3 and ends in line 6.

In line 3, the parentheses after the name, ( ), indicate the place where some input for this function may have been declared. Since there is nothing inside these parentheses, this function is expecting no input. The word int before the function name is an indication of the type of output that is expected from the function. In this case, it means that the program should produce an integer number (whole number). We will talk more of the type of outputs expected in functions later in this document and the course.

The process in this program consists of the two instructions in lines 4 and 5. Like in any other function, instructions are surrounded by curly brackets, { }. They clearly indicate where the function begins and ends. Observe also that each instruction ends in a semicolon (;). This is required of each statement inside a program, so the compiler will know where an individual instruction ends. Finally, notice that lines 4 and 5 are indented with respect to the lines containing the curly brackets. This is done so that future readers of the program may recognize at a glance that these lines are inside the function.

The core of the program is in line 4. It calls another function to do some printing, the printf function. We recognize that it is a function, because its name is followed by parentheses. However, the instructions inside this function are not visible in the current program. The fact is that this function is part of the set of functions provided by the C/C++ language in its libraries to help us when writing programs. All these C/C++ functions that make up the language are either loaded automatically in memory when the program is compiled or they need to be included in the code before compilation. Line 1 in the example above is adding the contents of the C header file stdio.h before anything is done with the program. As indicated before, this file contains a library of functions that deal with standard input/output issues. The printf function is inside that library. Because it is incorporated in the program before anything else, we can freely call printf (and any other function inside stdio.h) at any point within the program. Notice that the include command to incorporate the stdio.h file is preceded by a hash, #. The hash is an indication that the include command is not a C/C++ command, but it is actually a pre-processor command. Preprocessor commands are few instructions that are not part of the C/C++ language, but that are used to control the process of program compilation (the translation of the C/C++ code to machine code as we will see in the next section). They are placed before the actual C/C++ code (that is why they are called pre-processor, or before the process begin) and they all begin with a hash (#).     

As indicated before, the contents inside the parentheses after a function name are some input the function may use. The input provided to the printf function will be printed in some location, usually a screen or window. The printf function in line 4 on the example above is receiving the following input: "Hello World!\n". This is known as a string literal, or just a string. It is a sequence of characters to be taken, “literally”, as they come. For example, the printf will receive this string and it may print it in a screen exactly as it is. The "Hello World!" words will be printed and the cursor in the screen will then move to the next line. This happens because the ‘\n’ at the end of the string is actually a single character that means “go to the next line”

The main function was written with the intent to return an integer value, because of the word int before the word main, as previously described. Line 5 is performing this task, by returning a zero value. Every time a return statement is reached, a function ends its processing. No more statements are executed inside the function, and control of the program is passed to whoever called the function. In the example above, when the program is running, it is doing so because the operating system in the computer decided to execute the main function, usually because a user requested so. When execution reaches the return statement in line 5, the main function ends (and therefore the program execution). The operating system then receives the zero value produced by the main function and is free to do with it whatever it wants. Some operating system may toss the value out. Some other may use it as an indication of how successful the program run was, zero being a successful run, and any other number indicating a possible error while running.

The printf function also was defined by the C/C++ language as returning an integer value. This function returns the number of characters that it printed (13 characters in line 4 on the example above, including \n that counts as one). It may return a negative number if there was a problem printing and it could not do it. The same way the operating system may discard the returned value from main, the main program above is choosing not to do anything with the value printf is returning.  It is just discarded.

While every programmer is free to name functions as they fit, the name main is a special one within the C/C++ language. As indicated before, C/C++ compilers and programs running C/C++ code identify the main function as the beginning of a program or application.  We must have one and only one main function in every C/C++ application. We must organize every programming starting from within the main function.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205110/download?verifier=pGZkmDUemEDY7F94jj0QpH12104mgyyPpi11Tm0B&wrap=1] HelloWorldC.cpp that contains the code described in this section.

 

Read More

Read more about this basic C/C++ program in section 1.1 of the textbook.

 

Compilation of C/C++ programs

For a C/C++ program or application to run, it first must be compiled. Compilation is the process of translating the program code onto a set of instructions in machine language that the computer may understand and execute. C/C++ compilers are programs that perform this translation. There are many versions of these compilers and they are platform specific, meaning that the machine code they produce is specifically made for a kind of computer architecture. A C/C++ compiler for a Windows machine will produce different machine code than a C/C++ compiler for a Unix machine.  If a C/C++ application is going to be transferred from a Windows machine to a Unix machine, at the least, it will need to be recompiled.

The process of compilation actually consists of two parts: first the actual translation of instructions from C/C+ code to machine code, and then the process of linking the various pieces of the application together. This is especially true for applications that include multiple files. In the past, this two-step process required careful planning and involvement of a programmer. These days, these tasks are greatly simplified by the use of programming environments like the one used in this course: C/C++ in Microsoft Visual Studio. This programming environment facilitates not only the process of compilation, but also the organization of applications into projects with different folders for C/C++ files and header files, and the debugging of the code until a final product emerges. Students familiar with other programming languages would recognize the debugging process, or eliminating errors in the code, as one of the most time consuming tasks in any new development.

Review the Code

Read more about Microsoft Visual Studio in the document “Lecture:How to Use Visual Studio 2017 for C/C++”.

The remainder of the lecture will review basic concepts in the C/C++ language.

 

Identifiers

Identifiers are names. They are the names of the files, programs, functions, and everything else we will use in a program. We need to use names, so we can reference all these programs, functions, etc., without any confusion. The C/C++ language allows programmers to create and use in a program any identifier that abides by the follow restrictions:

Identifiers may start with a letter (upper or lower case). Some identifiers begin with underscore, but these are reserved keywords in the language, and programmers should avoid their use.

The initial letter or underscore may be followed by zero or more letters (upper or lower case), digits, or underscores in any order. Notice specially that spaces and any other special characters are not allowed as part of the identifier.

These days, depending of the compiler there may not be a limitation on the length of an identifier, but originally they may not be longer than 31 characters. Sticking to this size restriction would eliminate any portability problems (moving the code between different machines).

Language keywords cannot be used as identifiers.

Identifiers that follow the rules above will compile in C/C++, but that is not enough. One of the most important consideration while naming is readability. Programs are mostly written to be read by other programmers, most of which may not have been involved in the process of writing it in the first place. Maintenance of programs usually happen years after it was originally deployed. Most of the creating team of programmers may not be involved in the maintenance process, so it is important that programs are properly documented. One of the easiest and most effective ways to document a program is using identifiers that are meaningful for the application at hand. As we do in Math, one could use an identifier like x to refer to many things: an age, a date, a measurement, an address, etc. but if we actually use identifiers like age, birthDate, currentTemperature, homeAddress_01, etc. one can read and understand better the concept the program is referencing. Human memory is feeble, so using relevant identifiers may even help students remember what their programs were all about at the end of the semester when studying for exams.  

SPR:

Use meaningful names in all identifiers.

 

The example above used three identifiers already: the names of the functions, main and printf, and the name of the library stdio.h. All these names were given by the language designers and we are just using them. The function names satisfy all prescribed identifier rules, so they will compile. The name of the library does not follow these rules. It contains a special character, the dot (.). However, this is acceptable because the #include command is not a C/C++ command, but a pre-processor command. This command will pull the file stdio.h from the language set of libraries. C/C++ library names satisfy the naming conventions of files in the operating system where the compiler is hosted.  They do not need to abide by the C/C++ rules on identifiers.

On the other hand, the words int and return in the example are not identifiers, but keywords. Keywords are special words that have specific and special meaning within a language. There is a finite set of keywords any experienced C/C++ programmer may know. These are the keywords that the rule number 4 above indicates cannot become identifiers. For example, one cannot name a function either int or return. Students will learn in time all necessary keywords within the C/C++ language. In the meantime, if they accidentally use a keyword as an identifier, they will not be able to compile the program. Visual Studio displays keywords in a different color than identifiers, so students hopefully will find this mistake, if it happens to them, by noticing that their identifiers have a different look that they are supposed to have.

SPR DCL37-C

Do not declare or define a reserved identifier.

A program with more substance than the HelloWorld program described above may require space to store the input provided, the results obtained, and any intermediate value it needs to hold while performing its instructions. This space is no other than the computer’s RAM. Programs will request and obtain portions of RAM from the computer’s Operating System to use in calculations according to its needs. To be recognized, these portions of RAM are named and referenced by this name, an identifier. Therefore, we define a variable as a piece of RAM assigned to a program and labeled with a name (identifier).

Variables

In C/C++, every variable to be used in a program must have been previously declared. This means that before using it, a program must have previously declared its intention to use a name for a variable and the kind of variable it would be, known as the data type. This is done, so that when the program is running, the variable is recognized by its name, and it has enough space allocated in RAM for its contents. C/C++ provides a basic set of data types with appropriate sizes to represent numeric values of various kinds, and characters in various human languages. You may find some of the common types in the following list:  

Basic Structures and Commands

Data Type

Allocated RAM Size (Bytes)

Value Range

Character types (for single characters or small whole numbers)

unsigned char

1

[0 , 255]

char (or signed char)

1

[-128,  127]

Integer Types (whole numbers)

unsigned short int

2

[0, 65535]

short int 
(or signed short int)

2

[-32768, 32767]

unsigned int

4

[0, 4294967295]

int (or signed int)

4

[-2147483648, 2147483647]

Floating Point Types (decimal numbers)

float

4

[-3.4x1038, 3.4x1038]

with smaller numbers up to

[-1.17x10-38, 1.17x10-38]

double

8

[-1.7x10308, 1.7x10308]

with smaller numbers up to

[-2.22x10-308, 2.22x10-308]

 

The allocated RAM size and the corresponding range may change from implementation to implementation of the compiler. The values shown in the table are the ones available in Microsoft Visual Studio that we will use in the course.  If you want to be certain of the sizes available in your particular implementation you may review the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205108/download?verifier=u61xhPsPpWoSGZjbnoSc1g2RQfn7RxNFD0AkDPpf&wrap=1] ACheckSizes.cpp and  [link: https://canvas.park.edu/courses/62124/files/8205109/download?verifier=2KXPdBUe8HtiD8Gctgz4aoQMryzaXE3zE2smcg0e&wrap=1] BCheckLimits.cpp to verify.

The following examples declare the variable cVar, iVar and fVar in C/C++:

char cVar;
int iVar;
float fVar;

After declaring variables, and before they are used in a program, they must contain a value. One of the most common mistakes, and the cause of major security problems is to assume that because a variable was declared, it is ready to be used. In many languages, all that a declaration of variables does is to assign a name to an area of memory. There is no guarantee on the contents of that area in memory. This is especially true in C/C++. An assigned memory area may still contain values stored by old programs. Besides being this a potential security vulnerability, it also may produce extraneous results in our programs. Therefore, it is imperative that variables be initialized with an appropriate value as soon as possible, and certainly before its first use. If values are known at declaration, we could declare and initialize variables in C/C++ as follows:

char cVar = 'c';
int iVar = 123;
float fVar = 75.37;

This way we are certain that variables would begin with appropriate values before any other instruction is executed in the program. The equal symbol (=) used to initialize the variables above is the operator of one of the most basic of operations in any computer language, known as assignment, to be described in the following section. 

SPR DCL31-C

Declare identifiers before using them.

 

 

 

SPR

Be certain all variables are properly initialized before they are used in a program.

 

Assignments

Assignment is the computer operation that assigns a value to a variable. In C/C++, assignment can be performed in many ways, but the most basic assignment command has the following syntax:

            variable = expression;

where variable is any previously declared and accessible variable in the program, and

expression is any direct value, variable, or expression that produces a value to be assigned to the variable.

The equals symbol (=) is the symbol used for the assignment operation and indicates where the variable ends and the expression begins.

The compiler interprets this sentence as follows: compute the expression to the right side of the equals symbol and, when finished, assign its result to the variable to the left of the equals symbol.   

At the end of the previous section we showed a shorthand that collapses declaration with initialization, in effect, giving values to the variables as soon as they are declared. The following examples will modify those values. We assign a new character (x) to the char variable, a new whole number to the integer variable (321), and the result of a mathematical expression to the float variable:

cVar = 'x';
iVar = 321;
fVar = fVar + 1.0 ;

There is no need to declare the variables again. They already have memory allocated for their values. One can change these values as many times as needed with multiple assignment statements, but declarations can only be done once.

Because we declare variables once, before they can be used, it is highly recommended to declare all variables at the beginning of a program. While C/C++ allows declarations anywhere in a program, once again, readability dictates to declare variables at the beginning of the section of code where the variable is going to be used. So far, at the beginning of this course, this means to declare variables at the beginning of the function where they are used, right after the opening curly bracket, {.

The reason is this: a programmer reading somebody else’s program, specially a large one, may find an unfamiliar variable in the middle of the program. If that variable were declared anywhere in the program, the programmer will have to scan, potentially, the whole code to find the variable’s declaration and its type. If on the other hand, all declarations are at the beginning of the code, the programmer will know to go there to get familiar with this and any other variable in the program.

SPR

Declare all variables at the beginning of the piece of code where they are going to be used.

The last example of an assignment also highlights a very important point, and the source of confusion for many beginner programmers: the assignment statement is not an equation. It does not mean that the left side is equal to the right side in the statement. If that were the case, the last example will say that fVar is the same as fVar + 1 and that is mathematically impossible. The assignment statement is an instruction. It is telling the computer to evaluate the expression in the right side of the equals symbol and then erase the old value of the variable in the left side and replace it with the results of the expression. We also cannot write the following, as we do in an equation: 132 = iVar; this would try to change the value of the number 132, and again, this is impossible. 132 will always be 132. It is a number, not a variable.

At the time when C was developed, programmers did not have the luxury of large amounts of RAM memory, so all space available was at a premium. In those days, programmers devised a lot of tricks to save space for data, but also to make programs very compact. C was created under that philosophy, and provided programmers with a series of shorthand structures to write a good number of instructions with the minimum of keystrokes. The assignment command was one of the instructions in which C provided various shorthand structures. For example, the following assignment increases the value of the variable iVar by one:

iVar = iVar + 1;

C provided the += symbol to shorthand this instruction as follows:

iVar += 1;

Rather than writing the name of the variable twice, the += symbol indicates that the contents of iVar should not be discarded, but incremented by one.  The following is a table with other similar shorthand for the assignment command:

Shorthand for the Assignment Command

Symbol

Description

Examples (initially i=17)

+=

Add the contents of the variable in the left side to the value of the expression in right side and save it in the variable in the left side. 

Adding 3 to variable i:

     i += 3;

(i becomes 20)

-=

Subtract from the contents of the variable in the left side the value of the expression in right side and save it in the variable in the left side.

Subtracting 4 from variable i:

     i -= 4;

(i becomes 16)

*=

Multiply the contents of the variable in the left side by the value of the expression in right side and save it in the variable in the left side.

Multiplying by 2 the variable i:

     i *= 2;

(i becomes 32)

/=

Divide the contents of the variable in the left side by the value of the expression in right side and save it in the variable in the left side.

Dividing by 4 the variable i:

     i /= 4;

(i becomes 8)

%=

Obtain the remainder of the division of the contents of the variable in the left side by the value of the expression in right side by and save it in the variable in the left side.

Obtaining the remainder of the division of i by 3:

     i %= 3;

(i becomes 2)

++

Increments the value of the variable by one

Incrementing i by one:

     ++i;

(i becomes 3) OR:

     i++;

(i becomes 4)

--

Decrements the value of the variable by one

Decrementing i by one:

     --i;

(i becomes 3) OR:

     i--;

(i becomes 2)

 

The last two shorthand symbols require an additional explanation. When used on their own, ++ and -- can be used before or after the variable name with the same results, but C provided these two variants so that they can be used compactly in other expressions. For example, one may increment the values of variables i and j before they are added to get a value for the variable k, all in one command:

int i = 2, j = 5, k;
k = (++i)+(++j);

 

Notice the declarations and initializations were also compacted in one line. This is possible because all variables were of the same data type. After these lines, the values of the variables will be i=3, j=6, and k=9. However, if we locate the ++ after the variable names the results will be different:

int i = 2, j = 5, k;
k = (i++)+(j++);

 

In this case, after these lines the values of the variables i and j would be the same, but k will be 7. The reason is that placing the ++ (or --) symbol before a variable indicates to the compiler to perform the incrementing (or decrementing) before any other calculation is done.  This is known as pre-incrementing (or pre-decrementing). On the other hand, putting the symbol after the variable name indicates the compiler to use the value of the variable to calculate the expression before it is incremented (or decremented). This is known as post-incrementing (or post-decrementing).

 

These changes of the order of execution of commands due to some language features are part of what is known as side effects. Side effects could be very confusing, and the unexpected results they may produce motivates the following secure programming rule:

SPR EXP30-C

Do not depend on the order of evaluation for side effects.

Abiding by this rule is easier these days, when computer memory is more available and there is no need to compact statements in one line. A better approach to write the code above would be: 

int i = 2;
int j = 5;
int k;
i++;
j++;
k = i + j;

Once more, the advantage is readability. There is not confusion for a reader on which statements are performed first. In addition, any speed-up we might have had by having a compacted code is regained these days, by modern compilers who are equipped with optimizers that take advantage of the computer’s architecture to speed-up calculations.   

Arithmetic Operations and Data Type Conversions

C/C++ allows the following arithmetic operations in order of precedence:

Arithmetic Operations in order of Precedence

Order of Precedence

Symbol

Name

Examples

1

++, --

Post increment, post decrement

i++, j--

2

++, --

Pre increment, pre decrement

++i, --j

3

*, /, %

Multiplication, division, remainder

i * j, i / j, i % j

4

+, -

Addition, subtraction

i + j, i - j

 

The order above is used in arithmetic expressions made of a combination of operations. This means that, if there are no parentheses in an expression, it should be evaluated starting from the post increments or post decrements. Once all of them have been computed, all pre increments and pre decrements should be evaluated, and so on. In case there are more than one operation of the same order, these should be evaluated in order from left to right. For example, consider the following arithmetic expression used in an assignment:

int k = 15 - 4 * 2 + 13 / 4;

There are no post incrementing or post decrementing operations, no pre incrementing or pre decrementing operations, so we go to the third order of precedence and we need to evaluate first the multiplication and the division. We must first do the multiplication of 4 by 2, because it is to the left of the division of 13 by 4. Once these operations are completed we proceed to do the fourth order of precedence: addition and subtraction. The subtraction is executed first because is to the left of the addition. The following diagram shows the sequence of calculations:

15 - 4 * 2 + 13 / 4 

15 - 8 + 13 / 4 

15 - 8 + 3 

7 + 3 

10 

The value of 10 will be assigned to the variable k. If for some reason we want to alter the order of precedence we use parentheses to indicate which operations should be performed first. For example, if we would like to calculate the subtraction and the addition first, we could have the following expression and calculations:

(15 - 4) * (2 + 13) / 4 

11 * (2 + 13) / 4 

11 * 15 / 4 

165 / 4  

41   

Now, if we also want to perform the division before the multiplication we again surround that operation with parentheses. This will produce a group of nested parentheses: parentheses inside parentheses. These constructs must be computed always starting with the inner most parentheses going outside. This is shown below:

(15 - 4) * ((2 + 13) / 4)

11 * ((2 + 13) / 4)

11 * (15 / 4)

11 * 3

33

Notice that the all divisions in previous evaluations were integer divisions in which we obtain an integer result with no remainder kept. For example, 13 / 4 produces the value of 3, leaving a remainder of 1 that is not carried by the results. The remainder (or modulus) operation, symbolized by the %, can be used to obtain that remainder. For example, 13 % 4 produces the remainder value of 1. The division is computed as an integer operation because both operands (13 and 4) were integers. However, if any of them were a floating point value, identified by the decimal point, the operation would have been a decimal division. 13.0 / 4, 13/4.0, and 13.0/4.0 would all produce the decimal value of 3.25.

Before C/C++ performs an arithmetic operation it reviews the data types of the operands to compare their ranges (as described in the first table above). If any of them is of a data type that has a bigger range of values than the other operand, the one with the smaller range is promoted to the data type of the other operand with a higher range. This is done, so that the result of the operation always has the higher level of precision it may need. For example, if we multiply 3.25 * 2, the first operand is decimal, and the second is integer. The range of decimal numbers is bigger than the integers, so the result of this multiplication may lie in the decimal range. Therefore, the integer 2 is promoted to a decimal 2.0 and the result of 6.5 is also a decimal value. The same happens in the 13.0/4 division. Because 13.0 is decimal, the integer 4 is promoted to decimal 4.0 and the result of the division is 3.25, also a decimal number. On the other hand, in the 13/4 division, both operands are integers, and the result is also the integer 3 on which the remainder of 1 has been discarded.

In assignments, the data type of variable to the left of the equals symbol should have a range that is the same or larger than the one of the results the expression being evaluated to the right of the equals symbol. In a previously described example, the variable k is integer as well as the result of the operation, so the assignment will carry out without problems:

 int k = 15 - 4 * 2 + 13 / 4;

However, if one of the operands in the expression is described as decimal, the program will not be able to compile the program:

 int k = 15 - 4 * 2 + 13.0 / 4;

This is because there is a potential loss of precision when we trying to convert from a larger range value to a smaller one. Decimal values may be loss in this example. This is called a demotion. Demotions can only be performed if explicitly indicated by the programmer using a structure known as type cast. To type cast an expression onto another type, the expression is preceded by the desired data type in parentheses as follows:

data type) expression

Applying casting to the previous sample expression we should have:

int k = (int) (15 - 4 * 2 + 13.0 / 4);

The compiler would evaluate the whole expression and then cast the result onto the int data type to be saved on the variable k. Notice that the whole expression was surrounded by parentheses to convert the final result. If no parentheses were added, the cast operator would only be applied to the first operand, the number 15, and the result of the whole operation would still remain a decimal type that would not be able to be saved in the integer variable k.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205111/download?verifier=496xhiJOJmc7vsCY4KV8DFkysLGteiqceulLreQg&wrap=1] CArithmeticOperations.cpp that contain these operations.

Constants

Some computations require values that may never change. If we want to do geometrical calculations, we probably may need a value for the number pi (π). This value is never going to change. This is what a constant is all about. In C/C++ there are three main ways to assign permanent values to identifiers. The first one uses the pre-processor command #define, also known as a macro. A macro has the following syntax:

            #define identifier replacement_text

where #define is the pre-processor keyword,

identifier is any valid C/C++ identifier that will be replaced in the remainder of the program file with the replacement_text before the program is compiled, and

replacement_text is the text to replace the identifier before compilation.

For example, a macro to define the value of pi (π) could be created as follows:

#define PI 3.14159

Notice that the preprocessor statement does not end in a semi-colon, because it is not a C/C++ statement.

Customarily, identifiers for constants are written all with upper case letters, and using underscores to separate the words in their name. The following example creates a macro for the numbers of the days in a week:

#define DAYS_IN_A_WEEK 7

When a program contains a macro, the preprocessor will replace all instances of its identifier found in the file after the #define with the exact replacement text, then it will compile the converted file. With the two macros defined above, a program may have the following statements:

float salaryPerDay  = 125.0;
float salaryPerWeek = salaryPerDay * DAYS_IN_A_WEEK;
float radius = 10.00;
float area = 2 * PI * radius;

 

These statements will be converted before compilation in the following statements:

float salaryPerDay  = 125.0;
float salaryPerWeek = salaryPerDay * 7;
float radius = 10.00;
float area = 2 * 3.14159 * radius;

This conversion is automatic and not visible to the programmer when being performed.

Technically, a macro is not a constant, but a way to have a constant value replaced in a file before compilation. Consequently, macros may also be used to change specific lines of code. In the following example, a macro is used to replace the header of the main function:

#include <stdio.h>
#define MAIN int main()
MAIN {
    printf("Hello World!\n");
    return 0;
}

A second, and more popular, way to create a constant was incorporated in C++. It involves the use of the keyword const. A constant can be created the same way any variable is declared if preceded by this keyword. The variable must also be initialized at declaration time, so that its value remains constant. The following sentences declare the constants for the number of days in a week and the number pi (π):  

const int DAYS_IN_A_WEEK = 7;
const float PI = 3.14159;

A third way to create constants is using an enumeration constant. This C/C++ structure is mainly used to define more than one related integer constant, usually in a sequence.  An enumeration constant has the following syntax:

            enum enumID { cname1 = value1, cname2 = value2, … };

where enum is the C/C++ keyword for the enumeration,

enumID is a valid C/C++ identifier for the enumeration, and

each pair, cname# = value#, is a named constant with the identifier cname# and the assigned integer value value#. The value is optional. If not given, the value will be one more than the previous one. If the first constant was not given a value, it will have a value of zero.

For example, the following enumeration constant assigns a number to every named constant representing the days of the week:

 enum days {MON=1,TUE=7,WED=3,THU=7,FRI=5,SAT=10,SUN};

Notice that the named constants may be given any integer value, even a repeated one, or one out of order (as with TUE and THU), and if one is not given, they will take the value of the previous declared named constant plus one (as with SUN that has a value of 11). If MON would not have a value, its value would be zero (0). With this declaration of an enumeration constant, name constants can be used as part of the program wherever an integer may be used, for example:

int dueDay  = MON;
int dayExtension = MON+WED;

 

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205107/download?verifier=wRxbWpQoyteQjLD2aQFgdelq6E1qsg5bmZJUsF9v&wrap=1] DConstants.cpp that shows various ways to create and use constants.

Basic Input / Output (I/O) with C

A program needs some way to obtain input for a process and also some way to output results. Since we already used it, let us talk first about output.

As we have already seen, the function printf from the stdio.h library is used in C to print formatted results to a screen. This function takes as input a string that describes the format we want for the output, followed for as many variable names or expressions which values the programmers wants to print. For example, the following lines will print the value of the integer variable x and its power of 2:

int x = 10;
printf("The value of x is %d and its power of 2 is %d\n", x, x*x);

 

The format to be printed is the string "The value of x is %d and its power of 2 is %d\n". This string has two placeholders, indicated by the %d symbols. These symbols will not be printed, but before printing, they will be replaced in order by the values of the variable x (10) and the expression x*x (100). The final output will then be:

The value of x is 10 and its power of 2 is 100

The % symbol indicates the start of a placeholder in the format. The number of placeholders in the format must match exactly the number of variables and expressions that follow the format. In this case we had two placeholders, so we have two things to print, separated by commas: the variable x and the expression x*x. The letter d in the placeholder is used to indicate that the values to be printed should be integer values. Different data types may require different placeholders. Here are the most used:

Placeholders

Placeholder Character

Data Type

d

signed integer values (whole numbers)

u

unsigned integer values (whole numbers)

ld

signed long integer values (whole numbers)

lu

unsigned long integer values (whole numbers)

f

decimal values

lf

long decimal values (doubles)

e

decimal values to be printed in scientific notation

c

single character

s

string, a set of multiple characters

%

used if one requires to print the % symbol in the format

 

In between the % symbol and the placeholder character we can add optional flags. These are some possible flags to be used:

Flags

Flag

Description

-

Used to left aligned the value printed

+

Used only on numbers to indicate they always will be printed with a sign

space

Used only on numbers to print a blank space in front of positive numbers

0

Used to add padding zeroes in front of a value up to a requested size

 

After the flags, and optional number could also be added to the placeholder to indicate the minimum number of characters required to print the variable. If the value requires more characters than the minimum, this number will be ignored, but if it requires less, the remaining spaces will be filled with blank spaces or padding zeroes (if requested with the 0 flag). When the placeholder is for a decimal number, the number may be followed by a dot and the number of decimal positions we wish to display from the variable. Therefore, a number like 10.5 would indicate that we want the number to be given a minimum of 10 places, of which 5 will be used for decimal numbers. The decimal point is not considered as part of the 5 decimal places, so a number like 10.5 will only have 4 places for its integer part. If the number indeed needs more, the minimum size requirement will not be considered. The following table shows the numbers 123, -123, 3.21 and -3.21 printed using various formats. Be aware that the square brackets are not part of the placeholder, but they were just added to show the sizes occupied by the placeholders.

Examples of Integer Placeholders

Examples of Integer Placeholder (d)

Placeholder format

Result Printed

Description

[%d]

[123]

Integer number 123 is printed in free format

[%10d]

[                123]

Integer number 123 is printed over a 10-character size

[%1d]

[123]

Integer number 123 is printed in free format because it cannot be printed on the requested character size of 1

[%010d]

[0000000123]

Integer number 123 is printed over a 10-character size with padding zeroes

[%-010d]

[123                ]

Integer number 123 is printed left-aligned over a 10-character size

[%d] [%d]

[123] [-123]

Integer numbers 123 and -123 are printed in free format

[%+d][%+d]

[+123] [-123]

Integer numbers 123 and -123 are printed with their signs

[% d] [% d]

[  123] [-123]

Integer number 123 is printed with blank space in place of its sign

Examples of Decimal Placeholder (f)

Placeholder format

Result Printed

Description

[%f]

[3.210000]

Decimal number 3.21 is printed in free format

[%10.2f]

[             3.21]

Decimal number 3.21 is printed over a 10-character size with 2 decimal places

[%1.2f]

[3.21]

Decimal number 3.21 is printed in free format size with 2 decimal places because it cannot be printed on the requested character size of 1

[%010.2f]

[0000003.21]

Decimal number 3.21 is printed over a 10-character size with 2 decimal places and padding zeroes

[%-010.2f]

[3.21              ]

Decimal number 3.21 is printed left-aligned over a 10-character size with 2 decimal places

[%f\n%f]

[3.210000]

[-3.210000]

Decimal numbers 3.21 and -3.21 are printed in free format in different lines

[%+f\n%+f]

[+3.210000]

[-3.210000]

Decimal numbers 3.21 and -3.21 are printed in free format in different lines with their signs

[% f \n% f]

[ 3.210000]

[-3.210000]

In contrast to previous example, the decimal number 3.21 is printed with blank space in place of its sign

 

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205384/download?verifier=ol4jloaJdlM7oytdotmIa0Uy4Ei3rTCqwv1Ao4V3&wrap=1] EPrintFormats.cpp that created the results in the previous table.

 

Read More

Read more about printf in section 1.2 and Appendices B1.2 & B1.3 of the textbook.

Input for a process could be hard coded in a program, meaning that a variable can be set with a value to hold the input. This may be appropriate for values that may change little from program run to run, but not for all inputs, because it defeats the purpose of a program. A program is created to be run many times with different inputs to obtain different outputs. It is not practical to have to change the actual program, recompile and run for every set of inputs. It is better to obtain the input either directly from the user or from some file. We will discuss the topic of files later in the course, so here we will focus on direct user interaction.

In C, the same library that contains printf, stdio.h, has also the function scanf to obtain input from the keyboard. Its philosophy is similar to printf.  The scanf function takes as input a string that describes the format we will use to receive values, followed by the addresses of the variables for which we want to get a value.  For example, the following lines will request from the user a value for the variable x:

int x;
printf("Please enter an integer value for the variable x:");
scanf("%d", &x);

Considering that the program is interacting with a human user to obtain a value, before every scanf statement there should always be a print statement that indicates the user the kind of value the program expects. Otherwise the user may never know that the program is even expecting a value, and what type of value it should be. The scanf command waits from the keyboard for values that follow the format it contains. This format follows the same rules as the format in printf commands. In the example above, the format expects an integer value, represented by the %d format. After the user keys in an integer value, it is stored in the variable x. Notice that there is an ampersand before the name of the variable (&). This represents the address of the variable x in RAM, and is needed for the scanf command to be able to modify the contents of the variable. We will learn more about this operator in future classes. At this point just remember to add the ampersand before every numeric variable to be input with the scanf command.

If the user enters a value of a different type as the expected, the program will crash and stop. This will also happen if the ampersand symbol is not present. The program may compile, but it will crash while running.

It is possible to read more than one value with the same scanf command. It will be a matter of including formats for all variables to be read, but this is not advisable for user interaction. It is less confusing for the user to provide values for variables individually.

So far, we only have talked about obtaining input that is numeric, later in the course we will talk about using character and strings as input.

A note on using scanf in Microsoft Visual Studio: If trying to compile a program containing the scanf in Microsoft Visual Studio, the compiler may throw a warning (and an error) indicating that scanf is obsolete and it would be best to use the function scanf_s instead. This is a version of scanf specific for Microsoft. There are various ways to deal with this issue, but for the time being, you may replace scanf with scanf_s and your program should compile. Another alternative is to modify the option that treats warnings (minor mistakes) as errors (major mistakes) in Microsoft Visual Studio. You may find how to change this option in the document “Lecture: How to Use Visual Studio 2017 for C/C++”.

 

 

Comments and Indentation

A practice that will add readability to any program is the addition of comments for the human reader. Compilers need not such comments. They will ignore any text inside a comment. However, users reviewing the program may need some extra guidance that the comments can provide.

Comments can be added to C/C++ in two ways. The first way is using double slash symbols (//). These symbols indicate that any text appearing to their right and up to the end of the line should be considered a comment, and not a part of the program itself. For example, the following comments are describing the purposes of their respective variables:

int numberOfGuests;  // Number of guests invited to the wedding
float costPerGuest; // Cost of a guest in USD

 

Describing every variable in a program with a comment next to its declaration is one of the most important comments to have in any program, since a reader trying to find out the meaning of a variable will look for its declaration.

The second way to add comments to a C/C++ program is by surrounding it with the delimiters /* and */. This is usually done when the comment requires more than one line. For example, the following is a heading comment that was added at the beginning of the HelloWorld program (lines 2 thru 7):

 1: #include <stdio.h>
 2: /****************************************
 3: * HelloWorld.cpp
 4: * Author: <put author’s name here>
 5: *
 6: * This program says "hello" to the world.
 7: ****************************************/
 8:
 9: int main() {
10:   printf("Hello World!\n");
11:   return 0;
12: } // end of main

 

A heading comment helps anyone reading the code to identify the program and its purpose. Every program should start with such a heading comment indicating the name of the program, the author’s name, maybe a program version, and a brief description of what the program does. Later in the course, we will see programs that contain multiple functions, more than just the main function. A heading comment will be required for each one of these functions to explain their individual purpose.

The last line in the program above (line 12) ends the main function with the ending curly bracket (}). The rest of that line contains a comment started by the double slash (//) that pinpoints the end of the function. In a small program, like HelloWorld, such comment may not be necessary, but in larger programs involving many structures that contain curly brackets, it will be helpful to comment their ending, to be able to identify them at a glance.

Besides helping with readability, comments are very useful when debugging programs, especially when trying to find problems on programs that compile, but are not producing the expected results. In those cases, we may comment sections of a program and analyze how the program responds. By commenting a program section, it is taken out of the compilation, as if it were not part of the program, but it is not deleted. This is called commenting out a section of a program. 

Another important practice that improves readability of programs is a consistent use of indentation. Lines of code that are to be performed sequentially (one after another) should have their beginnings vertically aligned with each other. Generally, all these lines are bundled together in between curly brackets ({}). Therefore, the golden rule of indentation is as follows: indent every line that appears after the beginning of a curly bracket ({), and indent back only when the corresponding end of curly bracket (}) appears. For example, in the HelloWorld program in this section, all lines were aligned on column 1 until line 9, where the first begin of curly bracket appears. Because of this symbol, lines 10 and 11 are indented, indicating they belong to the function. Line 12 contains the end of the curly bracket, indicating the end of the main function, and therefore it is aligned back to column 1. Any sentence that may follow would have to be aligned again on line 1 until a new begin of curly bracket appears. We will use heavy indentation in the next unit when dealing with control structures.  

 

Practical Example

We covered a lot of topics in this unit, let us put them in practice with a concrete example. The task will be to write a program to evaluate gas consumption in a car and make some predictions using the values obtained.

Suppose you fill up your tank every time you go to the station, and you tend to fill it up only when the car tells you that you are nearing empty. You remember the mileage the last time you filled your tank (let us call this value oldMileage), and how many days ago you did it (a value we will call daysAgo). Now that you are filling the tank up again, you write down the following information: the current mileage (let us call it currentMileage), the number of gallons you are filling up now (to be called gallons) and the total price you paid at the pump (to be called price). With this data, we know one can obtain the following information:

The miles traveled per gallon (or mpg) will be the mile difference divided by the number of gallons: mpg = (currentMileage – oldMileage) / gallons.

The cost per mile (or usdPerMile) will be approximately the total price paid by the number of miles traveled:  usdPerMile = price / (currentMileage – oldMileage).

If you continue using the car in the same way you have used it lately, one could predict the number of days it will take to reach the next 10,000 miles (or daysToMore10K) with the division of 10,000 by the mile difference and multiplying this ratio by the number of days since last fill up: daysToMore10K = (10000/(currentMileage-OldMileage)) * daysAgo.

With the number of days to reach the next 10,000 miles, we can also obtain the number of weeks it will take to reach the same goal (or weeksToMore10K) with a division by 7: weeksToMore10K = daysToMore10K / 7. Since a year has approximately 52 weeks, we can also obtain the years to this goal by further dividing by 52.

Using the same rational, one can predict how much money one will spend on gasoline in the next 10,000 miles (or priceToMore10k): priceToMore10K = (10000/(CurrentMileage-oldMileage)) * price.

With the previous description, the first we need to do is to recognize the input and output in the program. The input will be all the values that a user must provide to perform all these calculations. The user will provide these values once, and the program will use these values as many times as it need them. Based on the calculations described in the narrative above, it should be clear that all the input we need from the user to perform all calculations are the values for the following variable: oldMileage, daysAgo, currentMileage, gallons, and price. Notice how giving names to concepts, help to define variables in our program and simplify their treatment.

The output of the program will obviously be the results of the requested formulas: mpg, usdPerMile, daysToMore10K, weeksToMore10K, (maybe yearsToMore10K too), and priceToMore10K. Here again, having the names for the concepts simplifies the problem.

Once input and output are spotted, we need to decide the data types for each one of them. As a general rule, in C/C++ variables that may never contain decimal numbers should be declared as int, and variables with decimal values should be declared as float. Decimal variables that we know may became extremely large or extremely small in absolute value may need to be declared to be double, but in this problem, this will not be the case.

This is one way in which one can think about the data types for the variables in this problem: if one notices it, variables that relate to the number of days, weeks or years will never be given or used as decimal numbers. If somebody is asked about “How many days ago did you fill up the tank?” one rarely will say 3 days and a quarter. The same should happen with variables that relate to mileage requested. So we can safely realize that the variables daysAgo, daysToMore10K, weeksToMore10K, yearsToMore10K, oldMileage and currentMileage should be declared int. All other variables may take decimals (review this for yourself), and should be declared float. 

Writing a C/C++ program for this problem will now follow straightforward steps: writing the skeleton for the main function; then, inside main, declare variables, write sentences to request user input, write assignment sentences to calculate the output, and print this output with appropriate labels (input, process and output).

Our first step is to write the skeleton of the program. We know we need a main function so we write:

int main() {
}

The program will read the variables from the user, so we best include the I/O libraries. This is the stdio.h C library:

#include <stdio.h>
int main() {
}

It is best to write the heading comment at this stage. Otherwise we will forget when we finish and we are already tired of the program. Something like this will do:

 #include <stdio.h>
/*
   Program Name: PracticalExample.cpp
   Author: <Your name here>
   This program calculates simple statistical values
   for a car usage and makes predictions for the next
   10,000 miles based on these stats.
*/
int main() {
}

 

Now, inside main, we declare variables as previously planned, and include comments to describe the variables, like shown below (comments were cut in this text for brevity see full comments in the attached program):

int oldMileage;          // Old mileage
int currentMileage;      // Current mileage
int daysAgo;             // Number of days since last fill-up
int daysToMore10K;       // Number of estimated days . . .
int weeksToMore10K;      // Number of estimated weeks . . .
int yearsToMore10K;      // Number of estimated years . . .

float gallons;           // Price paid for the current fill-up in USD
float price;             // Price paid for the current fill-up in USD
float mpg;               // Miles per gallons since last fill-up
float usdPerMile;        // USD per mile covered since last fill-up
float priceToMore10K;    // Estimated USDs to reach . . .

With the variables declared, we must read the input using printf statements to explain the user the kind of values expected, and scanf to read them appropriately. For example, to read the integer daysAgo variable we could use:

printf("How many days ago did you fill your car's tank? \n");
scanf_s("%d", &daysAgo);

For a float variable like the number of gallons we may use:

printf("How many gallons did you take in this refilling? \n");
scanf_s("%f", &gallons);

Once all input is read we could proceed to perform the calculations and store their results on the output variables. If one aims to write an efficient code, one could observe that the given equations have certain sections that repeat. In particular, the difference in mileage and the division of 10,000 by this difference. Rather than calculating these values over and over again in each equation, we could create auxiliary variables to hold these values and use them in formulas. The following can be declared:

float mileDifference;    // Miles covered since last fill-up
float milesRatio;        // Ratio of 10000 over mileDifference

 

And they can be calculated as follows:

mileDifference = currentMileage - oldMileage;
milesRatio = 10000.0 / mileDifference;

Notice that, even though currentMileage and oldMileage are integer, their difference was declared as float. This was done because the equations that use this difference will calculate decimal values. We could leave each equation to deal with this issue, but having the difference as a float, makes uniform the treatment of these calculations.

With the new variables calculated we can proceed to calculate the other formulas:

mpg = mileDifference / gallons;
usdPerMile = price / mileDifference;
daysToMore10K = (int) (milesRatio * daysAgo);
weeksToMore10K = daysToMore10K / 7 ;
yearsToMore10K = weeksToMore10K / 24 ;
priceToMore10K = milesRatio * price;

Notice how the variables mileDifference and milesRatio are reused. Notice also the use of type casting to obtain an integer value for the variable daysToMore10K in the third line. The divisions that follow these line are both integer divisions, since their operands are both integer.

The final step is to print the results with appropriate labels. For example, the miles per gallon could be presented as follows:

printf("The current miles per gallon are %.2f\n", mpg);

There are other ways to present results that are more direct, like tables, but this is the best we can do with what we have learn so far.

One final improvement: although there is nothing wrong with using numbers inside a program, it is a good practice to store these numbers in declared constants. The program will use these constants instead of the direct numbers. For example, rather than using the 10000.00 number inside the program we can declare the following constant:

const float MILEAGE_GOAL = 10000.00;

And use this constant in all places needed, like:

milesRatio = MILEAGE_GOAL / mileDifference;

The advantage of this practice is that if later on we want to modify the goal to 100,000.0, we do not have to search the whole program for proper instances where this number was used, and change them one by one. Instead, we only need to change the value of the constant once.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205386/download?verifier=ivXsBoXbLv9JBHP1TPcGrqsYbhPtUGrnyyJGxYeO&wrap=1] FPracticalExample.cpp that contains the complete code for this exercise.

 

Review the Code

For a complementary view of the topics in this lecture:

Read more in sections 1.1 thru 1.5, and 2.1 thru 2.5 of the textbook.

 

 

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
