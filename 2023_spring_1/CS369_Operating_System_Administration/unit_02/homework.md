# Unit 2: Homework

**Due:** 2023-01-23T05:59:00Z
**Points Possible:** 60.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to create and control your own virtual machine using your GCP account.

Preparation

See  [link: https://canvas.park.edu/courses/72082/pages/unit-2-notes] Unit 2 – Notes for how to get started with your own GCP account. You only need to do this once. You do not need to provide a credit card number and you do not need to start a free trial. If you are asked for either of these, STOP, you are going down a wrong path and should start over.

Assignment

To document the steps below, create a Word document that contains screenshots and brief explanations of what you did. This serves as a notebook for you and a summary for the instructor to grade. Be sure to label each screen shot with the step number from the assignment.

Set up your GCP account and give your instructor access to your project.

 Create a virtual machine as you did in the previous Qwiklab exercise. Choose whatever name you like. The only other difference should be that you use a Series of N1 and Machine type of “f1-micro (1 vCPU, 614 MB memory)”

Using a micro instance will minimize the amount of credits you use, and you will not notice any difference in performance for the work done in this class.

Connect to your instance using the SSH button, issue the date command, and take a screen shot showing the date and your Gmail name as the prompt:

Install the nginx web server, as you did in the previous Qwiklab.

Test your server by connecting to it by the External IP link on the VM instances page in Google Cloud Console. You will see the nginx Welcome page.

Using any editor, change the text file found in the directory /var/www/html. Add your name to the welcome message in the <body>, then save the file. Remember to use sudo to avoid permission errors.

Refresh your nginx welcome page to see your changes. Take a screenshot showing the IP address of the page and your name as part of the welcome.

Stop and start your instance from the Cloud Console. Make sure you can still access your web server after a restart. Show screen shots of your instance stopped and running

Figure out the commands for stopping and re-starting your instance from the Cloud Shell. Show screen shots of the results of each of these commands.

Submit Assignment

For documentation, you should submit your Word document to Canvas.

---

## My Submission

**Score:** 60.0/60.0
**Grade:** 60
**Submitted:** 2023-01-18T21:08:28Z

### Submitted Files

- **unit2_assignment_Bert.docx**
  - Downloaded: `files/unit2_assignment_Bert.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-01-24T11:50:30Z):

> Bert,

Excellent job on the lab this week. Do me one favor, if you haven't already, please switch my email from my official email to "cs369[INSTRUCTOR]@gmail.com".  Keep up the great work and don't hesitate reaching out if you have any question on any of the material covered this week.

Prof [INSTRUCTOR]
