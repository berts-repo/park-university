# Unit 1: Discussion



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-06-11T03:48:57Z

Class,

I chose to further explore switching modes. There is three types different switching modes, store-and-forward, cut-through, and fragment-free. Store-and-forward frames.

Fragment-free is a form of cut through switching, but this method isn't used very often. It reads at least 64 bytes of the packet before it forwards the packet.

Cut-though (fast-forward) egress' the packet as soon as it gets the its MAC address which is in the first 6 bytes. This method does not have to wait for the whole ethernet frame. This has the fastest latency, but requires one of the devices further down the path to recognize an invalid frame.  

Store-and-forward will hold the frame until the entire frame is received, then it will store the frame in the buffer and verify the frame with a frame-check-sequence (FCS) and cycle-redundancy-check (CRC).

 

Switching modes: Store-and-forward vs cut-through. NetworkAcademy.io. (n.d.). Retrieved June 10, 2022, from https://www.networkacademy.io/ccna/ethernet/store-and-forward-vs-cut-through-switching

---


### Feedback

**[INSTRUCTOR]:** Bert,
Welcome to the course – I’m happy to have you in the group!

Congratulations on your well thought out post in the threaded discussions for Week 1.  
I divide the 10 points for forum discussion into 6 points for the initial response and 4 points for the feedback to another student's post. Great job!

Let me know if you have any question about the minimum nj requirements on the posts. 

Feel free to contact me through email or by phone.
