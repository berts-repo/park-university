# Unit 2: Discussion 



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-03-24T09:57:54Z

Hey Class,

This week I wanted to explore Overlay Tunnels for IPv6, which I found when exploring prefixes for IPv6. Overlay tunneling is a Compatibility Address, which encapsulates IPv6 packets in IPv4 packets for delivery across an IPv4 infrastructure, especially where IPv4 routers are still being used. There are many different types of tunneling mechanisms used for this: manual, Generic Routing Encapsulation (GRE), IPv4-compatable, 6to4, and Intrasite Automatic Tunnel Addressing Protocol (ISATAP). This is often accomplished by embedding the IPv4 address into a IPv6 address, which is represented by w.x.y.z in a IPv6 address: 0:0:0:0:0:0:w.x.y.z. and converting the IPv4 address into hexadecimal, for example:

w
x
y
z

192
168
10
100

C0
0
A
64

 

source:

 [link: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/interface/configuration/15-s/ir-15-s-book/ip6-auto-comp-tun.html#GUID-798E8F9C-5EB0-485A-93BF-CB4ECF6A4310] https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/interface/configuration/15-s/ir-15-s-book/ip6-auto-comp-tun.html#GUID-798E8F9C-5EB0-485A-93BF-CB4ECF6A4310

---
