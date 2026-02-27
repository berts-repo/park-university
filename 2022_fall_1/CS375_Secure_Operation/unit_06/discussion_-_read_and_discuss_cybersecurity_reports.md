# Unit 6: Discussion - Read and discuss Cybersecurity Reports 

Directions

Initial Post

Identify one vulnerability on the  [link: https://nvd.nist.gov/] National Vulnerability Database website.

Find out its CVSS score and CVSS Vector (using CVSSVersion 3.x).

Perform detailed study on this vulnerability and explain what makes each vector metrics receive the corresponding value. For example, suppose a vulnerability has a CVSS vector “CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:H/A:N”, it means the Attack Vector (AV) is network (N), Attack Complexity (AC) is Low (L), Privileges Required (PR) is None (N), User Interaction (UI) is Required (R), etc.

You are expected to explain what the exact network attack vector is, why the attack complexity is low, the what kind of user interaction is needed to perform the attack, etc.

Peer Response

Reply to at least two classmates. Please keep your posts civil and show respect to your classmates

Due Date

First post is due 11:59 p.m., Wednesday, CT

Respond to two classmates by 11:59 p.m., Sunday CT

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2022-09-22T14:06:11Z

Class,

I am going with CVE-2022-37418, this is a Remote Keyless Entry (RKE) vulnerability that allows the threat actor to capture two consecutive fob keystrokes, a Rollback attack, gaining permanent access to the cars RKE. The current standard for an RKE is the signal from the keyfob changes with every click. By jamming the signal, so there is no beep, the threat actor can fool the owner in clicking the lock button twice, which allows the threat to exploit the Rollback exploit. This exploit takes advantage of the "resync" code sequence. (Williams 2022)

Base score: 6.4

Vector: AV:A/AC:H/PR:N/UI:R/S:U/C:N/I:H/A:H

Impact score: 5.2

Exploitability Score: 1.2

Attack Vector
Adjacent
The keyfob has to be in range of an RF scanner, like the HackRF, which operates in the range of 1MHz to 6GHz (Great Scott Gadgets 2022) (Csikor 2022)

Attack Complexity
High
This threat actor is required to know what model of car he is attacking, and he also has to have the proper hardware. (Csikor 2022)

Privileges Required
None
This is done with RF hardware and the attackers laptop. (Csikor 2022)

User Interaction
Required
Has to be in range, to record keyfob signals. (Csikor 2022)

Scope
Unchanged
This attack can be preformed on Nissan, Kia, and Hyundai vehicles through 2017.

Integrity
High
Once the required amount of keystrokes are recorded, the threat actor has a spare virtual keyfob, and it can be unlocked whenever. (CS.lev 2022)

Availability
High
Depending on the car the attacker has to collect 2-5 keystrokes without the car being "unlocked," otherwise the attacker has to restart. (CS.lev 2022)

 

So, it is good practice to only press the "lock" button once on your keyfob!

 

References: 

Cs.lev. (2022, September 21). Rollback- a new time-agnostic replay attack against the Automotive Remote Keyless Entry Systems. Medium. Retrieved September 22, 2022, from  [link: https://medium.com/codex/rollback-a-new-time-agnostic-replay-attack-against-the-automotive-remote-keyless-entry-systems-df5f99ba9490] https://medium.com/codex/rollback-a-new-time-agnostic-replay-attack-against-the-automotive-remote-keyless-entry-systems-df5f99ba9490

Csikor, L. (2022, August 11). YouTube. Retrieved September 22, 2022, from https://www.youtube.com/channel/UCHZ9ixqrunDhdTeVE0W5q_A

Great scott gadgets. (n.d.). Retrieved September 22, 2022, from https://greatscottgadgets.com/hackrf/one/

Williams, E. (2022, August 17). Rollback breaks into your car. Hackaday. Retrieved September 22, 2022, from https://hackaday.com/2022/08/17/rollback-breaks-into-your-car/

---
