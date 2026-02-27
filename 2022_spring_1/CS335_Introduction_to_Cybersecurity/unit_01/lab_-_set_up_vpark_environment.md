# Unit 1: Lab - Set Up vPark Environment

**Due:** 2022-01-17T05:59:00Z
**Points Possible:** 40.0
**Submission Types:** online_upload

## Instructions

Overview

The purpose of this lab is to set up the vPark Lab environment that is going to be used throughout the course. It will also help you to get familiar with the Linux system and commands.

Lab Instructions

Task 1
Follow the instruction document [link: https://canvas.park.edu/courses/65346/files/8729280?verifier=3xU0t4t7mBiJo2RfibCyFs36AZjSGn3ONSqyh8QZ&wrap=1]  1-vPark-set-up-user  [link: https://canvas.park.edu/courses/65346/files/8729287/download?verifier=SVGbkRSZiRrelwiKsUTikxXI1pOJItLXAcFTkrRF&wrap=1] to register a GENI user account, generate your SSH keys, and Join the GENI Project. Before you start, read carefully the following requirements.

In step 4 (Generate SSH Keys), make sure not forget the passphrase used when generating the SSH keypair. If you forget the passphrase, you will lose access to your virtual machines. If you don’t want to use your own passphrase, you can use cs335 as your passphrase, so that you won’t forget. However, this is not a recommended practice.

In step 4 (Generate SSH Keys), make sure you know the place where the putty/private key are stored.

In step 5 (Join a project), join the project named CS335, instead of ExampleProject. You have to wait for your request to be approved. Send out the request before Wednesday midnight.

A complementary video is posted below:

 [link: https://www.youtube.com/watch?v=z2kIhG7vPHY] CS335 vPark Setup UserNotice that the video might be different from the document. Use the pdf document as the standard. The video is only for reference purpose.

Task 2
Follow the instruction document  [link: https://canvas.park.edu/courses/65346/files/8729155/download?verifier=h3pqf3DmXveRhIwmiuzbSCYTJF077zf0D3xMYR3b&wrap=1] 2-vPark-set-up-lab to create a lab environment on GENI. Before you start, read carefully the following requirements.

In step 1 (Create a New Slice), make sure to create the slice under the project CS335. The slice name should be vPark-<your first name><your last name>. For example, if your name is John Smith, the slice name should be vPark-JohnSmith

In Step 3 (Apply the RSpec), use one of the following URL for the RSpec file.

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-clemson.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-clemson.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-stanford.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-stanford.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec (Links to an external site.)

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec 

 

c. A complementary video is posted below:

 

 [link: https://www.youtube.com/watch?v=5aLFVL4tpKY] CS335 vPark Setup LabNotice that the video might be different from the document. Use the pdf document as the standard. The video is only for reference purpose.

Task 3
Follow the instruction document  [link: https://canvas.park.edu/courses/65346/files/8728686/download?verifier=B0jrbCVSVL7VbCNHC09lWsw9RWC6A03CVIRwz4m0&wrap=1] 3-vPark-connect-to-virtual-machine to connect to the VMs. Read carefully the following requirements.

The document covers two types of operating systems (OS), Windows and Mac/Linux, locate the correct section based on your OS.

In Step 1.1, Download the Putty Key, use the passphrase that you have set in the step 4 of the tutorial 1-vPark-set-up-user. If you set the passphrase as the suggested passphrase cs335, simply type in cs335 when downloading the Putty key.

Step 6 (How to exit and resume your VNC desktop) in the Windows Machine section describes how to exit and resume your VM desktop. Read it carefully so that you can reuse your lab environment for the whole semester. The take away is that do not execute the command vncserver more than once, otherwise, you may mess up the environment.

A complementary video for connecting VMs from Windows machine is provided below: [link: https://www.youtube.com/watch?v=j0U1G945trI] CS335 vPark Connect To VM WindowsA complementary video for connecting VMs from Mac machine is provided below:

 [link: https://www.youtube.com/watch?v=Myp51xUli_o] CS335 vPark Connect To VM Mac

Notice that the videos might be different from the pdfs. Use the pdfs as the standard. The videos are only for the reference purpose.

Task 4
When you have completed all the steps in the instruction document 3-vPark-connect-to-virtual-machine, open a terminal in the VNC desktop of each machine (the Server and the Client) and type in command “date”. Take a screenshot to prove your desktop is ready.

Task 5
Type commands on the terminal of the Client machine answer of the following questions, take screenshots to justify your answers:

Who is the current user of the VM?

For the current user, what is the full path of its home directory?

Task 6
Write a brief report outlining your experience with this lab, especially describe the difficulties that you have encountered and how you have solved those difficulties.

Submissions

Create and submit a detailed lab report to answer the questions in the instruction. The questions that are required to be answered include: Task 1 c) (Make sure complete before Wednesday), Task 4, Task 5, Task 6. For points of each question, please refer to the rubric. 

Due Dates

Complete Task 1 a) - c) before Wednesday midnight;

Complete Task 2 – 6 before Sunday midnight.

Unit Learning Outcomes Reflected in Assignment

Use basic Linux commands (CLO 4)

Explain and operate on Linux file system and files (CLO 2, 4)

---

## My Submission

**Score:** 40.0/40.0
**Grade:** 40
**Submitted:** 2022-01-17T18:49:59Z
**Late:** Yes

### Submitted Files

- **lab1.docx**
  - Downloaded: `files/lab1.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2022-01-18T20:46:36Z):

> Good job! I am glad that you finally get the account registered.
