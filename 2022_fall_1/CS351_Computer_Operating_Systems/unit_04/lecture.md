# Unit 4: Lecture

Chapter 4: File Systems

A file system consists of file structure, directory structure, and storage management.

A file is a sequence of logic records. A logic record can be a byte, a line, or a complex data structure [2]. An operating system defines and implements the logic records, maps the logic records into physical records, allocates storage space for the physical records, and stores them in a physical storage such as a disk.

For the purpose of keeping track of files, operating systems usually have directories. It can be structured as a single-level directory system (Figure 1 from[1]), two-level directory system (Figure 2from [1]), or hierarchical directory system (Figure 3 from [1]).

 

Figure 1. A single-level directory system with 4 files which are owned by 3 different people, namely, A, B, and C

Figure 2. A two-level directory system in which each user has his own private directory

Figure 3. A hierarchical directory system in which each user can have any number of directories

Different systems provide different kinds of file systems. In this chapter, we will study the file systems in ISO 9660, CP/M, MS-DOS, Windows 98, and Unix.

This  [link: https://www.youtube.com/watch?v=HIXzJ3Rz9po] video provides supplemental information on the Linux file system.

This  [link: https://www.youtube.com/watch?v=TLKZEU1DZ9c] video provides supplemental information on the Windows file system.

Systems">Windows File Systems

Data Transfer Example

Problem: You have a harddrive with 6GB of data stored on it, and the files are fragmented.  The average size of a file is 16KB.  To defragment the files, the OS copies a file to a clean area of the drive reserved for compacting the drive, then writes the file back to contiguous sectors in the main storage area so there are no fragments in the file.   Average seek time and rotational delay for the drive are 6 and 5 milliseconds respectively, with a transfer rate of 4MB/sec.

How long does it take to write one file to the compression area and back to the main storage area of the disk? 

Solution: The time to transfer one file to the compacting area is:

seek time + rotational delay + transfer time

Since we are given seek time and rotational delay, we need to calculate transfer time for a file.  We are given a transfer rate of 4MB/sec, which in base 2 is 222 = 4,194,304 bytes/sec.  The average size of a file is 16KB, which in base 2 is 214 = 16,384 bytes.  If we divide 16,384 bytes by 4,194.304 bytes/sec, we get the time to transfer one 16KB file.  This calculation is 3.9 x 10-3 seconds, or 3.9 milliseconds.

Therefore the total time to write one 16KB file to the compression area is:

6 milliseconds + 5 milliseconds + 3.9 milliseconds = 14.9 milliseconds

To write the file back to the main storage area of the disk takes the same amount of time so the answer is 2 times 14.9 milliseconds, or 29.8 milliseconds.

Supplemental Resource

Chapter 4 Powerpoint Presentation

Chapter 4 File Systems

References

Modern Operating System. Andrew S. Tanenbaum. Prentice Hall. 4th edition
