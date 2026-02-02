#include "header.hpp"

int* iPtr;  //pointers to dynamically allocated arrays
float* fPtr;
float* fPtr2;

int size; // user input size for array
float temp; // user input for temperature, and temp variable for increment
float inc; // user input for increment

int main() {

	int* iPtr = NULL;
	float* fPtr = NULL;
	float* fPtr2 = NULL;

	int size = -1; // re-input for read value
	while (size < 0) 
	{
		printf("Please provide an array size: (0 to exit) ");
		scanf_s("%d", &size);
	}
	if (size != 0)
	{
		printf("Enter an initial Temperature(Fahrenheit degrees): ");
		scanf_s("%f", &temp);

		printf("Enter Temperature Increment (Fahrenheit degrees) ");
		scanf_s("%f", &inc);

		
		iInit(&iPtr, size); //functions to initiate dynamically allocated arrays
		fInit(&fPtr, size);
		fInit(&fPtr2, size);

		if (iPtr != NULL && fPtr != NULL && fPtr2 != NULL) //check pointers for null
		{
			// this block sets the values to the arrays
			for (int i = 0; i < size; i++)
			{
				*(iPtr + i) = 1 + i;
				*(fPtr + i) = temp;
				*(fPtr2 + i) = 5.0 * (temp - 32.0) / 9.0;
				temp = temp + inc;
			}
			// print table
			print(iPtr, fPtr, fPtr2, size);

			free(iPtr); free(fPtr); free(fPtr2); //free dynamically allocated array
		}

	}

	return 0;
}