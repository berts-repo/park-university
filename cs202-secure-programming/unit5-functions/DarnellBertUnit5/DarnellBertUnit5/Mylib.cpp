#include <Windows.h>
#include <bcrypt.h>
#include <stdio.h>
#include <string.h>

#pragma comment(lib, "Bcrypt")
#include "Header.hpp"

extern int globalArray[SIZE] = { 0,0,0,0,0,0,0,0,0,0 }; // declares external array to size and 0's

// this function produces random values
int generateRandomValues()
{
	BCRYPT_ALG_HANDLE Prov;  // Variable will hold the algorithm that Windows provide
	int randomNumber; // variable to hold random number

	int low = 100000;   // random number range
	int high = 1694208; //random number range

	int index = 0; // index for iteration
	int ok = 1; // returns positive number if successfull

	if (BCRYPT_SUCCESS(BCryptOpenAlgorithmProvider(&Prov, BCRYPT_RNG_ALGORITHM, NULL, 0))) {

		printf("\nGenerating random numbers ...");
		while (index < SIZE && ok) {

			if (!BCRYPT_SUCCESS(BCryptGenRandom(Prov, (PUCHAR)(&randomNumber), sizeof(randomNumber), 0))) {
				printf("\nError generating random numbers.\n");
				ok = 0;
			}
			else {
				if (randomNumber >= low && randomNumber <= high) {
					
					globalArray[index] = randomNumber; // sets the random number to external array
					
					index++;
				}
			}
		}
	}
	return ok;
}


// this fuction prints the tables and counts the number of times function is called
int printValues(char *msg) {
	char str1[] = "\nOriginal random values\n";
	char str2[] = "\nSorted random values\n";
	char str3[] = "\nModified random values\n";
	char str4[] = "\nModified and sorted random values\n";

	static int printCount = 0; // static to keep track of amount of times function is called
	printCount += 1;
	printf("\nPrinting number %d ...\n", printCount);
	
	if		(printCount == 1) { msg = str1; }
	else if (printCount == 2) { msg = str2; }
	else if (printCount == 3) { msg = str3; }
	else if (printCount == 4) { msg = str4; }

	while (*msg != '\0') {printf("%c", *msg); msg++;}  //prints to pass by pointer

	printf("---------------------------");

	for (int i = 0; i < SIZE; i++){printf("\n%d", globalArray[i]);} // prints external array 

	printf("\n---------------------------");

	return 1;
}

// this function get the remainder of the next index of array deivided by the first index, last index by first.
int modValues()
{
	printf("\nModifying random numbers ...");

	int first_index = globalArray[0]; //variable to hold first index for last remainder
	int index = 0;

	while (index < SIZE)
	{
		if (index + 1 < SIZE)
		{globalArray[index] = globalArray[index + 1] % globalArray[index];}
		
		else
		{globalArray[index] = first_index % globalArray[index];}

		index++;
	}
	return 1;
}