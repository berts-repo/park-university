# Unit 2: Discussion 



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-01-18T23:00:58Z

Class,

I did a Google search to see if there were any vulnerabilities with ACLs to present for my discussion post this week. I discovered a semi-recent vulnerability with ACLs filtering. The vulnerability allows unauthenticated, remote attacker to bypass a configured ACL (CVE-2023-20191, September 2023). The vulnerability has a CVSS score of 7.5 and it allows the threat actor to bypass the ACL security by sending traffic through an affected device.

The vulnerability affects Cisco routers and bypasses the ACL processing on MPLS interfaces in the inbound direction to the router. MPLS is a routing protocol that speeds up network traffic by labeling packets instead of using network addresses. This works by not having to read the packet, but just forwarding traffic according to the label instead (Multiprotocol Label Switching, 2024).

Cisco states the vulnerability has been “fixed” with some security updates, to address the situation, but some networks will still be vulnerable.

 

 

https://nvd.nist.gov/vuln/detail/CVE-2023-20191

https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-dnx-acl-PyzDkeYF

---


### Feedback

**[INSTRUCTOR]:** Great work replying to more than one post.  It improves the discussion.
