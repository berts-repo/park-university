/**********************************************************************
Bert Darnell
09-18-2021
cs202

This program generates 10 random numbers and adds them to an array,
it then sorts prints, sorts, modify and sorts again.
***********************************************************************/

#define SIZE 10

// function prototypes
int generateRandomValues();
int printValues(char* msg);
int modValues();
int sortValues(); 

extern int globalArray[]; // external array to hold values
extern char emptyStr[]; // emptry string for printValues function


