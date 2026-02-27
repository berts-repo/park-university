# Unit 3: Discussion

Introduction 

Participation in discussion threads is a weekly assignment that tests your reading process and critical thinking. You may participate in these discussion threads for this unit between 12:00 a.m., Monday, CT through 11:59 p.m., Sunday, CT. of the corresponding week.

 

Requirements

Your initial post must answer both of your chosen questions by 11:59 p.m., Thursday, CT.

You must complete your own posting and respond to at least one other student thread (different than your own) by 11:59 p.m., Sunday, CT.

Throughout the week, you must respond, to the best of your knowledge, the questions or requests made by Instructor and/or students, especially the Instructor’s requests for corrections.

Due Date

Initial post by 11:59 p.m., Thursday, CT

Respond to one or more classmates by 11:59 p.m., Sunday, CT

Directions 

After reading the assigned course material, you must select and answer any two (2) of the questions below. These questions require you to write small C/C++ programs to demonstrate certain features. You may write one program to answer each question, or merge both answers in one single program, clearly differentiated within the program. You must test your program(s) in Microsoft Visual Studio and show us the final product (C/C++ code and a sample run). Some of the questions give you the choice of selecting various cases, you must select only one case per question. In other words, your 2 examples must come from different questions. Do not forget also to explain the purpose of the programs in plain English:

Post your answers in this environment. Do not attach code, but copy and paste it onto the discussion thread. When you do that, you may lose some indentation. You need to restore this indentation manually to make the program readable.   

Please read what other students are posting and post all different examples. Do not repeat previous postings. Be Original. Also, do not write code containing material related to the Lab Activities/Homework. Homework is personal and it must not be shared with anyone but the Instructor.

Questions

Present a complete and syntactically correct example of C/C++ code that prevents wrap around when adding, subtracting, OR multiplying either unsigned char, unsigned short, OR unsigned long data types (select one operation and one data type). Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that prevents improper conversion of one of the following:

unsigned long to unsigned char

unsigned int to unsigned char

unsigned short to unsigned char.

Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that prevents wrap around when either unsigned int OR unsigned short data types (select one data type) is converted to signed char. Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that prevents wrap around when adding, subtracting, OR multiplying either signed long, signed int, OR signed char data types (select one operation and one data type). Explain in English which vulnerabilities are being prevented.

 

Present a complete and syntactically correct example of C/C++ code that prevents improper conversion of one of the following:

signed long to signed char

signed int to signed char

signed short to signed char.

Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that prevents improper conversion of one of the following:

signed long to unsigned short

signed long to unsigned char

signed int to unsigned short

signed int to unsigned char

signed short to unsigned char.

Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that prevents improper division by zero, remainder by zero OR overflow by division when dividing either signed short or signed char data types (select one operation and one data type). Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that prevents overflow by unary negation with signed int or signed char data types (select one data type). Explain in English which vulnerabilities are being prevented.

 

Present a complete and syntactically correct example of C/C++ code that prevents overflow when left-shifting one of the following data types:

an unsigned long

an unsigned char

a signed long

a signed char.

Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that prevents overflow when right-shifting one of the following data types:

an unsigned long

an unsigned short

an unsigned char

a signed long

a signed short

a signed char.

Explain in English which vulnerabilities are being prevented.

Present a complete and syntactically correct example of C/C++ code that uses tolerance properly applied to the comparison of two float variables.

Present a complete and syntactically correct example of C/C++ code that verifies that the parameters for a mathematical function are within their allowable value ranges. Indicate in English which are those allowable value ranges.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-09-01T12:02:44Z

/*********************************************************************************************
Prompt 2c: Present a complete and syntactically correct example of
C/C++ code that prevents improper conversion of a short to char.

Prompt 10b: Present a complete and syntactically correct example of C/C++
code that prevents overflow when right-shifting an unsigned short.

In this code I am preventing the loss of data by checking the precision of a right-shift short
integer with to a char with lower precision. The program
is also checking to make sure conversion of short to char data types doesn't
have a higher precision then the type that is converted.
**********************************************************************************************/
#include 
#include 

int main() {
    unsigned int some_int;  // Inputed short variable
    unsigned int shift_amount;  // Inputed right-shift amount
    unsigned char int2char; // Right-shift result

    printf("Enter a number between 256-65535 for a short integer: ");
    scanf_s("%u", &some_int);
    printf("Enter the amount of times you want to shift: ");
    scanf_s("%u", &shift_amount);

    if (shift_amount > 7 || shift_amount < 0) { // This block prevents overflow from right-shift. Promp 10b
        printf("Shift is greater then the precision of the integer type\n");
    }
    else {
        int2char = some_int >> shift_amount;
        if (UCHAR_MAX < some_int >> shift_amount) { //This block checks if conversion will fit in a lower data type. Promp 2c
            printf("This conversion from short int to char would result in losing numbers\n");
            printf("This would still be a short int of %u\n", some_int >> shift_amount);
        }
        else {         
            printf("The short to char conversion is: %u\n", int2char);
        }        
    }
    return 0;
}

---
