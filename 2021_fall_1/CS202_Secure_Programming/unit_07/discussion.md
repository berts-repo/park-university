# Unit 7: Discussion

Introduction 

Participation in discussion threads is a weekly assignment that tests your reading process and critical thinking. You may participate in these discussion threads for this unit between 12:00 a.m., Monday, CT through 11:59 p.m., Sunday, CT. of the corresponding week.

 

Requirements

Your initial post must answer both of your chosen questions by 11:59 p.m., Thursday, CT.

You must complete your own posting and respond to at least one other student thread (different than your own) by 11:59 p.m., Sunday, CT.

Throughout the week, you must respond, to the best of your knowledge, the questions or requests made by Instructor and/or students, especially the Instructor’s requests for corrections.

Due Date

Initial post by 11:59 p.m., Thursday, CT

Respond to one or more classmates by 11:59 p.m., Sunday, CT

Directions 

In previous discussion threads we had the opportunity to test various features of the C/C++ language with programs that interacted directly with users. This week we are exploring the use of files for input and output, so we will revisit previous programs and modify them to interact with files.

After reading the assigned course material in this unit, you must select one program that you have already presented in previous discussion threads. This program may have had some issues by the end of the unit when you submitted them. The first thing you must do is to fix these problems and be sure that the program receives input interactively from the user’s keyboard and produces output to the screen. Please be mindful that we are not talking of programs presented for Lab Assignments or Homework. No homework should be shared between students ever. Only programs used in previous discussion threads can be used here.

Once you have a working program, you must modify it to receive all user input from a single ASCII input file and to write all program’s output into a single ASCII output file.

Post your answers in this environment. Do not attach code, but copy and paste it onto the discussion thread. When you do that, you may lose some indentation. You need to restore this indentation manually to make the program readable. Post also the input file used and the output file produced.

Please read what other students are posting and post all different examples. Do not repeat previous postings. Be Original.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-10-02T02:18:15Z

Hey class,

This program takes user inputs and adds them to a file. It then uses the file to take the last entry and determine if right shift will cause loss of data, converting a short integer into a character.

I have a bug where it is printing the entire contents of the file where I just want the last input. I ran out of time though.

 

#include <stdio.h>
#include <stdlib.h> // atoi
#include <limits.h> // UCHAR_MAX
#include <string.h>
#include <ctype.h>

#define MAXSIZE 20

unsigned int some_int;  // Inputed short variable
unsigned int shift_amount;  // Inputed right-shift amount
unsigned char int2char; // Right-shift result

char file[] = "file_in.txt";  //input file for short variable and right shift amount
FILE* f = NULL;

char add_int[MAXSIZE] = "";   //temp buffers
char add_shift[MAXSIZE] = "";
char buffer[MAXSIZE] = "";

int add2file() {
    
    f = fopen(file, "a+");
    if (f == NULL) {
        fprintf(stderr, "File %s was not found\n", file);
        return -1;
    }

    fflush(stdin);
    printf("Enter a number between 256-65535 for a short integer: ");
    fgets(add_int, MAXSIZE, stdin);
    fputs(add_int, f);

    fflush(stdin);
    printf("Enter the amount of times you want to shift: ");
    fgets(add_shift, MAXSIZE, stdin);
    fputs(add_shift, f);

    if (fclose(f) == EOF) {
        fprintf(stderr, "There is an error at closing %s\n", file);
        return -1;
    }

    return 1;
}

int readFile() {
    int index = 0;

    f = fopen(file, "r");
    if (f == NULL) {
        fprintf(stderr, "File %s was not found\n", file);
        return -1;
    }

    //determines which is index of file is shift amount and short integer
    while (fgets(buffer, sizeof(buffer), f) != NULL) {
        if (index % 2 == 0) {
            add_int = buffer;
        }
        if (index % 2 == 1) {
            add_shift = buffer
        }
        index++;
    }

    // grabs last entry to file
    some_int = atoi(add_int);
    shift_amount = atoi(add_shift);
}

int conversion() {

    if (shift_amount > 7 || shift_amount < 0) { // This block prevents overflow from right-shift. Promp 10b
        printf("Shift is greater then the precision of the integer type\n");
    }
    else {
        int2char = some_int >> shift_amount;
        if (UCHAR_MAX < some_int >> shift_amount) { //This block checks if conversion will fit in a lower data type. Promp 2c
            printf("This conversion from short int to char would result in losing numbers\n");
        }
        else {
            printf("The short to char conversion is: %u\n", int2char);
        }
    }
    return 1;
}

int main() {

    add2file();
    readFile();
    conversion();

    if (fclose(f) == EOF) {
        fprintf(stderr, "There is an error at closing %s\n", file);
        return -1;
    }

    return 0;
}

---
