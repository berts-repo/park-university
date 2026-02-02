#include <limits.h>
#include <math.h>
#include <iostream>

int main() {

    int id = 1694208;

    /*******************************************************
    This block determines the student ID to binary in
    reverse and counts the base2 exponent position.
    ********************************************************/
    unsigned int counter = id;
    unsigned int position_value = 0;

    while (counter > 0) {
        counter = counter / 2;
        position_value++;
    }
    
    /***********************************************************
    QUESTION 1:
    The assignment will start with your Park ID Number. Convert
    this number to a binary number. Show the procedure followed
    to get your result (1 point).
    *************************************************************/
    unsigned int id2 = id;
    unsigned int exponent = position_value;

    printf("\n**************************************************************\n");
    printf("\nPrompt 1:\n"
           "\nThis is the representation of the ID number in binary. This"
           "\nwas solved by prooving if n >= 2^x and printing 1 or else 0,"
           "\nand the final binary number, was determined by prooving if"
           "\nthe least significant n >= 1 and printing 1 if true");
           
    printf("\n\nID number: 1694208");
    printf("\nBinary ID number: ");

    while (exponent > 0) {
        exponent--;

        if (id2 >= pow(2, exponent))
        {
            printf("1");
            id2 = id2 - pow(2, exponent);
        }
        else if (id2 >= 1 && exponent == 0)
        {
            printf("1");
        }
        else
        {
            printf("0");
        }
    }
    printf("\n\n**************************************************************\n");

    /**************************************************************************
    QUESTION 2:
    Show how the binary number obtained in (1) will be represented in RAM as
    an unsigned long, an unsigned int, and unsigned short. If these formats
    are too small to represent your number, show the digits that will be
    discarded next and to the left of the digits inside the format. Clearly
    differentiate the included and no-included digits (1 point).
    ***************************************************************************/

    printf("\nPromp 2:\n");
    printf("\nA unsigned long integer is 4 bytes or 32 bits");
    printf("\nBinary: 00000000000110011101101000000000");
    
    printf("\nA unsigned integer is 4 bytes or 32 bits");
    printf("\nBinary: 00000000000110011101101000000000");
    
    printf("\nA unsigned short integer is 2 bytes or 16 bits");
    printf("\nDiscarded: 000000000001100");
    printf("\nBinary: 1101101000000000");

    printf("\n\n**************************************************************\n");


    /****************************************************************************
    QUESTION 3:
    Write a secure piece of code that will convert the unsigned long obtained
    in (2) onto an unsigned char. Trace the code with your id number (1 point).
    *****************************************************************************/
    
    printf("\nPrompt 3:\n");

    unsigned char id2char;
    unsigned char force_id2char;
    unsigned long long_id = id;

    if (UCHAR_MAX >= long_id)
    {
        id2char = long_id;
    }
    else
    {
        printf("\nNumber is not safe to convert!");
        force_id2char = long_id;
        printf("\nIf forced your number would be: %u", force_id2char);
    }
    
    // Block for trace with id
    printf("\n\nThis is the code I used to check precision:");
    printf("\n\n char id2char;"
    "\n if (255 > 10000000000)"
    "\n {"
    "\n    id2char = id;"
    "\n }"
    "\n else"
    "\n {"
    "\n    printf(Not safe to convert!);"
    "\n }");    

    printf("\n\n**************************************************************\n");



    /***************************************************************************
    QUESTION 4:
    Write a secure piece of code that will convert the unsigned int obtained
    in (2) onto a signed int. Trace the code with your id number (1 point).
    ****************************************************************************/
    printf("\nPrompt 4:\n");

    signed int signed_int;
    signed int force_signed_int;
    unsigned int unsigned_int = id;

    if (INT_MAX < unsigned_int)
    {
        printf("\nCan't be converted without loosing numbers");
        force_signed_int = unsigned_int;
        printf("\nIf forced the signed integer would be: %d", force_signed_int);
    }
    else
    {
        signed_int = unsigned_int;        
    }
    printf("\n\n This is code I used to trace precision");
    printf(
    "\nif (2147483647 > 10000000000\n"
    "{\n"
        "printf(can't be converted without loosing numbers);\n"
    "}\n"
    "else\n"
    "{\n"
        "sign_int = unsign_int;\n"
    "}");

    printf("\n\n**************************************************************\n");

    /******************************************************************************
    QUESTION 5:
    Show how the negation of the binary number obtained in (1) will be represented
    in RAM as a signed int using two-complement’s format. Show the procedure
    followed to get your result (1 point).
    *******************************************************************************/
    printf("\nPrompt 5:");

    printf("\n\nBinary ID:  00000000000110011101101000000000");
    printf("\nNegated ID: 11111111111001100010011000000000");
    printf("\nTo get to this I take the negation of each bit then add 1 to it");

    printf("\n\n**************************************************************\n");

    /********************************************************************************
    QUESTION 6:
    Show how the signed int obtained in (5) will be represented as a signed
    char if the conversion is forced. Indicate also which number it will represent
    in the decimal system. Show the procedure followed to get your results (1 point).
    *********************************************************************************/
    printf("\nPrompt 6:");

    printf("\n\nA char is 1 byte which is 8bits.");
    printf("\nBinary ID as char: 00000000 and this would represent 0 in decimal");

    printf("\n\n**************************************************************\n");


    /********************************************************************************
    QUESTION 7:
    Show the effect of left-shifting on the unsigned short number obtained in (2).
    Apply left-shifting five times to this number and in each time show its RAM
    representation and its decimal value.
    *********************************************************************************/
    printf("\nPrompt 7:");

    printf("\n\nAn unsigned short is 2 bytes and 16 bits");
    printf("\nBinary id as short: 1101101000000000");
    printf("\nLeft shift << 1011010000000000 is 46080 in binary");
    printf("\nLeft shift << 0110100000000000 is 26624 in binary");
    printf("\nLeft shift << 1101000000000000 is 53248 in binary");
    printf("\nLeft shift << 1010000000000000 is 40960 in binary");
    printf("\nLeft shift << 0100000000000000 is 16384 in binary");

    printf("\n\n**************************************************************\n");

    /**********************************************************************************
    QUESTION 8:
    Show the effect of right-shifting on the unsigned short number obtained in (2).
    Apply right-shifting five times to this number and in each time show its RAM
    representation and its decimal value.
    ***********************************************************************************/
    printf("\nPrompt 8:\n");

    printf("\nAn unsigned short is 2 bytes and 16 bits");
    printf("\nBinary id as short: 1101101000000000");
    printf("\nRight shift >> 0110110100000000 is 27904 in binary");
    printf("\nRight shift >> 0011011010000000 is 13952 in binary");
    printf("\nRight shift >> 0001101101000000 is 6976 in binary");
    printf("\nRight shift >> 0000110110100000 is 3488 in binary");
    printf("\nRight shift >> 0000011011010000 is 1744 in binary");

    printf("\n\n**************************************************************\n");

    /******************************************************************************
    QUESTION 9:
    Show how the integer binary number obtained in (1) will be represented in
    memory if stored in a float variable using the IEEE-754 standard. Show the
    procedure followed to get your result (1 point).
    *******************************************************************************/
    printf("\nPrompt 9:\n");
    printf("\nSign: 0");
    printf("\nExponent: 2^(20 + 127): 10010011");
    printf("\nMantissa: 127-20: 10011101101000000000..2x107");
    printf("\nBinary float of ID: 01001001110011101101000000000000");

    printf("\n\n**************************************************************\n");

    /******************************************************************************
   QUESTION 10:
Select any of the mathematical functions in h that have domain restrictions and
write a secure piece of code to apply this function to a float variable. Trace
what your code will do on the number obtained in (9) and show the final result.
(1 point).
   *******************************************************************************/
    printf("\nPrompt 10:\n\n");

    float some_float = 1.10011101101000000000;
    float float_sqrt;
    
    if (some_float < 0.0)
    {
        printf("cant preform sqrt");
    }
    else
    {
        float_sqrt = sqrt(some_float);
        printf("The conversion is: %f", float_sqrt);
    }

    printf("\n\nif (some_float < 0.0)"
    "\n{"
        "\nprintf(cant preform sqrt);"
    "\n}"
    "\nelse"
    "\n{"
        "\nfloat_sqrt = sqrt(some_float);"
    "\n}");


    printf("\n\n**************************************************************\n");


    return 0;
}