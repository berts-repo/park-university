# Unit 5: Lab - HTTP

**Due:** 2022-02-14T05:59:00Z
**Points Possible:** 50.0
**Submission Types:** online_upload

## Instructions

Update: An alternative platform to complete the lab. 

Some students were unable to set up or restore a vPark (GENI) environment for this lab. I am providing an alternative platform for you to complete the lab. I have deployed all our labs in this semester (except for lab 1) on the Practice Cloud Store (https://store.edaas.net). All the labs (except for lab 1) in this semester are included in the "Cybersecurity I (5 Labs)" training course. Although the web page shows the course price as $0.99 (the minimum can be set on this platform), you don't need to pay for that lab. Instead, simply register an account and log in the system. Once you log in, you will find the course on your account. Regarding how to use the platform, please refer to the video embedded in the About Us page (https://store.edaas.net/product/findNewContact).

The name of this lab on the Practice cloud is "HTTP Basics and Request Interception (Free)".

You are free to choose either vPark or Practice Cloud Store. But make sure to complete ONE report document containing the answers of all the required questions listed in the Rubrics. If you are using the Practice Cloud, use the lab instruction on that platform. The instruction can be found by clicking the "View manual" button when entering the lab environment. You don't need the lab instruction on this Canvas page. However, if you are using vPark, please use the instruction on this page. 

The tasks in the two systems (vPark and Practice Cloud) are similar but might be slightly different. Please make sure to read the Rubrics to avoid missing important tasks. If you are using vPark, find the task number marked as "Task X.X in vPark". If you are using the Practice Cloud, find the task number marked as "Task X.X in P.C".

The lab can be non-trivial for some students. Please start the lab as early as possible. Let me know if you have additional questions. Thank you!

================================================

If you are using Practice Cloud, you can stop reading here and log into  [link: https://store.edaas.net] https://store.edaas.net to [link: http://www.thepracticecloud.net]  start the lab. If you are using vPark, please continue reading and use the instructions below. 

Overview

This tutorial will help you to get familiar with HTTP protocol. You will also become familiar with an HTTP Proxy, called ZAP, and looking at how HTTP works behind the scenes. First, we need to complete basic lab setup, as we would do with our GENI labs. 

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

Open a terminal on the Server machine, type in command ifconfig to find out its IP address. It should be in the format of 10.10.x.x. Normally it is 10.10.1.2.

On the terminal of the Server, type in the following two commands
                cd /vPark
              java -jar ./webgoat-server-8.0.0.M24.jar --server.address=<Server IP> 

, where <Server IP> is the IP address you found in Task 0A. Wait for a while. The WebGoat is ready when you see the message “Started StartWebGoat in xx.xxx seconds(……)”. Take a screenshot to show you have set up the WebGoat on the Server machine.  

On the Client machine, type in command firefox & in a terminal to start Firefox.

Type in the following address in firefox of Client machine: http://<Server IP>:8080/WebGoat, where <Server IP> is the IP address you found in Task 0A. Take a screenshot showing you can visit the WebGoat on the Client machine.

Register an account on WebGoat and log in with your registered account. Remember the account. You will also use it in next unit’s lab. 

The following labs are all performed on the Client Machine 

Task 1 – HTTP Basics

Preparation: To get familiar with HTTP, read Section 7.1.1 on the textbook and watch this  [link: https://www.youtube.com/watch?v=eesqK59rhGA] HTTP Introduction video first. 

Under the “General” tab of WebGoat (on the left bar), click on the “HTTP Basics”.

Complete page 1 on the WebGoat page
 

Take a screenshot to show you have completed page 2 on the WebGoat page and answer the question “How does the server handle the HTTP request”. 

Task 2 – HTTP Proxy Zap

Preparation: To get familiar with ZAP, please watch this  [link: https://www.youtube.com/watch?v=fa5LAfXmwoo] ZAP introduction video first. 

Under the “General” tab of WebGoat (on the left bar), click on the “HTTP Proxies”.

Study what a HTTP Proxy is in page 1 on the WebGoat page

Start ZAP in your Client Machine by following page 2 on the WebGoat page. Notice the following difference from the WebGoat tutorial:

ZAP is preinstalled under folder  /vPark/ZAP_2.7.0. You can start ZAP by issue the following command:
          cd /vPark/ZAP_2.7.0
          sudo ./zap.sh

WebGoat is not running locally. Therefore you don’t need to set ZAP’s port. 
Take a screenshot when the ZAP is started.

Follow page 3 on the WebGoat page to set up Firefox Proxy. Notice the following differences

The preference menu of Firefox can be found when clicking the “three bar icon” to the right of the address bar, as shown below.

The Network setting is at the bottom of the “General” category of the preferences. Click the button Settings…, you will be able to configure the proxy.

Since we are not hosting WebGoat locally, use port number 8080, instead of 8090.

Make a screenshot like page 4 on the WebGoat page to show ZAP is working.

Follow page 5 on the WebGoat page to exclude internal requests. Notice the following difference from the instruction.

Since we are hosting WebGoat server on the Server machine, you need to replace “localhost” with the IP address of Server machine. (To find IP address, refer to Task 0A, normally, the IP address is 10.10.1.2).

Follow page 6 on the WebGoat page to intercept and modify an HTTP request. Describe what will happen when you click the “Submit” button on WebGoat and how did you modify the HTTP request. Take a screenshot to prove your modification. Take a screenshot to show what did you see when submitting a modified request (Hint: If you saw a message under the text field saying “Well done, ……”, your work is correct).

Click the General HTTP Basics item on the WebGoat menu, and select page 3 on the WebGoat page. Complete the Quiz by using ZAP. Make a screenshot proving completing the Quiz.(Hint: you should see a message saying “Congratulations. …”, if you have filled in the form with correct information.) 

Task 3 – Disable HTTP Proxy

Close the ZAP.

Restore the Proxy setting on Firefox:

Open the Preference menu of Firefox. Go to the Network setting. The Network setting is at the bottom of the “General” category of the preferences. Click the button Settings…, you will be able to configure the proxy. (See Task 2D).

In the Network setting Box, select "Auto-detect proxy settings for this network".  Then click Ok

In the Firefox, type in the WebGoat address http://<Server IP>:8080/WebGoat to verify if the WebGoat can be connected. The <Server IP> is the IP address you found in Task 0A.

Reflection

Write a paragraph reflecting on your tutorial experience. What did you learn, what did you think was easy, what was difficult? Do you feel like you learned somet.hing about HTML and HTTP from this tutorial? Also include any other comments you may have had on this tutorial. 

Submission

Create and submit a detailed lab report to answer the questions in the instruction. The questions that are required to be answered include: Task 0B, Task 0D, Task 1C, Task 2C, Task 2E, Task 2G, Task 2H and Reflection. For points of each question, please refer to the rubrics

Due Dates

Complete all steps before Sunday midnight.

---

## My Submission

**Score:** 50.0/50.0
**Grade:** 50
**Submitted:** 2022-02-15T23:49:44Z
**Late:** Yes

### Submitted Files

- **lab5-1.docx**
  - Downloaded: `files/lab5-1.docx`

### Instructor Feedback

**Bert** (2022-02-14T04:26:26Z):

> Dr Wang,
I am having trouble with the last few steps. I have attempted this lab 3 times and I can not get ZAP to show a POST request. I would like to reattempt this assignment with some advice or a tip from you. I dont need the full points but I do enjoy learning this and I just cant get this to work the way I want.

**[INSTRUCTOR]** (2022-02-15T17:22:36Z):

> Hi, Bert. I can allow you to redo the lab. I will be glad to grade it. You can check the below videos. Hopefully they are helpful for you to find out where goes wrong:

https://drive.google.com/file/d/1gNQ-DxxasZqmhRenkTbhUp08LEtCaPIw/view?usp=sharing
https://drive.google.com/file/d/1_awCwwlNfolCe-v9wZJHSVaG3kPazR6b/view?usp=sharing
https://drive.google.com/file/d/1z8Fz0hQhbGBsO8ne8TI12gLM7Hp-BAh3/view?usp=sharing

Please use your park gmail credential to log in to visit.

**Bert** (2022-02-15T23:49:44Z):

> I figured it out. The link for the Google Drive videos did not work. I made sure I was signed in with my student account as well. My solution in a few parts, I was on the wrong page in firefox so I never got a 'POST' intercept. Feel stupid, now that I saw how easy my mistake was to fix.

**[INSTRUCTOR]** (2022-02-16T23:10:17Z):

> Thanks for the update. The score has been updated.
