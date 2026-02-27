# Announcements - CS369DLS1A2023 Operating System Administration

## Final Grades Posted
*Posted: 2023-03-06T11:08:48Z*

Class,

Your final grades are posted and have been submitted to the school.  It has been a pleasure having you all in class. 

Best of luck in all your future endeavors.

Prof [INSTRUCTOR]

---

## Last Day
*Posted: 2023-03-05T23:42:23Z*

Class,

There are still a few of you who have not taken their final exam.  Reminder, today is the last day of class.  If you haven't taken your final, please do so ASAP.

For those that have taken your exam, they have all been graded as of this posting.

Prof [INSTRUCTOR]

---

## Final Exam
*Posted: 2023-03-01T10:00:00Z*

Class,

There are only a few more days left to class.  There are still a handful of you who need to take the final exam.  Please ensure you get it knocked out before class ends.  

Also, if you have missing assignments, please get them turned in ASAP.  

Prof [INSTRUCTOR]

---

## Week 7 Recap / Week 8 Intro (with Forum Summary)
*Posted: 2023-02-27T10:00:01Z*

Class,

We are on the homestretch!  This is our last week.  As a friendly reminder, no assignments will be accepted once class ends.  Please ensure you get all your assignments in before midnight Sunday.

In the forum this week, we discussed backups. There is a good rule called the 3-2-1.  What this means is:

3: Create one primary backup and two copies of your data

2: Save your backups to two different types of media

1: Keep at least one backup file offsite.

Essentially, the 3-2-1 backup strategy reduces the impact of a single point of failure such as a disk drive error or a stolen device.

Data can be lost from any number of things such as data migration, software corruption, local disaster, hard drive failure, theft, etc….

This past week (week 7), you were introduced to installing and configuring a new disk and file system and scheduling processes to run at a later time.  You got to use Crontab.  Here are some good resources:

 [link: https://crontab.guru/] https://crontab.guru/Links to an external site.

 [link: https://phoenixnap.com/kb/set-up-cron-job-linux] https://phoenixnap.com/kb/set-up-cron-job-linuxLinks to an external site.

 [link: https://www.geeksforgeeks.org/crontab-in-linux-with-examples/] https://www.geeksforgeeks.org/crontab-in-linux-with-examples/Links to an external site.

This week is week 8.  This week you have your final exam.  Please ensure you get it done before midnight Sunday.  Keep up the good work and don’t hesitate reaching out if you have any questions on any of the material covered this week.

Prof [INSTRUCTOR]

---

## Week 7 Mid-Week Announcement
*Posted: 2023-02-22T11:53:23Z*

Class,

This week you are working continuing to work with PHP.  

I wanted share some resources that may help you with any problems/issues you are experiencing:

*PHP downloading verse executing:  [link: https://serverfault.com/questions/955715/nginx-downloads-php-instead-of-executing] https://serverfault.com/questions/955715/nginx-downloads-php-instead-of-executing

*PHP downloading verse executing:  [link: https://stackoverflow.com/questions/25591040/nginx-serves-php-files-as-downloads-instead-of-executing-them] https://stackoverflow.com/questions/25591040/nginx-serves-php-files-as-downloads-instead-of-executing-them

*PHP downloading verse executing:  [link: https://www.digitalocean.com/community/questions/php-files-are-downloading-instead-of-executing-on-nginx] https://www.digitalocean.com/community/questions/php-files-are-downloading-instead-of-executing-on-nginx

Configuration:  [link: https://linuxiac.com/how-to-configure-nginx-to-work-with-php-via-php-fpm/] https://linuxiac.com/how-to-configure-nginx-to-work-with-php-via-php-fpm/

Install PHP:  [link: https://www.keycdn.com/support/how-to-install-nginx-php] https://www.keycdn.com/support/how-to-install-nginx-php

Install PHP:  [link: https://www.rosehosting.com/blog/how-to-install-php-7-4-with-nginx-on-ubuntu-20-04/] https://www.rosehosting.com/blog/how-to-install-php-7-4-with-nginx-on-ubuntu-20-04/

Install PHP video:  [link: https://www.youtube.com/watch?v=fM9PFNY6jK8] https://www.youtube.com/watch?v=fM9PFNY6jK8

Keep up the good work.

Prof [INSTRUCTOR]

---

## Week 6 Recap / Week 7 Intro (with Forum Summary)
*Posted: 2023-02-20T10:10:00Z*

Class,

We are quickly approaching the finish line.  There is only two weeks left.  If you have missing assignments, please get them in ASAP.  No assignment will be accepted once the class ends.  This past week we touched on building a LEMP (Linux, (E)nginx, MySQL (MariaDB), and PHP) server.  One of the questions in the forum this past week asked for alternatives to LEMP.  Some alternatives include:

MEAN (MongoDB, Express, Angular, Node.js)

LAPP (Linux, Apache, PostgreSQL, PHP)

LEAP (Linux, Eucalyptus, AppScale, Python)

LLMP (Linux, Lighttpd, MySQL/MariaDB, PHP/Perl/Python)

XAMPP (Cross-platform, Apache, MariaDB, PHP, Perl)

For the homework assignment this past week, you got to play around with the setting up the LEMP server.  Some of you got stuck on the “my domain”.  The domain is just a filler for  [link: http://www.example.com/] www.example.comLinks to an external site. or the IP address.  In this case, you needed to use your GPC IP address 35.xxx.xxx.xxx:8083/info.php to access your site. 

Additionally, another common problem some of you experienced was that the php file being downloaded anytime you tried running the php server.  Some good references for this problem include:

https://serverfault.com/questions/955715/nginx-downloads-php-instead-of-executing

https://www.digitalocean.com/community/questions/php-files-are-downloading-instead-of-executing-on-nginx

https://stackoverflow.com/questions/25591040/nginx-serves-php-files-as-downloads-instead-of-executing-them

https://www.pcsuggest.com/setup-nginx-with-php/

This week (week 7) is pretty busy.  We will dive deep into installing and configuring a new disk and file system along with scheduling processes.  As always, please ensure you take a look at the notes page.  Don’t hesitate reaching out if you have any questions on any of the material covered.

---

## Week 5 Recap / Week 6 Intro (with Forum Summary)
*Posted: 2023-02-13T10:00:00Z*

Class,

This past week we discussed user management.  When it comes to user management, one of the most common things that comes up is how to manage remotely.  This requires using Secure Shell (SSH).  SSH is a cryptographic network protocol that allows you to operate services securely over an unsecured network (ie. Internet).   SSH key relies upon the use of two related keys, a public key and a private key, that together create a key pair that is used as the secure access credential.  The private key is secret, known only to the user, and should be encrypted and stored safely.  The public key is open to everyone and is used to encrypt the message. 

Here is a site on SSH if you want to dig deeper into the topic: https://www.ssh.com/academy/ssh/protocol#typical-uses-of-the-ssh-protocol

The discussion this past week touched on searching the internet for aliases or other settings that users might want to put in their login/logout configuration files.  This discussion is always an interesting one.

This week (Week 6) we are going to discuss how to install and configure a suite of complementary programs.  Specifically, you will be building a LEMP server.  LEMP stands for Linux, (E)nginx, MySQL (MariaDB), and PHP.  You will be installing a web application that makes use of all these services.  Please ensure you read the Unit 6 notes, especially in regards to testing your database.

As always, keep up the good work and don’t hesitate reaching out if you have any questions on any of the material covered this week.

Prof [INSTRUCTOR]

---

## Week 5 Mid-Week Announcement
*Posted: 2023-02-14T00:24:32Z*

Class,

Here are some areas to look at if you are stuck regarding the ~/.ssh/authorized_keys file:

sudo apt-get upgrade

 [link: https://askubuntu.com/questions/685456/no-such-file-or-directory-authorized-keys] https://askubuntu.com/questions/685456/no-such-file-or-directory-authorized-keys

 [link: https://askubuntu.com/questions/685456/no-such-file-or-directory-authorized-keys]  [link: https://docs.digitalocean.com/support/how-to-troubleshoot-ssh-authentication-issues/#:~:text=permissions%20or%20ownership.-,Here%20are%20some%20steps%20you%20can%20take%20to%20troubleshoot%20this,readable%20by%20the%20SSH%20client] https://docs.digitalocean.com/support/how-to-troubleshoot-ssh-authentication-issues/#:~:text=permissions%20or%20ownership.-,Here%20are%20some%20steps%20you%20can%20take%20to%20troubleshoot%20this,readable%20by%20the%20SSH%20client.

 [link: https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys] https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

 [link: https://access.redhat.com/solutions/327053] https://access.redhat.com/solutions/327053

 [link: https://stackoverflow.com/questions/22119866/authorized-keys-does-not-present-for-new-user] https://stackoverflow.com/questions/22119866/authorized-keys-does-not-present-for-new-user

 [link: https://stackoverflow.com/questions/60938337/ssh-no-such-file-or-directory] https://stackoverflow.com/questions/60938337/ssh-no-such-file-or-directory

---

## Week 4 Recap / Week 5 Intro (with Forum Summary)
*Posted: 2023-02-06T11:00:03Z*

Class,

Excellent job this past week. 

This past week we dove deeper into configuring the nginx webserver.  Specifically, regarding setting up multiple hosts on a single server.  The discussion this week touched on configuration options available for the nginx server.

We also touched on the Linux “tar” command.  File compression is an essential utility across all platforms.  It helps you reduce file size and share files efficiently.  Compressed files are also easier to copy to remote servers which was a part of your homework assignment this week. The Tape Archiver (tar) command is the most widely used archiving utility in Linux and is executed directly in the terminal using the tar command.  The utility is simple and has many helpful options for compressing files, managing backups, and extracting.

Here is a site that has some really good tar examples:  [link: https://www.tecmint.com/18-tar-command-examples-in-linux/] https://www.tecmint.com/18-tar-command-examples-in-linux/Links to an external site.

On the homework assignment this week, some of you realized quickly that if you weren’t in the right directory then you would get a permissions error.  The CCSC.tar file had to be in the /var/www/html directory in order for you to use the tar command.  You also likely had to use the “sudo” command in order to move the file from the home directory.

This week, (week 5), we will introduce you to user management.  We will examine the mechanisms that control user access both within a Linux environment but also through GCP.

Pay particular attention to the notes section.  This week has two homework assignments.  Start them early and don’t wait till Sunday night to start them.

Keep up the great work and don’t hesitate reaching out if you have any question on any of the material covered.

Prof [INSTRUCTOR]

---

## Great Collaboration
*Posted: 2023-02-02T11:54:23Z*

Class,

I was just checking the Question & Answer thread and I like the teamwork and collaboration I'm seeing.  As some of you have noticed, the instructions are not a complete step action for the assignments.  This is to mimic real world environments where you may be asked to set up a server or other system with some limited information.  For the most part, when it comes to step actions for cyber related things in general like setting up a server, these instructions are outdated once they are published or simply don't align to the countless configuration setups out there.  Take your home computer for example.  Everyone of us is using something different (ie. Windows, Mac, Linux, Chrome OS).  Even if we have the same operating system, our settings and configurations are different.  Our home security is different.  These all add levels of complexity that may cause instructions not align correctly.  This is similar to a real world enterprise environment.  Every company operates on different equipment, security, etc... 

Just like the real world where you can phone a friend, the Q&A forums is that tool.  The collaboration you all are doing is great.  

Switching gears, I wanted to share a port cheat sheet with everyone.  This is a good resource in general to save/bookmark:

https://packetlife.net/media/library/23/common_ports.pdf

Prof [INSTRUCTOR]

---

## Chat GPT
*Posted: 2023-01-31T13:33:37Z*

Class,

I wanted to share with you a good Artificial Intelligence site called ChatGPT.

The site is  [link: https://chat.openai.com/chat] https://chat.openai.com/chat

This site may help you as you work through some problems, or at the very least, expose you to AI.

Prof [INSTRUCTOR]

---

## Week 3 Recap / Week 4 Intro (With Forum Summary)
*Posted: 2023-01-30T10:00:02Z*

Class,

This past week we touched on some python programming.  So far, the assignments I’ve graded look great. 

In the discussion area we addressed logging. All operating systems maintain logs.  Logs are used for security and system administration purposes.  In Linux, logs are typically rotated and eventually purged.  If log files were not rotated, compressed, and periodically pruned, they could eventually consume all available disk space on a system.  This is why some logs have .1, .2, .3, etc… after them. Additionally, we touched on the GNU gzip which is a file compression algorithm which results in files being archived in a compressed file ending in .gz. 

This week (Week4) we are going to configure the nginx webserver and control it from the command line.  We will also touch on creating some firewall rules for the virtual private cloud (VPC).  Please ensure you take a look at the Week 4 notes before you dive into the assignments this week.  Especially the part about keeping a copy of your initial nginx configuration file in a separate location.

We are also going to talk about Apache and how it differs from nginx.  Apache is the most commonly used web server on Linux Systems.  Here is the web page for Apache if you want to dive deep into the site: https://httpd.apache.org/.

The discussion this week will address some configuration options for nginx.  For full credit in the forum, please ensure you respond to two different students.

As always, don’t hesitate reaching out if you have any questions on any of the material covered.

Prof [INSTRUCTOR]

---

## Week 3 Midweek Announcement
*Posted: 2023-01-27T02:50:05Z*

Class,

Great job so far dusting off your Python knowledge from your previous classes.  

Remember, when it comes to python, sky's the limit.  The code can be written a million different ways to achieve the outcomes you want.

For those that are having issues, here is some code to get you started on the instance.start:

///////////////////////////////////

from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'Name of your Project'

# The name of the zone for this request.
zone = 'us-central1-a'

# Name of the instance resource to start.
instance = 'vm-tb-01'

request = service.instances().start(project=project, zone=zone, instance=instance)
response = request.execute()

# Define variables
startingDate = []
startingTime = []

///////////////////////////////////

 

Prof [INSTRUCTOR]

---

## Week 2 Homework Solution
*Posted: 2023-01-24T23:58:07Z*

Class,

There were a couple of you who had issues with the assignment this week.  I spoke to Kenny and he gave me permission to share his screenshots.

This is a good example of the homework solution for the week 2 homework assignment.

Prof [INSTRUCTOR]

---

## Week 2 Recap / Week 3 Intro
*Posted: 2023-01-23T10:30:00Z*

Class,

This past week you set up the Google Cloud Platform (GCP), creating a virtual machine instance, and running a web server on your own instance.  Great job!  For the most part, the remainder of the class will use GCP for the homework assignments.  There are a couple of you who have not turned in the homework assignments.  Please do so ASAP.  Some of these assignments can be pretty intensive and it’s easy to fall behind.

I'm happy to see some of you are using the Questions and Answers forums.  As you continue with this class, this will be the main area for you all to help each other.  It will come in handy, especially this week.

This week, you will be introduced to Python and how to use it to complete a couple different types of system administration tasks.

Python is a high-level, general purpose programming language.  It is very popular.  Here is a good Python Tutorial from W3 Schools: https://www.w3schools.com/python/.

Please carefully review the Unit 3 Notes which may save you some time and heartache.  

Remember, when it comes to python, there are countless ways to tackle the problem.  

This week you have two homework assignments, the discussion, and quiz.  Try and get your discussion in early. 

As always, don’t hesitate reaching out if you have any questions on any of the material covered this week.

Prof [INSTRUCTOR]

---

## Week 2 Mid-Week Announcement
*Posted: 2023-01-18T11:58:40Z*

Class,

For those that turned in the Week 2 assignment already, they look great.  For those that haven't set up the Google Cloud Platform (GCP) yet, you probably should start.  Don't wait until Sunday to figure out you have issues.  GCP will be used through the rest of the class.  If you don't complete week-2 correctly you won't be able to complete any other week.  This is the most important week there is.

Everyone should have received an email from me with getting your Google Credits.  Please follow the instructions in the Unit 2 Module carefully.

For the assignment this week, please ensure you use my personal email "cs369[INSTRUCTOR]@gmail.com" which was set up specific for this class.  If you already submitted your assignment without that email, please just update it in CPC (Don't use my Park address).

A couple of you have noted issues.  You must be fully logged off your park account and signed into your personal account per the instructions.  Missing this step will cause issues.  There is a work around in the notes section if this happens.

As always, don't hesitate reaching out if you have any questions on any of the material covered.

Prof [INSTRUCTOR]

---

## Week 2 Homework Assignment
*Posted: 2023-01-16T13:53:29Z*

Class,

You all should have received an email with the link to request your Google Cloud Coupon.  Please check your Park/Classroom email.

If you haven't received it, please let me know.

Please use this email as detailed in the Homework Assignment: cs369[INSTRUCTOR]@gmail.com

This course will require a lot of time for trial and error, research, and using other outside resources to complete.  This is a hands on course, not a knowledge based course.  This course will test your ability to "do" and problem solve rather than simply memorize or write something.  

 

Prof [INSTRUCTOR]

---

## Week 1 Recap / Week 2 Intro
*Posted: 2023-01-16T13:52:39Z*

Class,

I sent everyone an email the other day for redeeming your Google Cloud Platform Credits this week.  These credits are not the same same ones you used for Qwiklabs in Unit 1.  The rest of the class will use the Google Cloud Platform.  Please ensure you follow the instructions on how to request them very closely.   Many of you also discovered that it's not good to wait till the last minute for these assignments.  I can tell you, if you don't start them early you will struggle.  These assignments will take you a lot of time to complete.  You'll need to do a lot of trial and error, youtube videos, research, and discussion with other classmates.  

This past week you used Linux Zoo to complete tutorials 1-6.   In these tutorials you had an opportunity to start using some of the command line features as well as learning the directory hierarchy.  One feature that you learned was the cal (calendar) feature.

This week, you will continue to use the command line to change file ownership and permissions and to search for and edit text information in files.  You will also use the Google Cloud Platform to create and run a virtual machine instance.

In the enterprise environment, virtual servers are extremely common.  Virtualization helps companies achieve faster and easier backup and recovery of key application workloads and data.  It also enables the organization to be more cost effective on how they deploy IT infrastructure.

If you want to play with virtualization some more, you can download Oracle VirtualBox ( [link: https://www.virtualbox.org/] https://www.virtualbox.org/ Links to an external site.) and install it on your home computer.  It’s a free Type 2 Hypervisor that will allow you to install other operating systems such as Linux without impacting your current OS.  It’s another great way test your skills that you are learning on your own Linux machine.

Keep up the great work and don’t hesitate reaching out if you have any questions or concerns on the material covered this week.

Prof [INSTRUCTOR]

---

## Posture for Success
*Posted: 2023-01-14T14:34:17Z*

Class,

I see some very good dialogue between a handful of students in the Week 1 Questions and Answers.  I would encourage everyone to do their best to start the assignments early in the week to give yourself enough time to work through problems.  This is the easiest week you'll have.  The more students that contribute to the questions and answers forum, the better.

Starting next week, we will move to the Google Cloud Platform.  This is the real cloud (not the qwiklabs your doing in the homework assignment this week).  Creating and provisioning web servers and databases can be a daunting task.  

If you are stuck on something, post it.  If you have a solution or recommendation to a problem, share it.  Scan this forum daily for updates and opportunities to share your success with others.  This is a collaborative effort.

Prof [INSTRUCTOR]

---

## Weekly Question and Answer Threads
*Posted: 2023-01-12T23:22:01Z*

Class,

If you have questions on the homework or assignments, please submit your questions in the weekly Question and Answer forum area.  I want students to get feedback from other students on what they did that solved the problems.  There is no doubt you will all encounter "things" not working.  Most of you will find work arounds.  This is where asking questions and students helping out students will aid in the learning process by creating shared understanding.

While these assignments are individual assignments, you can work together to share information on how you solved certain issues.  This is encouraged.

Many of the assignments will require you to do trial and error and review outside material on the internet to solve.  By asking other students what they did, you may cut down on a lot of heartache.

Prof [INSTRUCTOR]

---

## Week 1 Update
*Posted: 2023-01-11T05:00:03Z*

Class,

Some of you have already completed the homework assignments.  That's great to see.

These homework assignments / labs are not easy and progressively get harder each week.  They also build upon one another. 

For this week, I would encourage you to access the Google QWIKlab now and not wait until Sunday. 

Prof [INSTRUCTOR]

---

## Week 1 Introduction
*Posted: 2022-12-12T23:40:34Z*

Class,

Welcome again!  This should be a fun an exciting term.  I would encourage all of you to read the syllabus and familiarize yourself with the classroom as soon as possible.  I would also encourage you to start your assignments early in the week to give yourself some breathing room in case you run into problems.  Waiting till Sunday night to discover you have issues is a bad strategy ;-) 

If you haven't done so already, please fast forward to Homework #2 and ensure you request your Google Training Credits.  It can take a few days to process so start this now if you haven't already.  The instructions are in the Homework 2 section.

This week, you will need to register for an account on Linux Zoo where you will complete Assignment 1.  You can assess it buy going to LinuxZoo.net.  This is a hands-on course which will require some trial and error on your part as you learn the Linux Command Line.   

Here are some additional command line cheat sheets for Linux that I would recommend bookmarking for future reference:

 [link: https://www.guru99.com/linux-commands-cheat-sheet.html] https://www.guru99.com/linux-commands-cheat-sheet.html (Links to an external site.)

 [link: https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/] https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/ (Links to an external site.)

 [link: https://linuxconfig.org/linux-commands-cheat-sheet] https://linuxconfig.org/linux-commands-cheat-sheet

---

## Welcome to CS369
*Posted: 2022-12-12T23:40:08Z*

Class,

Welcome to CS369 Operating System Administration.   I am excited to be your instructor for the next 8 weeks and am delighted to have the opportunity to collaborate with you as you continue your journey to complete this course.

In this course, we will discuss the foundational knowledge regarding operating system administration.

Class starts on 01/9/2023

Please take some time to look through the course and ensure you review the syllabus.  I will post announcements each week.  Please ensure you read them as they may contain important information which will save you a lot of time and heartache.

For those wanting to know more about me see below:

Professional Experience

After graduating high school, I enlisted in the Marine Corps infantry where I spent 12 years traveling the world.  During that time, I obtained my BS in Management Computer Information Systems and a Masters in Information Security – I even started a PhD before getting out.  My education and training in the Marine Corps helped me land a job as a Special Agent with the Naval Criminal Investigative Service (NCIS) – yes, like the T.V. show ;-)  I was stationed in California and worked general crimes (death, sexual assaults, thefts, etc…). 

Currently, I am the Assistant Director of the U.S. Army CID's Cyber Directorate. I oversee all criminal investigations involving network intrusions and other malicious activity on the Army’s network.  I am a certified digital forensic examiner and hold a wide array of industry certifications such as the CISSP, Certified Ethical Hacker (CEH), CompTIA Security + (SEC+), and the Computer Hacker Forensic Investigator (CHFI) to name a few.

Besides catching the proverbial bad guy, I have been teaching network security and digital forensics for the last 9 years.  My favorite thing about teaching these classes is preparing students to enter the cyber workforce after they graduate and instilling the skills and confidence needed to address the future challenges of the virtual world.  The cyber environment is austere at best and it will take a well-educated workforce to tackle the complex challenges to prevent, detect, and investigate network intrusions and related compromises.

Good luck and welcome to the class.

 

Prof [INSTRUCTOR]

---
