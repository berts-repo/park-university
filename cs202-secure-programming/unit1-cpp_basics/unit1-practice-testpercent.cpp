#include <stdio.h>

/*
testpercent.cpp
Bert Darnell
8/19/2021

This program ask the user to input a test score,
and it calculates the percent they recieved.
*/
int main() {
    float score_received;
    float total_points;

    printf("how many points is the test worth?\n");
    scanf_s("%d", &total_points);

    printf("how many points did you get?\n");
    scanf_s("%d", &score_received);

    printf("you got a %.2f percent!\n", score_received / total_points);
}