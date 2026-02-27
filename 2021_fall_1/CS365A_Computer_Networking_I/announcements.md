# Announcements - CS365ADLF1A2021 Computer Networking I

## Unit 8 Packet Tracer 10.4.3 Scoring Issue and Work Around
*Posted: 2021-10-05T11:25:42Z*

Class,

For the Unit 8 Packet Tracer lab 10.4.3, you are randomly presented with one of three versions of the project.  Due to an issue with the scoring, only one version will allow you to score 100%.  This version has IPv6 network addresses of 2001:DB8:A::/64 and 2001:DB8:B::/64.

If you're presented with different IPv6 addresses, you can force a new version by going to Options, User Profile and making a small change in your profile (i.e.: adding a middle initial to your name).  This will randomly assign another version.  You might have to do this a few times. Then, it will cycle through to the only version that works. 

Please let me know if you have any questions about this issue.

r/s,
Tom [INSTRUCTOR]

---

## Week 8 Notes
*Posted: 2021-10-05T11:22:14Z*

Congratulations class. You’ve made it to the final week! :-)

I hope you found the course materials to be insightful and valuable as you continue your Park University studies and advance in your professional military or civilian careers.  

This week's Packet Tracer lab (10.4.3) has a scoring issue.  I've posted a work around solution in the Announcement section.

Please make sure you read the "Final Exam Notes"  and be sure to complete the Honorlock Practice quiz before attempting the final exam.

Please take a moment to complete the student survey.  We're always looking for student feedback to help shape and improve this course.  Let us know what you liked and what you think should be improved upon.

Let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Honorlock Access Code Prompt  ***PLEASE READ***
*Posted: 2021-10-04T20:38:36Z*

Class,

    I've received a few reports that when a student attempts the Honorlock practice quiz, the system is requesting an access code.  It should not ask you for a code, but should send you straight to the Honorlock Chrome extension install and then the face and ID recognition portion before you can take the quiz.

    I'm working with the program coordinator to have the issue resolved, but we need your help to determine if this is affecting all students or just a few.

    To that end, I'm asking that all students attempt the Honorlock practice quiz as soon as possible and report any issues back to me.

r/s,
Tom [INSTRUCTOR]

---

## Week 7 Notes
*Posted: 2021-09-28T12:07:38Z*

Good morning class and welcome to Week 7.  You're almost done!

This week is all about subnetting, which many students consider to be the most challenging part of this course. Please take your time with this week’s chapter readings, watch the below videos and send me your subnetting questions.

To help you with this week's material, I've included a VLSM subnetting chart for /24 and smaller networks. It really helps you visualize all of the subnets possible in a /24 network. It includes all of the possible network, first & last host and broadcast addresses.   (Just remember that you won't be able to use this chart during the Park final exam.)

It's really important for you all to understand and calculate the three different types of addresses in a network:

    Network address

    Host address (first and last host addresses)

    Broadcast address

    Please review Cisco 11.1.6 - Network, Host, and Broadcast Addresses and watch the video at Cisco 11.1.5.

***SPECIAL NOTE***

Don't confuse a subnet or network address with a subnet mask address:

   Here are some subnet mask examples and their corresponding prefix notations: 

        225.255.255.0 - /24

        255.255.255.128 - /25

        255.255.255.192 - /26

        255.255.254.0 - /23

        255.255.255.252 - /30 (common point to point WAN link network size)

    A subnet (or network address) is the IP address where the host portions are all zeros.

    Some examples include:

        192.168.1.0/24

        192.168.1.128/25

        172.16.2.64/26

   Here's how you can calculate the network address, given any IP address:

    If you have an IP address of 199.88.77.66/24, then the network address would have the last eight bits (32 - 24 = 8) turned to zero, like so:  199.88.77.0.

   Here's another example:  what is the network address of IP address 192.168.10.192/25?

    This one's a little harder.  The /25 prefix means that the first 25 bits are the network portion, and therefore, the last 7 bits make up the host portion (32 - 25 = 7).

        1.  Start by converting the last octet of the IP address to binary (192):  11000000.

        2.  Next, set the last seven bits (32 - 25 = 7) to zero:  10000000.   Why?  Because all of the host bits in a network address are set to zeros.  

        3.  Now convert that binary number back to decimal (128).  The network address of 192.168.10.192/25 is then 192.168.10.128.

Here are two helpful Professor Messer subnetting videos:

There are a lot of subnet calculators on the Internet. Here are the ones that I use:

http://www.subnet-calculator.com/cidr.php (for classless CIDR network calculations)

http://www.subnet-calculator.com/ (for classful network calculations)

***A subnet calculator can be very helpful, but please note that for the Park final exam, you will be required to calculate subnets manually. No calculators or websites will be allowed. Oh, and don't forget to read the Honorlock announcement and complete the practice quiz this week.***

Let me know if you have any subnetting questions or encounter any technical difficulties.

r/s,
Tom [INSTRUCTOR]

---

## Honorlock Student Information
*Posted: 2021-09-23T22:27:04Z*

Good afternoon, everyone. 

    Starting this term (Fall 1, 2021), Park University will use Honorlock as the proctoring system for the Park final exam.  Park University no longer uses ProctorU, which some of you may have used in the past. 

    Advantages:  there are no fees and no requirement for you to schedule your Park final exam.  You have the flexibility to take the final at anytime during week 8.  

    The following information includes important steps you need to complete before taking your final exam:

Honorlock Proctoring is required for your final exam.

You will not be charged for the use of Honorlock.

You must use Google Chrome as your web browser to take the final exam in Honorlock.

You will need a functioning webcam and microphone and the Honorlock Chrome extension.

You will use the Honorlock link on the Canvas main menu. Once you click, you will be prompted to install the Honorlock extension. 

You need to have a government issued form of identification available the day you take the exam.

Honorlock will walk you through a 60-second pre-test checklist that includes a room scan using your webcam. 

Please review the parameters for the final exam (what is allowed/not allowed).

If you have questions, please visit  [link: https://parkuniversity.freshdesk.com/support/solutions/articles/6000242302] Park University HonorLock information (FAQ, Resources, and Help Desk)

    Follow these instructions and complete the practice Honorlock quiz during week 7.  That should give you enough time to resolve any issues you might have.

    Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Week 6 Notes
*Posted: 2021-09-21T21:12:52Z*

Welcome to Week 6, everyone!

    This week, you'll learn the basics of router configuration. 

    I think you'll enjoy this week's Packet Tracer and Netlab assignments, where you get to practice this week's learning materials.  The Netlab is more a comprehensive lab, where you configure the PCs, the router and the switch.   Please pay particular attention to the 'sdm prefer' command on page 2 of the Netlab instructions.  

  Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Week 5 Notes
*Posted: 2021-09-14T23:21:58Z*

Hello class and welcome to week 5.

    This week, you'll learn the basics about the network layer (module 8) and address resolution (module 9).

    The network layer corresponds to layer 3 of the OSI model and the Internet layer of the TCP/IP model.  Packet routing takes place at the network layer and is critical for the data transport across the Internet.   You will learn about IPv4 and IPv6 packets, as well as how routing works.  

    In module 9, you'll learn about the different roles that MAC and IP addresses have and how address resolution is used to an IP addresses to MAC addresses.  A really important fact to remember is that MAC addresses do not leave the local network when a protocol data unit (PDU) travels from a source computer (host) to a destination computer (host) on a remote network via a router.  Please pay attention to the example in Cisco section 9.1.2 - Destination on Remote Network:

    "When the destination IP address (IPv4 or IPv6) is on a remote network, the destination MAC address will be the address of the host default gateway (i.e., the router interface)."

    You'll also get a quick introduction to the IPv6 Neighbor Discovery protocol.

    Here are a few videos to compliment this week's readings:

Please let me know if you have any questions or issues with this week's readings or lab assignments.

r/s,
Tom [INSTRUCTOR]

---

## Week 4 Notes
*Posted: 2021-09-06T19:44:04Z*

Good afternoon class and welcome to week 4!

Special Note for this week's Packet Tracer assignment:

    Cisco's module 4 lists two 4.7.1 Packet Tracers.  Please be sure you complete PT 4.7.1 - Connect the Physical Layer.  It is located in Cisco section 4.7.2.  

    Part 2 of this lab requires you to install modules in router East and switch Switch2.  You will need to install the correct modules in order to complete this lab.

This week is all about the Data Link Layer (OSI layer 2) and Ethernet switching.  Ethernet is considered one of the prominent LAN technologies.  Wireless LAN (802.11) being the other one.

Ethernet is defined by data link and physical layer protocols of the OSI model, which correspond to the Media Access layer in the TCP/IP model (7.1.1 - Ethernet Encapsulation)

Ethernet uses the media access control address (MAC address) that's "burned into" the network interface controller (NIC) of a device.  A MAC address is considered the physical Ethernet address and is expressed as a 48 bit hexadecimal number.  It is typically represented in one of these two formats:

    hh-hh-hh-hh-hh-hh or

    hhhh.hhhh.hhhh (where h represents a hexadecimal number)

Here are some examples:

 34-41-5D-50-FE-92

 FF-FF-FF-FF-FF-FF  - this is an Ethernet broadcast address

01-00-5E-00-00-C7  - this is an Ethernet multicast address for an IPv4 encapsulated packet (always starts with 01-00-5E)

33-33-1E-00-0A-7D  - this is an Ethernet multicast address for an IPv6 encapsulated packet (always starts with 33-33)

 000A.F3C0.D0C2 

0009.7c31.6501 - You see this format used in switches and routers.  Sometimes also referred to as the Burned In Address (BIA).

Please don't confuse an Ethernet broadcast address (FF-FF-FF-FF-FF-FF) with an IP broadcast address (i.e.: 192.168.0.255).  They are not the same.

In a local area network (LAN), a switch uses the source and destination MAC address in the header of the data frame to forward the information.  

Here are some additional websites and video to complement this week's learning materials:

-  [link: http://www.ieee802.org/3] http://www.ieee802.org/3  - IEEE 802.3 Ethernet
-  [link: http://ethernethistory.typepad.com/] http://ethernethistory.typepad.com - Ethernet History. This site also covers the researchers who developed Ethernet. Can be slow to load at times, but it's worth the history lesson. :-)
-  [link: https://en.wikipedia.org/wiki/Ethernet] https://en.wikipedia.org/wiki/Ethernet

As a reminder, you can take this week's Cisco exam more than once, if you're not happy with your first score.  Please note that Cisco will record the score of your most recent exam, even if it was lower than a previous score.  

Please continue to ask your questions about the labs and the materials.

r/s,
Tom [INSTRUCTOR]

---

## Week 3 Notes
*Posted: 2021-08-30T23:24:21Z*

Good evening class and welcome to week 3!

This week you'll learn about the physical layer and the binary and hexadecimal numbering systems.

    The physical layer of the OSI model sits at the bottom of the stack. It is part of the Network Access layer of the TCP/IP model. Without the physical layer, you would not have a network. This module explains, in detail, the three ways to connect to the physical layer.

    This is a 32-bit IPv4 address of a computer in a network: 

11000000.10101000.00001010.00001010. 

It is shown in binary. This is the IPv4 address for the same computer in dotted decimal: 192.168.10.10. 

Which one would you rather work with? IPv6 addresses are 128 bits! To make these addresses more manageable, IPv6 uses a hexadecimal system of 0-9 and the letters A-F.

    As a network administrator you must know how to convert binary addresses into dotted decimal and dotted decimal addresses into binary. You will also need to know how to convert dotted decimal into hexadecimal and vice versa. (Hint: You still need your binary conversion skills to make this work.)

    In addition to the video and website links listed in this week's overview page, here are a few related videos, which will enhance this week's learning material:

Let me know if you have any questions or concerns.

r/s,
Tom [INSTRUCTOR]

---

## Useful Cisco IOS Tips & Shortcuts
*Posted: 2021-08-23T22:11:16Z*

Class,

Here's a link to the most commonly used IOS shortcuts:

 [link: https://etherealmind.com/cisco-ios-cli-shortcuts/] https://etherealmind.com/cisco-ios-cli-shortcuts/

I use the up arrow (to scroll through the previous commands) and ? (to see which commands are available in a particular mode) most often.  For example, if I wanted to know which commands are available to configure an interface (int command), I'd use this:

S1(config)#int ?
Ethernet                    IEEE 802.3
FastEthernet           FastEthernet IEEE 802.3
GigabitEthernet    GigabitEthernet IEEE 802.3z
Port-channel           Ethernet Channel of interfaces
Vlan                              Catalyst Vlans
range                           interface range command

Entering Abbreviated Commands

You can abbreviate commands and keywords to the number of characters that allow a unique abbreviation. For example, the configure command can be abbreviated as config because the abbreviated form of the command is unique. The router accepts and executes the abbreviated command.

    Here are some commonly abbreviated commands:

Full Command
Abbreviated Command

show running-config
show run or sho run

copy running-config startup-config
copy run start

interface 
int (i.e.:  int vlan 1)

enable 
en (to enter privileged EXEC mode; this won't work for enable secret <password>)

configure terminal
config t or conf t

ip address 
ip addr

show ip interface brief
show ip int b

There are more, but these will get you started.

It's also worth mentioning that almost every IOS command has a 'no' version:

"Using the no Form of a Command

Almost every configuration command has a no form. Depending on the command, the no form enables or disables a feature. For example, when configuring an interface, the no shutdown command brings up the interface, and the shutdown command shuts down the interface. The username command creates a new user, and the no username command deletes a user when entered with a valid username."

For a really detailed explanation of tips, techniques and shortcuts, take a look at this Cisco article:

 [link: https://www.cisco.com/c/en/us/td/docs/routers/crs/software/crs_r4-1/getting_started/configuration/guide/gs41crs/gs41cli.html#wp1222048] https://www.cisco.com/c/en/us/td/docs/routers/crs/software/crs_r4-1/getting_started/configuration/guide/gs41crs/gs41cli.html#wp1222048

r/s,
Tom [INSTRUCTOR]

---

## Week 2 Notes
*Posted: 2021-08-23T22:08:53Z*

Good afternoon class and welcome to week 2.

By now, you are hopefully settling into a routine for this class that works best for you.   Or at least you're getting there. :-) It will get easier. You can do it!

Special Note for this week's Packet Tracer lab (2.9.1 - Basic Switch and End Device Configuration):

    The instructions state to "Use a console connection to access each switch."  This means that you'll need to connect a console cable from each of the computers to the switch.  You won't be able to click on the switch itself.  You'll get this error message: "Configure is locked."  The short video at the end of this announcement shows you how to do this.

This week, you’ll learn about ports, addresses, network protocols and models.

As you work on your assignments this week, please remember the following:

Packet Tracer - Don't forget to change the User Profile name from 'Guest' to your name and submit a screenshot of the Assessment Items page and your completed *.pka file.

Netlab - Take a moment and watch the Intro to Netlab video I posted in the Announcements before starting your first lab.

Please continue to ask questions and let me know if you're having any technical difficulties with Packet Tracer or Netlab.

r/s,
Tom [INSTRUCTOR]

---

## Getting Started with Netlab
*Posted: 2021-08-23T22:08:44Z*

Good afternoon class,

    I'm reposting this video to help you get started with the unit 2 Netlab assignment:  

    Please note that the maximum  lab time is now two hours, not four hours.  Make sure you read the separate announcement on how to save your Netlab configurations.  This comes in very handy, when you run out of time or have to end a reservation early.  Saving your configs will allow you to pick up pretty much where you left off, instead of having to rerun an entire lab from the beginning.  

    When scheduling a lab, please select:  AE CCNA1 v7.0 - MDP.

Let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## More Packet Tracer Information
*Posted: 2021-08-20T21:06:42Z*

Good afternoon Class,

   I wanted to take this opportunity to clarify the Packet Tracer assignments.  You do not have to submit the answers to the questions.

    The only items you have to submit are your saved, completed *.pka file, along with a screenshot of the assessment items.  There's no requirement to submit the answers.  The questions are designed to help you further understand the material.  Don't forget to add your name to the user profile when you start a lab.

    Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## How to Save your Netlab Configurations
*Posted: 2021-08-16T20:22:52Z*

Hello class,

    Your first Netlab assignment isn't due until the end of week 2, but this is good information to have now.

    Netlab gives you the option to save your router and switch configurations in Netlab.  You can then reload them when you restart the lab at a later date or time.  It does not save your PC configs, though.  You will have to reenter those.  This is very useful if you're not able to complete the lab within your allotted time frame.

    The attached PowerPoint presentation provides a step by step walk through:

    To save the configs, follow these steps:

    1. Click on the Pod link on the upper right side of the screen.  
    2. Select “Save All Devices”
    3. Select “Save to your files” and click “Yes”.
    4. Click on your account folder link.
    5. Click on “Save Here”
    6. Type in a file name and click “Create”

    To load the saved configurations, enter a lab.  Once the router and switch configurations have been loaded, follow these steps:

    1. Click on the Pod link on the upper right side of the screen.  
    2. Select “Load All Devices”
    3. Select “Replace existing configurations with new configurations.
    4. Click “Yes” on the Caution page.
    5. Select “File System” and click “Select”
    6. Click on your account folder link.
    7. Select the file name and click “Load Folder.”

    It will erase the current configs and load your saved configs.  This will take a few minutes to complete.

    Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Getting Started with Netlab
*Posted: 2021-08-16T20:15:06Z*

Class,

    This video should help you get started with the unit 2 Netlab assignment:  Please note that the maximum  lab time is now two hours, not four hours.  Make sure you read the separate announcement on how to save your Netlab configurations.  This comes in very handy, when you run out of time or have to end a reservation early.  Saving your configs will allow you to pick up pretty much where you left off, instead of having to rerun an entire lab from the beginning.

Let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## *** Important Packet Tracer Requirement ***
*Posted: 2021-08-16T15:02:08Z*

Good morning, class.

    Important reminder:  When completing the Packet Tracer labs, please remember to enter your name in the User Profile when starting each lab.  If you don't do this, you'll get a 0 for the assignment.

    The instructions state:

    "Open the file, and change the name from “Guest” to your name. Failure to do so will result in 0 points for the entire project. If you submit a file that has a different name from yours, you will get 0 points for the assignment as well as all prior Packet Tracer assignments. For example, if you submit a .pka file in unit 6 that has someone else’s name on it, then you will receive 0 points for unit 1 to unit 6 Packet Tracer assignments."

r/s,
Tom [INSTRUCTOR]

---

## Week 1 Notes
*Posted: 2021-08-16T14:57:11Z*

Good morning class and welcome to week 1 of Computer Networking I!

There's a lot of information for you to absorb this week. Some of you are also taking more than one class this term and having to work in three learning management systems  (Park's Canvas, Cisco's NetAcad & Fort Hays State University’s Netlab) can be daunting at first.

I'm here to get you through it all, so please continue to ask questions and let me know if you're having any technical difficulties with the different systems.

I post weekly notes in the Announcement section, so please be sure you check there first before asking your questions.

Before you get started with your weekly assignments, please first complete the following activities this week: 

You should start by making sure you can login to Cisco Networking Academy ( [link: http://www.netacad.com/] www.netacad.com) and that you can access the Cisco module (CS365A-2021-F1A-DL - Computer Networking I).

Enroll in and complete the "Introduction to Packet Tracer" course.  To enroll, login into the Computer Networking I Cisco course, click on “Resources”, "Student Resources", "Introduction to Packet Tracer Course", "Sign up today!", then "English".  The course will appear on your NetAcad home screen. 

Download and install the Packet Tracer app (v 8.0.1) on your computer.

Let me know if you're having any issues enrolling yourself.  If you have no Packet Tracer experience, it's really important that you complete this course before attempting any of the actual Packet Tracer labs for this class.

Login to Netlab (labs.fhsu.edu). I sent out your login information last week. Your first Netlab assignment isn’t due until the end of unit 2, but you should ensure that you can login this week so we can resolve any issues you might be having.

Watch the two videos that I posted in the "Getting started with Cisco's Networking Academy and Packet Tracer" announcement.

Important:

    Complete the various quizzes and exams in this order (after reading the weekly material, of course):

Complete the Cisco module quizzes.  These are not graded and you can complete them as often as you want.  They are found at the end of each module.

Complete the weekly Park chapter quizzes.  These are graded as well and can only be taken once.  These quizzes can only be taken during their respective week.  They are locked after their deadline.  Let me know if you have a life event that prevents you from completing a quiz when it's available.

Complete the Cisco module group exams.  There are three of these exams, to be completed during units 2, 4 and 6. These are a graded part of the class.  They can be taken up to ten times.  Cisco will record your last score.

Here are your activities/assignments for this week:

- Read & review this week’s reading materials, PowerPoint slides, websites and videos (Unit 1: Overview)
- Complete the Introduction under the module “Course Information.”
- Complete the Policy Quiz under the module “Course Information.”
- Complete Packet Tracer (PT) lab 2.5.5 found in this week's Cisco reading material.
- Complete the Job Market Research lab.
- Complete the Unit 1 Park quiz via Park Online website (Canvas).
- Participate in this week's discussion thread.

Please let me know if you have any questions or are having any technical/access issues.

r/s,
Tom [INSTRUCTOR]

---

## Where do I find the Packet Tracer Software?
*Posted: 2021-08-16T14:52:54Z*

Hello everyone,

    We'll be using Packet Tracer version 8.0.1 for this class.  Once you've registered and logged into NetAcad, you can find the Packet Tracer download section here:   [link: https://www.netacad.com/portal//resources/packet-tracer] https://www.netacad.com/portal//resources/packet-tracer

    Please download version 8.0.1.  I highly encourage you to enroll and complete the "Introduction to Packet Tracer" course if you've never used Packet Tracer before or you would like a refresher.

    Let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Getting Started with Cisco's Networking Academy and Packet Tracer
*Posted: 2021-08-16T14:44:55Z*

Good morning class,

    These two videos should help you get started with Cisco's Networking Academy and Packet Tracer (this one's rather long, but it provides you the basics to get you going.)  I highly recommend that you enroll in the free "Introduction to Packet Tracer" course in NetAcad.  For this class, please download and use Packet Tracer version 8.0.1.

 [link: https://youtu.be/mD4mVNZ_-pg] 

 r/s,
Tom [INSTRUCTOR]

---

## NetAcad and Netlab Accounts have been created
*Posted: 2021-08-12T20:43:48Z*

Hello class.

    I've enrolled everyone in the Cisco Networking Academy course (CS365A-2021-F1A-DL Computer Networking I) and created your Netlab accounts.

    You should have received a Course Enrollment Notification email from the Cisco Networking Academy in your Park email account ( [link: [REDACTED]@park.edu] [REDACTED]@park.edu) with the necessary login information today.

    You should also have an email in your inbox with instructions how to login to Netlab.  Please be sure to read the attached Netlab student guide.

    Please let me know if you haven't received these emails or are having trouble logging into the Networking Academy site or Netlab.

r/s,
Tom [INSTRUCTOR]

---

## Welcome to CS365A - Computer Networking I
*Posted: 2021-07-27T00:04:48Z*

Welcome, everyone!

My name is Tom [INSTRUCTOR] and I'll be your instructor for the next eight weeks. I'm an adjunct computer science instructor, living in Beaufort, SC.  I've been teaching face to face and online classes for Park since 2014.

IMPORTANT NOTICE: This course requires that the Park final exam be administered via remote proctoring. Please be sure to read the Park Online Proctoring Policy (link below) and acknowledge the “Notice of Required Remote Proctoring for Online Students”.  The Park Online Proctoring Policy can be found here:

 [link: https://www.park.edu/academics/park-distance-learning/academic-policies/#ProctorPolicy] PARK UNIVERSITY ONLINE PROCTORING POLICY

Please visit all items under the "Course Information" module before class starts. In particular, please read the "Syllabus", "Textbook and Resources", "Course Overview", and "Activities and Rubrics", "Course Schedule", and "Discussion Participation" for the policies and administration guidelines related to the course.

Familiarize yourself with "Learner Support" on the left-hand navigation menu and "Canvas Help" on the Home page will be good especially when you encounter problems using Park Online Canvas system.

Please note that you are required to have a device accessible to you such that you can execute "Cisco Packet Tracer" software locally to complete the laboratory projects and Cisco exams for this course. The “Cisco Packet Tracer FAQ” has the information about the required software and hardware for this course. Be sure to resolve any issue on running Cisco Packet Tracer software as early as possible.

The "Final Exam Study Guide" and "Skills Exam Study Guide" have assessment information so that you know what to expect in these exams throughout the course. Please visit "Introductions" and make a post to introduce yourself to the class.

You will need to take the "Policy Quiz" to see if you understand the policies and administration rules in this class.

We'll be using three online environments during this course:

1. Park University Canvas. We'll do most of our communications here (via the Inbox on the left side menu) and to post grade assignments. You will submit your weekly packet tracer files, participate in the weekly discussions and complete the weekly Park quizzes and Park final exam here.

2. Cisco Networking Academy ( [link: http://www.netacad.com/] www.netacad.com) - All lecture material for this course (CS365A-2021-F1A-DL - Computer Networking I), as well as the packet tracer assignments, are located here. You will also complete your Cisco module group exams here. You will receive your Cisco Welcome email in your Park email the weekend prior to day 1.  Please let me know if you haven't. 

If this is your first time accessing NetAcad, please click on the "Activate Account" link in the Cisco email.  If you've already registered before and can't remember your NetAcad password, navigate over to  [link: http://www.netacad.com] www.netacad.com [link: http://www.netacad.com/]  and click on "Log In, Forgot Password" to reset your password.

You will be using Cisco's Packet Tracer software (v8.0.1) to complete your weekly labs.  Please take the time and read the Cisco Packet Tracer FAQ page and the download instructions which are posted in the announcements before attempting any labs.  Packet Tracer is available for download here:   [link: https://www.netacad.com/portal/resources/packet-tracer] https://www.netacad.com/portal/resources/packet-tracer.  Please make sure you download Packet Tracer version 8.0.1.  

If you haven't used Packet Tracer before, I highly recommend you enroll in the Introduction to Packet Tracer course.

3. NetLab ( [link: https://labs.fhsu.edu/] https://labs.fhsu.edu) - You will complete your weekly NetLab assignments here. I will send a separate email to your Park email address with instructions and logon information for NetLab.  

If you haven't done so yet, please post a short introduction in Canvas. 

Please let me know if you have any questions or can't login to Cisco's NetAcad website or haven't received the Cisco login instructions by day 1 (16 August 2021).

Should you have any question before class starts, please visit my virtual office under "Instructor's Office". 

I look forward to working with you all over the next eight weeks.

r/s,
Tom [INSTRUCTOR]

---

## www.netacad.com and labs.fhsu.edu
(1) www.netacad.com is the Cisco Networking Academy site in which you will access all Cisco material for this course.

If you do not have an account in this site previously, you should have received an email via park.edu about your account and initial password to access to this Cisco site. If you have not received such an email by the end of the first day of the term, please let your instructor know.

If you encounter any problem while accessing Cisco Networking Academy (www.netacad.com) site, please click "Support" on the top menu bar > select either “Support Community” or “NetAcad FAQs” depending on your situation. If you select “NetAcad FAQs”, you can click either “System Help” or “Course Help.”

(2) labs.fhsu.edu is the Netlab site in which you will perform the Netlab projects. 

If you do not have an account in this site previously, you should have received an email via park.edu about your account and initial password to access to this site. If you have not received such an email by the end of the first day of the term, please let your instructor know.

---
