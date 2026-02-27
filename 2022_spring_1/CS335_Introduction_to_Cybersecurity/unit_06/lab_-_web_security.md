# Unit 6: Lab - Web Security

**Due:** 2022-02-21T05:59:00Z
**Points Possible:** 40.0
**Submission Types:** online_upload

## Instructions

Update: An alternative platform to complete the lab. 

Some students were unable to set up or restore a vPark (GENI) environment for this lab. I am providing an alternative platform for you to complete the lab. I have deployed all our labs in this semester (except for lab 1) on the Practice Cloud Store (https://store.edaas.net). All the labs (except for lab 1) in this semester are included in the "Cybersecurity I (5 Labs)" training course. Although the web page shows the course price as $0.99 (the minimum can be set on this platform), you don't need to pay for that lab. Instead, simply register an account and log in the system. Once you log in, you will find the course on your account. Regarding how to use the platform, please refer to the video embedded in the About Us page (https://store.edaas.net/product/findNewContact).

Please note that you have to complete two labs on the Practice cloud. The lab names are "Web Security: Cross-site Scripting (Free)" and "Web Security: SQL Injection (Free)".

You are free to choose either vPark or Practice Cloud Store. But make sure to complete ONE report document containing the answers of all the required questions listed in the Rubrics. If you are using the Practice Cloud, use the lab instruction on that platform. The instruction can be found by clicking the "View manual" button when entering the lab environment. You don't need the lab instruction on this Canvas page. However, if you are using vPark, please use the instruction on this page. 

The tasks in the two systems (vPark and Practice Cloud) are similar but might be slightly different. Please make sure to read the Rubrics to avoid missing important tasks. If you are using vPark, find the task number marked as "Task X.X in vPark". If you are using the Practice Cloud, find the task number marked as "Task X.X in P.C".

The lab can be non-trivial for some students. Please start the lab as early as possible. Let me know if you have additional questions. Thank you!

================================================

If you are using Practice Cloud, you can stop reading here and log into  [link: https://store.edaas.net] https://store.edaas.net to [link: http://www.thepracticecloud.net]  start the lab. If you are using vPark, please continue reading and use the instructions below. 

Overview

This tutorial will help you to get familiar with several Web attacks, including Cross-site Scripting and SQL injection. 

Lab Environment 

GENI Project: CS335 

RSPEC file: 

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-kansas.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-kansas.rspec

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec 

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec 

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec

Lab Topology

For this lab, our topology will consist of two hosts. We will have a Server machine, where the WebGoat Web server is hosted. We also have a Client machine, where user can launch Firefox to visit the WebGoat Web server and run Zap, the HTTP Proxy tool to manipulate the HTTP transaction.

Preparation

This lab will use the GENI environment that you set up in Lab 1(Set up vPark Environment). If you haven’t set up the environment, please refer to the instruction in Lab 1.  

How to resume your Lab desktop? 

If you are using your own Windows computer (not Citrix Virtual Desktop), you will have the Server and Client session saved on your Putty, as follows.

With the saved sessions on PuTTY, exiting and resuming your VNC desktop are easy.

To resume your Client machine desktop, follow the next four steps:

1. Open PuTTY, load the Client session you have saved and click the Open button to connect.

2. Type in the passphrase of your GENI SSH key to log into your VM.

3. In the VM, type in command vncserver   :1 to make sure vnc server is started. Make sure to leave a space between the word vncserver and the colon sign (:). You probably will see a message saying vnc server is already started. That is okay.

4. Open vncviewer, connect with the address 127.0.0.1:5901. You will need to type in the password of the VNC server that you set before. You will get to the resumed desktop.

To resume your Server machine desktop, complete the same four steps as above. However, make sure you use port number 2 and 5902 instead: 1) Open PuTTY and load the Server session you have saved and click Open button to connect. 2) Type in your GENI SSH key passphrase. 3) In the VM, type in command  vncserver   :2 . 4) Open vncviewer, connect with the address 127.0.0.1:5902.  

If you are using Citrix Virtual Desktop or Mac/ Linux Computer 

Server and Client session might not be saved on your Putty. You need to follow the “connect to virtual machine” document in Lab 1 to connect to Client or Server.

How to exit your Lab desktop?

Simply close the PuTTY and VNC viewer.

Other issues about the vPark Environment?

For other vPark Environment issues, such as VM is down or Lab Desktop is blank, please check the “vPark Lab Environment FAQ” document.

Task 0 – Start and Visit WebGoat

NOTE: This lab is reusing the environment in Unit 5: Lab - HTTP. Make sure the HTTP Proxy is disabled, which is described in Task 3 of the Unit 5: Lab -HTTP. If you already have the WebGoat and Firefox running, you can skip steps to start them, but only take screenshots required in Task 0 B and Task 0 D to earn the points.

Open a terminal on the Server machine, type in command ifconfig to find out its IP address. It should be in the format of 10.10.x.x. Normally it is 10.10.1.2.

On the terminal of the Server, type in the following two commands

cd /vPark

 java -jar ./webgoat-server-8.0.0.M24.jar --server.address=<Server IP>

, where <Server IP> is the IP address you found in Task 0A. Wait for a while. The WebGoat is ready when you see the message “Started StartWebGoat in xx.xxx seconds(……)”.

Take a screenshot to show you have set up the WebGoat on the Server machine.

On the Client machine, type in command firefox &  in a terminal to start Firefox.</li

Type in the following address in firefox of Client machine: http://<Server IP>:8080/WebGoat, where <Server IP> is the IP address you found in Task 0A. Take a screenshot showing you can visit the WebGoat on the Client machine. 

Register an account on WebGoat and log in with your registered account. Remember the account. You will also use it in next unit’s lab. 

The following labs are all performed on the Client Machine

Task 1 – Cross-Site Scripting (XSS)

To prepare for this task, watch the   [link: https://youtu.be/Cexe4d5WvcM] XSS Attack  lecture video

and other complementary videos here: 

 [link: https://www.youtube.com/watch?v=cbmBDiR6WaY] Stored XSS video

and  [link: https://www.youtube.com/watch?v=V79Dp7i4LRM] Reflected XS

Under the “Cross-Site Scripting(XSS)” tab of WebGoat (on the left bar), click on the “Cross Site Scripting”.

Go through page 1-6 in WebGoat to learn more knowledge about XSS.

On page 2 in WebGoat answer the question in the page bottom and submit. Make screenshot for the response page of your answer. Notice that the firefox in VNC is a little different from what the WebGoat describes. You cannot execute javascript:alert(document.cookie); on the address bar. However, you can execute the command at the Web Console, which can be found by selecting Firefox menu (the icon to the right of the address bar) Web Developer Web Console. 

Work on the challenge about reflected XSS attack on page 7 in WebGoat. Try to fill in web form with the script payload and trigger the alert box. Describe how you filled in the web form. Take a screenshot to show you have successfully triggered the alert box. 

Learn the stored XSS on page 12 in WebGoat and complete the challenge on page 13. Notice that to call the function webgoat,customjs.phoneHome. simply using the JavaScript statement webgoat.customjs.phoneHome() ; The function output can be seen at the Web Console, which can be found by selecting Firefox menu (the  icon to the right of the address bar) Web Developer Web Console. Answer the question at the bottom of page 13 in WebGoat and submit. Describe how you fill in the form to achieve the goal. Make screenshot for the response page of your answer.

Task 2 – SQL Injection

To prepare for this task, watch the  [link: https://youtu.be/SdLKb0I2u_I] SQL Injection lecture video

and other complementary video: [link: https://www.youtube.com/watch?v=WFFQw01EYHM] SQL Injection

Under the “Injection Flaws” tab of WebGoat (on the left bar), click on the “SQL Injection” item (the second item).

Study materials from page 1 to 6 in WebGoat .

Complete the challenge on page 7 in WebGoat. Describe what did you type in the box and make a screenshot to show that you have succeeded. 

Complete the challenge on page 8 in WebGoat. Describe what did you type in the box and make a screenshot to show that you have succeeded.

Reflection

Write a paragraph reflecting on your tutorial experience. What did you learn, what did you think was easy, what was difficult? Also include any other comments you may have had on this tutorial. 

Submission

Create and submit a detailed lab report to answer the questions in the instruction. The questions that are required to be answered include: Task 0B, Task 0D, Task 1C, Task 1D, Task 1E, Task 2C, Task 2D, Reflection.  For points of each question, please refer to the rubric.

Due Dates

Complete all steps before Sunday midnight.

---

## My Submission

**Score:** 40.0/40.0
**Grade:** 40
**Submitted:** 2022-02-22T19:06:39Z
**Late:** Yes

### Submitted Files

- **lab6.2.docx**
  - Downloaded: `files/lab6.2.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2022-02-20T17:18:24Z):

> Hi, Bert. I noticed that you have miss the lab SQL Injection. Remember that in this week, you have to complete two labs.

**[INSTRUCTOR]** (2022-02-22T18:00:35Z):

> If you submit the report for the SQL Injection part, I will be glad to grade that.

**Bert** (2022-02-22T19:06:39Z):

> Hello Dr. Wang,
I am sorry I did not notice there was two assignments last week. I was flipping my schedule from nights yesterday because I have some things I have to take care of, that is why I am late to responding to your message from yesterday. I did the lab SQL injection, and am having trouble with the last part. I have details in my word document, a tip would be great I feel like I am close. Sorry and thank you for informing me.

**[INSTRUCTOR]** (2022-02-22T22:05:27Z):

> Hi, Bert. Thanks for submitting the missing part. All the questions that take some scores work well. Good job!
