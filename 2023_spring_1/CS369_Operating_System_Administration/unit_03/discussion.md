# Unit 3: Discussion

Introduction

This unit’s discussion covers logging.

Initial post:

Consider the logging files in /var/log (and its subdirectories) on your GCP instance. For an initial post, pick an entry in one logging file that is interesting to you, describe how you viewed the file, show the entry, and then describe why it is interesting or confusing.  

Reply posts:

Respond to two different students, either by answering a question, describing what program did the logging and why it is useful, in what situation you might use this information, etc.

You can also describe why some files end in .gz, how to read the files that end in .gz, what the numbering system means, how to read the information in the files that aren’t text files, the permissions on the files, etc.

Directions

Make your initial post by 11:59 PM Wednesday and reply to at least two classmates by 11:59 PM Sunday. 

ULOs Reflected In Discussion

Discuss logging and the implications for system security (CLO 2)

Navigate a directory hierarchy (CLO 5)

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2023-01-25T06:31:39Z

Class,

when I was looking through some of the .log files I found myself in var/log/apt. When I was looking to see if I could comprehend some of the packages being installed with apt. I noticed there was a bunch of references to "unattended-upgrades," which caught my attention. When I went back into /var/log/ I noticed the directory /unattended-upgrades/ and investigated further.

There is a log file that i found interesting, and highlighted some of the things that caught my eyes:

I found this weird because it was using the installing/package tools like "apt" and "dpkg". When working through our assignment last we we initially installed and updated our new VM instance with the package manager "apt-get" so, this is odd to my baby linux brain. Why was three different package managers tools being logged?

After a quick search of "unattended-upgrades" I discovered it is a tool, that keeps your system up to date and secure automatically, which can (can?) be good as it requires less administrations intervention.

---


### Feedback

**[INSTRUCTOR]:** Bert,

Excellent job in the forum this week. Thanks for getting all your posts in.  This week we touched on logs.  All operating systems maintain logs.  Logs are used for security and system administration purposes.  In Linux, logs are typically rotated and eventually purged.  If log files were not rotated, compressed, and periodically pruned, they could eventually consume all available disk space on a system.  This is why some logs have .1, .2, .3, etc… after them. Additionally, we touched on the GNU gzip which is a file compression algorithm which results in files being archived in a compressed file ending in .gz.  Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material covered this week.

Prof [INSTRUCTOR]
