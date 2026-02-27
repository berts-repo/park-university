# Unit 4: Discussion

Guidelines

Answer one of the  [link: https://canvas.park.edu/courses/73627/files/9959115/download?verifier=6rbKtIkR4x1bgkIRgqaJGu5scy0MZOJpQYIFIUOS&wrap=1] discussion questions. Whenever possible, pick a question that has not been answered, or has an incorrect/incomplete answer. 

Refer to  [link: https://canvas.park.edu/courses/73627/pages/assignment-grading-and-final-exam#discuss] Assignments and Grading for detailed guidelines.

Due Dates

Post initial response by Thursday at 11:59 pm, CT.

Respond to two or more classmates by Sunday at 11:59 pm, CT.

**My Score:** 15.0/?

---

## My Discussion Posts

**Posted:** 2023-04-06T21:03:37Z

7. [Q3 in ch12 Pointers slides] What will be printed out?

 

Class,

This code initializes an integer array (arr), the length (5) and the first two indexes (1, 2). It then initializes a dynamic array (pArr), the length (5) and the first two elements (1, 2). The code then loops through a for-loop and prints the index fallowed by both arrays current iteration. The last thing is 'delete[]' which frees the dynamically allocated array.

#include <iostream>

int main() {
    int size = 5; // capacity
    int arr[5] = { 1, 2 };
    int *pArr = new int[size] { 1, 2 }; // C++11 syntax

    for (int i = 0; i < size; i++) {
        std::cout << "[" << i << "]: " << arr[i] << "; " << pArr[i] << "\n";
    }

    delete[] pArr;

    return 0;
}

Output:

 Because the array length was initialized to '5' the remaining elements were automatically initialized to zero with 'new'

---


### Feedback

**[INSTRUCTOR]:** Bert,
You met the discussion requirements, I especially love the output when provided, it really helps the understanding.
