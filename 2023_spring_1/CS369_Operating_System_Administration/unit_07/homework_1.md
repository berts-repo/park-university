# Unit 7: Homework 1

**Due:** 2023-02-27T05:59:00Z
**Points Possible:** 35.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to create snapshots of your instance as backups and use these snapshots to create additional instances.

A snapshot is a GCP object that contains the files from a disk. Don't confuse this with screenshot, which is a image you use to document some activity in the exercise.

Preparation

Read  [link: https://cloud.google.com/compute/docs/disks/create-snapshots] Creating Persistent Disk Snapshots to get an idea of the process. You use snapshots as a way of backing up disks used by your instances.

Assignment

Create a Word document that contains your screenshots and explanations of what you  are doing.

Create a new instance called unit7-base (f1-micro, standard persistent disk, allow http traffic), then install nginx and add your name and unit 7 to the index page.

Shut down your instance

Create a snapshot.

Start your instance, install php, test your instance to be sure it runs info.php.

Shut down your instance

Create another snapshot.

Start your instance, install a prebuilt php web site (see below).  Test your website. Take a screenshot showing the home page of the simple php website and the URL (ip address) you used to access the page.

Then shut down your instance.

Create a third snapshot. When it is finished, take a screenshot showing all three snapshots and their sizes.

At this point, you have three snapshots, one for each stage of the installation process. Now it is time to create instances using these snapshots. See  [link: https://cloud.google.com/compute/docs/instances/create-start-instance#createsnapshot] https://cloud.google.com/compute/docs/instances/create-start-instance#createsnapshot for information on this process.

Create a new instance named unit7-copy. Instead of creating it with a new disk, use your latest snapshot instead. 

Test your new instance. When you click on the External IP link and specify the new port number, you should see a web site that behaves exactly like the one you built originally. Take a screenshot of your simple php web site, showing your IP address and the home page. 

Take a screenshot of your current snapshots

Snapshots taken at regular intervals (daily, weekly, hourly) or after major changes, like adding new software, provide backups of your work which can be used to create new instances in the future.

At the end of your Word document, include the answers to the following questions:

Why are the snapshots of the same disk dramatically different sizes and why do they seem to get smaller even after adding software to the system?

Describe how you got the simple website files onto your instance.

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

Turn In

For documentation, you should submit your Word document to Canvas

Getting a php website

Add a prebuilt, php web site to your instance. There is one available  [link: https://github.com/banago/simple-php-website] here. There is a button to download all the files in .zip format to your PC. This might help you, if you install unzip on your instance. You can also install git on your instance and get the files directly, or use 7-zip on your PC and create a tar file. However you do it, put all the files on your new GCP instance, create a new web site configuration in sites-available and sites-enabled which uses port 7074 and points to the directory for this site.  (If the links on the site  don’t work, edit the file config.php and make sure to set 'pretty_uri' => false.)

Due Date

by 11:59 p.m., Sunday, CT

---

## My Submission

**Score:** 35.0/35.0
**Grade:** 35
**Submitted:** 2023-02-21T07:35:11Z

### Submitted Files

- **unit7-hw1-doc.docx**
  - Downloaded: `files/unit7-hw1-doc.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-02-28T10:50:19Z):

> Bert,

Excellent job on the assignment this week.  The screenshots was just for each instance.  You captured all three in just one.  This week you got to play around with creating snapshots.  The technologies behind snapshots have been around for a long time.  In short, they let you quickly make online disk-based copies of selected data sets that are easily accessed.  The digitization of business data has led to data sets becoming increasingly large and many businesses/organizations often fall behind in completing up to date backups of vital data.  This is mainly due to bandwidth constraints.  Snapshots fix this as they don’t affect bandwidth and are usually transferred locally to an external device.  They make restoration pretty easy.  Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material covered this week.

Prof [INSTRUCTOR]
