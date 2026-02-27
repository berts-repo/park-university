# New Unit 5: Discussion - Read and discuss cybersecurity conference papers

Directions

Initial Post

Pick one research paper that you are interested in the  [link: https://www.usenix.org/conference/usenixsecurity21/technical-sessions] Program page of USENIX Security Symposium.

Read the paper you have selected and watch its presentation. 

Answer the following questions:
What security issue the paper has found or what security problem the paper is trying to address?

What method the research is using?

What is the conclusion of this paper?

Peer Response

Reply to at least two classmates. Add two additional details that the original post was not covered. Please keep your posts civil and show respect to your classmates

Due Date

First post is due 11:59 p.m., Wednesday, CT

Respond to two classmates by 11:59 p.m., Sunday CT

**My Score:** 14.0/?

---

## My Discussion Posts

**Posted:** 2022-09-17T07:45:17Z

[link: https://www.usenix.org/conference/usenixsecurity21/presentation/dai] The Hijackers Guide To The Galaxy: Off-Path Taking Over Internet Resources

 

Class,

this paper focuses on the insecure practices and procedures involving Internet Resource Providers (IRPs), their resources, and how there is vulnerabilities in their policies, as well as how these resources are managed: these resources include, ip addresses managed with RiR's [RFC7020], domain names and their registrars,  virtual machines with infrastructure as a service (IaaS), and Certificate Authority (CA's). The text goes on to describe how threat actors are able to "silently" infiltrate these resources, often staying undetected for extended periods of time. Gaining access to these accounts and therefore resources gives the threat actor many different attack vectors, for e.g., domain name registrars can be used to launch phishing attacks, or by hijacking IaaS the attacker can gain access to virtual machines, records and processing power. 

The way they tested their method is by preforming three "off-path" cache poisoning attacks, from the perspective of the threat actor; "Unlike a MitM attacker, an off-path attacker cannot observe or modify legitimate packets sent between other parties, however, he can transmit packets with a spoofed (fake) source IP address - impersonating some legitimate party" (Gilad) The three off-path cache poisoning vectors they preformed included,  BGP prefix hijacks, side-channels and IPv4 defragmentation. They tested these attacks on controlled accounts under the popular IRPs, by creating victim accounts and preforming the poisoning on those accounts. They preformed the attacks live while the IRPs were still being used, so they used fake accounts for ethical purposes, but it is not hard for an threat actor to get access to an account identifier because most IRPs only require a email, and this can be found with a simple whois search.

Although I just described the first step, in the vectors of resource hijacking, the paper goes on to describe how easy it is to manipulate CA's and pivot to other resources once they preform the initial cache poisoning. This paper really demonstrates how vulnerable these IRPs and resources are. The article also leaves you with some practical solutions that people often don't want to implement, including stricter authentication policies. The paper does a good job of leaving you wondering if we want safety and privacy or ease-of-use procedures.

 

Gilad, Y., Herzberg, A., & Shulman, H. (n.d.). Off-Path Hacking: The Illusion of Challenge-Reponses Authentication. Retrieved September 17, 2022, from https://eprint.iacr.org/2018/623.pdf

---
