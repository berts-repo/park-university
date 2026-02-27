# Unit 7: Notes

This unit introduces you to installing and configuring a new disk with a Unix file system.

Traditional disks and file systems

There has been a lot of study and documentation about how to use a single disk or multiple disks for a standalone computer system. Single disks often get partitioned into different logical disks for purposes of reliability and security. Multiple disks are often configured as a single, logical volume, either through a RAID controller or with logical volume management.

Cloud disks

In the cloud, the constraints of a physical disk are removed from the system administrator and pushed down to the cloud provider. Instead of worrying about partitions and logical volumes, administrators can just add one or more disks, and then resize them as needed. This flexibility relieves the administrator of having to make complicated storage plans and just focus on how much of a commodity is necessary.

File system trees 

One big difference between the file systems in Unix and Windows environments is that a Unix system has a single file system tree, starting at the root directory /. No matter how many disks or partitions are added, they all appear somewhere in that single tree. This hides the underlying details of storage from users and programs, but it requires the system administrator to attend to the organization instead.

Windows on the other hand, requires the user to know about different devices, each of which has a separate file system. This is why you specify C: for the internal disk, D: for an external drive or CD, etc.

Cron

Often there are system administration tasks that need to be done on a regular basis, like rotating and archiving log files, generating reports, or checking the health of a system. Unix systems provide the cron facility for scheduling these types of tasks. The format of a crontab file can be confusing at first because there are so many fields, which imparts incredible flexibility. Rather than try to understand it all, it’s best to start by looking at scheduling something every day at the same time, or ever hour at the same time. Once you are comfortable with that, then extend it to every Sunday at a certain time, or the 1st and 15th of every month. These scenarios will probably cover over 85-95% of your scheduling needs.

Make sure you use the crontab program and don’t edit the scheduling file directly. Your changes won’t be made know to the scheduler if you edit the file directly.
