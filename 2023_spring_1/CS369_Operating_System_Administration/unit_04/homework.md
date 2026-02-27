# Unit 4: Homework

**Due:** 2023-02-06T05:59:00Z
**Points Possible:** 60.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to create multiple web sites using a single nginx web server.

Preparation

You may need to review material about nginx configuration, the Unix tar command, and the concept of symbolic links. Remember, the nginx configuration directory is /etc/nginx and the website directory is /var/www/html. This assignment will be done entirely on your running instance and Cloud Console.

Assignment

Keep a Word document with the steps you take and requested screenshots to document your work.

Create a site

Make a copy of the file

 /etc/nginx/sites-available/default

Put the copy someplace convenient. You'll want to review this in case you ever corrupt the actual configuration file.

Download the file  [link: https://canvas.park.edu/courses/72082/files/9774590/download?verifier=29lBxzuURhW3UFjubPjEwaYOz6aqEbeu32oAFTaF&wrap=1] CCSC.tar from Canvas to your local PC.

Upload this file to your GCP instance and copy it to the directory /var/www/html.

Use the tar command to extract the contents of the archive. Note that tar extracts files into the current directory, so you’ll want to cd /var/www/html before you issue the command

tar -xf CCSC.tar

This creates a directory called CCSC, which contains a file index.html along with 16 other directories, 01..16.

Test your web site by appending /CCSC to the IP address in a browser window. You should see a new web page about a Bazaar workshop. Click around on the links. They should all work.

Change the name of the directory from CCSC to CCSC1. Check that you can still access the site using IP#/CCSC1 in a web browser.

Put your name prominently on the opening web page, similar to what you did in Unit 2.

Take a screen shot showing your browser window with the URL, along with your name on the displayed page.

When you have finished this step, the directory tree should look like this.

Create another site

This means creating another directory tree, another configuration file, another symbolic link, and finally, adding a firewall rule to enable access to your new sites.

Extract the files in CCSC.tar again, then change the name of the directory to CCSC2. You’ll have two directories each with a copy of the same files. You'll find it helpful to change the text on the heading in each index.html to indicate which site is which.

This time though, you’re going to access your web site though a different mechanism. Normally you would use a different domain name to access the new site, but instead we’re just going to use a different port number.

Make a copy of the configuration file in the sites-available directory. In the copy you'll need to edit the root element to point to the directory you just created, and you'll need to edit the listen element to use one port in the range 7070-7075.

Create a symbolic link in sites-enabled to point back to the new configuration file.

Adding files to the directory tree doesn't affect the nginx server, but changing a configuration file does. You'll need to tell nginx to read its configuration files again. Use

sudo service nginx reload

You can find all the commands available by using

sudo service nginx help

Firewall rules

To create a firewall rule, you'll have to use the GCP console. See the attached image for where this is and what the settings should be. You want to enable a small range of ports, like 7070-7075, since you will be hosting several different web sites. Make sure that the Target is http-server. Note that the default rule is already there.

Once the firewall is opened, you should be able to get to your new website with a URL like http://1.2.3.4:7070, using your IP address and site port number. You’ll know it’s the correct site, because you have already modified the index.html file to show this is second site.

Take a screen shot showing your browser window with the URL, along with the modified front page.

Create a third site

Now repeat this all one more time, just so you get to practice the steps. The good news is that you don't have to create another firewall rule, as long as you use a port number in the right range.

Take a screen shot showing your browser window with the URL, along with the modified front page.

When you are finished, you will be able to access 3 web sites, each using a different port number on your server.

Reflection

Add your screenshots to a Word document, along with a brief summary of the steps you needed to take to get the web sites to work. This will be a reminder for how to repeat this assignment at a later time. Also include the answers to the following questions:

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

Submit Assignment

For documentation, you should submit your Word document to Canvas.

---

## My Submission

**Score:** 60.0/60.0
**Grade:** 60
**Submitted:** 2023-02-05T06:57:14Z

### Submitted Files

- **unit4hw1_doc.docx**
  - Downloaded: `files/unit4hw1_doc.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-02-06T23:18:05Z):

> Bert,

Excellent job this week on the homework assignment.  You did a great job creating multiple web sites using the single nginx web server.  You also had the opportunity to create a firewall rule.  

Here are some additional resources on the topics:

https://fedingo.com/how-to-host-multiple-domains-on-one-server-in-nginx/

https://www.learnbestcoding.com/post/15/hosting-multiple-websites-with-nginx

https://avinetworks.com/docs/latest/gcp-firewall-rules/

https://www.youtube.com/watch?v=8pqwoZflqPo

I enjoyed reading your reflection.  This wasn’t an easy assignment but you did it ;-)  Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material.

Prof [INSTRUCTOR]
