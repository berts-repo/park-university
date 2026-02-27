# Unit 7: Discussion - Read and discuss a Cybersecurity Alert

Directions

Initial Post

Identify one alert on the  [link: https://us-cert.gov/ncas/alerts] Cybersecurity & Infrastructure Security Agency website. It is better related with a system that you are using.

Find out what that alert is, what the technical details about it, what impact it has made, and what the countermeasures are.

Cite the addresses when you are using materials from other sources.

Peer Response

Reply to at least two classmates. Please keep your posts civil and show respect to your classmates

Due Date

First post is due 11:59 p.m., Wednesday, CT

Respond to two classmates by 11:59 p.m., Sunday CT

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2022-09-28T22:53:22Z

Class,

I chose the alert AA22-054A, Cyclopes Blink, which is the predecessor to the 2018 VPNFilter attack. The attack is executed by the actor responsible for the 2018 Olympics attacks, Notpeya, and the Black Energy attacks against Ukraine in 2015, among many more, and his handle is Voodoo or Sandworm. (Alert (AA22-054A) 2022)

The attack appears to not discriminate and is widely spread, creating a botnet by targeting routers and other network devices, which is often deployed to small and home businesses. The attack is executed through the fork() system call, and is a child process that is divided into four modules:  file upload/download, system information discovery, malware version update, and the fourth module allows the actor to download more modules. (NCSC 2022) The modules can be accessed through the Linux API execlp, and are commonly deployed through WatchDog devices. (NCSC 2022) The attack persist through reboot and firmware updates, so if affected it should be assumed that the system is compromised. Some of the mitigation techniques include: don't expose management interfaces to the internet update, multi-factor authentication, and monitor. (Alert (AA22-054A) 2022)

 

 

Alert (AA22-054A). CISA. (2022, February 23). Retrieved September 28, 2022, from https://www.cisa.gov/uscert/ncas/alerts/aa22-054a

NCSC. (2022, February 23). Cyclops Blink - NCSC. Retrieved September 28, 2022, from  [link: https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf] https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf

---
