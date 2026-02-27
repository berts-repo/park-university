# Unit 7: Discussion 1

Computer Security Threats

Conduct online research and find an article on computer security threats. Summarize your article and provide the link for others to view it. 

Post your reply to this thread. Also, respond to a minimum of two posts from your classmates.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-09-28T23:26:40Z

Class,

I chose the article  [link: https://www.cisa.gov/uscert/ncas/alerts/aa22-054a] New Sandworm Malware Cyclops Blink Replaces VPNFilter. The attack is executed by the actor responsible for the 2018 Olympics attacks, Notpeya, and the Black Energy attacks against Ukraine in 2015, among many more, and his handle is Voodoo or Sandworm. The attack is similarly deployed like the 2018 VPNFilter attack, and is considered the predecessor.

The attack creates a botnet by targeting routers and other network devices, and does not seem to discriminate, but is often deployed to small and home businesses. The attack is executed through the fork() system call, and is a child process that is divided into four modules:  file upload/download, system information discovery, malware version update, and the fourth module allows the actor to download more modules. (NCSC 2022) The modules can be accessed through the Linux API execlp, and are commonly deployed through WatchDog devices. (NCSC 2022) The attack persist through reboot and firmware updates, so if the system is affected it should be assumed that it is also compromised. Some of the mitigation techniques include: don't expose management interfaces to the internet update, multi-factor authentication, and monitor. (Alert (AA22-054A) 2022)

 

Alert (AA22-054A). CISA. (2022, February 23). Retrieved September 28, 2022, from https://www.cisa.gov/uscert/ncas/alerts/aa22-054a

NCSC. (2022, February 23). Cyclops Blink - NCSC. Retrieved September 28, 2022, from  [link: https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf] https://www.ncsc.gov.uk/files/Cyclops-Blink-Malware-Analysis-Report.pdf

---
