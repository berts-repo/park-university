# Unit 6: Lecture

Chapter 6: Deadlocks

In chapter 2, we saw that processes sometimes need to cooperate and synchronize with each other to accomplish their tasks. However, because of synchronization failure, potential problems such as deadlock can result. In this chapter, we will discuss deadlock in detail. In particular, we will talk about what the deadlock is, the conditions causing the deadlock, deadlock detection, deadlock recovery, deadlock avoidance, and deadlock prevention.

What is deadlock?

[3] defines that a deadlock is a situation in which two processes are each waiting for the other to complete before proceeding. In our textbook and a host of other textbooks in operating system expands this definition of deadlock to include more than two processes. In real life, the following figure, extracted from [2], best depicts what a deadlock is.

Figure 1. traffic deadlock in real life

In figure 1, a block of 4-way traffic deadlocked because traffic from each direction is waiting for cars blocked in the intersection to move. To prevent this scenario from occurring, a common courtesy is not to block the intersection if you can not drive your car clearly through the intersection.

Deadlock: Four Necessary Conditions

[2] describes that the following four conditions must hold simultaneously to cause a deadlock.

Mutual exclusion: For a particular resource, only one process at a time can use it.

Hold and wait: A process, holding certain resource, waits for other resource held by other processes.

No preemption: Once certain resource is held by a process, the system can not forcefully take away the resource from the process before it finishes using the resource.

Circular wait: There exists more than one process, circularly waiting for the next member in a chain to finish using the held resource.

This  [link: https://www.youtube.com/watch?v=Z7iHodl1jsM] video provides supplemental information on conditions necessary for deadlock.

Deadlock Modeling

To describe deadlock, a resource allocation graph such as the one depicted in figure 2 from [1] can be used.

Figure 2. Resource Allocation Graph: (a) process A holds resource R (b) process B requests resource S (c) A cycle in this resource allocation graph signals a deadlock.

In figure 2, a process is shown as a cycle, and a resource is shown as a square. Figure 2 (a) shows that resource R is assigned to process A, and figure 2 (b) shows process B requests for resource S. Figure 2 (c) clearly shows that two processes C and D, holding resource U and T respectively, are circularly waiting for resource T and U respectively.

Deadlock handling

There are many methods of handling deadlock, including deadlock detection, deadlock recovery, deadlock avoidance, and deadlock prevention.

Because of the high cost incurred for each of these methods, some systems such as Unix and Windows simply choose to ignore deadlocks altogether on the premises that the occurrence of a deadlock is very rare anyway.

Deadlock Detection

Detecting a deadlock, when there is one in the system, can be done by utilizing the resource graph technique. When the resource graph corresponding to a system's process and resource status shows a cycle such as the one in figure 2, there is a deadlock in the system.

However, the resource graph modeling is great for one copy for each type of the resource. If there are multiple copies for each type of the resource such as the one shown in figure 3 from [2], even though there is a cycle, there is no deadlock. To detect deadlock for this scenario, other technique such as resource allocation matrix can be used.

Figure 3. A resource allocation graph has a cycle, but does not have a deadlock

Deadlock Recovery

Once a deadlock in the system is detected, techniques such as preempting a resource, rollbacking the system to a state in which it does not have a deadlock, and killing process can be used to recover the deadlocked system.

Deadlock Avoidance

Avoiding deadlock in a system can be done by having processes declare their usage of the resource in advance. The system examines each request and decides whether to grant a resource to a particular process by examining whether the system can be still in a safe state (i.e., the system without deadlock) after the resource is granted to the process. This is similar to the fund allocation in the traditional banking system. Therefore, deadlock avoidance can utilize "Banker's algorithm" which will be described detailed in this lecture.

Deadlock Prevention

Remember that for a deadlock to occur, the four necessary conditions described above must happen at the same time. To prevent deadlock, one only need to break one of the four conditions that cause deadlock. For example, to allow for preemption of a resource, the system can allow the resource that is currently being assigned to a process which is in the wait state for other resource to be preempted. To prevent hold and wait, the system can require that a process which is requesting for a resource, does not hold any resource. Several techniques for deadlock prevention will be discussed in this lecture.

Starvation

Starvation can occurs when some parts of a system are running, but there are some jobs not being able to proceed. For example, in the shortest-job first scheduling scheme, a job requiring long CPU processing time waits for other short jobs to finish up. If short jobs keep coming while the long job is waiting, this long job may not get to use the CPU.

Deadlock and Starvation are two separate terms

The terms deadlock and starvation sometimes can be quite confusing. These are two separate terms. Deadlock is a situation in which four necessary conditions described above must hold simultaneously. In this situation, one would say that these processes are deadlocked. In a deadlock situation, one can say that it is the process own fault (because of the process stubbornness that the process would not give up the resource) so that the deadlocked processes can not move forward.

In the situation of starvation, one would say that the process is starved. In the starvation situation, it is not the process's fault (it is largely due to external events such as scheduling, low priority....) that the process cannot get resource time to move forward.

This  [link: https://www.youtube.com/watch?v=w0LwGqffUkg] video provides supplemental information on the Banker's algorithm.

Supplemental Resource

Chapter 6 Powerpoint Presentation

Chapter 6 Deadlock

References

Modern Operating System. Andrew S. Tanenbaum. Prentice Hall. 4th edition.
