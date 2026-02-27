# Unit 7: Homework 2

**Due:** 2023-02-27T05:59:00Z
**Points Possible:** 25.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to practice using cron to automatically run processes at predetermined times.

Preparation

A few sites to read about cron and get several examples are  [link: https://www.ostechnix.com/a-beginners-guide-to-cron-jobs/] A Beginner's Guide to Cron Jobs,  [link: https://www.geeksforgeeks.org/crontab-in-linux-with-examples/] GeeksforGeeks, or  [link: https://crontab.guru/] Crontab Guru.

Assignment

Keep a Word document which will show your process throughout the lab. Include the contents of the crontab file and any other files that you modify.

Use the program cronttab to create cron jobs that:

Append the output of the command uptime to a file in your home directory. This should run every 4 minutes.

Appends the disk space used in /var to a different file in your home directory. Include the date and time in some way. This should run 8 times a day,  evenly spaced throughout the day. You can choose the times. Make sure you are recording just the disk space used by /var, and not the disk space used by the entire partition that /var is on. Also, don't use human readable mode, since you will not be able to see any changes in the values if you do this.

Runs a python program (which you have to write) that searches through the file created in step 1 and outputs any lines where the 5-minute load average first goes above 2.00 and then the next line where the 5-minute load average is back below 2.00. Save the results to a third file in your home directory. This program should run once a day between 3 and 5 am. (You should make sure that your system has a high 5-minute load average at least once so you can test your script. See the program stress for a nice tool that can stress test your system.) For example, if the the 5-minute load averages were 
0.00
1.53
2.67
3.99
2.02
1.75
0.98
2.13
1.88
Then you would output the entire lines containing 2.67, 1.75, 2.13 and 1.88

At the end of your Word document, include the answers to the following questions:

The instance you used for this assignment, and the names of the files from steps 1-3

The location of your crontab file

The permissions on the file and directory

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

Turn In

For documentation, you should submit your Word document and your python program (the .py file, not a screenshot) to Canvas.

Notes

Before you run your cron jobs, make sure your commands work from the command line first. You shouldn't run into problems with environment variables except maybe a path problem. The easy solution is use absolute paths to all the files and programs specified in the cron job. Again, try this on the command line first. A final trick is to log error messages to your output file as well. This can be done by adding 2>&1 

after the file redirection in your cron job, like this:

... >> /home/yourname/my_file.log 2>&1

---

## My Submission

**Score:** 25.0/25.0
**Grade:** 25
**Submitted:** 2023-02-27T01:24:41Z

### Submitted Files

- **unit7-hw2-Bert.zip**
  - Downloaded: `files/unit7-hw2-Bert.zip`

### Instructor Feedback

**[INSTRUCTOR]** (2023-02-28T11:01:00Z):

> Bert,

Excellent job on the assignment this week.  In this assignment you had the opportunity to run cron to run a process at a predetermined time.  You did a good job.  The cron utility (also known as a cron job) is a job scheduler.  It allows the user the ability to set up automatic commands that run on a schedule.  Cron is a daemon, a long-running process that only needs to be started once and will run constantly in the background.  Cron wakes up every minute, examines its list of things to do to see if any scheduled tasks need to be executed, and if so, it executes them. If not, it goes back to sleep for another 59 seconds. The list of things to do is called a cron table, or Crontab for short.  Keep up the good work and don’t hesitate reaching out if you have any question on any of the material.

Prof [INSTRUCTOR]
