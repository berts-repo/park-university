# Unit 8: Discussion

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

In the last unit of this course, we are reviewing the secure programming rules (SPRs) that were described during the semester. The document “Summary of Secure Programming Rules in C/C++” contains a list of these rules.

After reviewing this document, select one (1) Secure Programming Rule (SPR) and explain it to the class. Present a concrete example of what does the rule tries to avoid and describe how it solves the problem.

Please read what other students are posting and post all different examples. Do not repeat previous postings. Be Original.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-10-08T18:31:58Z

Hello class,

We are at the end! I am going to cover EXP34-C. Do not dereference null pointers. If you were to dereference a NULL pointer it will cause undefined behavior, but it will allow hackers to use this situation to gain access to memory locations.

To fix the problem all you have to do is check if the pointer equals NULL before dereference.

 

if (ptr != NULL)
        {
            for (int i = 0; i < size; i++) {

                *(ptr + i) = i + 1;
                printf("%d\n", ptr[i]);
            }
        }

Just enter a number less then 5, for the size of the array, to dereference a NULL pointer.

 

#include 
#include 

int main() {
    int size;
    int *ptr = NULL;

    // enter a number less then 5 to have pointer to equale null for inproper dereference
    printf("pleas enter the size of the array: "); 
    scanf_s("%d", &size);
    
    if (size < 5) {
        ptr = (int*)malloc(size * sizeof(int));

        for (int i = 0; i < size; i++) {

            *(ptr + i) = i + 1;
            printf("%d\n", ptr[i]);
        }
    }
}

---
