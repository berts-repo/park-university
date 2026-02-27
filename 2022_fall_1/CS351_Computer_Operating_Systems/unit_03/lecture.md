# Unit 3: Lecture

Chapter 3: Memory Management

To execute a process, the process must be brought into the memory. The process may generate some temporary output that also needs some memory to contain them. As there can be many active processes concurrently running, managing memory efficiently among all the sharing processes is an important task. In this chapter, we will examine memory management in detail. This includes basic memory management, swapping, virtual memory, page replacement algorithms, modeling page replacement algorithms, design issues for paging systems, implementation issues, and segmentation.

Basic Memory Management

For the system allows only one user process, the memory management can be very simple. That is, once a program is loaded into the memory, it will stay in the memory until the job is done. Figure 1, extracted from [1], depicts three simple memory organizations that can be used for the system with only one user process.

Figure 1. Ways of organizing the memory with an operating system and one user process.

Operating system is at the bottom of the RAM.

Operating is in ROM at the top of the memory.

The operating system is in RAM and the device drivers are in ROM.

For the multiprogramming system, multiple processes can be in the memory at the same time. Techniques such as swapping andvirtual memory can be used.

Swapping

Swapping brings the entire process into the memory, lets it run for sometimes, and then brings it back to the secondary storage. The operating system can bring in a new program into memory as long as there is enough memory for it. Figure 2, extracted from [1], depicts the changes in memory allocation as time progresses. The shaded area signals the portion of the memory not being used.

Figure 2. The changes in memory allocation as processes come in and out of the memory.

From the figure 2(d, e, f), the unused areas can be fragmented. The problem is that each individual unused area may not be enough for a new program, but the combined unused area may be. Thus, memory compaction will need, from time to time, to combine all unused areas to become one large unused area.

Virtual Memory

In contrast with swapping, virtual memory is to let a process run even though only a portion of the process is in the memory. The basic idea is to use secondary storage to augment the main memory in the processor to form virtual address space. Figure 3 from [1] shows the relationship between virtual address and the physical memory address.

Figure 3. The mapping of virtual memory address space and physical memory address space.

 

Using a replacement algorithm, data is transferred from the secondary storage to the main memory when it is needed, and written back to the secondary storage when the space in the memory is being replaced. If the area being swapped has a fixed size as in figure 3, the swapping is called paging. If the size is variable, the swapping is called segmentation. In segmentation, data is split along logical chunks such as procedures. Systems such as MULTICS and Intel Pentium support the combination of paging and segmentation for providing two-dimensional virtual memory.

This  [link: https://www.youtube.com/watch?v=qlH4-oHnBb8] video provides supplemental information on virtual memory management.

Page Fault Example

Problem: Suppose page faults occur 90% of the time (i.e. a page is not in the TLB).  What is the average access time to retrieve a page from the harddrive if it takes 30 nano seconds to search the TLB and 15 milli seconds to read a page in from the harddrive? 

Solution: This is an expected value problem.  To calculate the expected average time:

(.90)( 30 x 10-9 seconds) + (.10)( 15 x 10-3 seconds) = .0015 seconds, which is 1.5 milli seconds

Supplemental Resource

Chapter 4 Powerpoint Presentation

Chapter 4 Memory Management

Calculating Expected Value

The expected value of an outcome is the sum of the probability of each outcome times the outcome.  Here is the formula:

Expected Value = 

To use the formula do these steps:

Multiply the probability of the event times the outcome of the event. Do this for each event.

Sum all the values calculated in step 1.

Here is an example.  Suppose you have a software program that has two possible paths through it.  If the first path takes 5 milliseconds to run and it gets executed 40% of the time, and the second path gets executed 60% of the time but it takes 8 milliseconds to run, what is the time expected for the program to run.

Expected Value = (5 milliseconds)(.4) + (8 milliseconds)(.6) = 6.8 milliseconds

In other words, on average we expect the program to take 6.8 seconds to run.  In summary, expected value is an average computed using probabilities.

 

References

Modern Operating System. Andrew S. Tanenbaum. Prentice Hall. 4th edition.

Operating System Concept. Silberschatz, Galvin, Gagne, 6th edition.
