# Unit 1: Lecture

Chapter 1: Introduction

An operating system is an essential part of a computer system. In this chapter, we will discuss what an operating system is, the history of operating systems, various types of operating systems, operating system concepts, various system calls, and the operating system structure. To get started, the following gives a highlevel introduction to each of these subjects.

What is an operating system?

Hardware and software are major components of a computer system. The software includes system programs and application programs. An operating system is a system program that controls the normal functions of a computer. Figure 1 from [1] shows the major components of a computer system and the location of the operating system within the computer system.

Figure 1. Hardware and software are major components of a computer system. The software is further made up of system programs and application programs.

In general, an operating system can be viewed as a resource manager and an extended machine.

Resource manager: The operating system manages the different parts of the system efficiently.

Extended machine: The operating system provides the users with a virtual machine that is more convenient to use than the actual machine.

History of Operating Systems

Various operating systems have been developed over the past 50 years. In the beginning, the operating system can only deal with one task at a time. Nowadays, the operating system is so sophisticated that it can perform multiprogramming and time-sharing among many interactive users simultaneously. The first chapter includes the highlights of early batch systems (see figure 2 from [1]), multiprogramming systems (see figure 3 from [1]), and personal computer systems (see figure 4 from [1]).

 

Figure 2. The process of an early batch system.

A programmer inserts cards to the card reader of machine model 1401.

Machine model 1401 reads batches of jobs onto a tape.

A computer operator physically carries the tape to machine model 7094.

Machine 7094 performs computation.

A computer operator carries an output tape to machine 1401.

Machine 1401 prints the output to a printer.

The process of an early batch system.

Figure 3. A multiprogramming system with three jobs in memory

Figure 4. From hardware view, a personal computer is made up of various components such as CPU, memory, to disk drive, etc.

See this  [link: https://www.youtube.com/watch?v=9GDX-IyZ_C8] video for information regarding operating system basics.

Operating system concepts

Figure 5 from [2] shows that an operating system closely interacts with the hardware. Thus, it is necessary to understand the computer hardware. An operating system possesses some basic components such as processes, memory management, I/O management, the file system, and security. In the subsequent chapters, we will discuss each of these components.

Figure 5. The interatcion between an operating system and various components of a computer system

System Calls

Internally, each of the basic components is handled by a set of systems calls. As an example, for UNIX operating system, we will examine have four sets of system calls, each relates to a separate component within the operating system.

Process creation and termination.

Reading and writing files.

Directory management.

Miscellaneous calls.

Figure 6 from [1] shows the major system calls that are standardized for Unix operating systems, also known as POSIX (Portable Operating System Interface) [3]. In particular, the system calls are grouped into different categories.

This group relates to process creation and termination.

This group is for reading and writing files.

This group is for directory management.

This group contains miscellaneous calls.

Figure 6. Various POSIX system calls, categoried as process management, file management, directory and file system management, and miscellaneous

This  [link: https://study.com/academy/lesson/system-calls-function-importance-categories.html] video for information regarding system calls.

Operating System Structure

Over the years, the designers of the operating systems have come up with several structures. Some of the most common ones are a monolithic system (figure 7 from [1]), a hierarchical layer system (figure 8 from [1]), a virtual machine system (figure 9 from [1]), an exokernel, and a client-server system (figures 10 and 11 from [1]).

Figure 7. The structure of a monolithic system

Figure 8. The structure of a hierarchical system

Figure 9. The structure of virtual machine, VM/370. The VM/370 interacts with CMS, Conversational Monitor System, to create different virtual 370s.

Figure 10. The structure of a client-server model in a distributed system

Please read the information provided in the supplemental resources to get more general understanding of operating systems.

Dominant Operating Systems

In 2015 Microsoft released its latest version of the popular Windows operating system, Windows 10. If the past is any indication then we can expect Windows 10 to have a lifetime of 3-5 years based on previous versions of Windows. According to Microsoft, Windows 10 has over 50 million lines of code, which pushes the minimum amount of memory recommended by Microsoft to 1GB for Windows 10. While some companies will put off upgrading to Windows 10, its growth in the smart phone market will likely push companies to upgrade their desktops and laptops to Windows 10 earlier than planned.

At one time Windows exceeded 70 million lines of code in Windows 8, and Microsoft did a major revision during Windows 10 development to get the total lines down to 50 million.

While not nearly as dominant in the market place as Windows, the "free" operating system Linux has gained a respectable following. Built initially in 1991 by Linus Torvalds, the use of Linux has grown and it is a popular operating system for servers. Built on the Unix model, Linux is a multiprocessing operating system that has show to be highly reliable, i.e. minimum downtime and reboots, in the demanding 24/7 environment that servers operate. One feature of Linux that draws users is that they may use, copy, modify, and redistribute the source code for Linux at no charge. This creates tight-knit groups of users who promote the virtues of Linux.

Supplemental resources

Chapter 1 power point presentation

Reference

Modern Operating System. Andrew S. Tanenbaum. Prentice Hall. 4th edition.

 [link: http://www.robelle.com/library/smugbook/posix.html] www.robelle.com/library/smugbook/posix.html
