# Unit 3: Lecture - Secure Programming with Integer and Floating Point Types

In the previous units we familiarize with the basic commands of C/C++. Starting with this unit with will go deeper into issues of security while programming. We will start with security on Integer and Floating data types. This is the only unit in which there is no relevant chapter on the textbook, except the appendices. Students should rely mostly on this lecture and the attached programs to get a grasp on the material.

As with other units, to highlight the main security points, in this document you will see paragraphs prefaced by the initials SPR. They indicate an important Secure Programming Rule that you must keep in mind when programming. This will be particularly important when a code and a number follows the initials SPR. They are the code and number assigned to this recommendation by the Software Engineering Institute at Carnegie Mellon University, a source of authoritative information on the discipline ( [link: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard] SEI CERT Coding STandard). You will also be directed to more information from the textbook and course material in paragraphs marked as Read more. References to companion C/C++ programs will also be prefaced by: “You may review the attached program(s).”

 

 [link: #fragment-1] Introduction 

 [link: #fragment-2] Wrapping and Unsigned Integers

 [link: #fragment-3] Conversion between Unsigned Integers

 [link: #fragment-4] Conversion from Unsigned Integers to Signed Integers

 [link: #fragment-5] Conversion between Signed Integers

 [link: #fragment-6] Conversion of Signed Integers to Unsigned Integers

 [link: #fragment-7] Operations with Signed Integers 

 [link: #fragment-8] Division, Remainder and Unary Negation Operations

 [link: #fragment-9] Left-Shift and Right-Shift Operations

 [link: #fragment-10] Floating Point Representation 

 [link: #fragment-11] Floating Point Values as Loop Counters

 [link: #fragment-12] Equality with Floating Point Values

 [link: #fragment-13] Mathematical Libraries 

 [link: #fragment-14] Floating Point Conversions

Introduction

In this unit we will make heavy use of binary numbers, therefore, we will review first the conversion from decimal to binary numbers and vice versa.

To convert a decimal number to binary, the procedure is to continuously divide the original number and its quotients by 2 until we have a remainder of 1. Every time we divide, we keep track of the remainders. All the remainders will form the binary number from the least significant digit to the right of the binary number, to the most significant digit to the left. For example, if we want to convert the decimal number 74 to binary, we first divide it by 2. The result or quotient is exactly 37. There is no remainder, therefore we write 0 as the least significant digit. Then we divide 37 by 2. This time the result is 18 with a remainder of 1. We write the 1 to the left of the previous remainder found. We now have 10. We continue dividing 18 by 2. The quotient is 9 with no remainder. We write a 0 to the left of 10 to obtain 010. Then, 9 divided by 2 is 4 with a remainder of 1 to be added to the left of 010, to obtain 1010. 4 divided by 2 is 2, with no remainder, adding 0 to 1010, to obtain 01010. 2 divide by 2 is now 1, with no remainder. This adds an extra 0 to the left of 01010 to become 001010. Because we cannot divide 1 exactly any further, the process stop and we add this last remainder of 1 to the beginning of the remainders we had so far to obtain the final binary number 1001010 that represents the decimal number 74 in binary.

If you observe this process carefully, you will notice that every time the number to be divided is even we add 0 to the left of the list of remainders. Every time the number to be divided is odd we add 1 to the left of the list of remainders. This may help us to device a faster way to convert a decimal number into binary. The procedure will be as follows:

Write the starting number to the right of the piece of paper and draw a line below this number from left to right on the paper. For example, we can begin to convert the decimal number 74 to binary by writing the following:

Aligned with the number, and below the line, write a zero, if the number above is even, or write a one, if the number above is odd. For our example, 74 is even, so we write a 0:

Divide exactly the number above the line by 2. Write the quotient to the left of the previous number, without decimals or remainder. In our example, 74 divided by 2 is 37:

Repeat steps 2 and 3 with the new number until the quotient becomes 1. Following these steps with our example we obtain:

 

When the quotient becomes 1, write another number 1, aligned with the quotient and below the line. The binary representation of the original decimal number will be the full number written below the line. In our example, the final result will be the binary number 1001010 that is produced below the line:

Converting a binary number to the decimal system involves the opposite process of multiplying its binary digits by powers of 2. We start by multiplying the least significant digit (bit) to the right of the number by the power zero of 2, that is the number 1 (20=1). We then multiply the digit to its left by the next power of 2, that is the number 2 (21=2). The following digit to the left of this one will be multiplied by the next power of 2, that is 4 (22=4). We continue this process for every digit in the binary number, always going from right to left (from the least significant to the most significant digit), and always increasing by one the power of 2. When the results of all multiplications are found, they are added and the result is the decimal number.

In our example, the binary number 1001010 is converted back to the decimal 74 by this process described in the following figure:

Only the powers of two that are multiplied by a 1 produce a value to be added for the final result. It would be wise for students to practice some conversions of numbers from decimal to binary systems and vice versa before tackling the contents of this unit, especially if they consider that their familiarity with this concept is a bit rusty.

Most of the problems one may encounter with data types, the main topic of this unit, come from the fact that, like anything else in life, computers have limitations. In particular, computers cannot deal directly with infinity. In mathematics, we have been introduced to the idea that, numbers are infinite, namely, there is no end to the numbers that exists and one could count, in theory. However, computers need space to represent numbers and be able to carry operations with them. As we saw in Unit 1, computers reserve certain amount of memory for every data type. This size produces a limit on the numbers that can be represented. For example, an unsigned integer data type in C/C++ uses 4 bytes that can represent all numbers between 0 and 4294967295. What would happen if we have the largest integer number in a variable and we add 1? Will it work? Where will this number go? This is the main issue we will discuss in this unit.

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205366/download?verifier=nlUT4DlhWsk7OKrwQ7XEWqdnk1fBtzNCOWNqMAee&wrap=1] AForAndDoLoopsUnsigned.cpp To obtain a glimpse to this problem. This program is a variation of the [link: https://canvas.park.edu/courses/62124/files/8205368/download?verifier=J6we3RZ7lfZJpT4sPj9X4eqYoAODrR2t8W3cCpPl&wrap=1]  HForAndDoLoops.cpp program we had last week. In both programs of these programs we use do-loops to limit the ranges of a table of powers. The main difference between these programs is that the new one uses unsigned int variables rather than just int and consequently the range of numbers has expanded. If one runs the new program to obtain the table of the 5th power of the numbers from 80 thru 90 we may get something like the following:

 

Table of the 5th power of the numbers from 80 thru 90

The table of numbers between 80 thru 90 to the power of 5 is:
------------------------------------
 80     | 3276800000
 81     | 3486784401
 82     | 3707398432
 83     | 3939040643
 84     | 4182119424
 85     | 142085829
 86     | 409302880
 87     | 689241911
 88     | 982351872
 89     | 1289092153
 90     | 1609932704
------------------------------------

As we can see the numbers for the power increases up to number 84, after which the power becomes smaller. How is that possible?

Wrapping with Unsigned Integers

The reason for this strange behavior is that we have reached the limit of the range for unsigned integers. 85 to the power of 5 is 4437053125, that is bigger than the limit of 4294967295 by 142085830 (4437053125 – 4294967295 = 142085830). If you notice the value printed next to 85 in the table above, it is one number less than this difference (142085829). What happened is that the numbers “wraparound” their range. After counting up to the maximum, they begin all over again starting at zero, that should be counted again as an additional value, up to 142085829.

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205099/download?verifier=3ksy0H4CsNIzK1F0WFxoksl20PkAi7Ej1JGb1Wa7&wrap=1] BWrappingWithUnsignedIntegers.cpp that takes a closer look at wrapping. If one runs the program, it shows the following at the beginning:

Example of Wrapping Program

-----------------------------------------------
Numbers around the largest unsigned int
-----------------------------------------------
Largest Unsigned integer value - 1: 4294967294
Largest Unsigned integer value    : 4294967295
Largest Unsigned integer value + 1: 0
-----------------------------------------------

The program is demonstrating what happens around the maximum unsigned number, UINT_MAX. This number is a constant defined in the C header file limits.h. If we add 1 to this number, it becomes zero. The explanation for this behavior can be better visualized if we see this number as it is stored in memory. An unsigned integer uses 4 bites, or equivalently 32 bits. The maximum unsigned integer will have all these bits set to 1 as shown below. When we add 1 to this number the next number will be represented by a carry-over to the next unit of 1, followed by 32 zeroes.

Because the carry-over cannot be stored in the space for the unsigned integer, it is discarded by the computer and all that is left are the zeroes. In effect, the count goes back to the beginning and that is why we call it a wrap-around. Because of this behavior we must be sure that when processing unsigned integers, they do not wrap.

SPR INT30-C

Ensure that unsigned integer operations do not wrap.

Even though this secure programming rule appears to be straight-forward, programmers must be cautious when dealing with unsigned integers. For example, the same attached program BWrappingWithUnsignedIntegers.cpp also presents two loops, one that counts up to the maximum unsigned integer number and another that counts down to 1, as shown:

Example of Two Loops in Program BWrappingWithUnsignedIntegers.cpp

limit = UINT_MAX;
start = limit - 5;
for (i = start; i < limit; i++) {
      printf(" %lu\n", i);
}

  4294967290
  4294967291
  4294967292
  4294967293
  4294967294

limit = UINT_MAX;
start = limit + 5;
for (i = start; i > 0; i--) {
      printf(" %lu\n", i);
}

  4
  3
  2
  1

While these loops are perfectly all right,  problems may appear if we change their conditional expressions. Suppose we use (i <= limit) instead of (i < limit) in the first loop. What would happen is that the loop will become an infinite loop. It will continue printing the next number, i = 4294967295, and then it will add 1 to i, producing a wraparound to zero. The conditional expression will check that (i < = limit), which will be true, since i is now zero, and the loop will continue forever. A similar situation will happen if we use (i >= 0) instead of (i > 0) in the second loop. You may see these behaviors for yourself if you uncomment the loops hidden in the program for this purpose.Special care should be taken in operations involving unsigned integers. When adding or multiplying unsigned integers, there is the risk that the result may be larger than UINT_MAX, therefore, before the operation is performed we must check that the operands will not go beyond that limit. For example, before the unsigned int variables aUint and bUnit are to be added, the following could be checked:
if (UINT_MAX – aUInt< bUInt) {
// Cannot add, do something else
}
else {
     // Proceed with the addition
}
Or, if these variables are to be multiplied, one could check:
if (UINT_MAX / aUInt< bUInt) {
// Cannot multiply, do something else
}
else {
     // Proceed with the multiplication
}
What to do in the case the operations cannot be performed because they exceed their limit is up to the application. In some cases, all one can do is to print a message informing of this condition. Sometimes an alternative value can be provided in lieu of the operation’s result, for example, a value of UINT_MAX could be used instead of the addition or multiplication.  In other situations, upgrading the operations to another data type may be required. Whatever the solution may be, it would be best to have a general policy to avoid wrapping up that applies to the whole application, especially if it is a large piece of software.Wrapping of unsigned integers may also occur when subtracting values. If we try to subtract an unsigned integer from a smaller one, the result will not be a negative number, but it will wrap backwards to the largest values in the range. To avoid this behavior when try to subtract the variable bUInt from the variable aUInt, we could also check:
if (aUInt< bUInt) {
// Cannot subtract, do something else
}
else {
     // Proceed with the subtraction
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205087/download?verifier=IidaFPUuMW4qIKEp5cg1mX7GGvL2GsqF79nPBmRj&wrap=1] CProblemsWithUnsignedIntOperations.cpp that demonstrates these operations.

The operations we just discussed involved unsigned integers with a “normal” precision. Similar comparisons should be made for operations involving unsigned integers of long, short or char precisions. They will use their own maximum values. These values, as defined in the C header file limits.h in the Microsoft Visual Studio implementation, are displayed in the following table:

Constants for Unsigned Integers

Name
Value
Description

ULONG_MAX

4294967295
Maximum value for unsigned long int

UINT_MAX
4294967295
Maximum value for unsigned int

USHRT_MAX
65535
Maximum value for unsigned short int

UCHAR_MAX
255
Maximum value for unsigned char

We will talk more about these constants in the following section. Characters who use the constant UCHAR_MAX will be studied in a future unit.

Conversion between Unsigned Integers

This and the next section will discuss the following secure programming rule:

SPR INT31-C

Ensure that integer conversions do not result in lost or misinterpreted data.

In a previous unit we reviewed the idea that we can use type casting to convert variables of different types, especially when we want to transfer data from a higher precision data type onto another with lower precision. When doing this, there is always the risk of losing information when the recipient data type is not able to represent the number fully. In this section, we will explore this possibilities, in regards to the conversion of unsigned integers.

Like with any other integer data type, C/C++ allows unsigned integers to come in four precisions: long, “normal”, short and char.  Generally, long numbers will have more precision than “normal” numbers, these in turn will have more precision than short numbers, and short numbers will have more precision than char numbers. Saying that they have more precision means that they can represent more numbers. It also means that they use more bytes to represent a number. However, C/C++ leaves the decision of how many bytes are needed for each type to the compilers and the specific platforms where those compilers are going to operate. In particular, the version of Microsoft Visual Studio that we are using in this course uses the same number of bytes to represent long and “normal” types, a number that is larger than the one used to represent short and char types. As we saw in a previous unit, an unsigned long int and an unsigned int use 4 bytes for representation, an unsigned short int uses 2, and an unsigned char uses 1.  As a consequence, the largest number for unsigned long int is the same as the largest unsigned int, and this number is larger than the maximum number for unsigned short. The maximum number for unsigned short is, in turn, larger than the maximum number for unsigned char.. These largest numbers that correspond to the unsigned long, “normal”, short and char precisions are stored in the constants ULONG_MAX, UINT_MAX, USHRT_MAX, and UCHAR_MAX shown in a previous table.

Because of these differences on size, whenever an unsigned integer variable of larger precision is going to be converted to another unsigned type of lower precision we must check if the number it contains can fit in the lower precision type. For example, if the unsorted long int variable named uLInt is to be converted to an unsigned short int type, the following must be checked:

if (USHRT_MAX < ULInt) {
     // Cannot be converted without losing numbers
}
else {
     // Conversion to unsigned short int is safe
}

Similar precautions must be taken when converting long or “normal” precision to short or char precision, and from short precision to char precision. One should also consider problems in conversions from long precision to “normal” precision if one wants to write a portable program, because, even if they have the same size in our implementation, this may not be true in other versions of the compiler.

Conversion from Unsigned Integers to Signed Integers

Additional problems may be present when one tries to convert unsigned integers to signed integers. Signed integers use the most significant bit of its representation for the sign. A zero in the most significant bit means a positive number, while a 1 means a negative number. Not only that, in most computers today, negative numbers are also stored in what is known as the two’s complement format. A negative number in this format is obtained by swapping the bits of the positive number and adding 1 to the result. For example, if the positive number 74 were stored in a byte (8 bits), its representation would be 0100 1010. The number -74 would be obtained by changing all zeros to ones and vice versa (1011 0101), then finally adding 1 to produce 1011 0110, as shown below:

The final number has a 1 in the most significant bit to the left, indicating that it is a negative number. To obtain its value in the decimal system, the procedure to be used in this two’s complement format is similar to the one used to convert binary numbers to decimal: each binary digit is multiplied from right to left (least significant to most significant digit) by an increasing power of 2, starting with 20=1 and all the results are added. The only difference, is that we must assign a negative value to the most significant bit. For example, to get the number -74 from (1011 0101) we do:

A negative signed integer represented in two’s complement is also ready for operations. Adding 200 to -74 will produce 126 as shown:

Because a signed integer uses one bit for the sign, the range of positive numbers it can represent is more restricted than for the unsigned integers, even when they use the same number of bytes to represent a number. For example, the UINT_MAX number cannot be converted to a signed number. As we saw above, UINT_MAX is represented by 32 bits, all set to 1. If we convert these number to signed int, it will actually wrap around to a value of -1. This is because the signed integer will be using two’s complement format. Therefore, the most significant bit will be multiplied by -231=-2147483648. All other bits will be multiplied by their corresponding power of two and their sum will add up to 2147483647. When adding these two values we obtain -1 in the decimal system. 

We can further observe the wrap around effect if we convert the largest positive number we can represent with a signed number and add 1. As with unsigned integers, the maximum values for signed integers are described in the C header file limits.h. This file contains the constants LONG_MAX, INT_MAX, SHRT_MAX and CHAR_MAX with the values for the largest signed numbers in long, “normal”, short and char precisions, respectively. Let us use the value of SHRT_MAX that is 32767 to show the wrap around. This value is represented in 16 bits (2 bytes) with a zero in the most significant bit (for positive numbers) followed by 15 ones. If we add 1 to this value we obtain a 1 followed by 15 zeros (a negative number), as follows:

This is the smallest number that can be represented by the signed short int. Its value in the decimal system is obtained by multiplying its most significant bit by -215=-32768.

Because of this behavior, whenever we convert an unsigned number to a signed one, we need to check if the number it contains can fit in the signed variable.  As before, this can be done with a conditional statement as the one below that prevents the unsigned short int uSInt to exceed the limit of a signed short integer:

if (SHRT_MAX < uSInt) {
// Cannot be converted without losing numbers
}
else {
     // Conversion to signed integer is safe
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205101/download?verifier=0zPSfAVZnBLvtTKOpE7YdKGfHTX1paUFuM7Zq9sD&wrap=1] DUnsignedToSignedConversions.cpp for some examples of conversions of unsigned integers.

 

Conversion between Signed Integers

Similar issues arise if one tries to convert a signed integer of a higher precision onto another signed integer of a lower precision. As before, we need to be certain that the number contained in the original signed integer can be represent with a reduced byte size for the lower representation. An added consideration is that now the original number not only could be larger than what is allowed, but also smaller than a minimum number, since numbers can also be negative.  

Once again, the C header file limits.h contains the constants LONG_MIN, INT_MIN, SHRT_MIN, and CHAR_MIN with the values for the smallest signed numbers in long, “normal”, short and char precisions. These values should be used to check the limits of the conversion. For example, if we want to convert a signed int variable sInt into a signed short int the following conditional statement could be used:

if ((SHRT_MAX < sInt)|| (SHRT_MIN > sInt) {
     // Cannot be converted without losing numbers
}
else {
     // Conversion to signed short integer is safe
}

 

Similar conditions should be written in other cases for the appropriate precision to which the value is to be converted. If the conversion is forced, regardless, the excess bit will be discarded and the original number may be lost. For example, converting the signed long integer LONG_MIN = -2147483648, represented in binary as a 1 in the most significant bit followed by 31 zeroes into a signed short int will discard the 16 bits most significant bits and leave the last 16 zeroes that represent the decimal number 0.

Conversion of Signed Integers to Unsigned Integers

There are no problems converting non-negative signed integers to unsigned integers of the same precision. Problems like the ones shown in the previous section may occur if converted to unsigned integers of lower precision. Those cases should also be checked before the conversion takes place to guarantee than the unsigned integer has enough space to hold the signed number.

Naturally, negative signed integer numbers cannot be converted onto unsigned integers. This situation must also be avoided with a conditional statement like the following one that checks if the signed integer variable sInt is negative:

if (sInt <0) {
     // Cannot be converted to unsigned int
}
else {
     // Conversion to unsigned integer is safe
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205092/download?verifier=cN4hgwTa8Esr4HyHR6ltaJCbiYYoVLPZNkw8MMqd&wrap=1] ESignedToUnsignedConversions.cpp for some examples of conversions of signed integers.

Operations with Signed Integers

We initially saw that we need to prevent overflowing in operations with unsigned integers. We should have the same precautions with signed integers, but this time we should prevent that operations end up producing numbers larger than the maximum numbers or smaller than the minimum numbers, that are negative.

Before adding signed integers, we must check that the result will be no larger than INT_MAX or smaller than INT_MIN.  For example, before the signed int variables sInt1 and sInit2 are to be added, the following could be checked:

if (((sInt2 > 0) && (sInt1 < (INT_MAX – sInt2))) ||
    ((sInt2 < 0) && (sInt1 < (INT_MIN – sInt2)))) {
     // Cannot add, do something else
}
else {
     // Proceed with the addition
}

Similar conditions could be checked if the signed integer sInt2 were to be subtracted from the signed integer sInt1:

if (((sInt2 > 0) && (sInt1 < (INT_MAX + sInt2))) ||
    ((sInt2 < 0) && (sInt1 < (INT_MIN + sInt2)))) {
    // Cannot subtract, do something else
}
else {
     // Proceed with the subtraction
}

In the case of multiplication, there are four conditions to consider since the sign of the result of the multiplication depends of the sign of the operands. To multiply the signed integers sInt1 and sInt2 we could check:

if (((sInt1>0)&&(sInt2>0)&&(sInt1>(INT_MAX/sInt2))) ||
    ((sInt1>0)&&(sInt2<0)&&(sInt2<(INT_MIN/sInt1))) || 
    ((sInt1<0)&&(sInt2>0)&&(sInt1<(INT_MIN/sInt2))) ||
    ((sInt1<0)&&(sInt2<0)&&(sInt2<(INT_MAX/sInt1)))) 
     // Cannot multiply, do something else
}
else {
     // Proceed with the multiplication
}

Review the Code

You may the attached program [link: https://canvas.park.edu/courses/62124/files/8205102/download?verifier=ngZITKoTdrinaRQMo8EpDjyzScxwhlfzrDQzyiSe&wrap=1]  FProblemWithSignedIntOperations.cpp for a review of these conditional statements in action.

Similar comparisons should be made for signed operations of other precisions: long, short and char. They will use their maximum and minimum values. These values are shown in the following table that summarizes all constants used on signed integers in the Microsoft Visual Studio implementation:

Constants for Signed Integers

Name

Value

Name

Value

Precision

LONG_MIN

-2147483648

LONG_MAX

2147483647

signed long int

INT_MIN

-2147483648

INT_MAX

2147483647

signed int

SHRT_MIN

-32768

SHRT_MAX

32767

signed short int

SCHAR_MIN

-128

SCHAR_MAX

127

signed char

 

The recommendations in this section are summarized in the following secure programming rule:

SPR INT32-C

Ensure that operations on signed integers do not result in overflow.

Division, Remainder, and Unary Negation Operations

Mathematically, dividing any number by zero produces undetermined results. That is why we should never divide by zero under any circumstances. The same would apply for the remainder (modulus) operation, since to obtain the remainder of two numbers, first their integer division must be known, and that is not possible when dividing by zero. This principle is the basis for our next secure programming rule:

SPR INT33-C

Ensure that division and remainder operations do not result in divide-by-zero errors.

Before any division or remainder operation, check that the divisor is not zero with a conditional statement like this:

if (divisor == 0) {
      // Cannot divide or obtain remainder, do something else
}
else {
     // Proceed with the operation
}

A special problem occurs when trying to divide the smallest signed integer number in a precision by -1. Because the absolute value of the smallest integer in a precision is larger than the largest value in the same precision, if the smallest number is divided by -1 the result will overflow. For example, INT_MIN is -2147483648, if divide by -1 it should become 2147483648, but this is larger than INT_MAX (-2147483647), so the operation will overflow. Therefore, if the signed int variable sInt1 is going to be divided by the signed int variable sInt2, a good conditional statement to have could be written as:

if ((sInt2 == 0) || ((sInt2 == -1) && (sInt1 == INT_MIN))) 
{
     // Cannot divide, do something else
}
else {
     // Proceed with the division
}

A similar problem may arise when trying to use the unary negation operation on the smallest number in a precision. The unary negation is the operation that changes the sign of a number, variable or expression. It is actually the minus sign that we see in front of some of these operations. For example, if we have the variable a, its unary negation will be –a. When we use the dash in between two operands, we know that it means a subtraction, but if there is no operand in front of the dash, this becomes the unary negation. If the number being negated is the lowest in a precision, when negated it will produce a number largest that the maximum in that precision. For example, if we try to negate a signed short int variable sSint that contains the value SHRT_MIN (-32768) with -sSint, it will produce the value 32768 that is larger than the maximum value of SHRT_MAX (32767), and it will overflow. A conditional statement checking for this condition could be written as follows:

if (sSInt == SHRT_MIN) {
     // Cannot perform unary negation
}
else {
     // Proceed with unary negation
}

Review the Code

You may review the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205320/download?verifier=E6cvXAfRT4j5Hg2iuMzXd7CfUAdUuZ8ItqcrI15d&wrap=1] GProblemsWithIntDivandRemainder.cpp and [link: https://canvas.park.edu/courses/62124/files/8205368/download?verifier=J6we3RZ7lfZJpT4sPj9X4eqYoAODrR2t8W3cCpPl&wrap=1]  HProblemsWithUnaryNegation.cpp to review these strategies to deal with division, remainder, and unary negation.

Left-Shift and Right-Shift Operations

In this section we are introducing two new operations for integer values available in C/C++: left- and right-shift. These operations should not be applied to floating point values.

From the start, C language wanted to provide maximum control over computations to programmers. Left-Shift and right-shift are two of the operations that provide control over the actual binary representation of variables.  They actually move the bits that make up the contents of a variable to the left and to the right. The syntax for these commands are as follows:

int_expression << number_to_shift;       // left-shift

            and

int_expression >> number_to_shift;       // right-shift

where int_expression is any value, variable or expression that produces an integer value, and

number_to_shift is any value, variable, or expression that produces a non-negative integer with the number of binary digits to be shifted.

For example, suppose the unsigned short int variable uSInt contains the value 331. The left-shift operation use the symbol <<. The command to left-shift once the contents of this variable will be:

 uSInt << 1;

The variable uSInt will be represented by 32 bits (4 bytes) with a binary value of 0000 0001 0100 1011. If this variable is left-shifted, its bit pattern will move as follows:

Notice that the carry over bits shifted to the left will be discarded and the vacant positions to the right will be filled by zeroes. The effect of left shifting once is to multiply the value by 2. If a value is left-shifted n places, its value is multiplied by 2n.

On the other hand, the right-shifting of the original value of the variable uSInt once will be performed with the following command:

uSInt << 1;

This operation will produce the following bit pattern change:

The carry over bits shifted to the right will also be discarded and the vacant positions to the left will be filled by zeroes. The effect of right shifting once is to divide the value by 2 without consider a remainder. If a value is right-shifted n places, its value is divided by 2n.

The following secure programming rule should be applied to shifting operations:

SPR INT34-C

Do not shift an expression by a negative number of bits or by greater than or equal to the number of bits that exist in the operand.

In either shifting operation, the number of positions to be shifted cannot be negative because it produces undefined behavior by the compiler. Undefined behavior also happens when trying to shift a value more times than the number of bits used to represent it. When talking about unsigned integers, the number of bits to represent it is given by the size of its representation: 8 bits (1 byte) for chars, 16 bits (2 bytes) for short integers and 32 bits (4 bytes) for the “normal” and long integers in the Microsoft Visual Studio implementation. 

Negative signed integers should not be left shifted or right shifted, because the bit for the sign will be confused with the other bits in the representation. Also, when shifting non-negative signed integers, the maximum number of positions that can be shifted should be reduced by one, because the bit for the sign should not be counted. Non-negative signed integers could be shifted at most 7 times for chars, 15 times for short integers and 31 times for “normal” and long integers in the Microsoft Visual Studio implementation. Even further, the number to be shifted cannot be negative. This also produces an undefined behavior.

Because of these restrictions, before a left-shift of an unsigned short integer uSInt is performed n times, the following checks should be implemented:

if ((n<0) || (n > 16)) {
     // Cannot perform left-shift
}
else {
     // Proceed with left-shift
}

Also, when left-shifting a signed short int like sInt a number of times (n) we should check the following:

if ((sInt<0) || (n<0) || (n >= 15) ||
     (sInt > (SHRT_MAX >> n))) ) {
     // Cannot perform left-shift
}
else {
     // Proceed with left-shift
}

The first three conditional expressions prevent both operands to be negative and having to shift more than the precision for a signed short integer. The last conditional expression requires further explanation.  The secure programming rule INT32-C above requires that no operation on signed integers should result in overflow. In the case of the left-shift it means that one should not shift to the left a signed number if doing so will produce a number larger than the maximum allowed. The last conditional expression above is checking that this constraint is respected. For example, suppose that the signed short integer number 213 = 8192 is to be left-shifted 3 times as shown in the picture below:

The operation would overflow the value to zero. Rather than calculating the maximum number of left-shifts allowed, the conditional expression evaluates the right-shift of the largest number in that precision by the number of requested left-shifts. This number should be bigger than or equal to the number we want to left-shift, otherwise it will overflow when left-shifting. The largest signed short integer is SRT_MAX= 32768 = 1111 1111 1111 1111. When right-shifted three times we obtain the number 8191 as seen here:

Because the right-shifted value of 8191 is smaller than the value we want to left-shift (8192), the left-shift cannot be performed 3 times, but at most two times.

When right-shifting, the same criteria applies, no more right-shifts than the precision allowed by the representation: 16 bits for unsigned short integers, 32 bits for unsigned “normal” and long integers, 15 bits for signed short integers and 31 bits for signed “normal” and long integers. Also, with signed integers, no operand could be negative.

Review the Code

You may review the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205093/download?verifier=WokPITXu8jG16cvOQ88PsRtuerHiBYbWmxY1S153&wrap=1] IProblemsWithLeftShifting.cpp and [link: https://canvas.park.edu/courses/62124/files/8205106/download?verifier=vaS72nhUuhpgA8fMdGiuQ8QWAtq9P8jvfX4yJ2wh&wrap=1]  JProblemsWithRightShifting.cpp to explore these issues with left and right shifting.

Floating Point Representation

Floating point types (float and double in C/C++) offer the opportunity for programmers to use a larger range of numbers than integer types. It also allows for the inclusion of decimal numbers. A float type may contain numbers in the range of -3.4x1038 thru 3.4x1038 and a double type may contain numbers in an even larger range, from -1.7x10308 thru 1.7x10308. However, this increase in capabilities is obtained at the expense of precision in the individual numbers. The computer may not be able to perform operations between two decimal numbers if there is a large difference in their orders of magnitude. Like with integers, the reason is the way floating point numbers are represented in memory.

The most widely used representation of floating point numbers is given by the IEEE-754 standard. Most platforms and compilers use this standard, Microsoft Visual Studio among them. We will review this standard with an example. Let us consider the decimal number 12.75. This number, written as a binary number will be 1100.11. The following figure explains why:

As we can see, the decimal part is also made up of zeros and ones and, as with integer numbers, they represent powers of 2. However, this time these are negative powers of 2: -1, -2, etc.

If we were to use this representation directly, we will need the same number of bits to represent the integer part of this number as we used when representing whole numbers, and we would need additional space to represent the decimal part. Rather than do that, the standard will move the decimal point to have only one digit in the integer part and it will save the power of 2 corresponding to this number. In our case, the binary 1100.11 would become 1.10011 x 23. This is similar to the scientific notation that uses power of 10, but because this is a binary number, we use powers of 2. With this arrangement, the standard will now store three pieces of information to save a floating point number: its sign, the exponent of the power of 2, and the decimal values in the number, 10011, known as the mantissa. Notice that we do not need to save the integer 1, because every number represented this way would begin with a 1, so it is redundant to save it. These 3 pieces of information should fit the number of bits given to the float and the double data types.

The float data type uses 32 bits in C/C++. The first bit (most significant bit) is used for the sign: 0 for positive, 1 for negative. The following eight bits are used to store the exponent of the power of 2. This allows for 256 possible exponents. Because exponents could also be negative when numbers are smaller than 1, rather than saving a sign for the exponent, the eights bits are used to store the exponent plus 127. The last 23 bits are used to store the mantissa. The following figure shows our decimal 12.75 stored in a float data type:

The sign bit is set to zero. The following 8 bits contain the added exponent (3+127) =130. And the mantissa 1101, that translated to a decimal number is equivalent to 19/32 = 1/2+1/16+1/32.

A similar arrangement is used for the double data type, but because it used 64 bits in C/C++, the first bit (most significant bit) is still used for the sign, but the following 11 bits are used for the exponent and the remaining 52 bits are reserved for the mantissa.

While this arrangement allows for large numbers, it makes operations to behave in somewhat strange fashion.

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205373/download?verifier=ovvGHM4GdTceMsREGEfywi3WEqSBtzsi5VzpeywT&wrap=1]  KProblemswithPrecision.cpp to see some of these problems. This program initially presents a pair of large float numbers. The first is the largest float value. This value is contained in the constant FLT_MAX in the C header file float.h. The second is the number 1x1031. When the program tries to obtain their difference (FLT_MAX -  1x1031), this produces a wrong value. In fact, the value obtained is the same as FLT_MAX, as if the operation was never computed. The same happens when the program tries to obtain the difference of the largest double number, DBL_MAX (declared also in float.h) and 1x10291. This difference is also incorrectly computed.

The reason for this problem is that even though the second numbers are large, they are still too small to modify the stored bits of larger numbers. According to the standard representation above, FLT_MAX in binary (1.111 … x2127) will be stored in a float data type with an exponent of 127 and 23 bits of ones. Only the most significant (first) 23 bits of this number are stored in the representation, so there are 104 = 127 - 23 decimal places in the number that are not stored. Similarly, according to the same standard, the number 1x1031 in binary (1.111…x2102) will be stored in a float data type with an exponent of 102 and 23 bits of decimals. Here again, only the most significant (first) 23 bits of this number are stored in the representation, and 79 = 102 - 23 decimal places in the number are not stored. As we can see in the following diagram, all the numbers used to represent 1x1031 lie in the region of FLT_MAX that is ignored. Therefore, when we try to add both numbers, the result is not storable.

  

A similar situation happens with the double data type. Therefore, when doing calculation with floating point data types, programmers should be extremely cautious and avoid possible mismatch in the order of magnitudes of the operands.

Unfortunately, there are no general rules that can be applied to all situations, but there are known common problems that can be avoided. We will discuss some of them.

Floating Point Values as Loop Counters

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205375/download?verifier=KQ2Za3wnoBlCnxgmjnALQFLCCwvA5YQNIqUPKZgb&wrap=1] LProblemsWithFloatCounters.cpp to see the first situation we will discuss. This program presents cases involving the use of floating point variable as loop counters. In the first one, the following loop tries to print values of a variable x from 0.1 to 1.0 with the following loop:

for (float x = 0.1f; x <= 1.0f; x += 0.1f) {
    printf(" In loop step %d \tx=%f\n", i, x);
    i++;
}

Unfortunately, the loop does not print the last value of 1.0 because the numbers are represented in binary, and the calculations may not yield exact values in the decimal system. In this case, 0.1 is represented by the number 1.10011001100110011001101x2-4 in IEEE-754 standard, that is not exactly 0.1 in decimal, but an approximation, 0.100000001490116. The loop After 9 loop steps this number will be slightly larger than 1.0, the loop condition will be false and a value of x = 1.0 will never be printed.

The same program also shows a potential infinite loop:

 i = 1;
 for(float x = 100000000.0f;
      (x <= 100000010.0f)&&(i<=20); x += 1.0f) {
          printf(" In loop step %d \tx=%f\n",i,x);
          i++;
      }

The loop is stopped because of the variable i, but if this variable were not present, the loop will be infinite. The reason is that the value being used to increment the floating point counter x (1.0) is too small in comparison to the initial value of x (1.0x108). The value of variable x never changes with the addition. This is similar to what happened when we tried to subtract a value from FLT_MAX above.

Because of these problems, the following secure programming rule must be enforced:

SPR FLP30-C

Do not use floating-point variables as loop counters.

Equality with Floating Point Values

Another common problem in dealing with floating point types is equality comparison. Suppose we have two floating point variables, value1 and value2, and we want to know if they are equal with the following command:

 if (value1 == value2) {

This conditional statement will only become true if the IEEE-754 representation of the numbers in both variables is exactly the same. This may not be appropriate in all situations. For example, consider the number 1/7. We may obtain this number directly by dividing 1 by 7. We may also produce this number by subtracting 13/7 from 2. Mathematically, both numbers should be the same. The following sentences may be used to produce these two values:

double value1 = 1./7.;
double value2 = 2.-(13./7.);

When evaluated, these variables will contain the following values: value1 = 0.14285714285714284921 and value2 = 0.14285714285714279370. They are very similar. The difference only starts in the 17th significant digit. However, if we compare them using the symbol == as in the conditional statement above, the result will be false. They are not the same number.

Because of this situations, it is never advisable to use == to compare directly floating point variables. A better approach is to use an additional number for tolerance. Rather than compare the variables directly, we check if the absolute value of their difference is smaller than the tolerance. In our case, a constant TOL=10-15 could be used effectively in the following statement:

 if (fabs(value1 - value2) < TOL) {

The function fabs calculate the absolute difference of an expression and it will be reviewed in the following section. With this statement, when the absolute difference between value1 and value 2 is calculated to be 5.551x10-17, this value will be smaller than the tolerance, and the contents of both variables may be consider equal.

The value for the tolerance must carefully chosen to match the order of magnitude of the values being compared. For example, a value like 10-15, used above, will not be appropriate if the numbers being compared are smaller than this tolerance.

Review the Code

 You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205377/download?verifier=D4HuYkg94Kju73eWbjM1ZxIJnXDQxrCC0WEtZzQo&wrap=1] MProblemswithFloatEquality.cpp that demonstrates this issue with equality.

A related issue to this topic is division by zero. In here, as we discussed in the section of Division, Remainder and Unary Negation Operations, the spirit of secure programming rule SPR INT33-C applies.

SPR INT33-C

Ensure that division do not result in divide-by-zero errors.

We achieve this goal by checking that the divisor is not equal to zero, but because floating point types cannot be compared directly for equality, we may use tolerance, as follows:

if (fabs(divisor) < TOL) {
     // Cannot divide, too close to zero. Do something else
}
else {
     // Proceed with division
}

Mathematical Libraries

C and C++, each offer programming libraries with the most commonly used mathematical functions. In order to use these functions in C, the library math.h must be included in the program. The functions in this library require the programmer to provide appropriate input values, that are within the domain of the function. For example, if we want to calculate the square root of a number, we only can do it if the number is non-negative (zero or larger). Namely, the domain of this function are all non-negative numbers.

The following table describes the most important mathematical functions in math.h:

 

Mathematical Functions in math.h

Function

Description

Domain Restrictions

fabs(x)

Absolute value of x

None

sqrt(x)

Square root of x

x>=0

log(x), log10(x), log2(x)

Logarithms in base e, 10 and 2 of x

x>=0

pow(x,y)

x to the yth power

(x >0) || (x==0 &&y>0) || (x<0 && y is integer)

ceil(x)

Smallest integer that is >= x

None

floor(x)

Largest integer that is <= x

None

sin(x), cos(x), tan(x)

Trigonometric functions sine, cosine and tangent of x

Angle x should be in radians

asin(x), acos(x)

Inverse of sine and inverse cosine of x

(-1 <= x && x<=1)

atan(x)

Inverse tangent of x

None

atan2(y,x)

inverse tangent of (y/x)

(x!=0 && y!=0)

isnan(x)

Returns a non zero integer value if x is not a number, otherwise, it returns zero

None

isinf(x)

Returns a non zero integer value if x has an infinite value, otherwise, it returns zero

None

 

Before using functions with domain restrictions, a programmer must verify that the values to be sent to these functions are within their respective domains. For example, before using the sqrt function on a variable x, we may use the following conditional statement:

if (x < 0.0) {
     // Cannot use sqrt. Do something else
}
else {
     // Proceed with sqrt(x)
}

A function like pow(x,y) has various restrictions, but not all of them should be checked with a conditional statement. For example, the condition that (x<0 && y is integer) means that if x is smaller than zero, y must be integer. Here the programmer must be sure that the variable y is of integer data type. There are no conditions to be coded. If on the other hand, x is zero, the following condition applies: (x==0 && y>0). A programmer could use a conditional statement to be sure that that y is bigger than zero, but in this case, the result will always be zero, so there is really no need to perform the operation. It would be best just to return zero. The only real case to check is if x is larger than zero. If that is the case, the function pow(x,y) can be computed, no matter the value of y.

Some functions, like log, log10 and log2 may produce infinite values on certain inputs. In the case of these functions, an input of zero will produce this result. These are known as pole errors and can be prevented the same way domain errors are prevented, by restricting access to these input values, as the example with sqrt above shows. However, if they are not prevented, a variable may hold a value of infinity. The IEEE-754 standard designates two special values for infinity: 2128 for positive infinity and -2128 for negative infinity. The C header file math.h also offers the constant INFINITY that contains the positive infinity, and the method isinf to test if a value, variable, or expression is infinite, either positive or negative. This function will return a non-zero integer if the variable is infinite, or integer zero if not.

Similarly, the method isnan would test if a value, variable or expression is not a numeric (NaN). Some mathematical operations may return this result. For example if we try to subtract INFINITY from INFINITY. NaN is represented as the number 1.1x2128 in IEEE-754 standard, and the C header file declares a constant with this value named NAN.

Keep in mind that the handling of infinity and NaN may change in different implementations of compilers.

Some other functions may return a value that is not infinite, but it is too large to be represented. For example, (2.5)1000 is larger than the maximum double value DBL_MAX. In those cases, the results obtained cannot be trusted. The way we can check if the values obtained from a function are reliable is by checking the value of the integer variable errno. This variable is part of the C header file errno.h, and it needs to be included in the program to have access to it. Before calling a function that may produce a large number we must set the value of the variable errno to zero. After evaluating a function, if the number obtained is too large or if there was any other problem calculating the function, the variable errno will have a value different than zero. This value can be queried with a conditional statement, like the following:

errno = 0;
result = pow(x, y);
if (errno) {
      // result of function was too large. Do not use it.
}
else {
     // function produced a good result value.
}

Notice that as with the functions isinf and isnan, the conditional statement above uses the C rule that a value of zero is considered as false, while any other number is considered true. The value of errno changes every time a new function is evaluated, so to be correct, it must always be initialized to zero before the function is evaluated and checked immediately after the function was evaluated. However, be sure all other errors are dealt with before acting on errno. This behavior is prescribed on the following secure programming rule:

SPR ERR30-C

Set errno to zero before calling a library function known to set errno, and check errno only after the function returns a value indicating failure.

C++ also provides a library of equivalent mathematical functions. To access these functions the cmath library must be included. Because we are mainly interested in C structures, we will not discuss this library any further. The only recommendation at this point, is not to mix the use of both libraries together in one program. As with mixing the use of input/output libraries, the results may be undetermined. 

The following secure programming rule summarizes the recommendations in this section:

SPR FLP32-C

Prevent or detect domain and range errors in math functions.

 

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205379/download?verifier=XKb4X99mR6E5uzXbHdTlHZXq8qhkfMZHBpsQakGw&wrap=1]  NUseOfMathFunctions.cpp that shows the use of mathematical functions in C.

Floating Point Conversions

Floating point type values may be converted onto integer values, if the loss of decimal values is not of concern. To make this possible the programmer must be certain that the number they want to convert will fit in the format for the integer representation. For example, if the contents of a float variable are to be converted onto a signed integer, the value should not be bigger than INT_MAX or smaller than INT_MIN, the limits of the range for a signed integer. However, here again, the story is a little more complicated since a floating point value closer to the limits of a signed integer may not be able to be properly represented.  

If we try to create a float variable containing the value INT_MAX (2147483647), the closer we are going to obtain is 2147483648, because it is equivalent to 231, a value that can be easily represented in the IEEE-754 standard. Trying to represent INT_MAX exactly would be the equivalent to trying to evaluate 231 – 1 = 231 - 20. The difference on the numbers of bits used to represent these two numbers (31-0=31) is larger than 23, the number of significant bits that are stored for a float data type in IEEE-754 standard. Therefore, the subtraction will not be executed correctly and all that we obtain is 231. If we try to convert this number to a signed int, we will obtain a wraparound to the negative values.

The largest float number we can convert to signed integer is 2147483520.0 = INT_MAX-127.0, because that is the closest number to INT_MAX that is smaller than INT_MAX and can be properly represented in the IEEE-754 standard.

Converting the smallest number signed integer number gives no problems because is a multiple of 2: INT_MIN=-231.

With these issues in mind, before trying to convert a float number like aFloat into a signed integer we could check the following:

if ( isnan(aFloat)) || {
    (aFloat > (INT_MAX -127)) || {
    (aFloat < INT_MIN) || {
    // Cannot convert float to signed int
}
else {
     // Proceed with conversion of float to signed int
}

The first conditional uses the function isnan from the C header file math.h to checks if the value of aFloat is indeed a number. This may be eliminated if the programmer is certain that this will not be the case.  

Converting a float data type into and unsigned integer has similar constraints. If we try to store UINT_MAX into a float variable, the value stored will be UINT_MAX + 1 = 232. This is the closest number that can represented with the IEEE-754 standard, but it cannot be properly converted later into unsigned int. The largest number that can be represented properly in IEEE-754 standard and that is also smaller than UINT_MAX is actually UNIT_MAX - 255. Unsigned integers do not take negative numbers, so the smallest float number to be converted is zero. With these considerations, before converting a float value like aFloat into unsigned int one could check the following:

if ( isnan(aFloat)) || {
    (aFloat > (UINT_MAX - 255)) || {
    (aFloat < 0) || {
    // Cannot convert float to unsigned int
}
else {
     // Proceed with conversion of float to unsigned int
}

Review the Code

You may review the correct way to do these conversions with the attached program  [link: https://canvas.park.edu/courses/62124/files/8205382/download?verifier=qyQnBjhK9ZpcFFa71htAsWqUjyYqUi7985tNKpDL&wrap=1] OFloatToIntegerConversions.cpp.

Compilers and operating systems may have ways to represent floating point types, therefore, the largest and smallest numbers that can be properly converted from float to integer need to be properly determined in each implementation. Similar considerations should be taken into account when converting double data types onto integers. The largest and smallest numbers that can be properly converted from double to integer may be different than the ones mentioned above.

The points discussed in this section, so far, can be summarized with the following secure programming rule:

SPR FLP34-C

Ensure that floating-point conversions are within range of the new type.

Given that floating point data types handle a larger range of numbers than integer data types, one may think that any number on an integer data type could be easily converted to a floating data type. However, the issue of precision makes this also tricky. We have already seen how INT_MAX cannot be converted to a float data type without losing precision. Similarly, the largest integer UINT_MAX will suffer similar problems when converted to float. The reason is that an unsigned integer may use 32 bits to represent a number, while a float may only represent the 24 more significant bits of a binary number (23 bits for the mantissa plus the unsaved leading 1). Therefore, if we need to convert integer numbers onto floating point numbers without losing precision, the solution is to convert them to double data types, because they use 52 bits for the mantissa and 1 unsaved leading 1. This precision is enough to hold any converted integer number. This recommendation would satisfy the requirement of our last secure programming rule in this unit:

SPR FLP36-C

Preserve precision when converting integral values to floating-point type.

While this lecture includes all relevant topics for this unit, the textbook also contain some additional information on its appendices. Appendix B4 explains the math.h library, while appendix B11 talks about the limits.h and float.h libraries.

Review the Code

Read more about this topic in Appendices B4 and B11 of the textbook.

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
