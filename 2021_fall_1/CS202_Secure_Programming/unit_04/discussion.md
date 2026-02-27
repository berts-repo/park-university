# Unit 4: Discussion

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

After reading the assigned course material, you must select and answer any two (2) of the questions below. 

Post your answers in this environment. Do not attach code, but copy and paste it onto the discussion thread. When you do that, you may lose some indentation. You need to restore this indentation manually to make the program readable.   

Please read what other students are posting and post all different examples. Do not repeat previous postings. Be Original. Also, do not write code containing material related to the Lab Activities/Homework. Homework is personal and it must not be shared with anyone but the Instructor.

Questions

Show an example of a piece of C/C++ code that uses (incorrectly) out-of-bound indexes and show also code on how this can be prevented.

Show an example of a piece of C/C++ code that may produce erroneous results because it uses signed characters in computations. Describe the reason for the problem and show code on how it can be solved.

Show an example of a piece of C/C++ code that calls incorrectly a function from the ctype.h C library with signed characters as parameters. Indicate the problem that may occur and show code on how it can be solved.

Show an example of a piece of C/C++ code that has problems because it handles a string that was not ended with a null character. Describe the problem and show code on how it can be solved.

Show an example the problems that a piece of C/C++ code may encounter when it sends a string that is not ended with a null character to the strlen Describe the problem and show code on how it can be solved.

Show an example where the use of the concatenation functions (strcat or strncat) produces a string that does not end in a null character. Describe the problem and show code on how it can be solved.

Show an example where the use of the string-copy functions (strcpy, strncpy, or memcpy) produces a string that does not end in a null character. Describe the problem and show code on how it can be solved.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-09-10T00:27:56Z

Hello class,

This week was a little rough for me, I spent a few days sick and did not get enough time to play with this weeks readings in Visual studio. I don't like my examples and would spend more time on it if I didn't have to get some rest before work.

Show an example of a piece of C/C++ code that calls incorrectly a function from the ctype.h C library with signed characters as parameters. Indicate the problem that may occur and show code on how it can be solved.

When you run the code with an signed integer that is outside the limits of the SCHAR_MIN and SCHAR_MAX. This will cause a runtime error. It can be solved by converting the signed char into a unsigned char.

#include 
#include 
int main() {

unsigned char u1 = 128;
signed char s1 = u1;
printf("%d", isprint(u1));
printf("%d", isprint(s1));
}

Show an example of a piece of C/C++ code that has problems because it handles a string that was not ended with a null character. Describe the problem and show code on how it can be solved.

This can be solved by using the function strlen in the string.h header and checking to to see if the length of the string will fit before the NULL

#include 
#include 
int main() {

char s1[6] = ("Hello");
s1[6] = '!';
printf("%s", s1);
}

---
