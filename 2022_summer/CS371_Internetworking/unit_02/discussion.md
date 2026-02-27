# Unit 2: Discussion 



**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-06-18T04:50:22Z

Class,

I wanted to further expand on my understanding of which ports are being blocked in the Spanning Tree protocol.

The first step is to determine the root switch: this is determined by the lowest switch priority, and if they are tied it is further determined by the lowest MAC address.

The next step is to determine the root ports, which are the ports that lead to the fastest route back to the root switch: these are ports that are determined by the lowest path cost, which is the total of the different paths back to the root switch. If two paths have the same cost then the lowest priority switch and the lowest port number determine the tie breaker.

The next step is to determine the designated ports, these are the best ports to the root switch when you're on a specific segment. This is determined again by the path cost. Side note, because all ports on the root switch technically connect the root switch, they can all be considered designated ports.

---


### Feedback

**[INSTRUCTOR]:** Bert,
Congratulations on your well thought out post in the threaded discussions for Week 2. I divide the 10 points for forum discussion into 6 points for the initial response and 4 points for the feedback to another student's post. Great job! Let me know if you have any question about the minimum nj requirements on the posts. Feel free to contact me through email or by phone.
