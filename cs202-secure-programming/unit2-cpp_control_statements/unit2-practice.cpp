/*******************************************************************************************************
Promp: 4 Show a complete and syntactically correct example of C/C++ code that contains a loop to print a table.
To be complete, the code must declare and initialize all the variables it needs. For example, a loop
may print all rows of a addition or multiplication table. Add headers to the table.

Prints a multiplication table
********************************************************************************************************/

#include 

int main()
{
    printf("   *******************************************\n");  //table header
    int column = 1;
    while (column < 10) { //interates through the columns of the table
        
        for (int row = 1; row < 10; row += 1)  //interates through the rows of the table
        {
            printf("%5d",row*column);   //multiplies the variables for the table
        }

        printf("\n"); //new line for each row of the table
        column += 1;
    }
    printf("   *******************************************\n");  //table footer
    return 0;
}

/********************************************************************************************
Promp 3: Show a complete and syntactically correct example of C/C++ code that contains a loop
used to validate user input. To be complete, the code must declare and initialize
all the variables it needs. For example, a loop may continuously request the user
for a value within certain range. The code will only stop when this condition is satisfied.

Has the user input data untill the correct answer is given.
*********************************************************************************************/
#include 

int main() {

int answer = 2;
int guess;
    do {
        printf("What does is 1+1?");
        scanf_s("%d", &guess);
}   while (guess != answer);
}