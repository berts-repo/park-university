# Unit 5: Lecture - Functions

Until now, all programs we have used in this course had declared only one function: main.  In this unit we will review how to declare, how to implement, and how to use more than one function in C/C++.

As with other units, to highlight the main security points, in this document you will see paragraphs prefaced by the initials SPR. They indicate an important Secure Programming Rule that you must keep in mind when programming. This will be particularly important when a code and a number follows the initials SPR. They are the code and number assigned to this recommendation by the Software Engineering Institute at Carnegie Mellon University, a source of authoritative information on the discipline ( [link: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard] SEI CERT Coding STandard). You will also be directed to more information from the textbook and course material in paragraphs marked as Read more. References to companion C/C++ programs will also be prefaced by: “You may review the attached program(s).”

 

 [link: #fragment-1] Why Functions

 [link: #fragment-2] Defining Functions

 [link: #fragment-3] Passing Parameters to Functions

 [link: #fragment-4] Compiling Programs with Multiple Functions

 [link: #fragment-5] Scope and Lifetime

 [link: #fragment-6] Overloaded Functions

 [link: #fragment-7] The stdlib.h Library

Why Functions

Even though we have only written one function per program in previous units, main, we have described and used many functions provided by the language: printf, scanf, the math functions, the string functions, etc. Functions allow the packaging of the solution to a small problem into a unit that can be called at will. For example, the printf function is a solution to the problem of printing and we call it every time we want the program to print something. Similarly, the strcpy function is a solution to the problem of copying a string and we call it any time we need to do so, instead of writing a program to copy the string ourselves. Rather than trying to solve each and every single issue that writing a program requires, we rely in functions to help us solve small issues within the program, and we organize the completed solution by calling these functions when appropriate.

For example, assume you have a collection of grades from various courses and students. You may want to obtain the average grade, the maximum, and the minimum of these grades per course. You could write a solution to this problem using a program with only one main function, but this function may contain a lot of repeated structures. For instance, once all grades of a course have been identified, and probably stored in an array, there will probably be a loop to add all these grades to calculate the average, possibly another loop to calculate the largest grade, and maybe another one to calculate the smallest value. Keep in mind that these loops will have to be repeated for each of the courses that we are processing. If we use functions instead, we could create a function to calculate the average, another to calculate the maximum, and another to calculate the minimum. These functions will be called once for each of the courses. We only write the functions once, but we can call them (use them) many times. This is known as the “Divide and Conquer” approach to solve a problem: we identify smaller sub-problems within the general one, and we solve those. Then, we organize these solutions in a manner that satisfy the overall problem.

Defining Functions

A function is a set of instructions clearly separated from all other functions or instructions in a program. Each function is like a mini-program. Like every program, each function requires a well-defined input, has its own instructions, and produces a well-defined output.

Anyone with access to a function may use a function by calling it with its name and passing some information the function may require. This is also known as invoking the function. When this is done, the function will execute the instructions it contains in order (from top to bottom) and at the end it may return something to whoever called the function in first place. However, before a function may be called, it must be completely defined. This is done in a similar way as the main function is defined. A generic syntax to define a function is as follows:

output-type function-name (parameter list) {
          set-of-ordered-valid-sentences
}

where:

function-name is the given name for the function, and the one used to call it when is needed.

output-type is whatever the function will produce after it finished performing its instructions. This could be any type of variable, or it could return nothing with the void keyword.

parameter-list, also known as argument-list, it is a list of comma-separated input variables for the function. Each input variable is declared in this list by identifying its data type and given it a name to be used inside the function. More than one variable in the input should be separated by commas.  For example, a list like  (int myInt, float myFloat) indicates that the function expects two variables, an integer and a float numbers in that order, to be called  myInt and  myFloat inside the function.

set-of-ordered-valid-sentences these are the instructions inside the program. A function may use any correct C/C++ command, and it may call any previously declared function, either from the language or within the program. At some point in the instructions, if the function has an output-type other than void, the function must return a value, variable or expression of that given data type with a return command.

{ } Curly brackets are used to indicate the limits of the function. It separates the instructions inside the function from the rest of the program.

We present the function named  maximum as an example of a function definition:

double maximum(double a, double b, double c) {
     if (a>b) {
          if (a>c) {return a;}
          else {return c;}

     }

     else {
          if (b>c) {return b;}
          else {return c;}

     }
}

The function-name is  maximum. This function requires as input three  double numbers that are going to be called a, b and c, respectively, inside the function. These are indicated in the parameter-list in between parentheses. The output-type of this function is also a double number, indicated by the first word  double before the function-name. This means that once the function ends with calculations, it will return a  double value. This can be seen throughout the program with the various  return commands. After deciding which  double variable contains the largest value, these commands return it.

Once the function is defined, a program may call it whenever is needed, by calling its name, giving an appropriate parameter list and expecting the result back. The following lines show examples of possible calls to the maximum function:

double w = 29.19, x = 23.45, y = 17.17, z=38.21;
double s =  maximum(y, z, x);
double t =  maximum(w, s, s);
printf(“The maximum of %f, %f, and %f is %f\n”,x, y, z, s);
printf(“The maximum of %f, and %f is %f\n”,
                                     w, y, maximum(w,y,w));
printf(“The maximum of all numbers above is %f\n”,t);
printf(“The maximum of 7.3, 2.1, and 6.5 is %f\n”,
                                   maximum(7.3, 2.1, 6.5));

This will produce an output similar to the following:

The maximum of 23.45000, 17.17000, and 38.21000 is 38.21000
The maximum of 29.19000, and 17.17000 is 29.19000
The maximum of all numbers above is 38.21000
The maximum of 7.3, 2.1, and 6.5 is 7.3000

Notice that the program calls the maximum functions with various kinds of variables and numbers. As long as the maximum function receives 3 double numbers, it will not complain and it will return the maximum of the three values. Notice also that program receives the result of the calls to minimum in two different ways: it either stores the value in a variable for further use (like in variables s and t), or it uses it right away, as when the returned number is printed in the last sentences. This shows that a function call can be placed anywhere its returned output-type is used. In the last sentence, maximum is placed in the printf statement where a double data type was expected.   

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205281/download?verifier=VIK4SIWquiXRGL674E6pfo7HI49QOa1wT1VeA71e&wrap=1] AMaximum.cpp, which contains this example.

Passing Parameters to Functions

We have seen that when a function is defined, the parameter-list declares all the input variables it will use. However, when we call the function, we can pass any set of values, variables or expressions we want, as long as they are of the data type that the function expects, and in the same order. This is possible, because when the function is called, and before it runs, the operating system copies the values being submitted onto the input variables. This is what is called pass-by-value.  For example, the maximum function described before was declared as follows:

double maximum(double a, double b, double c)

One of the calls to this the function was:

double s =  maximum(y, z, x);

When the call was made, the values of the variables y, z, and x where copied respectively onto the variables a, b and c in the function. The copies are absolutely independent of the original variables. This means that the values on the copies can be modified, but they will not affect the values on the original variables y, z, and x, whatsoever. When the function ends processing, all values of all its variables are discarded, a, b and c included. That is why, in many functions, we may want to retrieve a final result with the return command, otherwise it will be lost, together with all other values of variables in the function.

The variables a, b and c declared in the function header are called the formal arguments, because they formally represent some input the function needs. On the other hand, values, variables, or expressions that are passed to a function, like y, z, and x, are called the actual arguments, because they hold the actual values that will be given as input to the function. In C/C++ actual parameters are copied onto the formal arguments, so as a general rule, all input for a function is passed-by-value, but as we will soon see, this general rule has its caveats.

Functions may receive any kind of data type in their parameter-list, consequently, not only numeric data types can be submitted to functions but also, characters, arrays and strings.   The following example shows a program that uses the function maxInArray to find the largest element in an array of doubles.  Notice that the function must declare the array in the parameter list without any size specification. This is an important issue. Functions do not know the size of arrays beforehand. They can calculate it, as we will see later on, but if the array is not completely filled with information, the total number of active array elements should also be submitted to the function in a separated variable, as shown:

#include <stdio.h>
#define ELEMENTS 20
double maxInArray(double array[], int size) {
  double max = array[0];   
  for (int i=1;i<size;i++) {
     if (max<array[i]) { max = array[i]; }
  }
  return max;
}
int main() {
  double a[ELEMENTS] = { 23.5, 72.89, 12.26, 54.93, 33.15,
                         97.34, 87.84, 7.65, 64.45, 42.11};

  int realSize = 10;
  printf("Largest value=%f\n" , maxInArray(a, realSize));
}  

Even though C/C++ uses pass-by-value to transfer input values to a function, the values of the elements of an array are not individually copied to a function. Instead, the actual elements themselves are available to the function for calculations. For example, the following function receives an array of doubles and changes its values by multiplying them with two:

void byTwo(double array[], int size) {
     for (int i = 0; i<size; i++) { array[i] *= 2.0; }
     return;
}

And it could be executed with the following call from main:

byTwo(a, ELEMENTS);

After this function call, the values of array a will be doubled in the main function. This appear to be a contradiction on what we mentioned before. We indicated that values passed to a function are copied, and that these copies are independent of the original values. With the byTwo function, it appears that the array a itself was submitted to the function, that it used the array name as a disguise in the byTwo function, that it modified the values of its elements, and that it returned to main with the values changed. This is in fact what was happened, and this behavior is known as pass-by-reference. Rather than copying all elements of the array (as in pass-by-value), only a reference to the array in main was passed. The byTwo function then has complete access to the elements of the array. C/C++ does this, because it would be too costly to copy all elements of an array every time it is submitted to a function. It would take too much time, use a lot of resources, and the operating system does not even know what the size of the array is. The programmer is the only one who knows how long the array is. C/C++ uses pass-by–value when transfer data types with smaller, well-known size. On the other hand, it uses pass-by-reference when passing large objects, or objects of unknown size, like arrays.

The reality behind this behavior is that when passing an array, the reference we are passing is the actual address in memory (RAM) where the first element of the array is located. We mentioned in a previous unit that this is a called a pointer. It points to the array by holding the value of the RAM address where it is located. The programmer does not need to see or know the value of this address. It only needs to know that it leads to the place where information is to be found. When passing an array to a function we are passing the array by-reference, but the reference itself is being passed-by-value. It is the pointer to the array that is actually copied to the function. We can change the value of this pointer inside the function, but it will not affect its original value in the function that calls it.

Because of this behavior, when declaring an array as part of a parameter-list in a function, one can also declare it as a pointer. A pointer is declared using the asterisk (*) after the data-type of the variable is pointing at. For example, the following declares pointers to int and double variables:

int* iPointer;
double* dPointer;

Notice that a pointer to a data type is in itself a data type, that is different to pointers to other kinds of data types. Namely, a pointer to an integer variable is of a different type from a pointer to a double variable.

We can use the notation above when declaring an array inside a parameter-list for a function. The following function, minInArray, uses this notation to declare an array of doubles as input. The function will find the smallest element of the array:

double minInArray(double* array, int size) {
     double min = array[0];  
     for (int i = 1; i<size; i++) {
          if (min>array[i]) { min = array[i]; }

     }
     return min;
}

Notice that the array is declared as a pointer to double (double*). This pointer is passed-by-value, but it provides complete access to the array. Inside the function, the array is treated like any other array we have seen before.

Review the Code

You may review the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205284/download?verifier=mXpVPg9cewDPMVqCo8xHyeF2ElyAnmG8FsETadGo&wrap=1] BPassingArrays.cpp and  [link: https://canvas.park.edu/courses/62124/files/8205066/download?verifier=sXS2RJbXAA51n34sNHcmi6QXAa1B6WfaMxksGis4&wrap=1] BPassingArraysWithoutSize.cpp. The first one contains the methods to pass arrays described above. The second one is a variation of the first one in which the number of elements on the array is calculated using the following expression:

int size = sizeof(array) / sizeof(array[0]);

As we have seen in programs in unit 1, sizeof is a C/C++ operator that produces the number of bytes used by a given variable or data type.  The expression above allows the calculation of the number of elements of an array when dividing the total number of bytes used in the array by the number of bytes used in a single element. This expression can be used in calculations, when a function is guaranteed that all array elements contain useful information.

Single characters are easy to pass to functions. They just need to be declared as char in the parameter-list. Strings, on the other hand are arrays, and may be declared in a function’s parameter-list using the two methods described above for passing arrays. The following example shows two functions that receive characters and arrays:

int replace(char c, char* s) {
   int vowelsChanged = 0;
   if (s!=NULL) {
     for (size_t i=0; i<strlen(s);i++) {
       if (s[i]=='a'||s[i]=='A'||s[i]=='e'||s[i]=='E'||
           s[i]=='i'||s[i]=='I'||s[i]=='o'||s[i]=='O'||
           s[i]=='u'||s[i]=='U') {
            s[i] = c;
            vowelsChanged++;
       }
     }
   }
   return vowelsChanged;
}
void nullify(char s[]) {
     if (s != NULL) { s[0] = '\0'; }
}

The function replace receives a single character c and the string S declared as a pointer to char. This function will replace all vowels in string s with the character c. The function nullify receives a string as an array and converts into the empty string if not null. Inside both functions, the string is treated as an array, but notice that there is no need to transfer the length of the array, since properly constructed strings are expected to end with the null character ‘\0’.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205274/download?verifier=SlxkulxoPhfmCe0f3gDezcSXlqmWl1FnwiiFylUa&wrap=1] CPassingCharAndStrings.cpp, which contains these methods.

Pointers are a very important and powerful structures in C/C++, and the source of many security issues, so they will be studied in detail in the next course unit.

Compiling Programs with Multiple Functions

To compile C/C++ programs, the cardinal rule is that no part of the code may make reference to anything that was not previously declared. We know, for example, that a variable cannot be used if it has not previously declared.  We also know that we need to initialize a variable before we use it, but it cannot be initialized, unless it has been previously declared. The same happens with functions. A function has to be previously declared for a program to call it. This means that all functions that are going to be called need to be declared before any other function that is bound to call them, in particular the main function. Since the main function is the starter of any application, in theory, the main function should be declared last. We will see in this section how this may change, but to illustrate how functions should be declared in a single C/C++ file for successful compilation we will use an example inspired on the polish calculator, described in sections 4.3 thru 4.4 of the textbook.

The polish calculator is a program that calculates basic operations (+, -, * and /) applied on numbers that are written in polish notation. Polish notation performs the operations on previously defined operands. For example if we want to calculate (2+3), we need to indicate first the operands (2 and 3) and then indicate the operation (+). This operation in polish notation is so expressed as follows: 2 3 +. The result will still be 5 in any format. The textbook also shows the following expression (1 -2) * (4 + 5) in polish notation as 1 2 – 4 5 + * with a result of -9.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205302/download?verifier=hePM1pbccqOHbHFVOpnFGs1UPdRkTRKiUPEu5Tx2&wrap=1] DPolishCalculatorV1.cpp, which contains a version of the polish calculator in one single file. If we compile and run this program, a command line will appear expecting the user to enter an expression in polish notation in one line. If we enter one of the expressions above and we press enter, the result will show up in the following line. The program will continue to wait for polish expressions until the buttons Ctrl-Z are pressed together. This produces the EOF (end of file) character that will stop the program.

This program has five functions: push, pop, getch, cungetch, getop, and main. Notice that they are declared in the program in the order that will allow compilation. The functions push and pop are described first. They are going to be called by the main function, declared at the end of the file. The functions getch and ungetch are described after the function pop. They are going to be called by the function getop that is declared after them. In turn, the function getop itself will be also called by the main method declared at the end, as previously indicated.   

All constants are also declared at the beginning of the program, so all functions may use these values if needed. Notice also that there are certain variables that were declared outside any functions, these are known as global variables, since they do not belong to any specific function. By contrast, variables declared inside functions are known as local variables. Global variables may hold their values throughout the run of the program. Local variables only hold their values while the function where they are declared is actively running with a function call.  Once global variables are declared, they are available to all functions declared below them. In the example, the variables sp and val, are global variables required and used by the push and pop functions. By declaring the variables above and outside these functions, both functions have access to the same variables and can use them at will, knowing they will hold their values between function calls. The same is happening with the variables buf and bufp declared before the functions getch and ungetch. Both of these functions can use these variables at will and they will retain their values between functions calls.

Having to declare functions that are being called before the functions that call them may be a complicated task that gets harder as the number of functions increases in an application. Therefore, C/C++ makes a distinction between declaring a function and defining a function. Declaring a function just proclaims that a function exists. This proclamation can be performed by writing what is known as a function prototype. The function prototype is the function header that states the output-type, the name, and the parameters-list of the function followed by a semicolon (;). For example, the following are the function prototypes for the functions push and pop in DPolishCalculatorV1.cpp:

void push (double);
double pop(void);

On the other hand, defining a function is implementing the whole function, by writing its function header followed by its contents inside curly brackets, namely, writing all the instructions for the function. The difference between declaring and defining a function is the same as declaring and defining a variable. The declaration of the variable only declares its existence, while defining a variable requires to declare and initialize it. Because it is possible to separate declaration from definition in a function, we can now declare all functions needed at the beginning of a C/C++ file using function prototypes, and define them later in any order we want.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205058/download?verifier=ibPdhYL0QBNf1C2VgldGP7GdRl0llzu1r3xmKM8P&wrap=1] EPolishCalculatorV2.cpp, which contains a version of the polish calculator in one single file using prototypes. This version declares prototypes for all functions in the file, except main, right at the beginning, after the declaration of all constant macros. Because all functions are so declared, this file can then define the main function followed by the definitions of all other functions in any order: getop, getch, ungetch, push, and pop. The global variables are also defined later, just before the definition of functions that need them.

When programs start to grow and contain many constant macros, global variables, and functions, it is customary to break them in sections, each one in different files. The first and much easier breakage of a single C/C++ file is the creation of a header file (.hpp)  from the original C/C++ file (.cpp). A header file usually contains declarations of structures that are of interest to the files that will use the header file. These declarations may contain constant macros, #include pre-processor commands, global variables, and other definitions, some of which we will review in future units, and others which involve C++ constructs that will not be discussed in this course. While header files may actually contain any C/C++ construct we want, they usually do not contain function definitions, only declarations with prototypes. Header files usually use .hpp as their suffix for the file type in their file names. Once a header file is created, other C++ files may include it, in the same manner they include C/C++ libraries with the #include pre-processor command.

Review the Code

You may review the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205060/download?verifier=HHrNZHEhlOAN0LALlcrTtECw97cSenjbmKufgPyd&wrap=1] FPolishCalculatorV3.hpp and  [link: https://canvas.park.edu/courses/62124/files/8205059/download?verifier=6lvafc7rD4LFrs9YIowqR45e1WcW11Frfa3MQqzC&wrap=1] FPolishCalculatorV3.cpp, which contain a version of the polish calculator that uses a header file. To compile this program, both files should be included in the Microsoft Visual Studio project. The .hpp file as a header file, and the .cpp file as a source file.  Notice that the .hpp file contains all include statements, all constant macros and all function prototypes previously displayed in the EPolishCalculatorV2.cpp program. On the other hand, the .cpp source file only contains the function definitions, with their global variables, and the following sentence at the beginning of the file:

#include "FPolishCalculatorV3.hpp"

This sentence includes the contents of the header file before the contents of the source file while pre-processing. Because it is located at the beginning of the file, all contents of the header file will be compiled first before the contents of the .cpp source file.

Having a header file is not the only way to break a single C/C++ program in sections. We may want to break the program in separate files, each one with a set of functions that are logically related, but independent of the other sections.  The polish calculator presented in the textbook is broken in this fashion and we present it here as our last version of the polish calculator.

Review the Code

You may review the programs inside the GPolishCalculatorV4 folder, which contains a header file ( [link: https://canvas.park.edu/courses/62124/files/8205067/download?verifier=cwSRUTHWMUydM2jO9jhFjC3BWyDSUgq0BnCVBDRI&wrap=1] calc.hpp) and 4 .cpp files ( [link: https://canvas.park.edu/courses/62124/files/8205055/download?verifier=3P0op6qJZW8K6bzCBCnhQtFhYqgYM9X2hjTn0uCy&wrap=1] getch.cpp,  [link: https://canvas.park.edu/courses/62124/files/8205063/download?verifier=pM2hZjs8TTMuemk7OmCIhoPEKuiaScNPiL09UabS&wrap=1] getop.cpp,  [link: https://canvas.park.edu/courses/62124/files/8205277/download?verifier=wIXnZe1twpqvKRG0HvJ754F4yJN8JGSjlwSANaFe&wrap=1] stack.cpp and  [link: https://canvas.park.edu/courses/62124/files/8205068/download?verifier=dNpfyJQDcYMm2ErZnjLHbS5JmO9OQb2lnvOWsMKY&wrap=1] main.cpp). These programs are the same ones described on the textbook. Each one of them contains logically related functions, their global variables, and the constant macros that are relevant to these functions.

The advantage of this arrangement is that global variables can only be seen and used by the functions that need them. In previous versions, some global variables may have been unnecessarily available to some functions. For example, in versions 2 and 3 of the polish calculator, the variables buf and bufp, that are used by the getch and ungetch functions, were also accessible by the pop and push functions because of the location of their definitions, even though access was not needed. This is a vulnerability that can be avoided by the partition of the program presented in the latest version. Here, both variables buf and bufp, are defined in the getch.cpp file, together with the functions that need them, and no more. Since the constant macro BUFSIZE is only needed by the variables and functions in this file, they were also included here.

At compilation time, Microsoft Visual Studio will direct the compiler to compile separately each individual .cpp file together with its attached header files. Each of these groups is known as a translation unit, and each one produces one object file after compilation. The object file contains the translation into the specific machine language for the platform of the C/C++ code in the translation unit. After all individual files are compiled successfully, Microsoft Visual Studio will put together all object files into an executable file with a process known as linking, where all references to external variables and functions are matched with their definitions. For example, the linking process will replace all calls to the push function made by the main function with the location where the push function is to be found in the object file from stack.cpp. In the past, compilation and linking have to be explicitly requested and monitored by programmers using the command line.  Microsoft Visual Studio makes this process easier, and somewhat transparent for the programmer with the selection of the Build Solution option.

Scope and Lifetime

Scope and Lifetime are attributes of variables and functions that we can only study now, having multiple functions in a program.

We already have seen scope, but we did not define it. The scope of a variable are all the places where the variable is visible within a program. In C/C++, a variable declared inside a function (or its parameter-list) is visible only inside that function. We knew these variables from previous sections as local variables. We can say that the scope of these local variables is the function where they are defined.

Some variables inside a function may have an even more restricted scope. For example, a variable declared inside a loop, like the counter i in the following loop, only has the loop as its scope, even though it may be inside a function:

 for (int i=0; i<10; i++) { printf(“%d ”,i) } 

The variable i cannot be used after the loop ends, because its scope is only the body of the loop.

We also saw that C/C++ variables can also be declared outside any function. We knew these variables as global variables. So far, we know that a global variable is visible from the moment is declared up to the end of the file. This is their scope.

When dealing with multiple files we may need to increase the scope of some global variables, to make them available to more than one file. This could be achieved by declaring these variables as external using the extern keyword, like in the following declaration and initialization:

extern int aExternVar = 123;  

To explain how external variables work, consider the following program made out of three files:

ExternA.cpp

 1: #include <stdio.h>
 2: extern int aExt = 10; //Definition of Global variable
 3: void funcA(void) {  aExt = 15; }
 4: void funcB(void) {
 5:  int aExt;           //Local variable
 6:  aExt = 98;
 7:  printf("Inside funcB aExt=%d\n", aExt);
 8: }

Extern.hpp

 1: #include <stdio.h>
 2: extern int aExt;     //Declaration of Global variable
 3: void funcA(void);    // Function prototypes
 4: void funcB(void);

ExternB.cpp

 1: #include "Extern.hpp"
 2: extern int aExt; // Unnecessary re-declare. Already declared in Extern.hpp
 3: int cExt =  70; //Global variable (just for main)
 4: int main(){
 5:   extern int aExt; //Re-declare of extern var. Unnecessary. Avoid.
 6:  printf("Initial external value aExt=%d\n", aExt);
 7:  aExt = 12;
 8:  printf("After modification in main aExt=%d\n",aExt);
 9:   funcA();
10:  printf("After modification in-funcA aExt=%d\n",aExt);
11:  funcB();
12:  printf("After NO mod. in-funcB aExt= %d\n,aExt);
13:  printf("Variable visible to main cExt=%d\n", cExt);
14:}

This program has the main function in file ExternB.cpp. This file includes the header file ExternB.hpp. Both files will be compiled together because they form one translation unit. A separate file named ExternA.cpp contains independent functions that will be called by main. This file alone forms a second translation unit. Because main will need access to the functions in ExternA.cpp, their prototypes are declared in the header file.  The variable aExt is defined (declared and initialized) in line 2 of ExternA.cpp. This is a global variable because it is declared outside any function, and therefore, visible up to the end of the file.  Every function in ExternA.cpp has access to it and they can modify it at will, as it is done in funcA at line 3. Now, because it was also declared as external, any other transactional unit may use it, as long as they also have it declared as external. The header file is doing that in its line 2. The ExternB.cpp file has access to this declaration because of its inclusion of the header file. We can also see that the variable aExt is re-declaring this variable twice: the first time before the main function in line 2 of ExternB.cpp, and the second time inside the main function in line 5 of the same file. Both of these re-declarations are allowed, but they are not necessary. One declaration per translation unit is enough. However, we do not see a re-initialization on any of these two declaration lines. This would be a re-definition of a variable and the program would not compile. Even though this variable cannot be initialized again, its value can still be changed as shown in line 6 of ExternB.cpp.

This example shows that external variables must be defined (declared and initialized) outside a function only once. They could be declared many more times inside or outside functions, but they cannot be initialized more than once, because this will mean we are defining the variable twice, and that is not allowed in C/C++. The external variable aExt was declared and initialized in line 2 of ExternA.cpp. There were multiple declarations and changes of value for this variable in the program, but there is no other definition of the variable (declaration and initialization in the same line).

Another global variable in this program is the variable cExt, declared in line 3 of ExternB.cpp. This variable is just visible in main , because it was declared right before main , and its scope is only from this declaration point until the end of the program. Attempts to use it in either funcA or funcB will produce a compilation error. They are not aware of its existence, because it is defined in another translation unit. If we want to grant access to this variable to funcA or funcB, we will need to do two things: declare this variable as external wherever is needed and make its definition (declaration and initialization) visible to all files that need it. Specifically, we may need to define (declare and initialize) this variable as external in ExternA.cpp and declare it as external in  ExternB.cpp without an initial value, as follows:

Add this line after line 2 in ExternA.cpp   : extern intcEXT = 70;
Add this line after line 2 in Extern.hpp      : extern int cExt;
Delete line 3 from ExternB.cpp                      :  intcExt = 70;

Finally, we should also notice that function funcB declares another aExt variable in line 5. This is a local variable. Although it has the same name as the external variable, it is not the same one. This local variable has a limited scope. It is only visible within funcB. Unfortunately, because it has the same name as the external variable, it “masks” (or “hides”) the external variable. This makes the external variable unreachable within this function, in fact, reducing its scope. 

Review the Code

You may review the programs inside the HExternSamples folder, which contains a header file ( [link: https://canvas.park.edu/courses/62124/files/8205069/download?verifier=u05T2hiBYpv4EeFAuEM8TRSzZOHGHayoVWKWU5c9&wrap=1] ExternSamples.hpp) and 2 .cpp files ( [link: https://canvas.park.edu/courses/62124/files/8205288/download?verifier=ctUNDrtdBcFIohelTG15HgjxPtchfkoXE70tmJWy&wrap=1] ExternSamplesA.cpp, and  [link: https://canvas.park.edu/courses/62124/files/8205295/download?verifier=kU1P1wnzeEaxKjEyqFT7nveO3HIOSJBAdBZeya3f&wrap=1] ExternSamplesB.cpp). They contain a similar example as the one we just described that uses external variables.

Lifetime is another variable’s attribute. The lifetime of a variable is the time that passes from when the variable is declared until it is discarded by the program. Usually, the lifetime of a local variable ends when the segment of code where it was declared finishes. In C/C++, a segment of code is limited by curly brackets. For example, a function is a segment of code. It is separated by curly brackets from other functions. A local variable declared inside a function (including the variables in the parameter-list) ends its lifetime when the function ends, after a return statement. In addition, a for-loop may also be a segment of code when it uses curly brackets to separate the actions of the loop from other commands. A variable declared inside such a for-loop does not end its lifetime when the function ends, but when the loop ends. This variable is discarded by the program after the loop finishes.

The lifetime of global and external variables begins when the variable is defined (declared and initialized) and ends when the program is no longer active. Some local variables may also be upgraded to have the same lifetime that global variables have, if they are declared as static. Static variables may be declared inside functions, but remain alive while the program is active and retain their values in between function calls. The following piece of code shows an example of the use of a static variable to keep track of the number of times a function was called:

void countUse(void) {
     static int timesUsed = 0;
     int localTimes = 0;
     timesUsed = timesUsed + 1;
     localTimes = localTimes + 1;
     printf("This function was used %d times.\n",timesUsed);
     printf("The value of localTimes is %d.\n",localTimes);
}

The variable timesUsed is declared as static and initialized at zero. If a static variable is not explicitly initialized, it will always be initialized with zero by the compiler. Suppose that a main function calls countUse five times. During the fifth call, the function will print that the value of variable timesUsed is 5, while the value of variable localTimes is 1. timesUsed remains alive and keep its value in between function calls. It will remain alive while the program is active. localTimes is created and destroyed with every function call.

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205292/download?verifier=OkPfsCFmFZnSPt3tIOOaNZw4nIqbknl7AcbSW06g&wrap=1]  IStaticSample.cpp, which contains another example of the use of a static variable.

Global variables may also be declared as static, but this is not necessary, since they already have a lifetime that spans the life of the program. In fact, programmers should pay attention not to have conflicting declarations of global and static variables. Variables declared as external should be declared as external in all translation units where they are used. Variables declared as static should only be declared in one translation unit. If they are meant to be visible by more than one translation unit, they should not be declared as static, but external. It is advisable not to declare as static any global variables. Contradicting declarations of static and global variables may lead to undefined results when linking the program, and they are discouraged by the following secure programming rule:   

SPR DCL36-C

Do not declare an identifier with conflicting linkage classifications.

The linkage classification refers to their status as external, global, or static variables.

Another secure programming rule is concerned with trying to access a variable beyond its lifetime. For example, the following function creates a local array of characters and tries to return it, using its address (char*):

char* badCreateArray(void) {
     char newArray[10] = "My array";
     return newArray;
}

When the function returns, the array is discarded, but a reference to its first position is sent back to whomever called the function as if it were a pointer to the array. Unfortunately, because the array was discarded, the results are undefined.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205298/download?verifier=EKNiHfNgKLJZse2JXqOIVkKMtrLRwLtiV04dQJ8b&wrap=1] JLifetimeProblems.cpp, which uses this function to demonstrate the undefined results it produces. It also shows similar effects when instead of returning the array, it is assigned to a global variable.

As we see in the examples above, it is not easy to create an array inside a function that can be exported for use outside its boundaries. To do so we will need the use of pointers and dynamic allocation, that we will review in the following unit. 

The admonition to respect the lifetime of variables is summarized in the following secure programming rule:

SPR DCL30-C

Declare objects with appropriate storage durations.

We talked about scope and lifetime in regards to variables, but they also apply to functions. The scope of functions is global by default. They are visible to all functions in a translation unit from the moment they are declared to the end of a file. This scope may be extended within the same translation unit and beyond if their prototypes are first visible declared. They do not need to be declared using the keyword external. They are implicitly external. However, functions can be declared static, but it has a different meaning that we have for static variables. In functions, the keyword static applies to its scope, not its lifetime. A static function reduces its scope by making it visible only in the file where it is defined. This is done, so that the same function name may be used in different files with different effects.

A final warning on the issues of declaring variables and functions in multiple files comes from the following secure programming rule:

SPR DCL40-C

Do not create incompatible declarations of the same function or object

Incompatible declarations may come about when an external variable is declared with a given type in one file, and then re-declared with a different type in another. For example, the variable aVar may be defined initially as an integer in one file:

extern int aVar = 23; 

But, a programming mistake may declare it in another file as a short integer:

extern short aVar; 

These incompatibilities should be avoided, because they produce undefined results. In this case, both, the definition in one file, and the declaration in the other should be of the same integer variable, or the same short variable.

Programmers need to ensure that all external variables are declared with the same data types in all translation units. A particular example of this problem is the declaration of external arrays. While we have seen in previous sections that pointers can be used when passing arrays as parameters to functions, declarations and definitions of external arrays should not rely on pointers, since they may produce incompatible memory allocations. Suppose we declare an external array in one file as follows:

extern char aString[] = “Hello”; 

The following declaration of this variable in another file may create incompatibilities:

extern char* aString; 

Even though a string may be declared as an array of char, or a pointer to char, the incompatibility arises because each declaration may allocate different sizes to hold array elements.

Not only variables, but also functions may fall under incompatible declarations if programmers do not pay attention. A function prototype may be declared in one file with certain data types for its parameters and output, but later modified when defined in another file. This also should be avoided. Function definitions should match their function prototypes.

Overloaded Functions

When programs are compiled in C/C++, among other things, the compiler creates a table to identify the location and all other information of the various functions used in the application. There will be a record in this table for each function used. A function will be recognized by its signature. The signature is concatenation of the name of the function with the data types of the arguments in its parameter-list, in the order in which they were declared. For example, the following table shows a couple of functions we saw already in this unit, with their respective signatures. Notice that output types are not considered as part of the signatures. Also, arrays are stored as pointers type in their signatures.

Sample of Functions and their Signature

Function Declaration

Signature

double maximum(double a, double b, double c);

maximum-double-double-double

double maxInArray(double array[], int size);

maxInArray-double*-int

double minInArray(double* array, int size);

minInArray-double*-int

int replace(char c, char* s)

replace-char-char*

void nullify(char s[]);

nullify-char*

 

To be stored in the table created by the compiler, signatures must be unique. There could be functions that have the same name, but with different number of parameters, different data types, or even different order for the data types. All these functions that share the same name, but have different and distinguishable parameter lists are known as overloaded functions. These functions are mostly used, when we want to offer the same program to handle diverse input parameters. For example, if we have a function that produces the largest element of an array of integers, we could have similar functions that will evaluate the largest element of an array of float or double numbers. They could be declared as follows: 

int maxInArray(int array[], int size);
float maxInArray(float array[], int size);
double maxInArray(double array[], int size);

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205062/download?verifier=LQ297glyDBRKA83rwYMFtb8AhaRZ7z5NeN8Oewqx&wrap=1] KOverloadedFunctions.cpp, that contains these overloaded methods.

The stdlib.h Library

So far we have been talking of C/C++ functions in general, so let us finish this unit by presenting the functions inside the C library stdlib.h.  Besides miscellaneous functions, this library mainly contains functions related to three activities: number conversion with strings, random numbers, and memory allocation. We will deal with memory allocation in detail in the next unit. So let us review the other functions listed in the following table: 

Selected functions from stdlib.h        

Function

Description

atof(s)

Returns the double value of the number that is stored as a string in s

atoi(s)

Returns the integer value of the number that is stored as a string in s

atol(s)

Returns the long integer value of the number that is stored as a string in s

strtod(s,t)

Returns the double value of the number that is stored as a prefix in string s. The remainder of the string is stored in t, unless is NULL

strtol(s,t,b)

Returns the long value of the number that is stored as a prefix in string s. The remainder of the string is stored in t, unless is NULL. The base of the number is indicated in parameter b (2-> binary, 10-> decimal, etc)  

rand()

Returns a pseudo-random number between 0 and the value of the constant RAND_MAX (no smaller than 327767)

srand(seed)

Uses the integer seed to reset and initialize the pseudo-random number generator

 

The conversion functions atof, atoi, and atol are useful when converting a string containing a number. Strings cannot be used in arithmetic computations; therefore, they need to be converted to a numeric type.  These functions expect the string only to contain the number. The functions strtod and strtol perform a similar conversion, but they only expect the number at the beginning of the string (prefix). The remainder of the string is returned in the second parameter.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205064/download?verifier=pE0CTtd419Hzacd8tZnaXnPRNjqDOFwQrgzQsWAB&wrap=1] LStdlibConversion.cpp, that contains an example of the use of this conversion. The program reads and adds numbers from the user, but it may also read an indication that the list of numbers has ended. The indication is the letter ‘Q’ or the letter ‘q’. Because the loop is expecting these characters, the numbers must also be read as characters and converted to numbers with the function atof.

C/C++ also offers the functions rand and srand to generate pseudo-random numbers. A pseudo-random number is not completely random, because there is a procedure that generates it and it is not just chance. However, pseudo-random numbers appear to be random when evaluated statistically. The problem with the functions provided in stdlib.h is that they are poor generators of random numbers, and the numbers they generate tend to repeat in the long run. Because of this problem, the following two secure programming rules are stated:

SPR MSC30-C

Do not use the rand() function for generating pseudorandom numbers

 

SPR MSC32-C

Properly seed pseudorandom number generators

Programmers in need of random numbers must look elsewhere to satisfy these recommendations.  Fortunately, there are other libraries available depending of the platform on which the program is to be run. For Microsoft Windows programmers, the recommended libraries to use are Windows.h and bcrypt.h. These libraries contain a set of functions to generate reliable pseudo-random numbers and that are properly seeded, satisfying MSC30-C and MSC32-C secure programming rules above.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205070/download?verifier=KUl9t5ZFZEDJ2KONHFRZosnTzUg8M3sWteAYxQcW&wrap=1] MRandomInWindows.cpp that demonstrates the use of these libraries to generate random numbers.

You may review the attached program MRandomInWindows.cpp that demonstrates the use of these libraries to generate random numbers.

References on The Windows Pseudo-Random generator:

 [link: https://docs.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom] BCryptGenRandom function

 [link: https://docs.microsoft.com/en-us/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom]  [link: https://wiki.sei.cmu.edu/confluence/display/c/MSC30-C.+Do+not+use+the+rand%28%29+function+for+generating+pseudorandom+numbers] MSC30-C. Do not use the rand() function for generating pseudorandom numbers 

 

Read More

Read more about functions in Chapter 4 of the textbook.

 

Read More

Read more about stdlib.h in Appendix B5 of the textbook.

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
