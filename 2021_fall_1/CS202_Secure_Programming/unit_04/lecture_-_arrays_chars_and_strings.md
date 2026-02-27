# Unit 4: Lecture - Arrays, Chars and Strings

In this unit we will review one of the most important data structures of C/C++ (and many other languages), the array. We will then talk about characters and end up by combining both topics with the study of Strings.

As with other units, to highlight the main security points, in this document you will see paragraphs prefaced by the initials SPR. They indicate an important Secure Programming Rule that you must keep in mind when programming. This will be particularly important when a code and a number follows the initials SPR. They are the code and number assigned to this recommendation by the Software Engineering Institute at Carnegie Mellon University, a source of authoritative information on the discipline ( [link: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard] SEI CERT Coding STandard). You will also be directed to more information from the textbook and course material in paragraphs marked as Read more. References to companion C/C++ programs will also be prefaced by: “You may review the attached program(s).”

 

 [link: #fragment-1] Array Declaration and Initialization 

 [link: #fragment-2] Array Usage

 [link: #fragment-3] Array Security 

 [link: #fragment-4] Characters

 [link: #fragment-5] Strings

 [link: #fragment-6] Wide Strings and Strings in C++

 [link: #fragment-7] Bi-dimensional Arrays

Array Declaration and Initialization

An array is a collection of consecutive values of the same data type (known as elements), all referenced by a single identifier (the array’s name). Arrays are designed to keep various pieces of similar data together without having to name each one individually.  Instead, we only have one name for the whole set and we give a unique number to each individual element.

The syntax to declare an array in C/C+ is similar to the declaration of any other variable:

            dataType  identifier[maxSize];

where dataType is the datatype of each and every element of the array,

                        identifier is the name of the array, and

                        maxSize is an integer with the maximum number of elements the array may have.

Once an array is declared, the operating system that runs the program separates a chunk of memory with a size equal to the multiplication of the specified maxSize by the number of bytes required to represent a variable of the given datatype. For example, the following declaration creates an array of 5 integer variables named anArray:

int  anArray[5];

Because each individual integer variable is represented by 4 bytes, the operating system will separate an area of 5x4 = 20 bytes for the array and name it anArray. This is how RAM may be allocated:

The diagram shows 5 consecutive boxes, each containing 4 bytes, however, the declaration does not clear that area in RAM, nor put any initial value inside it (as indicated by the question mark). The previous contents of this area in memory may still remain in those positions. Like any other variable, to be used, each element of the array must be initialized. One way to do so is with direct assignment of values:

anArray[0] = 24; anArray[1] = 47;
anArray[2] = 73;
anArray[3] = 36;
anArray[4] = 65;   

This changes the values of the elements as shown:

 

Notice that we refer to each element of the array with an integer number, known as the index or offset, that indicates how far is the element from the beginning of the array. It begins with the first element at position zero, because its distance to the beginning is null. The last element of the array is always the size of the array minus 1. In this case, the last element is 4 = 5-1. This is its distance from the first element.

If the values of the array elements are known from the start, initialization can also be done at declaration using a list to specify each value, in which case the size of the array maybe omitted, like this:

int  anArray[] = { 24, 47, 73, 36, 65 };

If on the other hand, a value for the size is given, it should be equal or bigger to the number of values for the elements in the list, as in the following:

int  anArray[5] = { 24, 47, 73, 36, 65 };

OR

int  anArray[7] = { 24, 47, 73, 36, 65 };

In the second declaration, only the first 5 elements are initialized. Some compilers may initialize the last two elements to zero, but secure-minded programmers should not rely on this fact, but provide specific values to initialize all elements of an array before use.

Array Usage

Many of the activities involving an array are usually a repetition of a set of steps onto each of its elements. For these tasks, loops are a natural way to manipulate the arrays, and in particular for-loops. For example, if the elements of an array are going to be initialized with values that follow a pattern, like with odd numbers, the following for-loop could be used to initialize its first 5 elements:

for(int i=0; i<5; i++) { 
    anArray[i] = 2 * i + 1;
}   

In a similar manner, to print the elements of the array we could use:

for(int i=0; i<5; i++) { 
    printf(“anArray[%d] = %d\n”, i, anArray[i]);
}   

You may review the attached programs [link: https://canvas.park.edu/courses/62124/files/8205388/download?verifier=vEPQNC8vw0WtJbBjjB95auRreXdEqTiIFBcBQTDD&wrap=1]  AArrayManipulation1.cpp and [link: https://canvas.park.edu/courses/62124/files/8205391/download?verifier=cvWXr2RkwnLlfSMfxWOUaDvz95FGeZWkHLaefhU7&wrap=1]  BArrayManipulation2.cpp for more examples of the use of loops with arrays. These programs show the calculation of the minimum, maximum, total and average values of the elements for various types of arrays. In both programs, a constant for the size of the arrays is declared in a macro:

#define SIZE 10

This is a common strategy to handle array sizes, since it allows a change of size with recompilation. Unfortunately, array sizes are static and do not change at will when the program runs. Once declared, the size of the array will remain constant for the life of the array. That is why most applications use a maximum expected value for an array’s size and then keep an additional variable that indicates the actual number of elements the array contains. Arrays that are more dynamic, and that can be created of any given size while the program is running, will be reviewed in future units.  

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205184/download?verifier=3OSBvSgXE9uXekMWhAeJHSCJKrgr869j8ejJTCfH&wrap=1] CArrayManipulation3.cpp that shows a variation of ArrayManipulation1.cpp in which the variable realSize is used to keep track of the actual number of usable elements in the array. As it can be seen in these examples, for every array in C, we need to have a variable (or a constant) to tell us how big the array is, and another one to tell us how many of the elements in the array have useful information. In some other languages, there are functions that may tell us these values while the program is running, but that is not possible in C. This is why we always need to keep these values in variables.

Among other things, the program BArrayManipulation2 show us the use of parallel arrays. Parallel arrays are arrays of the same size in which the data contained in elements with the same index may be related. The arrays named iArray, fArray, and dArray in ArrayManipulation2.cpp are treated as parallel arrays. They have the same size and the element i of each of these arrays is treated as if they are related to each other. Think for example that, if the information in these arrays is data from patients, in which iArray contains their ID, fArray contains their weight, and dArray some medical measurement, then the fifth patient has its ID in  iArray[4], its weight in fArray[4], and  her/his medical measurement in dArray[4]. If you are confused on why the fifth patient uses the index 4, remember that the first patient has the index 0.  The advantage of using parallel arrays for related data is that we do not have to keep separate variables for the sizes of each array. Notice that all arrays in the program use the same SIZE variable.   

Array Security

The main security concern one must have with arrays is not to try to access data beyond the limits of their size. We use an index to locate a particular element in the array. This index may be a number, variable, or expression that should produce an integer within zero and the maximum number of elements in the array (either the true maximum or the maximum of available elements, depending of the application).

The last example above shows a loop that prints the 5 elements of anArray. If the conditional expression in that loop were to change to (i<7), the loop may still print something, but it will include the contents of memory passed the last element of the array. This mistake should be avoided for two reasons. Firstly, for the purposes of the program itself, it is incorrect to go beyond its data. This is an indication that something does not agree. Either the array size should be changed or the loop’s conditional expression is the one at fault. Secondly, and more importantly, going past array boundaries creates vulnerabilities in the system that can be exploited by potential attackers. In the example above, we are only printing the elements of the array, but if the loop steps include execution of commands for each element, these actions would be performed in areas of memory that are supposed to be out of reach and that may compromise other programs and the whole system.

We can be certain of the limits of most loops when we have control over the values of their variables. In the case above, the programmer has the ability and responsibility of providing the correct limits (starting with i equals to 0 and finishing when i reaches 5). However, there are occasions when the limits are handed to the loop from an external source, a user or another program. In those cases, the programmer must check that these limits will be within the range of the array. The following code shows an example where the integer variables start and end have been supplied by an external source:

printf (“ From which element do you want to start to print?”); 
scanf(“%d”,&start); 
printf (“ In which element do you want to end printing?”); 
scanf(“%d”,&end); 
if ((start<0) || (end>5)){ 
    printf (“ Request out of bounds”);
} 
else { 
    for(int i=start; i<end; i++) { 
        printf(“anArray[%d] = %d\n”, i, anArray[i]);
}   

SPR APR 30-C

Do not use out-of-bounds indexes.

Characters

So far in this course we have mainly dealt with numbers, but letters and words are also very important when writing programs, so here we will start with the most basic unit of text, the character. Characters are individual letters, digits, and symbols that have been codified as integer numbers between 0 and 255. This means that each character only needs 1 byte (8 bits) to be represented. The code used is the ASCII code, of which there is a sample in the table below:

Selected ASCII codes

ASCII code

Character

ASCII code

Character

ASCII code

Character

ASCII code

Character

65

A

97

a

48

0

0

‘\0’ (null)

66

B

98

b

49

1

9

‘\t’ (Horizontal TAB)

67

C

99

c

50

2

10

‘\n’     (New Line)

68

D

100

d

51

3

13

(Carriage Return)

88

X

120

x

52

4

32

(Blank space)

89

Y

121

y

53

5

92

\

90

Z

122

z

54

6

43

+

 

For a complete list of ASCII codes you may review the websites on sites like  [link: https://ascii.cl/] https://ascii.cl/. The program  [link: https://canvas.park.edu/courses/62124/files/8205187/download?verifier=SK8tfjZBB40TG0fgXfoGhi7VPWpHJue088Pp9tdL&wrap=1] DCharTable.cpp also shows the printable characters.

When written individually in a program, characters must be surrounded by single quotes, like ‘A’ and ‘a’.

An important thing to remember is that every letter has a corresponding integer number that represents it and they are ordered according to the English alphabet, so the code for the letter ‘A’ is smaller than the one for any other upper case letter. The same happens with lower case letters and digits. The letter ‘a’ has a smaller ASCII code than any other lower case letter, and the digit ‘0’ has a smaller ASCII code than any other digit. Any digit is smaller than any upper case letter and any upper case letter is smaller than any lower case letter. This hierarchy is helpful when organizing letters and words, and it is similar to the way dictionaries are organized. This is called the lexicographic order of the characters.

Many characters in the ASCII code have no printable representation and may be used as commands of some sort. The ASCII code 7, for example, produces a BEEP sound when printed, so is known as the bell character. The ASCII code 10 (‘\n’) also does not print a character, but indicates that future printing should begin on the next line, and therefore is called the new line character. Do not be confused by the fact that this character is represented by two characters: the slash (\) and the letter ‘n’. Together they are treated as a single character. Similarly, tabs are written as two characters, the slash (\) and the letter ‘t’, but they are only one character represented by the ASCII code 9. The slash alone is the ASCII code 92. A character that will be very important for us when dealing with words is the null character, NUL or ‘\0’. This is the ASCII code we will use to indicate when a collection of characters, known as a string has ended.

In C/C++, characters are declared with the char data type. This type allocates 8 bits (1 byte) for each character and it is considered an integer data type, therefore it can be treated as a character or as an integer number at any point in time. C/C++ uses the char data type of 1 byte as their integer data type for values smaller than the short data type, which uses 2 bytes. Applications like image analysis may use char variables to store the values of pixels in images. These values are usually between 0 and 255.

When treated as characters, char variables can be printed with the %c format in printf. Their code could also be printed as integer numbers if one uses a format for integers, like %d or %u. If treated as a number, it could be signed or unsigned, just like any other integer data type. As a character, their value is just interpreted as code in the ASCII table, but as a number it could be part of operations like any other integer number. The following piece of code shows how these two roles are interchangeable at any time:

char letter1 = 'A'; 
char letter2 = 'a'; 
letter1 = letter2 + 3;  //using both char variables as integers 
printf("is letter %c before letter %c? ", 
         letter1, letter2); // printing as characters
if (letter1 < letter2) {    // comparing their number value
        printf("true\n"); 
} 
else { 
        printf("false\n"); 
}

This code will print "is letter d before letter a? false". The value of the variable letter1 was changed to the ASCII code for the letter ‘d’, then this letter is compared with the letter ‘a’ and its code is found to be larger.

When comparing characters, the way they are declared is relevant. If a variable is declared as a signed char, when used as a number its sign is considered, and so its numeric value will be between -128 and 127. On the other hand, when declared as unsigned char, if used as a number, its value will be between 0 to 255. This may reveal unexpected results, as in the following code:

signed char sc1 = 'A';
signed char sc2 = 255;
unsigned char uc1 = sc1;
unsigned char uc2 = sc2;
if (sc1 > sc2) {
     printf("sc1 > sc2\n");
}
else {
     printf("sc1 <= sc2\n");
}
if (uc1 > uc2) {
     printf("uc1 > uc2\n");
}
else {
     printf("uc1 <= uc2\n");
}

This code will produce the following result:

sc1 > sc2
uc1 <= uc2

Even though, both, signed and unsigned variables have the same values of ‘A’ (0100 0001 in binary) and 255 (1111 1111 on binary), when used as signed characters, the conditional (sc1 > sc2) is true, because the expression compares if (65 > -128). At the same time, when unsigned characters are used, the conditional (uc1 > uc2) is false, because the expression compares if (65 > 255).

Because of this behavior, when having characters as repository of numbers, and they are going to be used in computations, it is best to convert them to unsigned characters before any of these calculations, as prescribed by the following secure programming rule:

SPR STR34-C

Cast characters to unsigned char before converting to larger integer sizes.

Keep in mind that variables declared only as char are usually considered to be signed char, but this behavior is implementation dependent and it may change from environment to environment. The compiler in Microsoft Visual Studio consider char variables as signed char.

The C header file ctype.h contains useful functions to test the nature of char variables. The following table described some of them:

Selected functions from ctype.h       

Function

Description

isdigit(c)

Returns a non-zero integer if the unsigned char c is a digit (0-9)

isalpha(c)

Returns a non-zero integer if the unsigned char c is an upper or lower case letter

isalpnum(c)

Returns a non-zero integer if the unsigned char c is digit or alpha

islower(c)

Returns a non-zero integer if the unsigned char c is a lower case letter

isupper(c)

Returns a non-zero integer if the unsigned char c is an upper case letter

isprint(c)

Returns a non-zero integer if the unsigned char c is printable

isspace(c)

Returns a non-zero integer if the unsigned char c is a blank space, carriage return, or tab

tolower(c)

Returns an int with the ASCII code of the unsigned char c converted to lower case

toupper(c)

Returns an int with the ASCII code of the unsigned char c converted to upper case

 

All methods in ctype.h expect the input to be an unsigned char. This means that the programmer must be sure to cast other types of char onto unsigned char, before using these functions. The following secure programming rule prescribes likewise:

SPR STR37-C

Arguments to character-handling functions must be representable as an unsigned char.

 

If the methods tolower and toupper receive a char variable that cannot be converted to either lower or upper cases respectively, they return the integer value corresponding to the input character unchanged.

Read More

Read more about ctype.h in Appendix B2 of the textbook.

 

Strings

Strings in C are arrays of characters. They are used to hold textually related characters together, like words, sentences, or text of any kind. They need to be declared like any other array with square brackets and an indication of their maximum size. For example, the following declares the string word with at most 100 characters:

char word[100];

Strings may be initialized with the same methods arrays are initialized, however, a very important distinction that separates strings from any other array is the fact that the last used element of the array must contain the null character of ‘\0’. C/C++ requires this character to indicate the end of the array, because not all elements of an array may contain information. The following will correctly initialize strings s1 and s2 in C:

char s1[100] = {‘H’,‘e’,‘l’,‘l’,‘o’,‘\0’};
char s2[] = {‘B’,‘y’,‘e’,‘ ’,‘b’,‘y’,‘e’,‘\0’};

These variables will be stored in memory as follows:

String s1 has 100 bytes reserved for elements, but it only uses the first 6 for the letters of the words “Hello” and the null character. On the other hand, string s2 reserves exactly 8 bytes for the words “Bye bye” (including one byte for the empty space) and the null character.

Because strings are heavily used in programs, C offers a shorthand to initialize or assign values to a string. One can write the text of the string surrounded by double quotes, and there is no need to add the null character. C will add the null character automatically. The following shows strings s1 and s2 initialized with the shorthand:

char s1[100] = “Hello”; 
char s2[] = “Bye bye”;

To print a string in C, we may use the “%s” placeholder on the printf command. The following will print “Hello and Bye bye” with the variables we just created:

printf(“%s and %s”, s1, s2);

Like with other placeholders, “%s” may also use a number after the % to indicate the minimum number of characters to be printed. If the string to be printed is smaller, some blank spaces will be left in place, but if the string is larger, the whole string will be printed and the minimum size ignored.

Individual characters on a string can be modified, as they are elements of an array. For example, changing the word “Hello” to “Yellow” on string s1 can be done with the following sentences:  

s1[0] = ‘y’; 
s1[5] = ‘w’;
s1[6] = ‘\0’;

Notice that because “yellow” is one letter longer than “Hello”. When adding the letter ‘w’ the code erases the null character, therefore, we need to add it again at the end of the word, otherwise C will not know where to find the end of the string.  If we try to print a wrongly constructed string, that does not have the null character in the end, the program will continue printing the contents of memory that follow the string until a null character is found. They may reveal memory contents that potential attackers may use to their advantage. Suppose that instead of printing, a program is actually changing the contents of a wrongly constructed string. Because there is no end to the string, the program may try to modify adjacent memory areas. This may produce computing errors, but also could be an opportunity for attackers to store malicious code in memory.

Programmers should always be aware of the extra character at the end of strings (‘\0’). The following piece of code shows how easily this can be forgotten. It tries to copy a string s into a string t, using a loop:

for (int i=0;s[i]!= ‘\0’;i++) { t[i]=s[i]; }

All characters in s where copied, except ‘\0’, therefore string t is badly constructed. Another possible problem is that if s was not properly constructed, and it also misses the null character at the end, or is larger than t, the loop will not work properly either. A possible solution would include a possible maximum size for string t, like ARRAY_SIZE:

int i;
for (i=0;(i<ARRAY_SIZE-1 && s[i]!= ‘\0’);i++) { t[i]=s[i]; }
t[i]=‘\0’;

Notice how the loop takes care not to use all elements on array t. By checking that the loop counter does not go into ARRAYSIZE-1 (the last element of the array), it reserves that space to insert the null character ‘\0’ if all other elements are used.

Having strings properly ending in the null character and that do not exceed their allocated memory, is so important that it merits the following secure programming rule:

SPR STR31-C 

Guarantee space for the character data and the null terminator (‘\0’).

C provides a library of methods for strings in its header file string.h. This file also declares a constant and a data type, both very important when dealing with strings. The constant NULL is declared in string.h to represent a non-existent string. Some functions may return this constant if they fail to produce a string. It can also be used to compare it with a string variable, to verify if the variable is not empty.  NULL is defined as the integer 0, but programs dealing with strings make more sense when the variable NULL is used instead of its internal value.

string.h also defines the data type size_t. This data type is used when dealing with sizes of strings, arrays, and any other similar construct that reserves larger sizes of memory from RAM. Actually, this data type is only an alias name for unsigned integer, but it provides a standard type used by functions to deal and communicate about data sizes. Therefore, using it makes programs more portable between various platforms, since they do not rely in the actual implementation of unsigned integer.

The following table shows the most important functions in string.h. Notice that strings are referred as char *s. This is a general notation that means “pointer to string s” or most directly, “the address in RAM of string s”. We will study this notation in detail in unit 6, but for this section, think of it as an index that indicates the beginning of a string. Also, if this notation is preceded by the keyword const, it means that the string will not be modified by the function.

            Selected functions from string.h     

Name

Parameters

Return Type

Description

Functions for length

strlen

(const char* s)

size_t

Returns the real length of string s (before ‘\0’)

Functions for concatenation

strcat

(char * t, char *s)

char *

Returns the modified string t, that was concatenated to string s.

strncat

(char * t, char *s, size_t n)

char *

Returns the modified string t, that was concatenated with, at most, the first n characters of string s.

strcat_s

(char * t, size_t m,  char *s)

int

Concatenates t with s up to a size of m. m should be smaller than the size of t-1. Returns zero if successful, other number otherwise.

strncat_s

(char * t, size_t m,

  char *s, size_t n)

Int

Concatenates t with, at most, the first n characters of s up to a size of m. m should be smaller than the size of t-1. Returns zero if successful, other integer otherwise.

Functions for comparison

strcmp

(char * s1, char *s2)

int

Compares string s1 with string2 lexicographically. Returns an integer number as follows: <0 if s1 is before s2, 0 if s1 is exactly as s2, >0 if s1 is after s2.

strncmp

(char * s1, char *s2, size_t n)

int

Compares the first n characters of string s1 with string2 lexicographically. Returns an integer number as follows: <0 if s1 is before s2, 0 if s1 is exactly as s2, >0 if s1 is after s2.

Functions for copying

strcpy

(char * t, char *s)

char *

Returns the modified string t, which has a copy of string s, including the null character (‘\0’).

strncpy

(char * t, char *s, size_t n)

char *

Returns the modified string t, which has a copy of, at most, the first n characters of string s, including the null character (‘\0’).

memcpy

(char * t, const char *s, size_t n)

char *

Returns the modified string t, which has a copy of exactly the first n characters from string s.

strcpy_s

(char * t, size_t m, char *s)

int

Returns the modified string t, which has a copy of string s. The maximum size of t is m (not including ‘\0’).

strncpy_s

(char * t, size_t m,

 char *s, size_t n)

int

Returns the modified string t, which has a copy of, at most, the first n characters of string s. The maximum size of t is m (not including ‘\0’).

memcpy_s

(char * t, size_t m,

  const char *s, size_t n)

int

Returns the modified string t, which has a copy of exactly the first n characters from string s. The maximum size of t is m (not including ‘\0’).

Functions for searching

strchr

(char * t, int c)

char *

Returns a pointer to the first position of character c found inside string t. NULL if not found.

strstr

(char * t, const char *s)

char *

Returns a pointer to the first position of string s found inside string t. NULL if not found.

Let us discuss these functions in detail.

The function strlen is very useful to find the true size of a properly constructed string. It provides the length of the string without including the place for the null character ‘\0’. For portability, the function returns an integer of type size_t, which is an unsigned integer. If the string is the empty string, strlen returns zero. If the string does not contain a null character in the end, the results are undetermined, since the function may go beyond the limits of the array. strlen is generally used in loops that process the elements of the string. For example, the following loop may be used to change all occurrences of the letter ‘r’ into the letter ‘t’ for a string s

for (size_t i=0; i< strlen(s); i++) {
          if (s[i] == 'r') { s[i] = 't'; }
     }

Concatenation is the operation of creating a new string by putting together two other strings side by side. The functions strcat and strncat both receive two strings, the second string (or a section of it in strncat) is copied and attached at the end of the first one, which is permanently modified. In the process, the original null character ‘\0’ at the end of the first string is replaced by the first character of the second string, and all other characters of the second string are also added afterwards. This is what happens with strcat. If strncat is used instead, only the first n requested characters of the second string are copied. If the second string is smaller than the size requested in strncat, the complete copy of the second string is attached, regardless. In both functions, a null character ‘\0’ is added at the end of the addition. Programmers should be certain that the first string has enough space to receive the added characters and the new null character ‘\0’. Failing to do so, produces undetermined results, since the function may go beyond the limits of the array. For example, the intent of the following code is to produce the string “bad string bad” into string t, but we go beyond its size limits, since string t only has 8 characters at declaration (including ‘\0’):

char s[] = “bad ”;
char t[] = “string ”;
strcat(t,s);
strncat(t,s,3);

A solution would be to give t enough elements to take string s, like declaring it char t [100] to begin with. However, Microsoft Visual Studio provides also secure versions of these methods, strcat_s and strncat_s. Their purpose is to avoid going beyond the limit of the first string by indicating its size with an extra parameter added between the two strings. The following piece of code shows how to use these functions in the case above. Notice that the number provided as the maximum size for the concatenation is 99, leaving one element of the string t for the null character ‘\0’:

char s[100] = “bad ”;
char t[100] = “string ”;
if (strcat_s(t,99,s)>0){
     printf(“There is a problem with concatenation”);
}
if (strncat_s(t,99,s,3)>0) {
     printf(“There is a problem with concatenation”);
}

All these concatenation functions assume that the strings to be concatenated do not overlap in memory.

Two strings can be compared using the lexicographic order previously described. The functions strcmp and strncmp, both receive two strings and return an integer number indicating the position of the first string respect to the second string in a lexicographic (dictionary) order. If the number returned is negative, the first string would be found in a dictionary before the second one. If the number is positive, the first string would be found after the second. If the number is zero, both strings are the same. The difference between strcmp and strncmp, is that the strcmp compares all characters in the string, while strncmp only compares the first n requested characters. For example, the following piece of code would print that string s is before string t when using strcmp:

     char s[] = "star trek";
     char t[] = "star wars";
     if (strcmp(s, t) < 0) {
          printf("%s is before %s\n",s,t);
     }
     else if (strcmp(s, t) > 0) {
          printf("%s is after %s\n",s,t);
     }
     else {
          printf("%s is the same as %s\n",s,t);
     }

However, if we replace strcmp(s,t) with strncmp(s,t,5), the program will print that both are the same.

 

A string can be copied onto another using the functions strcpy and Both functions receive two strings, the second string (or a section of it in strncpy) is copied over the first one, which is permanently modified. As with other string functions, programmers should be certain that the first string has enough space to receive the characters of the second string plus the null character ‘\0’. Failing to do so, produces undetermined results, since the function may go beyond the limits of the array. The following code copies the first two letters of string s onto string t:

char s[] = “beyond”;
char t[] = “go”;
strcpy(t,s,2);

However, if we attempt to copy the whole string s onto string t using strcp(t,s) instead, it will go beyond its size limits, since it only has 3 characters at declaration (including ‘\0’). To solve this problem, the string t should have enough elements to take string s, like declaring it char t[100] as we indicated before. Here again, Microsoft Visual Studio also provides secure versions of these methods, strcpy_s and strncpy_s. They also avoid going beyond the limit of the first string by indicating its size with an extra parameter added between the two strings. The following piece of code shows how to use strcpy_s correctly, with a maximum size for the concatenation as 99, leaving one element of string t for the null character ‘\0’:

char s[100] = “beyond”;
char t[100] = “go”;
if (strcpy_s(t,99,s)>0) {
     printf(“There is a problem with copy”);
}

If the intent is to copy a string in the middle of another, the function memcpy can be used. This function is similar to strcpy, but it only copies the number of required characters, without adding the null character ‘\0’. For example, the following code will transform the word “beyond” into the word “behind” in string s:

char s[100] = “beyond”;
char t[100] = “hi”;
memcpy(s[2],t,2);

Notice, that the index of string s is used to indicate the correct place where the string t should be copied, and only two characters will be copied. The null character ‘\0’ was not included in the copy. As with the other copy functions, the function memcpy_s is provided to avoid an unsecure copy with an added parameter to indicate the maximum size of the 

Destination string.

All these functions to copy assume that the strings to be copied do not overlap in memory.

 

A character or a string can be located inside another string using the functions strchr and strstr. These methods will receive the string to be searched together with either the character, or the string being looked for, respectively. If the string does not contain them, they will return NULL, but if they are found, the functions will return a pointer to the exact location in the string where it was found first. As we indicated before, this pointer is an address of memory for a character and will be of type char *. For example, the following code will find the first occurrence of the letter ‘e’ in the word “ukulele”:

char s[100] = “ukelele”;
char * index = strchr(s,’e’);
printf(“%s\n”,index);

The last line shows that the pointer to char (char *) can be treated as a string. It will print the string “elele”, since the index variable is pointing to the first place in s where the letter ‘e’ appears. The following code will find the first occurrence of the “le” string. It prints the word “lele”.

char s[100] = “ukelele”;
char * index = strstr(s,”le”);
printf(“%s\n”,index);

A loop can be used to find all occurrences of a character or string inside a word. Before the loop, we find the first occurrence of the character or string, and the loop will continue while the search does not produce NULL. For example, the following code will change all occurrences of the letter ‘e’ for the letter ‘a’ in “ukelele” and print “ukalala”:

char s[100] = “ukelele”;
char * index;
index = strchr(s,’e’);
while (index !=NULL) {
     memcpy(index, “a”, 1);
     index = strchr(s,’e’);
}
printf(“%s\n”,s);

We have emphasized in all these string methods the importance of ending strings with the null terminator ‘\0’. This is such important concept that deserves the following secure programming rule:

SPR STR32-C

Do not pass a non-null-terminated character sequence to a library function that expects a string.

 

Review the Code

You may review the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205100/download?verifier=HVCRSxYAyGCRGOweLTGfRAdV7uibS1u6m2aJnUcr&wrap=1] EString01.cpp,  [link: https://canvas.park.edu/courses/62124/files/8205394/download?verifier=Qhr7KjWCkRZB88gVYNM1sYuen159GgI0zxshQchH&wrap=1] FString02.cpp and [link: https://canvas.park.edu/courses/62124/files/8205179/download?verifier=YQFyw3i6z4YZvpQQHZsLgK4ACcsQZEHVoQFAEAwz&wrap=1]  GString03.cpp for more examples with functions from the string.h C header file.

Wide Strings and Strings in C++

Arrays of characters ending with a null character ‘\0’ are not the only strings available in C/C++. The C header file wchar.h defines the wide character data type, which increases the possible characters to be used in a string, and incorporates new functions to handle them. C++ also creates the string data type and its functions on the string C++ header file. We will not use these libraries and data types in this course, but if one decides to use them, one should pay special attention to the following secure programming rule, that recommends to be careful with the mix:

SPR STR38-C

Do not confuse narrow and wide character strings and functions

This also applies to C++ strings. Do not confused them with strings terminated by the null character ‘\0’. Always use all functions with their expected data types. Calling functions with the incorrect data types will prevent compilation or produce undetermined results.

Bi-dimensional Arrays

Let us end this unit with a review of a topic that may relate to arrays and strings: Bi-dimensional arrays. These are arrays than represent information arranged as tables, with rows and columns to indicate their positions. Consider for example the following table:

This table can be represented in C/C++ as a bi-dimensional array, by adding a second index dimension as follows:

int biDim[2][3] = { { 8, 3, 5 } , { 2, 7, 6 } };

The first index on the array represent the number of rows on the table ([2]), while the second one represent the number of columns ([3]). As we can see, this array can be initialized at declaration using the curly brackets, but notice that they contain additional internal curly brackets that separate the elements of the various rows. The elements of the array are initialized row by row. This also reveals the way the array is going to be stored in memory, with the elements of the first row before the elements of the second row, and so on. This arrangement is known as row major and it is depicted in the following memory representation:

When elements of a bi-dimensional array are initialized at declaration only the first set of square brackets can be left without a size. The previous declaration command could have also been:

int biDim[][3] = { { 8, 3, 5 } , { 2, 7, 6 } };

Arrays with more than 2 dimensions may also be declared, but they become difficult to handle if they have more than 3 dimensions.

Having two dimensions these arrays usually require two indexes to be manipulated. The following depicts a nested loop used to print the contents of the bi-dimensional array biDim, considering it as a table:

for (int i=0; i<2; i++) {
     for (int j=0; j<3; j++) {
              printf(“%d ”,biDim[i][j]);
     }
     printf(“\n”);
}

The printf at the end of the first loop makes the printing jump to the next line when a row has been printed. However, because we know the way the array is stored in memory, the following code that does not consider the structure of the array could also be used to print the array elements (one element per line):

for (int i=0; i<6; i++) {
     printf(“%d\n”,biDim[i]);
}

An important bi-dimensional array to consider is an array of strings. The first index will indicate the maximum number of strings the array will hold, while the second index indicates the maximum size of each string. All strings will have the same maximum size, but they can have different real sizes (up to the maximum), since they should all end with the null character (‘\0’). The following piece of code creates, initializes and print an array of strings:

int words[][6] = { “Hello”, “Hi”, “Hola”, “Aloha” };
for (int i=0; i<4; i++) {
    printf(“%s\n”,words[i]);
}

Notice that the maximum size for the Strings should make allowance for the null character (‘\0’). The longest word (“Hello”) has 6 characters including the null character (‘\0’). The diagram below show how is the array imagined as an array of strings:

The following diagram shows how the array of strings is stored in memory:

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205182/download?verifier=UGWox4G3WnYYPCbqJj3i66dB5FqJGtiWIvtoNX4L&wrap=1] HBiDimensionalArrays.cpp. that contains an example of the use of bi-dimensional arrays.

We will later see in unit 6 a method that uses dynamic allocation to create arrays of string in which each element may have a different size.

Read More

Read more about string.h in Appendix B3 of the textbook.

 

Read More

Read more about character input and output, arrays, and character arrays in sections 1.5, 1.6, and 1.9 of the textbook.

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
