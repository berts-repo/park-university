# Unit 3: Notes

This unit covers using Python programs to do two different types of system administration tasks. The first type is processing data in a log file, typically to filter or summarize it. There are many ways to accomplish this, especially by chaining together shell commands, but we’re going to focus on Python in this unit. This task will be done on your running instance. The second type of task is controlling your virtual machine instance. You’ve been able to start and stop your instance using the Cloud Console, and now you’ll learn how to do it from a program. You’ll run this on your Cloud Shell, since you don’t have to worry about setting up any special authentication mechanism, though just note that if you got the authentication correct, you could run your programs off your local machine to control your cloud instances!

Review Python Programming

You can review some of the Python skills you will need from the free, online textbook,  [link: https://runestone.academy/ns/books/published/thinkcspy/index.html] How to Think Like a Computer Scientist: Interactive Edition. You will have to log in and either use your book from CS 152, or just the generic book thinkcspy.

Running Python

You may be used to running your Python programs from an IDE, but on the systems you’re using, you’ll stick with the command line. There are two different versions of python installed on your systems, and you probably want version 3, not version 2. To do this, at the command prompt just use python3 followed by the name of your program, like

CS369-instructor@cloudshell:~ (cs-369-fa-2019)$ python3 stopme.py

Developing Python 

For Assignment 1 this unit, you may find it easier to work initially on your local computer and then upload your program to your running instance for final testing. This is fine. You’ll just need a copy of the data file, which you can download from Canvas.

However, you really can’t do this for Assignment 2, since there is no easy way to test the program except when it is on the Cloud Shell.
