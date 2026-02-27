# Unit 2: Lecture

Chapter 2: Processes and Threads

In this unit, we will begin to study in detail how an operating system accomplishes its objectives. In particular, we will concentrate its most central concepts: process and thread. The topics to be examined include: What is a process? What is a thread? How does an operating system schedule among its processes and threads? How do processes/threads communicate with one another? We will also introduce many classical interprocess communication problems.

What is a process?

A process is a running program. It is referred to as a basic unit of work [2] within an operating system. Every process requires some operating system resources such as CPU time, memory space, I/O access for the purpose of accomplishing its task. For example, when you are writing a Microsoft Word document, you are executing a process within your operating system.

In modern operating systems, there are usually several processes running concurrently. For example, when you are writing a Microsoft Word document, you can also have a process running Internet Explore to check for your bid on the ebay at the same time. While you are executing your user processes, the operating system has many system processes running in the background to help you accomplish your tasks.

[Exercise] To see what processes that are currently running in your system, you can do the following. If you are in Windows environment, you can right click on the task bar and select “task manager”. Then click on the “processes” tab. If you are in Linux environment, you can type in “ps aux” in the command line.

A process can be created and terminated dynamically. Once it is created, it is allocated with its own address space. It will go through several states such as ready, running, and waiting, before termination, see figure 1 from [1].

Figure 1. A process can go through many states.

What is a thread?

A thread in [2] is defined as a basic unit of CPU utilization. In the old days, it used to be the case that each process has only one thread. Nowadays, most operating systems allow multiple threads running within a single process. As an example of a multi-threaded program, consider Microsoft Word. When you are writing a Word document, one thread can be enabled to catch your spelling mistakes by highlighting the mistakes when it catches them. Another thread can be enabled to wrap around your sentence if your sentence gets outside the boundary. Yet another thread can be enabled to auto format your document so that bullets are automatically indented and sequentially inserted.  Figure 2 from [1] gives a high level view of single-thread processes and multi-threaded processes.

Figure 2. (a) Three single-threaded user processes (b) One multi-threaded user process

A thread is sometimes called as a lightweight process because threads within a process do not have their own address space. Threads within a process share the process address space. The sharing of the address space among threads is best described by the figure 3 from [2].

Figure 3. The address space of a single-threaded process vs. that of a multi-threaded process

View this  [link: https://www.youtube.com/watch?v=O3EyzlZxx3g] video for information regarding processes and threads.

Inter-process communications

Sometimes processes need to cooperate with each other for the purpose of sharing information, speeding up the computation, or simply allowing for convenience. Cooperating processes will need to communicate with each other. This is provided through inter-process communications (IPC) mechanisms such as semaphores, monitors, or messages. These mechanisms permit that cooperating processes synchronize among each other, and share data in an orderly fashion, therefore not leading to contention. Interthread communications, similar to IPC, allow threads within a process to cooperate and communicate with each other.

Classical Interprocess communication problems

In the literature dealing with Operating System, there are many problems dealing with synchronization. For examples, dining philosophers (Figure 4 from [1]), reader and writer, sleeping barbar (Figure 5 from [1]), cigarette smokers, and consumer and producer are some of the classical ones. The basic problem is that concurrent processes compete for the share data, resulting in errors, deadlocks, or process starvation. IPC mechanisms can solve many of these synchronization problems.

Figure 4. Dining Philosopher Problem: Each philosopher needs two forks (or best yet two chopsticks) to eat a plate of spaghetti. If all philosophers pick up their right fork at the same time, everyone will be waiting for their left fork and no one will get to eat any spaghetti. Then the system will get deadlocked.

See this  [link: https://www.youtube.com/watch?v=NbwbQQB7xNQ] video for Dining Philosopher Problem.

Figure 5. Sleeping Barber Problem. A classical problem illustrates the importance of synchronization without getting into race conditions.

Scheduling

In a multiprogramming operating system, many processes can share a CPU simultaneously. In order to decide which process gets the CPU, an operating system has a scheduler. The schedule’s job is to choose a process among all the processes in the ready state according a scheduling algorithm and send the process to the CPU. There are many scheduling algorithms exist today, e.g., first come first serve, shortest job first, round robin, priority scheduling, multilevel queues, guaranteed scheduling, lottery scheduling, and fair-share scheduling.  Different scheduling algorithms will favor different classes of processes. Figure 6 from [1] describes the objectives of a scheduling algorithm under different environments.

Figure 6. The objectives of a scheduling algorithm are different under different operating system environments.

Scheduling Example

Problem: Suppose the CPU has to wait 60% of its time on I/O completion, and there are two processes that need to run: A and B.  If A and B takes 12 minutes each of CPU time, then how long will it take for them to run sequentially?  

Solution: Using the formula on page 96, if a single process runs by itself then CPU utilization is 1 - .61 = .40, assuming I/O waiting probability equals 0.60.  If run sequentially, A takes 12 min/.4, or 30 minutes to complete.  Process B running next also takes 12 min/.4, or 30 minutes.  Therefore the total time for both processes to run sequentially is 30 + 30, which equals 60 minutes. 

If the two processes are run in parallel then CPU utilization is 1 - .62 = .64, or said another way, 64% of the CPU is available.  Because we have two processes running, each gets one half of the 64%, or 32% of the CPU, which is .32.  Since the two processes take 12 minutes, and they are running at the same time, we can compute the time to run one process and the other process will require the same amount of time.  We do this by 12 min /.32, which is 37.5 minutes.  Therefore, it takes 37.5 minutes if the two processes run in parallel.

Supplemental Resource

Chapter 2 Powerpoint Presentation

Chapter 2 Processes and Threads

References

Modern Operating System. Andrew S. Tanenbaum. Prentice Hall. 4th edition.

Operating System Concept. Silberschatz, Galvin, Gagne, 6th edition.
