#include <stdio.h>
#include <cstdlib>
#include <cmath>
#define SIZE 10 //the total number of grades

int main()
{
int calculate_mean = 0; int mean = 0;
int standard_deviation = 0; int calculate_deviation = 0; int calculate_absolute = 0;
int grades[SIZE] = {34, 47, 53, 88, 92, 67, 95, 83, 99, 72};

/* This calculates the mean */
for (int i=0; i<SIZE; i++)
{calculate_mean += grades[i];}		 //summation of  grades

mean = calculate_mean/SIZE;			 //calculates the average

printf("\n");

/* This calculates the standard deviation */
for (int i=0; i<SIZE; i++)
{
calculate_absolute = abs(grades[i] - mean);     			 // |x-u| in math formula
calculate_deviation += calculate_absolute * calculate_absolute;	 // summation of the absolute squared
}
standard_deviation = sqrt(calculate_deviation/SIZE);    		 //square roots after division

/* Prints results */
printf("This is the mean: %d\n", mean);
printf("This is the standard deviation: %d\n", standard_deviation);

return 0;
}
