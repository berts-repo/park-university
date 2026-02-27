# Unit 6: Discussion

Introduction

For Unit 6 discussion, we will be looking at Smart Forensics related to the Internet of Things. 

Unit Learning Outcomes 

Explain the challenges of forensic acquisitions of data stored on Internet of Anything devices (CLO 2)

Directions

Initial Post

Read the article  [link: https://securityintelligence.com/smart-forensics-for-the-internet-of-things-iot/] “Smart Forensics for the Internet of Things (IoT)”. Identify one IoT device. It can be smart camera, smart watch, Amazon Echo, etc. Search information on the Internet and create a forensic plan for investigating this type of IoT device. You plan should include:

How to perform acquisition on IoT device.

What information can be collected on the IoT device.

What tools can be used to perform forensics on this device. 

Cite the source of the information you found on the Internet.

Peer Response

Reply two of your peers, commenting on their plan. Identify alternative or missing acquisition plan, collected information, or tools

Please keep your posts civil and show respect to your classmates

Due Dates

First post due 11:59 p.m., Wednesday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2024-02-14T03:02:19Z

Class,

I am going with an ip-based camera, like the ones you can view from your phone. I based my discussion post on OSACs standard practice for CCTV system. There are some things that I want to mention that I took note of while researching this. Most of these IoT cameras are proprietary and require a video/audio codec to uncompress the data and archived formats. It is also important to remove the SD-card promptly, if applicable, due to the potential that video is time sensitive and can be overwritten. Also, cameras could be nested into a smart home system, and could change the acquisition procedure. So, it is important to know what you’re working with prior to the acquisition.

The first step of the acquisition is analyzing and documenting (e.g. model, version, firmware) but not all the metadata and artifacts are documented until steps are taken to prevent data loss.

The second step is preventing loss. This can include things like disconnecting external sources of access to the device, removing the SD-card, and leaving the system recording during acquisition, but this last one can vary and depends on knowing what you work with.

The third step is acquisition. This all depends on the scenario, like was the event taking place over 10 minutes, or is it a 24-hour surveillance. There are many more “if” scenarios.

A good commercial tool I found for forensic videos is Magnet DVR Examiner, but Autopsy does work with various video formats too. Binwalk is another good tool for validity and analyzing data as it can uncover usernames, passwords, IP-addresses, as well as hardcoded emails that are commonly associated with malware deployed in the firmware of IoT devices (Bhardwaj, Kaushik, Bharany, & Kim, 2023).

 

 

Sources:

Bhardwaj, A., Kaushik, K., Bharany, S., & Kim, S. (2023). Forensic analysis and security assessment of IoT camera firmware for smart homes. Egyptian Informatics Journal, 24(4), 100409.  [link: https://doi.org/10.1016/j.eij.2023.100409] https://doi.org/10.1016/j.eij.2023.100409

Organization of Scientific Area Committees (OSAC) for Forensic Science. (2020). Standard practice for data retrieval from digital CCTV systems (Version 2.0). Retrieved from https://www.nist.gov/system/files/documents/2020/06/26/DMSAC-VL_Standard%20for%20DVR%20Retrieval_V02_OSAC%20Proposed_June2020.pdf

---


### Feedback

**[INSTRUCTOR]:** Bert,
Excellent job in the forums this week and thanks for getting all your posts in. It really helps to keep the discussion going. This week we discussed different IoT devices, how we might perform a forensic acquisition on it and what artifacts could be collected from it. IoT devices are exploding in numbers with an estimated 30 billion by 2025. As examiners, you may experience an IoT device that you have never encountered before. You’ll have to do your research and try to figure out what data you can get off it (if any). Not all IoT devices host data, rather a lot of them store information in the Cloud. Understanding how to get that information is also important. Keep up the good work and don’t hesitate reaching out if you have any questions on any of the material covered this week. Prof [INSTRUCTOR]
