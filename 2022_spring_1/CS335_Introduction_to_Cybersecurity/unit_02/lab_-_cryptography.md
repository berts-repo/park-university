# Unit 2: Lab - Cryptography

**Due:** 2022-01-24T05:59:00Z
**Points Possible:** 40.0
**Submission Types:** online_upload

## Instructions

Update: An alternative platform to complete the lab. 

Some students were unable to set up or restore a vPark (GENI) environment for this lab. I am providing an alternative platform for you to complete the lab. I have deployed all our labs in this semester (except for lab 1) on the Practice Cloud Store (https://store.edaas.net). All the labs (except for lab 1) in this semester are included in the "Cybersecurity I (5 Labs)" training course. Although the web page shows the course price as $0.99 (the minimum can be set on this platform), you don't need to pay for that lab. Instead, simply register an account and log in the system. Once you log in, you will find the course on your account. Regarding how to use the platform, please refer to the video embedded in the About Us page (https://store.edaas.net/product/findNewContact).

The name of this lab on the Practice cloud is called Hash and Symmetric Encryption with OpenSSL (Free).

You are free to choose either vPark or Practice Cloud Store. But make sure to complete ONE report document containing the answers of all the required questions listed in the Rubrics. If you are using the Practice Cloud, use the lab instruction on that platform. The instruction can be found by clicking the "View manual" button when entering the lab environment. You don't need the lab instruction on this Canvas page. However, if you are using vPark, please use the instruction on this page. 

The tasks in the two systems (vPark and Practice Cloud) are similar but might be slightly different. Please make sure to read the Rubrics to avoid missing important tasks. If you are using vPark, find the task number marked as "Task X.X in vPark". If you are using the Practice Cloud, find the task number marked as "Task X.X in P.C".

The lab can be non-trivial for some students. Please start the lab as early as possible. Let me know if you have additional questions. Thank you!

================================================

If you are using Practice Cloud, you can stop reading here and log into  [link: https://store.edaas.net] https://store.edaas.net to [link: http://www.thepracticecloud.net]  start the lab. If you are using vPark, please continue reading and use the instructions below. 

Overview

The purpose of this lab is to practice different encryption algorithms with OpenSSL. You will need to use different hash algorithms and test the performance of AES-256. You need to turn in a report to canvas (in the form of PDF or Word) describing your experiment procedure.

Lab Environment

GENI project: CS335

RSPEC file choices:

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-kansas.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-kansas.rspec

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec

Lab Topology

This lab only needs one virtual machine. You can complete all steps on either the Server machine or the Client machine.

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

Lab Instructions

Part 1 – Generate digests with OpenSSL

On the vPark VNC environment, right click the desktop and select “Open Terminal Here”

In the terminal, create a file contain your name and current time. For example, suppose your name is John Smith and the current time is 15:23:00, 2019/07/11, type in echo “John Smith, 15:23:00, 2019/07/11” > message.txt you will create a text file with the content “John Smith, 15:23:00, 2019/07/11”.

OpenSSL can generate the digest of a file. To generate the md5 hash of the file message.txt, simply type the command openssl dgst -<hash algorithm> <file name>. The supported digest algorithms include md5, sha1, sha256, sha512, etc. For example, to create a md5 digest of message.txt, simply type the command openssl dgst -md5 message.txt. More information can be found in  [link: https://www.madboa.com/geek/openssl/#how-do-i-create-an-md5-or-sha1-digest-of-a-file] madboa.com

Task 1: Create a digest for message.txt with sha1, sha256, and sha512, respectively. Take a screenshot for each of the digests, and answer how many bits each digest has.

Open Firefox by typing firefox & on the terminal. Go to  [link: http://www.apache.org/index.html#projects-list] Apache Project List. Select a project from this web page. Click the link of that project, browse the project and find the download page. In the download page, you might see several packages are listed. Select the package that have a digest link besides it. Download the package. For instance, in the following page (The download page of project Olingo), you can select “Olingo OData2 Sources”, because it has a digest next to it available, i.e., md5 and sha512.

Download that package to your GENI VM.

NOTE: the downloaded file will be in the directory of ~/Downloads. To run the command to compute the digest, you first need to go to that directory by using command  cd ~/Downloads. For details, please review Linux commands in the CCNA Linux unhatched course.

Use the digest command in step 3 to compute the digest of your downloaded file and compare it with the digest that displayed in the web page. For example, below image is the web page displaying the sha512 digest of olingo-odata2-parent-2.0.10-source-release.zip.

Task 2: Follow instructions in step 4 to download a project package, compute its digest, and compare it with the value displayed on the project’s web page. Take a screenshot to prove the two values are the same.

Task 3: Write a paragraph to explain why the website posts the package’s digest. What does it mean when the digest you generated is different from what the website claims.

Part 2 – Symmetric encryption with OpenSSL

On the terminal, go back to the directory where message.txt is located. For example, suppose the message.txt is located in ~/Desktop, simply type cd ~/Desktop.

To encrypt message.txt with AES CBC mode, type in the following command. You will be asked to type in passphrase that is used to encrypt the file. 

openssl enc -aes-256-cbc -a -salt -in message.txt -out message.enc

To decrypt message.enc, type in the following command. You will be asked to type in the passphrase that were used to encrypt the file.

openssl enc -d -aes-256-cbc -a -in message.enc -out message.dec

Task 4: Open message.enc and message.dec, show the content of each file. Take a screenshot.

Read the following webpage:  [link: https://www.madboa.com/geek/openssl/#how-do-i-simply-encrypt-a-file] madboa.com. Learn how to encrypt and decrypt a file without typing the passphrase. Download a file from the  [link: http://www.apache.org/index.html#projects-list] Apache Project List that is over 10MB.

Task 5: Measure the time used for encrypting and decrypting the file without typing the passphrase. (Hint: you can use Linux command  [link: https://www.lifewire.com/command-return-time-command-4054237] time to measure the encryption/decryption time) Take a screenshot for the command you use and its output.

Submissions

Create and submit a detailed lab report to answer the questions in the instruction. The questions that are required to be answered include: Task 1, Task 2, Task 3, Task 4, Task 5. For points of each question, please refer to the rubrics. 

Due Dates

Complete all steps before Sunday midnight.

Unit Learning Outcomes Reflected in Assignment

Explain and use symmetric, asymmetric and hash cryptographic algorithms (CLO 1)

---

## My Submission

**Score:** 40.0/40.0
**Grade:** 40
**Submitted:** 2022-01-22T20:29:41Z

### Submitted Files

- **lab2.docx**
  - Downloaded: `files/lab2.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2022-01-25T22:39:09Z):

> All correct. Good job!
