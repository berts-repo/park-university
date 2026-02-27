# Unit 5: Discussion

Guidelines

Answer one of the  [link: https://canvas.park.edu/courses/73627/files/9959016/download?verifier=ZB02siU2KCR3cJtR9GLYIhF9ygpKS6tdWMXWrL8u&wrap=1] discussion questions. Whenever possible, pick a question that has not been answered, or has an incorrect/incomplete answer. 

Refer to  [link: https://canvas.park.edu/courses/73627/pages/assignment-grading-and-final-exam#discuss] Assignments and Grading for detailed guidelines.

Due Dates

Post initial response by Thursday at 11:59 pm, CT.

Respond to two or more classmates by Sunday at 11:59 pm, CT.

**My Score:** 15.0/?

---

## My Discussion Posts

**Posted:** 2023-04-14T02:03:26Z

6. [Practice #3-1 in ch10 OOP slides] Define a class counterType to implement a counter. Your class
must have a private data member counter of type int and functions to set counter to the value
specified by the user, initialize counter to 0, retrieve the value of counter, and increment and
decrement counter by one. The value of counter must be nonnegative. Step 1. UML class
diagram.

Class,

I have a hard time fallowing OOP algorithms, especially in others programs. I took this on to help me work though it a little:

class counterType {
private:
    int counter; // private data member

public:
    // constructor to initialize counter to 0
    counterType() {
        counter = 0;
    }

    // function to set counter to a specified value
    void setCounter(int value) {
        if (value >= 0) {
            counter = value;
        }
    }

    // function to retrieve the value of counter
    int getCounter() const {
        return counter;
    }

    // function to increment counter by one
    void increment() {
        counter++;
    }

    // function to decrement counter by one
    void decrement() {
        if (counter > 0) {
            counter--;
        }
    }
};

I can provide main() if someone wants.
Output:

---


### Feedback

**[INSTRUCTOR]:** Bert,
You met the discussion requirements for this week.
