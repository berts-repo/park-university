# Unit 3: Discussion

Introduction

This unit's discussion we will discuss processing a crime scene.

Unit Learning Outcomes 

Describe available digital forensics software tools (CLO 3)

List some considerations for digital forensics hardware tools (CLO 3)

Describe methods for validating and testing forensics tools (CLO 3)

Directions

Initial Post

Study one digital forensic tool by searching on the Internet. You can watch some videos and web pages, or install it by yourself to test it out. Based on your discovery, discuss its features of the following aspects. Please clearly cite the source if you are using Internet resources.

Acquisition

Validation and verification

Extraction

Reconstruction

Reporting

Peer Response

Reply the initial posts from two of your peers, make comparison on the above aspects between the tool you are studying and the tool your peer is studying. 

Please keep your posts civil and show respect to your classmates

Due Dates

First post due 11:59 p.m., Wednesday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2024-01-24T22:48:22Z

Class,

I chose to explore Parrot OS, which is a Linux operating system that is designed for penetration testing, ethical hacking, and digital forensics. Parrot is like other distributions, including Kali, but doesn’t require as much overhead to run. It includes tools that can be used in digital forensics.

I played around some of the tools for functions such as acquisition, validation and verification, extraction, reconstruction, and reporting. I am theorizing that it would be easier to practice validity by being able to run commands to determine the accuracy of a tool (e.g., creating an image with different tools). Ultimately, I would want to use a suite for my primary tool when investigating, to make generating a report easier.

 

Acquisition

Here I am taking the target drive, creating a md5 hash .txt file, setting the block size to 512, not recording errors, and splitting the drive into 650mb raw images, and finally storing the images in home directory. 

 

Extraction

Here I am using Autopsy, in Parrot OS, to do a word search for “David,” I know the file contains a mp3 of David Bowie

 

 

Reconstruction

 Reconstructing the split images with concatenate and a redirected to one file:

 

Validation and verification

 I compared the md5 hash of reconstructed usb image to the original md5 hash, by redirecting and appending to the images original md5 .txt file.

Autopsy in Parrot has the same hash value:

 

Reporting

I only found some general tools for report generating. I am speculating that I would use a primary digital forensics suite to generate reports, or manually do it.

---


### Feedback

**[INSTRUCTOR]:** Bert,
Excellent job in the forums this week and thanks for getting all your posts in ;-) Your posts added value to the discussion. As you should be continuing to see, there is an overabundance of forensic tools out there. It is highly recommended that you be familiar with a wide range of these tools. As I’ve mentioned previously, some tools work better than others for specific tasks. I think you will also find that open-source tools are extremely powerful so don’t think that the price of a tool determines how good it works. Keep up the good work and don’t hesitate reaching out if you have any questions on any of the material covered this week. Prof [INSTRUCTOR]
