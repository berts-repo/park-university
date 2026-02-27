# Unit 4: Discussion

Introduction

This discussion will let you practice comparing loops with recursion. Note that this is just for practice to show the equivalence of loops and recursion. This does not imply that one method is better than the other, and in the example code, there is an even simpler loop that accomplishes the same thing. These are things that you should comment on as part of the discussion.

Directions

Initial post

For your initial post

Write a method with one loop in Java that prints a pattern or calculates and returns a value

For  example:

void printTri(String s) {
    while (s.length() > 0) {
        System.out.println(s);
        s = s.substring(0,s.length()-1);
    }
}

Peer Response

For each of your follow-up posts

Rewrite someone else’s loop using recursion

Comment on someone else’s solution

void printTriRec(String s) {
    if (s.length() > 0) {
        System.out.println(s);
        printTriRec(s.substring(0,s.length()-1));
    }
}

Grading

To view the rubrics, click the menu (the three dots) to the top right of each discussion board or visit the  [link: https://canvas.park.edu/courses/74667/pages/grading-and-schedule] Grading and Schedule page. 

Due Dates

Initial post: by 11:59 p.m., Thursday, CT

Two or more peer responses: by 11:59 p.m., Sunday, CT

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2023-06-30T02:49:59Z

Class,

public static void foo(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            System.out.print("* ");
        }
        System.out.println();
    }
}

Output:

* 
* * 
* * * 
* * * * 
* * * * *

---


### Feedback

**[INSTRUCTOR]:** Bert, You earned 10 of 10 Discussion points.  Great job!  Thank you for your participation on the Discussion Board this week.
