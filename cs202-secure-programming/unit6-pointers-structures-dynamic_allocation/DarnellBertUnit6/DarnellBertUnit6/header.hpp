/*****************************************************************************
Bert Darnell
09/26/2021
CS202

Unit 6 Lab

This program prints a table of degrees and converts Fahrenheit to Celsius.
This function dynamically allocates 3 arrays and initializes them 0. It
returns errors if there is a problem creating the array or inputting the
array size. It then initializes the arrays from read entries for starting 
temp, increment size and the size of the array.
******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

int iInit(int**, int);    //function that initializes a dynamic array to 0
int fInit(float**, int);  //function that initializes a dynamic array to 0
void print(int*, float*, float*, int);  //function to print table of arrays

