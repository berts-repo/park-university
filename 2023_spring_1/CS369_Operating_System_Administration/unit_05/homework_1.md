# Unit 5: Homework 1

**Due:** 2023-02-13T05:59:00Z
**Points Possible:** 35.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to review files and configurations associated with user accounts.

Preparation

Start your GCP instance and connect to it using the SSH link.

Assignment

Keep a Word document with the answers to the following questions.

Look at your users (15 points)

Look at the contents of the file /etc/passwd. In your Word document:

List the entire line with your account. What is your home directory? What is your user id? What is your group id? You are a non-system user. Are there any other non-system users? How can you tell?

Show the result of the groups command.

Since you have an account on your instance, you have an entry in /etc/passwd, and you also have an entry in /etc/shadow. View this file.

List the line for your account. What does the password field contain? What does this mean? Explain why this seems like a contradiction.

We’ll explore this topic in more detail in the next assignment.

What command did you have to issue before you could read the file /etc/shadow? What does this command let you do in general? Not all users on a system will be able to issue this command. From what you’ve seen so far in this lab, what gives you the permission to issue the command?

Look at your configuration files (10 points)

List all the files in your home directory, including the hidden ones. Show the command you used and the output.

Identify all the files that you have that are also described in the text, then compare the contents of the files you found with the contents of the files described in the text in Chapter 30. Briefly describe any additions or deletions.

Issue the alias command and show the results.

Edit the appropriate file to uncomment one of the predefined aliases. Save the file. Reissue the alias command. You shouldn’t see your new alias. This is because these configuration files are normally only sourced once when you log in or create a new shell. After you make a change, you can certainly log out and in again, though this is overkill. You just need to issue the source command instead. Now, add your own alias that will get established every time you open a new shell window.

Document in which file you added your alias, and show that it now works.

Utility program (7 points)

Write a Linux command or series of commands, or a python program that prints a count of the number of system user accounts listed in /etc/passwd. Show your code and its output.

Reflection

At the end of your Word document, include the answers to the following questions:

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

Turn In

For documentation, you should submit your Word document to Canvas.

---

## My Submission

**Score:** 35.0/35.0
**Grade:** 35
**Submitted:** 2023-02-08T23:22:54Z

### Submitted Files

- **unit5hw1_doc.docx**
  - Downloaded: `files/unit5hw1_doc.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-02-14T00:31:48Z):

> Bert,
Overall good try on the homework assignment this week.  In this homework assignment you were asked a series of questions which gauged your knowledge of files and configurations associated with user accounts.   You did a great job answering the questions.  I also appreciate your candid reflection on the assignment.  Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material covered.

Prof [INSTRUCTOR]
