# Unit 4: Discussion



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-09-09T16:43:00Z

Hello class,

I want to check my understanding of the ARP protocol. To my understanding the ARP works like a switch, the source will send out a broadcast to all the devices on the LAN looking for the IP match. When the match is found the destination device will send a response back, and the source will store then IP and MAC address in it's cache. 

What I don't understand is why a switch would be more efficient? As I look at Wireshark and the ARP request, I see that the request has both the source IP and MAC address. So, when the broadcast reaches the matched destination, it already has the source IP and MAC address for unicast response. Everything is stored in cache, just like the MAC address table on a switch. Why would it be more efficient to use a a MAC table when a broadcast does the same things as forwarding through all ports?

---
