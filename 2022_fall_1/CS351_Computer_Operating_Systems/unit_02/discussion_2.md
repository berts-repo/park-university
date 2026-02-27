# Unit 2: Discussion 2

Scheduling Simulation

In this discussion you will run an online simulation for CPU scheduling. 

 [link: https://www.youtube.com/watch?v=pVzb3TUcDLo] First, watch this video to understand CPU and I/O bursts.

 [link: https://ess.cs.uni-osnabrueck.de/software/AnimOS/CPU-Scheduling/index.html] Next, go to this site to use the CPU simulator.

You will want to review the Help information for the simulator by clicking on the Help tabs. 

Once you think you understand how the simulator works, using the default processes setup as below and a First-Come-First-Served scheduling strategy.

 

Press the play button and let the simulation run.

 

You can run other scheduling algorithms to see how they change the statistics.

Directions

Write an analysis of what you think is occurring in the simulation and why each of the three processes got the percent of CPU time in the statistics output report. 

The analysis needs to be at least 200 words. 

Place the screenshots of the statistics in a Word file and attach the file to your post. 

Also respond to at least one other student’s analysis with constructive comments.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-08-25T23:10:19Z

Class,

the simulation represents 3 different process over 200 CPU cycles. With the First-Come First-Serve (FCFS) scheduling strategy, each process is read by the CPU in the order that it arrives, hence first-come first-serve name. Each process continues running until it finish its designated CPU-burst cycle length, Process1 with 4 cycles, Process2 with 5-7, and Process3 with 3 cycles. When the FCFS CPU-burst cycle finishes it start the IO-burst cycle, but at the same time the next process starts being executed from the, next in line, CPU burst cycle.

It appears in the simulation that the CPU is able to start executing the next-step process while fetching the first process IO-burst. IO-burst take time between IO requests, not because they have especially long I/O requests, but it takes the same time to issue the hardware request to read a disk block. (Tanenbaum 156)

In the simulations statistics the CPU percentage is calculated by the total CPU cycles and the CPU-bursts. With the FCFS scheduling, Process1 CPU-burst was executed 16 times, then take 16 times, the CPU-burst length of 4, and divided by 200, and you get the CPU-percentage of 32%:

(executed CPU-bursts)   *   (length CPU-burst)   /   (total CPU-cycles)   =   (CPU percentage)

Process1: 16 * 4 / 200 = 32%

Process2: 15 * (7   +   7   +   5   +   5   +   6   +   7   +   7   +   6   +   5   +   6   +   5   +   6   +   7   +   6   +   6 ) / 200 = .455

Process3: 15 * 3 / 200 = .225

 

P.S.     The CPU had 100% uptime because it didn't have to wait for any IO reads.

 [link: https://canvas.park.edu/users/91372/files/9457319?wrap=1&verifier=9z4yy3yko1z1tYmXZ2fVCyPYOdKwBg4HZRF7jAtf] disc2.docx

---
