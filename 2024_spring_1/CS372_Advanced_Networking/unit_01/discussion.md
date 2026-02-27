# Unit 1: Discussion



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2024-01-13T03:39:49Z

Class,

I ran into some confusion when determining when it would be better for setting the OSPF bandwidth cost value and changing the OSPF priority serve different purposes in OSPF configuration. I ended up finding a good YouTube series that I will link below.

The OSPF cost is a metric that OSPF used to determine the best path for data to travel. You might want to manually set the OSPF cost on an interface to influence the path selection process, e.g. if you have multiple paths to a destination and you prefer one path over the other, you can adjust the OSPF cost to make one path more desirable. An advantage of configuring a cost over setting the interface bandwidth is that the router does not have to calculate the metric when the cost is manually configured.

On the other hand, OSPF priority is used in the election of the DR and BDR on multi-access networks. Changing the OSPF priority on an interface can influence which router becomes the DR or BDR. The router with the highest priority on a network segment becomes the DR1.

So, while both settings are important in OSPF configuration, they serve different purposes and are adjusted in response to different needs.

 

https://youtube.com/playlist?list=PLIFyRwBY_4bSkwy0-im5ERL-_CeBxEdx3&si=np8gzCeNsE27OgyF

---
