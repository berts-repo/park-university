# Unit 3: Homework 1

**Due:** 2023-01-30T05:59:00Z
**Points Possible:** 20.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to write a Python program to process a log file and print some summary results. The philosophy of programs like this is to write all output to the screen. After the program is working, you’ll use output redirection to save the results to a file.

Preparation

While you can certainly edit files on your running instance, you may find it easier to develop this program on your local machine and then upload it to your instance for final testing. You will need access to a Python compiler or you may use Park’s virtual student desktop.

If you do your development on another machine, then you need a copy of the data file  [link: https://canvas.park.edu/courses/72082/files/9774605/download?verifier=jmcstdW6UqqrU6uW2gLKfbKGKM4Mc8Llyuqk3uPD&wrap=1] auth.log.

Assignment 

The operating system logs many events. One file that contains interesting events is /var/log/auth.log, which shows, in part, unsuccessful logins to your system. Some lines of the file will look like this:

May 26 07:29:20 instance-1 sshd[20327]: Disconnected from 61.147.247.146 port 45177 [preauth]
May 26 07:32:22 instance-1 sshd[20351]: Invalid user nagios from 159.65.144.233 port 49715
May 26 07:32:22 instance-1 sshd[20351]: input_userauth_request: invalid user nagios [preauth]
May 26 07:32:23 instance-1 sshd[20351]: Received disconnect from 159.65.144.233 port 49715:11: Normal Shutdown, Thank you for playing [preauth]

Your task in this exercise is to write a python program to read the lines of data from this file, and print out a sorted list of invalid user names to the screen, one per line, like the partial list shown below.

aD-min.123
admin
admin
admin
admin
admin
admin
backups
…
web3
zabbix
zabbix
zabbix
zimbra

This isn’t a long program. Depending on how verbose your code is, it should be done in 10-25 lines.

A general outline of this program is to

Open the file

For each line in the file

Find if this line contains an invalid user name

If it does, add the name to a list of names

When all lines have been processed, sort the list

Print each element in the list to the screen on a separate line

Finding the invalid user name is the hardest part of this assignment. Use the fact that the user name is always immediately preceded by either ‘Invalid user’ or 'invalid user'. (Note that there are two lines in the log file for each failed login attempt - you only want to process one of them.

Be sure to comment your code, including a header comment with your name and the date.

Once your program works on your local machine, start your instance from the Cloud Console, then login using the SSH button. From there you can upload your program to your instance. Use the gear icon, then select upload file. The file will end up in your home directory.

Make sure your program still works. Most likely you’ll have to change the path to the file to be exactly ‘/var/log/auth.log’. Your output will be different, since this file is different from the one copied to your local machine. Save your output in a file using output redirection.

Download your output file to your local computer. If you made any changes to your program, download a copy from your instance to your local machine so you can submit it to Canvas.

In a Word document, write a paragraph about what you liked about this assignment, what you disliked or found confusing, and what you do to improve your code if you had another couple of hours to work on it.

Turn In

For documentation, you should submit your Word document, your python program and the output file to Canvas. The python program should be the actual file, not a screenshot. You should use a .zip or .gz file to simplify the submission process.

---

## My Submission

**Score:** 20.0/20.0
**Grade:** 20
**Submitted:** 2023-01-29T06:03:13Z

### Submitted Files

- **unit3hw1_Bert.zip**
  - Downloaded: `files/unit3hw1_Bert.zip`

### Instructor Feedback

**[INSTRUCTOR]** (2023-01-30T00:43:58Z):

> Bert,

Overall good job on the lab this week.  Python isn’t easy but you did a great job.  Using Python in your daily work is a good way to automate system administration tasks.   Here is a good site that has 10 Python tools for system administration: https://www.activestate.com/blog/top-10-python-tools-for-it-administrators/.  I enjoyed reading your reflection.  I've also been learning Java which is another great language to learn ;-)  Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material covered.

Prof [INSTRUCTOR]
