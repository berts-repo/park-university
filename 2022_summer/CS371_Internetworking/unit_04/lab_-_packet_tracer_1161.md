# Unit 4: Lab - Packet Tracer 11.6.1

**Due:** 2022-07-04T04:59:00Z
**Points Possible:** 100.0
**Submission Types:** online_upload

## Instructions

Directions

Click the two tabs below. The first tab contains your Lab-Packet Tracer guidelines. The second tab contains the details for the Packet Tracer assignment. 

 [link: https://canvas.park.edu/courses/68420/pages/faq-packet-tracer-netlab] FAQ: Packet Tracer, Netlab

 [link: #fragment-1] Packet Tracer Project Guidelines

 [link: #fragment-2] Packet Tracer 11.6.1 Directions

Packet Tracer 11.6.1– Switch Security Configuration 

Figure 1. The location of the PT 11.6.1

Submission

The network file (.pka) and the screenshot file (.gif)

Due Date

by 11:59 p.m., Sunday, CT.

---

## My Submission

**Score:** 100.0/100.0
**Grade:** 100
**Submitted:** 2022-07-02T09:49:19Z

### Submitted Files

- **11.6.1-packet-tracer---switch-security-configuration_Bert.pka**
  - Downloaded: `files/11.6.1-packet-tracer---switch-security-configuration_Bert.pka`
- **Screenshot 2022-07-02 044803.png**
  - Downloaded: `files/Screenshot 2022-07-02 044803.png`

### Instructor Feedback

**[INSTRUCTOR]** (2022-07-11T12:56:18Z):

> Bert,
A good security practice is to separate management and user data traffic. The management VLAN, which is VLAN 1 by default, should be changed to a separate, distinct VLAN. To communicate remotely with a Cisco switch for management purposes, the switch must have an IP address configured on the management VLAN. Users in other VLANs would not be able to establish remote access sessions to the switch unless they were routed into the management VLAN, providing an additional layer of security. Also, the switch should be configured to accept only encrypted SSH sessions for remote management.
