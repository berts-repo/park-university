// Bert
// Unit 5 Linux Assignment
// 9-20-2022

//This script takes positive number inputs from the user and prints out the mean and deviation.

#include <stdio.h>
#include <cstdlib>
#include <cmath>
#define MAXSIZE 50

int main()
{
    int input = 0; int size = 0; int calculate_mean = 0; int mean = 0;
    int standard_deviation = 0; int calculate_deviation = 0; int calculate_absolute = 0;
    int high = 0; int low = 2147483647;
    int grades[MAXSIZE];

    /* user inputs positive numbers*/

    while (input >= 0)
    {
        scanf("%d", &grades[size]); //user inputs grades
        input = grades[size];

        if (input >= 0)
        {
            size += 1;                              //detemines length of array
            if (input > high) { high = input; }        //highest grade
            if (input < low) { low = input; }          //lowest grade
        }
        else
        {
            printf("You entered %d grade(s): ", size);      //loops through array size and prints grades
            for (int i = 0; i < size; i++) { printf("%d ", grades[i]); }
        }
    }

    /* This calculates the mean */

    for (int i = 0; i < size; i++)
    {
        calculate_mean += grades[i]; //sum of grades
    }

    mean = calculate_mean / size; //calculates the average

    printf("\nThis is the mean: %d\n", mean);


    /* This calculates the standard deviation */

    if (size > 1)   //makes sure there are at least two inputs for standard deviation
    {
        for (int i = 0; i < size; i++)
        {
            calculate_absolute = abs(grades[i] - mean);     // |x-u| in math formula
            calculate_deviation += calculate_absolute * calculate_absolute; // sum of the absolute squared
        }
        standard_deviation = sqrt(calculate_deviation / size);    //square roots after division

        printf("This is the standard deviation: %d\n", standard_deviation); //prints standard deviation

    }
    else { printf("Not enough inputs for standard deviation\n"); } //prints deviation error


    printf("This is the range: %d - %d\n", low, high); //prints range, from low to high

    return 0;
}
