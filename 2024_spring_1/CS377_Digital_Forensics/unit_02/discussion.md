# Unit 2: Discussion

Introduction

In Unit 2 we will discuss data acquisition tools. 

Unit Learning Outcomes 

Explain ways to determine the best acquisition method (CLO 4)

Explain how to use acquisition tools and how to validate data acquisitions (CLO 3 and CLO 4)

Directions

Initial Post

Research one data acquisition tool other than dd, dcfldd, or FTK Imager. It could also be the data acquisition function in a digital forensic tool. You can research that tool by watching videos or reading web pages on the Internet, You can also install it by yourself to test it out. List the tool name, latest version number, vendor name and its features. For the features, discuss the following aspect:

What image file formats does this tool support? Raw, proprietary, or AFF?

Does this tool compress acquisition image? What are the main features of its compression algorithm?

Does this tool support remote network acquisition?

What method does this tool use to validate the image? (MD5, SHA-1, or something else)

What are the major steps to image a disk with this tool? It is preferred to try this tool and provide some screenshots.

What other special acquisition features does this tool provide?

Peer Response

Reply the initial posts from two of your peers, make comparison between the tool you are studying and the tool your peer is studying. Discuss whether your tool has a feature that is similar to the special feature introduced by your peer. 

Please keep your posts civil and show respect to your classmates

Due Dates

First post due 11:59 p.m., Wednesday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2024-01-17T22:56:59Z

Class,

The tool I am going with is ddrescue which is an open-sourced data recovery tool. I found a blog when reading about the CLI tool dc3dd, that talked about how dc3dd and ddrescue pair well together, when used in conjunction. Dc3dd is notably known for its automatic hash verification (md5, sha-1, sha-256, and sha-512), compared to the other dd forks. I also discovered that ddrescue works well with other tools like affuse, to convert .raw files to .aff files, and lzip for compression of backups.

Ddrescue is considered a data recover tool, developed as part of the GNU project. It is the ideal tool to use when you are suspecting ‘bad’ blocks. Ddrescue does not write zeros or truncate the output file. So, you can run it multiple times on a ‘bad’ file, and it will try and continue to fill in the gaps and ‘fix’ the bad block. This works with merging copies of two backups: if you have two more damaged copies of a file, and output them to the same file, they will attempt to fill in the gaps.

Ddrescue is very simple to run. It was designed for Linux CLI but will work with MacOS and Windows. The format for running ddrescue is:

ddrescue [options] infile outfile [mapfile]

infile and outfile may be files, devices, or partitions. mapfile is a regular file and must be placed in an existing directory. If mapfile does not exist, ddrescue will create it.

 

Target USB:

 

Acquisition:

P.S. Benefit of these tools is they can be used with Python scripts

 

Sources:

 [link: https://tmairi.github.io/posts/forensic-aquisition-with-dd-tools/] https://tmairi.github.io/posts/forensic-aquisition-with-dd-tools/

https://www.gnu.org/software/ddrescue/

---


### Feedback

**[INSTRUCTOR]:** Bert,

Excellent job in the forum this week.  Thanks for getting all your posts in.  It really helps to keep the discussion going.  This week, you had the opportunity to choose a forensic tool and discuss the image file formats that the tool supports, whether the tool was capable of remote network acquisitions and other special acquisition features the tool had.   At this point, you should be seeing a common theme – there are a lot of forensic tools and they all have similar features.  But this isn’t’ to say all tools are the same even if they can do the same thing.  You will find that some tools work better than others for certain tasks.  You will want to be familiar with a wide array of forensic tools.  Keep up the good work and don’t hesitate reaching out if you have any questions on any of the material covered this week.

Prof [INSTRUCTOR]
