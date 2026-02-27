# Unit 3: Homework 2

**Due:** 2023-01-30T05:59:00Z
**Points Possible:** 40.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to control your instance using a Python program from the Cloud Shell

Preparation

Read through this entire lab so you have a sense of what is expected of you before you start.

Read the page  [link: https://cloud.google.com/compute/docs/reference/rest/v1/instances/stop] Methods: instances.stop,  which describes the process for stopping a running instance using an API. You do not need to worry about installing any packages or authorization keys as long you run your code in the Cloud Shell.

Assignment 

To document the steps below, create a Word document that contains screenshots and brief explanations of what you did. This serves as a notebook for you and a summary for the instructor to grade.

On the page  [link: https://cloud.google.com/compute/docs/reference/rest/v1/instances/stop] Methods: instances.stop, use the API Explorer in section “Try this API” to test stopping your instance using an API. The three fields you need to set are project (id not name), zone, and instance name. Run this tool until you get the parameters correct, then take a screenshot.

Copy the python code from the section “Examples” and put it in a file on the Cloud Shell. You can either save the file on your local computer and upload the file, or you can open the Cloud Shell code editor. The convention is for the file to end with a .py extension.

Edit your python program to change the sections marked TODO, to use the parameters you found in step 1.

Run your program from the Cloud Shell command line using python3 filename.py 
Make sure your program stops a running instance. You can check this by looking at the Cloud Console.

Modify your program so that instead of printing the entire dictionary, response, it only prints the following, each on a separate line: user, operation type, start date, start time

User name: instructor@gmail.com

Operation:  stop

Starting date:  2019-05-26

Starting time:  13:12:36.826-07:00

Since response is a dictionary, you access the elements like response['user']. Take a screenshot of the output of your program.

In addition to stopping your instance, you should now be able to write a python program to start your instance. See the page  [link: https://cloud.google.com/compute/docs/reference/rest/v1/instances/start] Method: instances.start for all the details, though you should find things are very similar to what you have just done. This program should print the same type of information as in step 5 of this assignment. Take a screenshot of its output.

In your Word document, write a paragraph about what you did to write the program in step 6. Include any Linux commands you used.

See the page  [link: https://cloud.google.com/compute/docs/reference/rest/v1/instances/list] Method: instances.list, for generating a list of your instances. Copy the python program and upload it to your Cloud Shell. Edit the program to specify your project and zone, then replace the print statement with

        print(instance['name'], 'is', instance['status'])

Run your program to get a list of your instances and their current status.

Stop your instance, any way that you like. Then run your programs in this order

list, start (wait for it to finish), list, stop, list

Take a screenshot of the output, including the command prompt, so that it shows the following information. Be sure it is a screenshot image.

Notes

When uploading files from your computer to the Cloud Shell, Google will not overwrite any file that is already there. Instead, it adds a version number to your file. This may not be what you expect. So the first time you upload the file runme.py, you'll get runme.py on the Cloud Shell. But the second time, you'll get runme_(1).py and the third time runme_(2).py . You'll either have to keep track of the latest one, or you can delete the file from the Cloud Shell before uploading a new one.

Turn In

For documentation, you should submit your Word document and your python programs to Canvas. The programs should be the actual python files, not a screenshot. You should use a .zip file to simplify the submission process.

---

## My Submission

**Score:** 40.0/40.0
**Grade:** 40
**Submitted:** 2023-01-28T07:25:49Z

### Submitted Files

- **unit3hw2_Bert.zip**
  - Downloaded: `files/unit3hw2_Bert.zip`

### Instructor Feedback

**[INSTRUCTOR]** (2023-01-31T12:51:35Z):

> Bert,

Overall good job on the homework assignment this week.  This wasn't an easy task but you did a good job trying to work through the problem. What I want you to take away from this experience is that you can use scripting to help automate tasks.  From a cyber perspective, this can save you a ton of time and heartache.  Once a script is written, you can save it and always use it.  Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material covered.

Prof [INSTRUCTOR]
