/*
   Program Name: sort.cpp
   Author: GT
   Lab Activity / Homework5 - insertion sort for students.

   This function sorts an external array of int values named globalArray
   with SIZE elements.
   The array globalArray must be declared as external and
   the value of the constant SIZE should be available for the
   function to work properly
*/
#include "Header.hpp"
#include <stdio.h>

int sortValues() {
	int insert;   // temporary variable to hold the element to be inserted
	int moveItem; // index of the element to be moved
	
	static int sortCount= 0;
	sortCount++;
	printf("\nSorting numbers %d ...", sortCount);


	for (int i = 0; i<SIZE; i++) {
		insert = globalArray[i];   // hold current element
		moveItem = i;              // initial search for moveable item
		while ((moveItem >0) && (globalArray[moveItem - 1] > insert)) {
			globalArray[moveItem] = globalArray[moveItem - 1];
			moveItem--;
		}
		globalArray[moveItem] = insert;
	}
	return 1;
 }
