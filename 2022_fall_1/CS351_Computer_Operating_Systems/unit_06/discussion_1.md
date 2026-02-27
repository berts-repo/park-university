# Unit 6: Discussion 1

Deadlock Management

Of course, we would like to prevent deadlock if possible but the overhead to do so is often too high to make prevention the best option.  Come up with a checklist for how you would manage deadlock on Windows, Linux, or some other operating system you are familiar with.  As a programmer, is there anything you can do to minimize deadlock?

Post your reply to this thread. Also, respond to a minimum of two posts from your classmates.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-09-22T15:58:29Z

Class,

The four conditions for a deadlock are mutual exclusion, hold and wait, no preemption, and circular wait. Mutual exclusion conditions must hold for non-sharable resource, but resources like read-only file do not require mutually exclusive access and thus cannot be involved in deadlock.

On Linux you could check and see if a process is stuck with the command:

trace -p <pid>

If the command returns with a "wait" then you could be in a lock, and you can go to the next step of running the command:

ps aux | grep <application name>

If this returns "D" (uninterruptible sleep) it could mean that there is a deadlock. 

There are some way to prevent deadlocks when programing, and one is maintaining a lock order: whenever multiple locks are being used make sure they are acquired in the same order. Another option is never re-use the same lock you are holding, and also try not to hold locks across long operations like I/O. (Oracle 2022)

 

Oracle. (n.d.). Avoiding deadlock. Avoiding Deadlock (Multithreaded Programming Guide). Retrieved September 22, 2022, from https://docs.oracle.com/cd/E19455-01/806-5257/6je9h0347/index.html

---


### Feedback

**[INSTRUCTOR]:** The Linux commands you provided were great examples for this discussion.
