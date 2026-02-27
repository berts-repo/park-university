# Unit 5: Discussion

Introduction 

Participation in discussion threads is a weekly assignment that tests your reading process and critical thinking. You may participate in these discussion threads for this unit between 12:00 a.m., Monday, CT through 11:59 p.m., Sunday, CT. of the corresponding week.

 

Requirements

Your initial post must answer of your chosen question by 11:59 p.m., Thursday, CT.

You must complete your own posting and respond to at least one other student thread (different than your own) by 11:59 p.m., Sunday, CT.

Throughout the week, you must respond, to the best of your knowledge, the questions or requests made by Instructor and/or students, especially the Instructor’s requests for corrections.

Due Date

Initial post by 11:59 p.m., Thursday, CT

Respond to one or more classmates by 11:59 p.m., Sunday, CT

Directions 

After reading the assigned course material, you must select and answer any (1) of the questions below

Post your answers in this environment. Do not attach code, but copy and paste it onto the discussion thread. When you do that, you may lose some indentation. You need to restore this indentation manually to make the program readable.   

Please read what other students are posting and post all different examples. Do not repeat previous postings. Be Original. Also, do not write code containing material related to the Lab Activities/Homework. Homework is personal and it must not be shared with anyone but the Instructor.

Questions

Present an example that uses correctly a global variable within a single translation unit. Explain the purpose of declaring the variable as global, how it should be declared, and how it is used. Show as much C/C++ code as needed to explain your example.

Present an example that uses correctly an external variable within two translation units. Explain the purpose of declaring the variable as external, how it should be declared, and how it is used. Show as much C/C++ code as needed to explain your example.

Present an example that uses correctly a static variable inside a function. Explain the purpose of declaring the variable as static, how it should be declared, and how it is used. Show as much C/C++ code as needed to explain your example.

Present an example that uses correctly a local variable inside a function to mask (hide) it from a global variable. Explain the purpose of masking the variable, how it should be declared, and how it is used. Show as much C/C++ code as needed to explain your example.

Present an example that uses correctly overloaded functions. Explain the purpose of the overloading, how it should be implemented, and how the functions are used. Show as much C/C++ code as needed to explain your example.

Present an example that uses any of the conversion functions in stdlib.h for a concrete purpose. Explain the rationale for using the conversion in this case, and how is the function used. Show as much C/C++ code as needed to explain your example.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-09-14T10:59:11Z

Hello class,

Prompt 2: Present an example that uses correctly an external variable within two translation units. Explain the purpose of declaring the variable as external, how it should be declared, and how it is used. Show as much C/C++ code as needed to explain your example.

The external is used so you can increase the scope of a variable, between multiple files. The variable can only be initialized once but can be declared multiples, and a new value set.

My code takes calls a function prototype, and external variable, initializes it, and declare the external as 0, and then call the function from main, to change the external to 1.

 

/*************************************************************************
Header.hpp

This header file declares the external variable and a function prototype
**************************************************************************/

extern int externalInteger; // external variable
void changeBase(void); // function prototype
/********************************************************
changeBase.cpp

This file initializes external integer and the function
changeBase is called from main to change the external integer
*********************************************************/

extern int externalInteger = 0; 
void changeBase(void) { externalInteger = 1; } 
/***************************************************************************************
Source.cpp

This file is my main function that calls my changeBase function from another file.
It prints the external variable before and after being called by the first translation
****************************************************************************************/

#include 
#include "Header.hpp"

int main() 
{
    printf("The external variable before second translation: %d\n", externalInteger);
    changeBase();
    printf("The external variable after second translation: %d\n", externalInteger);
}

---
