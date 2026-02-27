# Unit 2: Discussion

Introduction

This discussion will let you see appropriate and inappropriate uses of a linked list when solving problems. 

Directions

Initial post

For your initial post, you may either:

Propose a specific problem where a linked-list of objects is an appropriate data structure. Use objects besides Strings or Java primitive data types (int, double, etc.)

Describe the object including some attributes and any methods besides accessors/mutators.

Briefly describe how you add to the list, delete from the list, and how to search the list.

OR

Post a question about the previous unit's Assignment 1 or 2, such as where you were confused or where you had a problem. Don’t post more than 3 or 4 lines of code. The idea is clarify concepts or get pointed in the right direction, not for someone else to generate code for you.

Peer Response

For each of your follow-up posts

Respond to another student’s proposal by commenting on the appropriateness of the data structure (either appropriate or inappropriate), adding additional components to the object, or proposing additional functionality to the list.

OR

Answer a question asked by another student. Note that it won’t help the other student if you wait until Sunday night to offer advice.

 

See Unit 1 discussion for examples

Grading

To view the rubrics, click the menu (the three dots) to the top right of each discussion board or visit the  [link: https://canvas.park.edu/courses/74667/pages/grading-and-schedule] Grading and Schedule page. 

Due Dates

Initial post: by 11:59 p.m., Thursday, CT

Two or more peer responses: by 11:59 p.m., Sunday, CT

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2023-06-14T00:55:13Z

Class,

I want to propose clipboard copy and paste functionality. The clipboard can store various objects, including text and pictures. It will allow the application/user to traverse backwards and forwards through the copies, and then paste the object into the application.

Attributes:

plainText - String for text.

imageData - 2-d array for image data.

name - Name for object

timestamp - When copy was made

Methods:

copy() - Individual copy methods for different objects.

paste() - Paste methods for different objects.

delete() - Delete methods for objects.

forward() - Method for traversing through the list.

backward() - Method for going backwards through the list.

Adding to the List:

To add to the clipboard we can create a new object with the appropriate constructor to determine object type, it will then record the name and timestamp by inserting it at the begging of the linked list. This will make sure the most recent copy is viewed first.

Deleting from the list:

The list will automatically delete after x amount of copies. It will accomplish this by calling the delete() method and removing the last node of the linked list.

Searching the List:

To view the clipboard options the list can be traversed by iterating through most recent node to the least recent node, and calling the other method to traverse in reverse.

---


### Feedback

**[INSTRUCTOR]:** Bert, You earned 10 of 10 Discussion points.  Great job!  Thank you for your participation on the Discussion Board this week.
