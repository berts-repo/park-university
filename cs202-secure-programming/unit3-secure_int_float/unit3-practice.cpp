/*********************************************************************************************
Prompt 2c: Present a complete and syntactically correct example of
C/C++ code that prevents improper conversion of a short to char.

Prompt 10b: Present a complete and syntactically correct example of C/C++
code that prevents overflow when right-shifting an unsigned short.

In this code I am preventing the loss of data by checking the precision of a right-shift short
integer with to a char with lower precision. The program
is also checking to make sure conversion of short to char data types doesn't
have a higher precision then the type that is converted.
**********************************************************************************************/
#include 
#include 

int main() {
    unsigned int some_int;  // Inputed short variable
    unsigned int shift_amount;  // Inputed right-shift amount
    unsigned char int2char; // Right-shift result

    printf("Enter a number between 256-65535 for a short integer: ");
    scanf_s("%u", &some_int);
    printf("Enter the amount of times you want to shift: ");
    scanf_s("%u", &shift_amount);

    if (shift_amount > 7 || shift_amount < 0) { // This block prevents overflow from right-shift. Promp 10b
        printf("Shift is greater then the precision of the integer type\n");
    }
    else {
        int2char = some_int >> shift_amount;
        if (UCHAR_MAX < some_int >> shift_amount) { //This block checks if conversion will fit in a lower data type. Promp 2c
            printf("This conversion from short int to char would result in losing numbers\n");
            printf("This would still be a short int of %u\n", some_int >> shift_amount);
        }
        else {         
            printf("The short to char conversion is: %u\n", int2char);
        }        
    }
    return 0;
}