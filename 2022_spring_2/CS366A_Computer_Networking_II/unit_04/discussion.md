# Unit 4: Discussion



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-04-07T08:22:15Z

Hey,

I wanted to explore some different protocols in the transport layer. QUIC is a relatively new standard, which officially released it's standards by the IETF in 2021, and many people call it the protocol that will replace TCP. Many client side applications including Chrome, Edge, and Firefox already have it integrated, and servers like Facebook and Google have already switched over to it. The reason for this is: TCP is an old protocol, from 1981 that remains fairly unchanged. With faster internet and as higher level protocols are being developed, the header byte size is becoming insufficient.

What's interesting about QUIC is that is established over a UDP connection. It still establishes a connection and is secure, but it removes the handshake. Without understanding the concept well, QUIC helps with "Head of line blocking," which has to do with dropped packets and sequence numbers.

---
