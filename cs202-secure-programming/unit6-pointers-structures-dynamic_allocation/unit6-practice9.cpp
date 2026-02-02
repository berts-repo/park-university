/*
Prompt #9: Show an example of a piece of C/C++ code that creates and initializes a structure with a flexible array member (incorrectly). Show also code that fix this problem.
*/


struct myBox {    
    int someArray[]:  // can't have two uninitialized array in structure
    int dynArray[];   // array must be declared at end of structure
    int someNumber;
};

typedef struct myBox box;      
box* point = NULL;            
int size = 5;

point = (box*)malloc(sizeof(box) + size * sizeof(box));