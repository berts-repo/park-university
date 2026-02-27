# Unit 6: Discussion

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

After reading the assigned course material, you must select and answer any two (2) of the questions below.

Post your answers in this environment. Do not attach code, but copy and paste it onto the discussion thread. When you do that, you may lose some indentation. You need to restore this indentation manually to make the program readable.   

Please read what other students are posting and post all different examples. Do not repeat previous postings. Be Original. Also, do not write code containing material related to the Lab Activities/Homework. Homework is personal and it must not be shared with anyone but the Instructor.

Questions

Show an example of a piece of C/C++ code that creates and uses pointers (incorrectly) to perform mathematical operations. Show also code that fix this problem.

Show an example of a piece of C/C++ code that de-reference pointers incorrectly. Show also code that fix this problem.

Show an example of a piece of C/C++ code that presents problems because of improper type casting of pointers. Show also the correct way to use type casting in this situation.

Show an example of a piece of C/C++ function that has problems because it receives a parameter by value, when it should receive it by reference, with a pointer. Describe the problem and show code on how it can be solved.

Show an example of a piece of C/C++ code that uses pointer arithmetic (incorrectly) to perform operations on an array. Show also code that fix this problem.

Show an example of a piece of C/C++ code that incorrectly compares pointers that refer to different arrays. Show also code that fix this problem.

Show an example of a piece of C/C++ code that incorrectly adds or subtracts scaled integers to pointers. Show also code that fix this problem.

Show an example of a piece of C/C++ code that uses incorrectly the functions calloc, malloc, or free. Describe the problem and show code on how it can be solved.

Show an example of a piece of C/C++ code that creates and initializes a structure with a flexible array member (incorrectly). Show also code that fix this problem.

Show an example of a piece of C/C++ code that defines a structure data type and uses the dot notation to create and initialize some variables of this data type. Convert later this code to replace the dot notation with the arrow notation.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-09-23T09:33:04Z

Hello class,

I will be answering prompt 9 and 10.

There is a couple problems with this code, when declaring empty arrays in structures, you can only have one empty array at the bottom of the structure. 

struct myBox {    
    int someArray[]:  // can't have two uninitialized array in structure
    int dynArray[];   // array must be declared at end of structure
    int someNumber;
};

typedef struct myBox box;      
box* point = NULL;            
int size = 5;

point = (box*)malloc(sizeof(box) + size * sizeof(box));
Prompt 10: Dot Notation
#include 
#include 

struct myBox {
    int someNumber;
    int dynArray[];
};

typedef struct myBox box;      // nickname for structure
box* point = NULL;             // pointer for dynamic array
int size = 5;                  // size of array

int main() {

    // this line initializes the array
    point = (box*)malloc(sizeof(box) + size * sizeof(box));

    // this block sets values to the array
    for (int i = 0; i < size; i++)
    {   
        // dot notation
        (*(point + i)).dynArray[i] = (2 * i);
    }

    // this block prints the array index, the dynamic array values, and the location in memory
    for (int i = 0; i < size; i++)
    {
        // dot notation
        printf("dynArray[%d]: %d | address: %d\n", i, (*(point+i)).dynArray[i], &(*(point + i)).dynArray[i]);
    }
    return 0;
}
Promp 10: Arrow notation
#include 
#include 

struct myBox {
    int someNumber;
    int dynArray[];
};

typedef struct myBox box;      // nickname for structure
box* point = NULL;             // pointer for dynamic array
int size = 5;                  // size of array

int main() {
      
    // this line initializes the array
    point = (box*)malloc(sizeof(box) + size * sizeof(box));
    
    // this block sets values to the array
    for (int i = 0; i < size; i++)
    {
        // arrow notation
        (point + i)->dynArray[i] = (2 * i);
    }
    
    // this block prints the array index, the dynamic array values, and the location in memory
    for (int i = 0; i < size; i++)
    {
        // arrow notation
        printf("emptyArray[%d]: %d | address: %d\n", i, (point + i)->dynArray[i]), &((point + i)->dynArray[i]);
    }
}        

I noticed somethign interesting when working with these different notations. The dot notation leaves a range in the memory address, and the arrow notation has the same address for all the elements of the array. Am I printing the placeholder wrong? I could not get it to work properly

---
