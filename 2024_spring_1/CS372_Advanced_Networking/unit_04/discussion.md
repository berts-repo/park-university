# Unit 4: Discussion



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-02-01T00:58:50Z

Class,

For this week’s discussion I want to discuss when it is appropriate to use a VPN for security and when it’s not. A VPN is essentially just an encrypted tunnel, which is being sold by companies (e.g., ExpressVPN) as an enhanced proxy server. When the traffic leaves the VPN server it no longer is encrypted, and it behaves like a proxy by using the last hop IP of the server. This doesn’t benefit anyone running it on their home computer unless they wanted to hide their traffic from their ISP or avoid geo-location. But none of that would matter if the VPN provider were recording the traffic and selling the traffic, which they might be keeping log records too.

This remote-access VPN is good in situations where the device is on a public network, where the threat actor would be monitoring the local network traffic (MITM attack). It would also be good in a situation where a company hosts their own VPN server and all the global traffic is not decrypted until it reaches the companies' local network, where the VPN server is hosted.

I also think site-to-site VPN holds value in a security sense. By an office building encrypting and tunneling their traffic to two VPN gateways, the company could establish a secure tunnel between two branches of their own company, that are not in the same LAN.

There are many more benefits to a VPN, but for most home users I don't see it as good a security solution as marketing makes it out to be.

 

https://gist.github.com/joepie91/5a9909939e6ce7d09e29

https://www.computer.org/publications/tech-news/trends/when-to-use-a-vpn

---
