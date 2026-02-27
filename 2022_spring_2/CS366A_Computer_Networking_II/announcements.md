# Announcements - CS366ADLS2A2022 Computer Networking II

## Week 8 Notes
*Posted: 2022-05-02T23:01:26Z*

Congratulations class. You’ve made it to the final week!

I hope you found the course materials to be insightful and valuable as you continue your Park University studies and advance in your professional military or civilian careers.  

Please make sure you read the "Honorlock Student Information"  and "Netlab Skill Assessment Instructions Note" announcements.

The Park final exam covers the material you learned in this class. 

The Cisco final exam covers all of the material from CS365 and CS366.  If it's been a while since you took CS365 or you have CS365 transfer credit, I recommend you review all of the module quizzes.  I've opened up the first three Cisco Module Group exams, and you can take them several time to practice for the Cisco final.  As a reminder, you will need to complete the Cisco Feedback before you can take the Cisco final exam.

As a reminder, you can take the Cisco skills assessments multiple times.  The system will record the most recent score. This may be a good option to consider to improve your score. You have until the end of this course to retake the assessment.

Please take a moment to complete the student survey.  We're always looking for student feedback to help shape and improve this course.  Let us know what you liked and what you think should be improved upon.

Let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Honorlock Student Information  ***PLEASE READ***
*Posted: 2022-05-02T22:58:35Z*

Good evening, everyone. 

    Park University uses Honorlock as the proctoring system for the Park final exam.  Park University no longer uses ProctorU, which some of you may have used in the past. 

    Advantages:  there are no fees and no requirement for you to schedule your Park final exam.  You have the flexibility to take the final at anytime during week 8.  

    The following information includes important steps you need to complete before taking your final exam:

Honorlock Proctoring is required for your final exam.

You will not be charged for the use of Honorlock.

You must use Google Chrome as your web browser to take the final exam in Honorlock.

You will need a functioning webcam and microphone and the Honorlock Chrome extension (which will be installed during the practice quiz).

You will use the Honorlock link on the Canvas main menu (left side). Once you click, you will be prompted to install the Honorlock extension.  **Do not use the To Do link to Honorlock on the right side as this will result in an error message.**

You need to have a government issued form of identification available the day you take the exam.

Honorlock will walk you through a 60-second pre-test checklist that includes a room scan using your webcam. 

Please review these parameters for the final exam (what is allowed/not allowed):
This exam is closed book, closed notes, closed electronic devices, and closed Internet access, except for exam itself.

You may use the Honorlock calculator.

You may use a small whiteboard or single sheet of blank paper in a transparent sleeve, and a dry erase marker for scratch paper. You are required to show your scratch paper/white board on camera at the start of the testing session, and erase and show it on camera after you finish the test before exiting the testing session.

After you answer each question, the question will be locked, therefore, you won't be able to revisit the question again.

No restroom break is allowed.

If you have questions, please visit  [link: https://parkuniversity.freshdesk.com/support/solutions/articles/6000242302] Park University HonorLock information (FAQ, Resources, and Help Desk)

    I recommend you complete the Honorlock practice quiz early this week before attempting the Park final exam, especially if you haven't used Honorlock before.  That should give you enough time to resolve any issues you might have.

    Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Netlab Skills Assessment Instructions Note
*Posted: 2022-05-02T22:53:42Z*

Class,

    Here's a quick announcement for this week's Netlab Skills Assessment:

    When scheduling this assessment, you'll need to select 'AE CCNA1 v7.0 SA - MDP' CCNA1: Introduction to Networks v7.0 Skills Assessment'

    The instructions state, "...Your instructor will assign one of the IPv4 networks from the table below."  

    

    Please select the 192.168.10.0/24 network.

    In part 2, step 2, you'll need to configure the IPv6 addresses for switch S1.  By default, the switch won't accept IPv6 addresses.  You will have to use the correct "sdm prefer" command, followed by the reload command to allow IPv6 configuration.

    Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Week 7 Notes
*Posted: 2022-04-25T22:46:00Z*

Good evening everyone and welcome to week 7.  You are almost done with this course! 

    Up to this point, you’ve learned most of the fundamentals of setting up your own network.   This week, you put it all together as you build a network and make sure it’s working correctly. 

    Some of you may find this week's NetLab assignment (17.7.6) to be the most challenging lab this term. One of the missing configurations is a static route for R1. Cisco 8.5.3 provides a brief introduction of this topic, including this example (which, by the way, is not the answer for the lab):

        ip route 10.1.1.0 255.255.255.0 209.165.200.226

    You could also create a Gateway of last resort route, which uses this format:  ip route 0.0.0.0 0.0.0.0 <ip address of the destination interface>

    Static routing is covered in greater detail in the next class, CS371 - Internetworking

    Please let me know if you’re still stuck after reading 8.5.3 or if you have any other questions about this lab.

r/s,
Tom [INSTRUCTOR]

---

## Week 6 Notes
*Posted: 2022-04-18T23:20:41Z*

Good evening class and welcome to Week 6!

There are only three weeks left in this term. You're almost there!

This week, you'll learn about the Application layer.

In the OSI and the TCP/IP models, the application layer is the closest layer to the end user. As shown in the figure, it is the layer that provides the interface between the applications used to communicate, and the underlying network over which messages are transmitted. Application layer protocols are used to exchange data between programs running on the source and destination hosts.

Here are your assignments for this week:

Complete Packet Tracer 16.5.1

Complete Netlab 16.5.2

Complete the Wireshark HTTP lab

Take the Cisco Module Group Exam for modules 14 & 15.

Take this week's Park Quiz.

Participate in this week's discussions.

Complete all remaining unit 5 assignments by this Wednesday, 4/20/22.

Let me know if you have any questions or encounter any technical difficulties.

r/s,
Tom [INSTRUCTOR]

---

## Unit 5 Assignment Extension
*Posted: 2022-04-16T21:26:23Z*

Good afternoon everyone,

This week’s assignment due date has been extended out to Wednesday, 4/20/22.

r/s,
Tom [INSTRUCTOR]

---

## Week 5 Notes
*Posted: 2022-04-11T23:18:02Z*

Good afternoon class and welcome to week 5!  You are halfway through the course.

This week, we’ll skip over module 15 and go straight to module 16, where you’ll learn about the fundamentals of network security:

Security Threats and Vulnerabilities

Network Attacks

Network Attack Mitigation

Device Security

This is a really important topic, as cyber attacks and incidents have significantly increased over the last few years.  The incidents listed here ( [link: https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents] https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents) can be quite eye opening.  In addition to learning about the concepts of network security, this week's labs will give you hands on experience with securing (or 'hardening')  routers and switches.

Please let me know if you have any questions or issues with this week’s assignments.

r/s,
Tom [INSTRUCTOR]

---

## Week 4 Netlab 13.3.2 Helpful Tip
*Posted: 2022-04-08T23:55:33Z*

Hello class,

    This week's Netlab assignment has you entering a series of commands for S1 and R1.  The instructions state to copy and paste the configurations.  Netlab has a feature which allows you to do just that, so there's no need to manually type in each line one at a time.  (Which is very tedious, especially if you are running the lab several times.)

    Here's how you do it (I'll use S1 as an example):

    1. Start up Netlab 13.3.2 and wait for the devices to fully start.
    2. Copy the initial configs for S1 from the lab instructions to your clipboard.  (Part 1, step 2)
    3. Select S1 and enter global config mode (config t)  *** This is important, as the copy/paste won't work if you're in user exec or privileged exec mode.
    4. Click on the down arrow on the S1 box and select "Paste to Terminal"
    5. Click inside the box and paste the configs from your clipboard. Make sure you position your cursor to the right of the "end" command and hit enter.
    6. Click on the "Paste" button.  This will copy the configs to the CLI.

   I've attached a few screenshots of this process.

    Let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Week 4 Notes
*Posted: 2022-04-05T11:42:52Z*

Good morning class and welcome to Week 4.

This week is all about the transport layer (module 14).  At this layer (OSI layer 4 or TCP/IP transport layer), you will learn about the two protocols, Transmission Control Protocol (TCP) and User Datagram Protocol (UDP), how these protocols establish and terminate sessions and how port numbers play an integral part in the sessions. 

You have a total of three labs due this week:  one Packet Tracer, one Netlab and one Wireshark lab which you were introduced to last week.  

Please note that this week's Packet Tracer lab is a simulation project.  You will need to complete and submit the project report form.  You can find this form in the Unit 4 Packet Tracer 14.8.1 directions.

Here are four additional videos to complement this week's learning material:

 

  

Please let me know if you have any questions. 

r/s,
Tom [INSTRUCTOR]

---

## Week 3 Notes
*Posted: 2022-03-28T23:48:55Z*

Good evening, class.

   This week, you'll finish up module 12 and learn about IPv6 subnetting.  Current best practice is to subnet along the subnet ID, which is the fourth hextet:

    There is some ongoing discussion about using a /126 or /127 prefix for point to point WAN connection (similar to a /30 network in IPv4).  However, Cisco recommends using a /64 prefix throughout your implementation, as other prefixes can break the functions of these operations:

Neighbor Discovery (ND)

Secure Neighbor Discovery (SEND) [RFC3971]

Privacy extensions [RFC4941]

Parts of Mobile IPv6 [RFC4866]

Protocol Independent Multicast - Sparse Mode (PIM-SM) with Embedded-RP [RFC3956]

Site Multihoming by IPv6 Intermediation (SHIM6) [SHIM6] 

    (Cisco IPv6 Addressing Guide)

    You'll also cover module 13 - ICMP (Ping & Traceroute).

    Please take a look at the unit 3 Wireshark TCP lab description this week.  The lab isn't due until unit 4, but now is the time to download the Wireshark software and get familiar with it.  I've attached the step by step lab instructions.

    Let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Week 2 Notes
*Posted: 2022-03-21T23:29:04Z*

Good evening class and welcome to week 2!  

I hope you are all settling into your rhythm for this class.  If you came to this class with a transfer credit from your work experience or another university class, it might seem like you were going from zero to 100 mph last week as the material went straight into subnetting IPv4 networks!  Be patient with yourself.  It does get easier. 

Like this week, which is all about IPv6 addresses (Module 12).  As a refresher, IP addresses operate at layer 3 of the OSI model and provide the means for devices to communicate between networks.  Remember that devices on the same network communicate via MAC addresses (layer 2).

Although IPv6 looks more challenging (it's longer and is in hexadecimal format), it's actually easier to work with, as there are no subnet masks to deal with!  (Really, it is.  You just need to get used to the hexadecimal format. :-) )

Please continue to send me your questions, as you go through this week's materials and assignments.

Here are some important things to remember when learning about IPv6:

1.  Address representation:  An IPv6 address is 128 bits long.  In order to make it easier to read, you can omitting leading zeros and use double colons.  However, you can only use a double colon once in an address!
        For example:

            This is an acceptable use, since there's only one ::  -  2001:db8:acad::1/64
            This is an unacceptable example, because there are two separate ::  -  2001:db8:acad::0::2/64 

    While you can omit leading zeros, you CANNOT omit trailing zeros.  

    Let's use this uncompressed example to apply the rules in 12.2.2 (omit leading zeros) and 12.2.3 (double colon):

         2001:0db8:0000:0200:0010:0000:0000:0001/64

    Here's the correct use of the rules to get the most compressed IPv6 address:

        2001:db8:0:200:10::1/64 

    Incorrect use of the rules:

        2001:db8::200:1::1/64

      Reasons: 

        The double colon is used more than once.  It should be used to replace the most consecutive instances of 0000s, which are the sixth and seventh hextets.

        The fifth hextet (0010) is incorrectly compressed as 1.  You can only omit leading zeros, from 0010 to 10.  You can't omit the trailing zero (0010 to 1), because that changes the number itself. 

2.  Subnet masks are not used.  Instead, you use the prefix length.  This is annotated in a slash format, just like in IPv4 (i.e.: /64)

3.  There are many different types of IPv6 addresses, the most common being the global unicast address (equivalent to an IPv4 public address).  Another common one is the link local address (also unicast).  This is a non-routable address used by devices to communicate with each other within a specific subnet.  They start with FE80:.

4.  An IPv6 address consists of three parts:  the Global routing prefix (48 bits long), the subnet ID (16 bits) and the Interface ID (also called the host ID) (64 bits).  

5.  You can subnet an IPv6 address, but it's much easier.  You typically use the subnet ID to create the different subnets.

    Here's an example of subnetting an IPv6 address, using the subnet ID.  (The subnet ID is the fourth hextet)

    Let's say you've been given a global routing prefix of 2001:db8:acad.  To create subnets with the subnet ID, you could have the following subnets:

        subnet 1:  2001:db8:acad:0001/64 (or 2001:db8:acad:1/64 compressed)
        subnet 2:  2001:db8:acad:0002/64
        subnet 3:  2001:db8:acad:0003/64
        subnet 4:  2001:db8:acad:0004/64
       and so on...

Here are two informative IPv6 videos:

Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Netlab Assignment List for CS366A
*Posted: 2022-03-21T23:24:38Z*

Hello class,

Here's the complete list of NetLab assignments, by unit (week).  These labs are located here: AE CCNA1 v7.0 - MDP

Unit 1 - Chapter 11 Section 11.10.2 Netlab - Design and Implement a VLSM Addressing Scheme

Unit 2 - Chapter 12 Section 12.7.4 Netlab - Identify IPv6 Addresses

Unit 3 - Chapter 12 Section 12.9.2 Netlab - Configure IPv6 Addresses on Network Devices

Unit 4 - Chapter 13 Section 13.3.2 Netlab - Use Ping and Traceroute to Test Network Connectivity

Unit 5 - Chapter 16 Section 16.4.7 Netlab - Configure Network Devices with SSH

Unit 6 - Chapter 16 Section 16.5.2 Netlab - Secure Network Devices

Unit 7 - Chapter 17 Section 17.7.6 Netlab - Troubleshoot Connectivity Issues.  Use the 192.168 network address.

Unit 8 - NetLab Skills Assessment  (located here:  AE CCNA1 v7.0 SA - MDP)

Please note that you will be competing for simulation time slots with students from other Park networking courses.  Netlab allows you to pre-schedule your lab days or even weeks in advance.  This may be a helpful tool, since the time slots do tend to fill up quickly on the weekends.

Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## How to Save your Netlab Configurations
*Posted: 2022-03-19T17:04:55Z*

Hello class,

    Netlab gives you the option to save your router and switch configurations.  You can then reload them when you restart the lab at a later date or time.  It does not save your PC configs, though.  You will have to reenter those.  This is very useful if you're not able to complete the lab within your allotted time frame.

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

## Week 1 Notes
*Posted: 2022-03-14T15:33:33Z*

Good afternoon class and welcome to Week 1 of Computer Networking II!

Please read all of the Announcements for this week.

This week's lessons continue with module 11 (IPv4 Addressing), which you should have started during week 7 of your CS365A - Computer Networking I class.  Some of the readings will be a review, but the second half will be new material.

Make sure you review this week's PowerPoint slide, websites and videos found on the Unit 1 overview page.

Please take your time with this week’s chapter readings, watch the below videos and send me your subnetting questions.

To help you with this week's material, I've included a VLSM subnetting chart for /24 and smaller networks. It really helps you visualize all of the subnets possible in a /24 network. It includes all of the possible network, first & last host and broadcast addresses.   (Just remember that you won't be able to use this chart during the Park final exam.)

It's really important for you all to understand and calculate the three different types of addresses in a network:

    Network address

    Host address (first and last host addresses)

    Broadcast address

    Please review Cisco 11.1.6 - Network, Host, and Broadcast Addresses and watch the video at Cisco 11.1.5.

***SPECIAL NOTE***

Don't confuse a subnet or network address with a subnet mask address:

   Here are some subnet mask examples and their corresponding prefix notations: 

        225.255.255.0 - /24 (If you've been around networking for a while, you may have heard this referred to as a "class C" network, which is technically incorrect now, since we've moved to classless inter-domain routing (CIDR) many years ago)

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

***A subnet calculator can be very helpful, but please note that for the Park final exam, you will be required to calculate subnets manually. No calculators or websites will be allowed. ***

Let me know if you have any questions (subnetting or otherwise) or encounter any technical difficulties logging into NetAcad or Netlab.

r/s,
Tom [INSTRUCTOR]

---

## ***Important Packet Tracer Requirement***
*Posted: 2022-03-14T15:27:33Z*

Good morning, class.

    Important reminder:  When completing the Packet Tracer labs, please remember to enter your name in the User Profile when starting each lab.  If you don't do this, you'll get a 0 for the assignment.

    The instructions state:

    "Open the file, and change the name from “Guest” to your name. Failure to do so will result in 0 points for the entire project. If you submit a file that has a different name from yours, you will get 0 points for the assignment as well as all prior Packet Tracer assignments. For example, if you submit a .pka file in unit 6 that has someone else’s name on it, then you will receive 0 points for unit 1 to unit 6 Packet Tracer assignments."

    Also, please make sure to upload a screenshot of the Assessment Items tab of your completed lab.

r/s,
Tom [INSTRUCTOR]

---

## Refresher Training on Packet Tracer and Netlab+
*Posted: 2022-03-14T15:26:13Z*

Class,

    Here are two useful videos if it's been a while since you worked in Cisco's Networking Academy and the NetLab+ environment or are a transfer student who used a different lab environment.

    The Netlab video is geared for CS365A students, but the contents apply to this class as well.

Please let me know if you have any questions.

r/s,
Tom [INSTRUCTOR]

---

## Cisco Networking Academy and Netlab+ Enrollments
*Posted: 2022-03-14T15:23:11Z*

Hello everyone!

    I've enrolled everyone in the Cisco Networking Academy course: CS366A-2022-S2A-DL Computer Networking II, as well as the Netlab+ course.

    I sent an email to everyone with the login instructions for both learning environments.  Please let me know you haven't received the email or are having issues logging into either sites.

r/s,
Tom [INSTRUCTOR]

---

## Welcome to CS366A - Computer Networking II
*Posted: 2022-03-07T20:53:31Z*

Welcome, everyone!

My name is Tom [INSTRUCTOR] and I'll be your instructor for the next eight weeks. I've lived in Beaufort, SC since 2001 and I've been teaching face to face and online classes for Park University since 2014.

IMPORTANT NOTICE: This course requires that the Park final exam be administered via Honorlock proctoring. Please be sure to read the  [link: https://canvas.park.edu/courses/65366/pages/honorlock-student-information-access-to-final-exam-through-honorlock-on-canvas-menu] Honorlock Student Information (Access to Final Exam Through Honorlock on Canvas Menu)

and complete the Student Acknowledgement of Course Remote Proctoring Requirements.

Please visit all items under the "Course Information" module before class starts. In particular, please read the "Syllabus", "Textbook and Resources", "Course Overview", and "Activities and Rubrics", "Course Schedule", and "Discussion Participation" for the policies and administration guidelines related to the course.

Familiarize yourself with "Learner Support" on the left-hand navigation menu and "Canvas Help" on the Home page will be good especially when you encounter problems using Park Online Canvas system.

Please note that you are required to have a device accessible to you such that you can execute "Cisco Packet Tracer" software locally to complete the laboratory projects and Cisco exams for this course. The “Cisco Packet Tracer FAQ” has the information about the required software and hardware for this course. Be sure to resolve any issue on running Cisco Packet Tracer software as early as possible.

The "Final Exam Study Guide" and "Skills Exam Study Guide" have assessment information so that you know what to expect in these exams throughout the course. Please visit "Introductions" and make a post to introduce yourself to the class.

You will need to take the "Policy Quiz" to see if you understand the policies and administration rules in this class.

We'll be using three online environments during this course:

1. Park University Canvas. We'll do most of our communications here (via the Inbox on the left side menu) and to post grade assignments. You will submit your weekly packet tracer files, Netlab reports, participate in the weekly discussions and complete the weekly Park quizzes and Park final exam here.

2. Cisco Networking Academy ( [link: http://www.netacad.com/] www.netacad.com) - All lecture material for this course (CS366A-2022-S2A-DL - Computer Networking II), as well as the packet tracer assignments, are located here. You will also complete your Cisco module group exams here. You will receive your Cisco Welcome email in your Park email account prior to Day 1.  Please let me know if you haven't received the email by Monday, 3/14/22

If this is your first time accessing NetAcad, please click on the "Activate Account" link in the Cisco email.  If you've already registered before and can't remember your NetAcad password, navigate over to  [link: http://www.netacad.com/] www.netacad.com [link: http://www.netacad.com/]  and click on "Log In, Forgot Password" to reset your password.

You will be using Cisco's Packet Tracer software v8.1.1 (this is a new version) to complete your weekly labs.  Please take the time and read the Cisco Packet Tracer FAQ page and the download instructions which are posted in the announcements before attempting any labs.  Packet Tracer is available for download here:   [link: https://www.netacad.com/portal/resources/packet-tracer] https://www.netacad.com/portal/resources/packet-tracer.  Please make sure you download Packet Tracer version 8.1.1.  

If you haven't used Packet Tracer before, I highly recommend you enroll in the Introduction to Packet Tracer course.

3. Netlab ( [link: https://labs.fhsu.edu/] https://labs.fhsu.edu) - You will complete your weekly Netlab assignments here. I will send a separate email to your Park email address with instructions and logon information for Netlab.  

If you haven't done so yet, please post a short introduction in Canvas. 

Please let me know if you have any questions or can't login to Cisco's NetAcad or FHSU's Netlab website or haven't received the Cisco login instructions by day 1 (14 March 2022).

Should you have any question before class starts, please visit my virtual office under "Instructor's Office". 

I look forward to working with you all over the next eight weeks.

r/s,
Tom [INSTRUCTOR]

---

## www.netacad.com and labs.fhsu.edu
(1) www.netacad.com is the Cisco Networking Academy site in which you will access all Cisco material for this course.

If you do not have an account in this site previously, you should have received an email via park.edu about your account and initial password to access to this Cisco site. If you have not received such an email by the end of the first day of the term, please let your instructor know.

If you encounter any problem while accessing Cisco Networking Academy (www.netacad.com) site, please click "Support" on the top menu bar > select either “Support Community” or “NetAcad FAQs” depending on your situation. If you select “NetAcad FAQs”, you can click either “System Help” or “Course Help.”

(2) labs.fhsu.edu is the Netlab site in which you will perform the Netlab projects. 

If you do not have an account in this site previously, you should have received an email via park.edu about your account and initial password to access to this site. If you have not received such an email by the end of the first day of the term, please let your instructor know.

---
