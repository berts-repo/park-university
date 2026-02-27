# Unit 2: Discussion 1

Processes and Threads

Describe the concept of processes and threads within an operating system, and explain how processes are managed.  Should processes have the same priority?  Explain the rationale for your answer.

In addition,  [link: https://docs.microsoft.com/en-us/windows/win32/procthread/creating-threads] read this article. 

What is the purpose of the CreateThread function and how would you use it?

Post your reply to this thread. Also, respond to a minimum of two posts from your classmates.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-08-24T18:29:12Z

Class,

with processes and threads the computer is able to leave the illusion of multitasking. If only one process could be run at a time then the computer would be idle and not running any process, because the computer would always be waiting for you to click something. A process, essentially, is a certain application being converted to machine code. Threads are further divide the application up into tasks, this allows the process to share different threads while another thread is being executed, or reading data from the disk, or taking I/O inputs, so on.

When creating a new process Unix will use the system call fork(), and Windows will use Win32 function CreateProcess. The unix child process will share the same address space as the parent until altercations are made. A process will run until it's complete or until it's interrupted, often caused by one of the four terminations, normal exit, error, fetal, and killed. After the interrupt the system has to save the state, this is done by pushing the current address location onto the stack, and pulling the next address location from the Scheduler.

Process priority is essential for modern computers, but according to figure 2-6, in the textbook, the CPU can get a lot utilization from a single running process instead of a multiprocessing cpu:

so, a unconventional CPU might benefit from sharing process priority. That being said, priority is important in the current multiprogramming CPU's, if not then even doing things like moving the mouse while loading a web page would not work.

 

CreateThread is a Win32 function call. This function creates thread on the stack, that has the address location of code to be executed, when called with the OpenThread function.

HANDLE CreateThread(
  [in, optional]  LPSECURITY_ATTRIBUTES   lpThreadAttributes,
  [in]            SIZE_T                  dwStackSize,
  [in]            LPTHREAD_START_ROUTINE  lpStartAddress,
  [in, optional]  __drv_aliasesMem LPVOID lpParameter,
  [in]            DWORD                   dwCreationFlags,
  [out, optional] LPDWORD                 lpThreadId
);
HANDLE OpenThread(
  [in] DWORD dwDesiredAccess,
  [in] BOOL  bInheritHandle,
  [in] DWORD dwThreadId
);

 

 [link: https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread#remarks] https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread#remarks

https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthread

---


### Feedback

**[INSTRUCTOR]:** Great explanation on processes and threads and how a system prioritizes them.  Also, great reference to the textbook (fig 2-6).  Great work.
