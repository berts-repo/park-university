# Unit 3: Discussion  2

Memory Management Simulation

In this discussion you will run an online simulation for page management.

 [link: https://solver.assistedcoding.eu/page_replacement] Go to this site to use the page management simulator. (disregard the Danger Alert statement on the web page.  It just indicates a new version of the simulator is available)

Use the default setup depicted below and click on the Build schedule button to run the simulation. 

 

 

Next, take a screen shot of the schedule the simulation builds and save it.

Now run the simulation again with the same setup, except change the algorithm to Least Recently Used (LRU).  Save this schedule as well.

Directions

Write an analysis of what you think is occurring in the simulation with regards to which pages are being swapped out, and why the hit and fault rates for the two algorithms are different. 

The analysis needs to be at least 200 words. 

Place the screenshots of the schedule in a Word file and attach the file to your post. 

Also respond to at least one other student’s analysis with constructive comments.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-09-02T04:07:28Z

The page-frames f1, f2, f3 , and f4, are the frames designated for that particular process. The ref row determines the step order for the next process that is to be executed. The process checks to see if the first ref (1) is in main-memory, it is not, so there is a page-fault and 1 is added to the first column of f1, When there is a page-fault the system forks the page-frame, which loads the first ref into the current page (t1), and there is now currently two page frames. (Tanenbaum 198)

This process continues until we get to t5 were there is a hit on page-frame f3 and we get another hit on t6 in frame f4. When there is a hit the page-frames that do not contain the next page they reference the last instruction for that frame. (e.g. t5 and t6 for page-frames f1 and f2

On page-frame t7 we have a page-fault and no page-frames left to fork to, so the system drops a packet according to the appropriate algorithm, FIFO in this circumstance, which stores the first ref into secondary memory, which v represents in the simulation.

The LRU scheduling algorithm takes the page that has gone the longest without being used (e.g 3 on t7 and 4 on t8).

 [link: https://canvas.park.edu/users/91372/files/9474872?wrap=1&verifier=KkoNNIwWrds9KjXU5e8oY6npVIN63gfAJFgsFf4g] disc3.docx

---
