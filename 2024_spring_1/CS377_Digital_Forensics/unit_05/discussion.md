# Unit 5: Discussion

Introduction

For this discussion, we will look at the processing of crime scenes. 

Unit Learning Outcomes 

Describe the process of a live acquisition (CLO 2)

Directions

Initial Pots

Describe the configuration and software on your computer, then design a live acquisition plan for your running computer. Notice that you DO NOT have to perform the actual live acquisition.

To describe the configuration and software, list the hardware configuration, OS and network configuration, as well as the running software and service.

Describe your live acquisition plan. List your plan as a series of steps. For each step, specify its purpose and the tools you are using.

Peer Response

Reply the initial post from two of your peers. For each step, specify what alternative tools can be used to achieve the step.  

Due Dates

First post due 11:59 p.m., Wednesday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2024-02-07T18:21:59Z

Class,

I am working on a Windows 11 Home, x64 based system.  My system, hardware, and software configurations were easy to view and save to a .nfo file. To accomplish this just search for the application “System Information” or go to Run and type ‘msinfo32’ from here you can just view and save what you need to.

Inside the NFO file I can see details for each of the prompts regarding my discussion post. I can see what hardware my system has, and the resources as well. The network configuration is listed here and can find information about my network adapters and configurations. I am using quite a few virtual adapters, as I have been playing around with hypervisors and virtualization. As for software configurations (e.g., environment variables, running tasks, and services) I just look at the Software Environment label in the System Information, NFO file, that I first described.

There seem to be many ways to look up the configurations, but I think most everything needed is found in the System Information. For example, another way I can view network configuration is by looking at ‘ipconfig’ in the CLI, or ‘netstat’ for active TCP connections. I can also find running services by going to Run and typing ‘services.msc’ which allows me to export the list, unlike Task Manager where I can’t seem to save anything.

One thing that System Information didn’t contain was logs. If I had to perform a live acquisition on my own system, I would assume it is because I was compromised and hacked, and my network logs would become pertinent evidence. To get Event Viewer logs I go to Run and type ‘eventvwr.msc’. To get the Windows Firewall logs I run ‘wf.msc’ and I can find more information about the network with the CLI tool ‘netsh’.

When it comes to the steps to acquire all this information, I would need to follow the order of volatility (OOV), but the first thing I would do is make sure that the reason for the acquisition is contained and can’t spread through the network. I would also document everything. I can use OSForensics and FTK Imager to accomplish the acquisition (software write blockers) if I was worried about writing to the system.

I am fallow the OOV from INFOSEC (Imam, 2017):

Cache, registers.

ARP cache, routing table, memory, kernel statistics, process table

Temporary files

Disk

Monitoring data and remote logging pertaining to the computer in question

Physical configurations, network topology

Archival media

 

Source:

Imam, F. (2017, November 23). Security+: Basic forensic procedures (SY0-401) [decommissioned article]. Infosec. https://resources.infosecinstitute.com/certifications/retired/security-plus-basic-forensic-procedures-sy0-401/

---


### Feedback

**[INSTRUCTOR]:** Bert,
Excellent job in the forums this week and thanks for getting all your posts in. This week you discussed your own system specs and a plan to conduct an acquisition of it. While there is more than one way to approach this, what’s important is that you remember the order of volatility. If the system is on, you will want to ensure that you collect the RAM first. Additionally, once the RAM is collected, you’ll want to make sure that any encryption is turned off. Otherwise you may not be able to get back into the system once the system is shut down. Keep up the good work and don’t hesitate reaching out if you have any questions on any of the material covered. Prof [INSTRUCTOR]
