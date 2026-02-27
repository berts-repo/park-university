# Unit 5: Discussion 1

System Calls and I/O

Recall the Unit 1 discussions on systems calls. What are some system calls for I/O, and how do the different data types (integers, doubles, character, strings, etc.) impact I/O?

Post your reply to this thread. Also, respond to a minimum of two posts from your classmates.

**My Score:** 8.0/?

---

## My Discussion Posts

**Posted:** 2022-09-17T11:45:06Z

Class,

I chose to go with the C library stdio for the "wrapper" that utilizes the system call. "Usually, system calls are  not  invoked  directly:  instead, system  calls  have  corresponding  C  library  wrapper  functions which perform the steps required." (Ubuntu Manpage 2022)

fopen() - opens a file, which is called with two parameters, the pathway, and the mode; the mode consist of different i/o switches (e.g. read, write, and append.)

fclose() - closes an open file

printf() - formats and outputs the function to screen

Different data types are referenced in main memory by different amounts of bytes, depending on what processor and what compiler are being used. In most standard 64-bit Unix systems the data types are:

char
1 byte

short
2 bytes

int
4 bytes

long
8 bytes

float
4 bytes

double
8 bytes

pointer 
8 bytes

 

Standard Data Types. IBM. (n.d.). Retrieved September 17, 2022, from https://www.ibm.com/docs/en/ibm-mq/7.5?topic=platforms-standard-data-types

Ubuntu Manpage: Introduction to System Calls. Ubuntu Manpage: Intro - introduction to system calls. (n.d.). Retrieved September 17, 2022, from https://manpages.ubuntu.com/manpages/trusty/man2/intro.2.html#:~:text=A%20system%20call%20is%20an,to%20invoke%20the%20system%20call.

---
