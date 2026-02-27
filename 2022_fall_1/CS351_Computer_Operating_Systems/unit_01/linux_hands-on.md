# Unit 1: Linux Hands-on

Setup a user account in Pond Linux server (5 points):

You should have received an email from Park's ITS in your Park email account (possibly with the subject of "SSH account"). That email includes your user name and password for the Pond server. Check with your instructor if you haven't received such an email. 

You will need an SSH client to connect to the Pond server. Any SSH client would work. If you haven't used any, use one of those:

Windows users may use PuTTY. To download it, go to  [link: http://www.putty.org] http://www.putty.org and click on the download link at the top of the page. Scroll down to the "Alternative binary files" section on the next page. Download the 64-bit x86: putty.exe file if your processor is "x64-based processor" ("x64" is derived from 64-bit x86). Download the 64-bit Arm: putty.exe file if your processor is "ARM-based". See  [link: https://www.tenforums.com/tutorials/176966-how-check-if-processor-32-bit-64-bit-arm-windows-10-a.html] https://www.tenforums.com/tutorials/176966-how-check-if-processor-32-bit-64-bit-arm-windows-10-a.html   

Mac users may use the build-in tool Terminal. By default, Terminal is located in Applications > Utilities folder. You may also search for "terminal" using Spotlight search.

Make sure that you can log in to the Pond server with your Pond user name and password. To connect to the Pond server, use address pond.park.edu (or its IP address 68.66.1.81).

Windows users: see  [link: https://canvas.park.edu/courses/69412/files/9320733?verifier=GctFNtPMfFcEvt9UpBvQCX6YxGahTyBWQSniOM6Q&wrap=1] How to Configure PuTTY for Park Server.pdf

Mac users:
start Terminal, type in ssh you_user_name@pond.park.edu (or use the IP address), and hit Enter to connect.

You will be asked to confirm the authenticity of the Pond server if this is your first time connecting to this server. Type yes.

Type in the password from that ITS email. Be aware that you will not see anything displayed on screen (not even *) while you type in your password. Don’t be alarmed. That's one of the security features of SSH. If you accidentally typed the wrong password, you will be allowed to enter the password again.

Now you're ready for the hands-on exercises for this course.

Similar to DOS, Linux has many commands that you can use from the command-line interface. Here are a few that a regular user may use often: ls, cd, pwd, mkdir, cp, mv, rm, rmdir, cat, and chmod. Some additional basic commands: echo, find, locate, grep, tar. To understand what each of these commands does, type in command man for manual. For example, man cd displays the manual page of command cd.

If needed, reference this  [link: https://canvas.park.edu/courses/69412/pages/linux-help] Linux Help page (also listed on the Course Home page).

Do the following:

Required: use man to find out the information of one of the commands listed above. Pick a command that hasn't been posted by others. Use your own words to describe what that command does and provide a meaningful usage of that command. If needed, do some additional research on that command.

Optional: You may also post any question, problem, issue, and positive or negative experience that you may have about obtaining the user account and getting the ssh to work.

Required: Respond to a minimum of one post from your classmates.

**My Score:** 5.0/?

---

## My Discussion Posts

**Posted:** 2022-08-15T23:12:08Z

grep

 

Class,

grep is a tool that allows the user to search for a phrase within a file with different parameters. This works kind of like ctrl-f on a web-browser. The search is done by typing:

grep "Whatever you're looking for" sometext.txt

The man-pages calls the searched string a "pattern." The search will return the entire line and it works with partial searches, so if you search for "what" you will find every instance including "whatever," this can be turned off with -w. The tool also has some helpful parameters like -n, which prints the line where the string was found.

---
