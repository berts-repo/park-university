# Unit 7: Discussion

Introduction

This unit’s discussion covers various backup systems.

Initial post:

In the exercise, you are working with snapshots, which are a simple form of backup for an entire disk. Research other backup strategies and present your findings. Be sure to cite your references. Some additional topics are:

Explain some other tools or programs for making backups.

Explain how you might backup a live system, since anymore shutting the system down like we did to make a snapshot won’t work in a 24-7 always-on environment.

Explain the benefits and drawbacks of an incremental backup system.

Explain how you might structure your system so you don’t have to backup an entire large disk every time.

Reply posts:

Respond to two different students. Provide an additional reference and show how it expands on the original post. Comment on the feasibility of the proposed backup solution and offer any improvements or suggests. You are encouraged to share any of your own backup experiences, both good and bad.

Directions

Make your initial post by 11:59 PM Wednesday and reply to at least two classmates by 11:59 PM Sunday.

ULOs Reflected In Discussion

Contrast the benefits and performance of different file system organizations (CLO 4)

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2023-02-21T01:20:13Z

Hey Class,

the command I am going with is the 'dd' command in linux, a very powerful tool for creating and managing backups, which is shipped with most linux distributions. This tool makes a bit by bit copy of many different things including, hard drives, partitions, binary-files and magnetic tape. A bit by bit copy means that it doesn't just backup the data, it makes a copy of the empty data too. This tool can do many other things besides making backups; including, striping header files and changing data formats. Because, this tool is versatile and considered very powerful as it, it is recommended to use it with caution, because you can erase everything by mistyping a source to destination path. (Wallen 2016)

 

Wallen, J. (2016, August 19). Full Metal Backup using the DD command. Linux.com. Retrieved February 20, 2023, from https://www.linux.com/topic/desktop/full-metal-backup-using-dd-command/

---


### Feedback

**[INSTRUCTOR]:** Bert,

Excellent job this week in the forums. Thanks for getting all your posts in. As I’ve mentioned previously, it really helps to keep the discussion going. This week we discussed backups and more specifically the 3-2-1 model. This model states, there should be 3 copies of data, on 2 different media, with 1 copy being off site. There are a ton of ways to skin the cat on this. You can use backups on disks (SAN, NAS, etc…), snapshots, bold archive storage in the public cloud, or any number of other solutions. Today’s personal and business environments are bombarded with threats. Software corruption, local disaster, ransomware attack, hard drive failure, theft, and human error expose us and our organizations to the risk of losing our data. Backups today are a must. Keep up the great work and don’t hesitate reaching out if you have any questions on any of the material covered.
