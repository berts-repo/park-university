# Unit 1: Discussion 2

System Calls

Operating systems provide an interface to user programs that enable them to access operating system features and system hardware in a secure way. Do an online search and located a list of system calls for an operating system of your choice. List at least three operating system calls that you found and list the statement in a programming language that uses that system call.  [link: https://docs.microsoft.com/en-us/cpp/c-runtime-library/system-calls?view=msvc-160] Here is a good resource that lists functions in C and C++.

If you have experience using system calls then please post how you used them and your comments regarding their importance. Post your reply to this thread. Also, respond to a minimum of two posts from your classmates.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-08-18T01:18:12Z

Class,

I'm going with Linux system calls which was provided by the Ubuntu documentation.

setitimer(2) - get or set value of an interval timer

#include sys/time.h

       int getitimer(int which, struct itimerval *curr_value);
       int setitimer(int which, const struct itimerval *new_value,
                     struct itimerval *old_value);

rename(2) - change the name or location of a file

#include stdio.h

       int rename(const char *oldpath, const char *newpath);

pipe(2) - creates a pipe

#include unistd.h

       int pipe(int pipefd[2]);
#define _GNU_SOURCE             /* See feature_test_macros(7) */
#include fcntl.h             /* Obtain O_* constant definitions */
#include unistd.h

       int pipe2(int pipefd[2], int flags);

 

https://manpages.ubuntu.com/manpages/trusty/man2/syscalls.2.html

---


### Feedback

**[INSTRUCTOR]:** The Ubuntu documentation examples enhanced this topic.  Great work.
