# Unit 5: Homework 2

**Due:** 2023-02-13T05:59:00Z
**Points Possible:** 25.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to practice with using public/private key pairs to log in to your cloud instance.

Preparation

Obtain a ssh client for your local computer. If you have a Mac or Linux system, there is already a command line ssh client built in. If you have a Windows system, a simple free option is  [link: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html] putty and puttygen. Or, for a slightly nicer environment, I use  [link: https://mobaxterm.mobatek.net/download.html] MobaXTerm. Get the portable versions if you do not have administrator rights to install software on the computer you are using. 

Start your Cloud Console and start your instance. Click on the SSH link to log in.

Assignment

Keep a Word document with the answers to the marked questions and with screenshots as required.

Overview

On your instance, look in the file ~/.ssh/authorized_keys, which contains PUBLIC keys of people allowed to log into your account. Note the general format of an entry, especially the comment #Added by Google. If you don’t see this file, logoff from your instance and then log back on. The file will be there then.

Copy one entry and add it to your Word document.

The general steps to this assignment, and to using public/private keys to access a system are to

On your PC, create a public/private key pair and put each one in a separate file.

Append the public key to  ~/.ssh/authorized_keys on your instance.

Use the private key with your ssh program to access your instance.

Note that rather than do step 2 directly, we’re going to add it to the GCP configuration and let GCP update the file on the instance automatically as needed. You should not be changing any files on your instance for this exercise.

Create a key pair

On a PC, using MobaXterm/Tools/MobaKeyGen or puttygen (see image)

Click the Generate button, then follow the instructions to move the mouse

Add a Key Passphrase, retype in the Confirm box

Click Save Private Key and give a file name. The file will have an extension of .ppk.

Copy the public key from the top box, labelled Public key for pasting into OpenSSH server

See the section on Adding a public key to GCP

Linux/Mac

Run the program ssh-keygen

Enter a file name for the private key. I’d use John-Key

Enter a pass phrase. Reenter the phrase

You’ll end up with two files in the same directory. One will have the extension .pub. This is your public key. Open or view the file and copy the contents.

See the section on Adding a public key to GCP

Adding a public key to GCP

As far as a Linux instance is concerned, the file ~/.ssh/authorized_keys  controls access to the instance. However, GCP wants to manage this file itself. One way it does that is through metadata. Click on the metadata item in Cloud Console, then SSH keys. You should see some keys allowing you to log into any instance in your project. If you don't see these, start an SSH session, then return to this page in GCP.

Notice that the keys specify the username for the account the key works with. Your first task is to add your own key you can use to log into your account directly from your PC without going through GCP. Once you click Edit, you can add or delete ssh keys, but not change them. Click Add Item, then copy/paste the public key you generated above into the space provided. The system will use the last item in the ssh key as the user name, as in the key at the bottom of the figure below, so be sure to change it to your GCP username.

Watch out for line breaks in the key that you paste. There shouldn’t be any, though they can sneak in based on the way you do your copy.

Take a screen shot of your ssh keys as shown above (Metadata/Ssh-Keys/Edit) in GCP and add it to your Word document. Be sure to show your usernames. Explain why it isn’t a security breach to give the instructor a copy of your key.

Log in directly from your computer

Login from PC

Create a new session in putty or mobaxterm

host is IP of your instance

username is the username next to the key in the metadata section of GCP

Left menu/Session/SSH/Auth to specify file with your PRIVATE key

Connect

Establish a connection to your instance

Say yes if prompted about unknown server

Enter the password for your Private key file

Enter username if prompted

Login from Linux/Mac

            ssh username@IPaddress –i privatekeyfile

Once you have logged in to you existing account,

Take a screenshot showing you have logged in with your own key pair. Add it to your Word document.

Adding another public key to GCP

Repeat the key generation steps and add another key to your GCP project. This time, change the username to something different. If your username is AlfredENeuman, then use the new username CS369AlfredENeuman. Take a screenshot that shows your keys in the metadata section. Be sure to show the username.

Log into your instance using this second key. Taks a screenshot showing you've logged in, then look at the last few lines of your /etc/passwd file. What is there that wasn't there before!?

Explain in your Word document what Google’s infrastructure did under the hood that enabled you to log in with this second generated key pair.

Reflection

At the end of your Words document, include the answers to the following questions:

In a sentence or two, what did you learn?

In a sentence or two, what did you like about this project?

In a sentence or two, what did you find confusing or would like to see done differently regarding this project?

Turn In

For documentation, you should submit your Word document to Canvas.

---

## My Submission

**Score:** 21.99/25.0
**Grade:** 21.99
**Submitted:** 2023-02-10T11:17:45Z

### Submitted Files

- **unit5hw2_doc.docx**
  - Downloaded: `files/unit5hw2_doc.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-02-14T11:16:56Z):

> Bert,

Great job on the homework assignment this week. In this homework assignment you had a chance to practice using public/private key pairs to log into your cloud instance. As you have learned, there are some free tools out there that could be used to SSH into a system. These include putty and MobaXTerm. Logging into the new account was part of the requirements this week.  Keep up the good work and don’t hesitate reaching out if you have any questions on any of the material covered.

Prof [INSTRUCTOR]
