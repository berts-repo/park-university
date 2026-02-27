# Unit 2: Discussion

Guidelines

Answer one of the  [link: https://canvas.park.edu/courses/73627/files/9959623/download?verifier=xWhunDcfvYHbCLUkLsvJtFgn4tBZbmUXjMEPFNuy&wrap=1] discussion questions. Whenever possible, pick a question that has not been answered, or has an incorrect/incomplete answer. 

Refer to  [link: https://canvas.park.edu/courses/73627/pages/assignment-grading-and-final-exam#discuss] Assignments and Grading for detailed guidelines.

Due Dates

Post initial response by Thursday at 11:59 pm, CT.

Respond to two or more classmates by Sunday at 11:59 pm, CT.

**My Score:** 15.0/?

---

## My Discussion Posts

**Posted:** 2023-03-23T22:19:53Z

4. Given this C++ function

 

Class,

I rewrote the function to include a main, header library, the prompted function, and some test cases:

#include 

int mystery(int n1, int n2)
{
    if (n1 > 0)
    {
        for (int i = 1; i < n1; i++)
        {
            n2 = n2 * i;
        }
        return n2;
    }
    else if (n2 > 0)
    {
        for (int i = 0; i <= n2; i++)
        {
            n1 = n1 + i;
        }
        return n1;
    }
    return 0;
}

int main()
{
    // Test cases
    std::cout << "mystery(4, -5) = " << mystery(4, -5) << std::endl;
    std::cout << "mystery(-8, 9) = " << mystery(-8, 9) << std::endl;
    std::cout << "mystery(2, 2) = " << mystery(2, 2) << std::endl;
    std::cout << "mystery(-2, -4) = " << mystery(-2, -4) << std::endl;

    return 0;
}

Output:

I will use the first test case as the explained example: when main() calls one of the functions it passes the parameters provided, (4 and -5) It checks if the first number is greater then zero (4), if not it then checks if the second number (-5). Since the first number is larger, it then runs a loop through four iterations, as the loop is conditioned to the length of n1 (i = 0; i<4; i++) In each iteration it takes the the iteration of n2 (-5), and multiplies it by a incrementing i, which increases from 0-3. The function returns the new n2.

---


### Feedback

**[INSTRUCTOR]:** Brandon,
You met the requirements for this week discussion, especially your replies, very nicely written expanding on the topic nicely.
