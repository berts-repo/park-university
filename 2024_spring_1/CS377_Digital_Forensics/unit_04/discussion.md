# Unit 4: Discussion

Introduction

In Unit 4, our discussion focuses on identifying unknown file formats.

Unit Learning Outcomes 

Describe types of graphics file formats and data compression (CLO 4)

Explain how to locate and recover graphics files (CLO 4)

Describe how to identify unknown file formats (CLO 4)

Directions

Initial Post

 Identify one binary (non-text) file format, such as Office Word document, Office Excel, Picture, Database, etc. Then do research on the Internet, and complete the following tasks

List its extension name, e.g., doc, docx, xls, png, gif, sqlite, etc. 

Describe the function of this type of file, e.g., the .sqlite file is a database file created with SQLite, a lightweight relational database.

Describe its binary digital format, e.g., the JFIF JPEG format has 0x FFD8 FFE0 in the first four bytes.

Specify a second file type with its extension name and function so that other students can reply with its binary digital format.

Peer Response 

Reply to ONE initial post of your peer, research and describe the binary digital format of the second file type provided by your peer.

Due Dates

First post due 11:59 p.m., Wednesday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2024-01-30T22:12:52Z

Class,

The binary file format I wanted to explore was windows executables (.exe), which is an executable file, an extension to a program, that runs in a windows system.

The .exe is structured as a Portable Executable (PE), that starts with a MS-DOS stub, which is a different type of header, that is placed in front of an .exe.

 

and at the end of that MS-DOS stub, offset 0x3c, there is a pointer to the PE signature.

 

The pointer (0x3c) says the PE signature is at offset 0x100, which is denoted by “PE” and “50 45 00 00.”

 

Immediately following the PE signature is the Object header (COFF File Header), which has 7 attributes and offsets. One of the attributes lets you add another optional header, which can pivot into more fields and attributes.

Regarding prompt 3: I am also interested in the binary digital format of Excel if someone wants to provide the format of .xlsx for me.

 

Source:

https://learn.microsoft.com/en-us/windows/win32/debug/pe-format

---


### Feedback

**[INSTRUCTOR]:** Bert,
Excellent job in the forums this week and thanks for getting all your posts in.  This week you were tasked with identifying one binary (non-text- file format and doing some research to answer some specific questions related to it.   You selected a great binary file and one that is extremely common throughout the cyber arena.  As a forensic examiner, it’s important to be familiar with a wide array of file types.  It’s also important to understand what data is available and what tools you need to extract those digital artifacts.  Keep up the good work and don’t hesitate reaching out on any of the material covered.

Prof [INSTRUCTOR]
