# Unit 2: Discussion

Introduction 

Participation in discussion threads is a weekly assignment that tests your reading process and critical thinking. You may participate in these discussion threads for this unit between 12:00 a.m., Monday, CT through 11:59 p.m., Sunday, CT. of the corresponding week.

 

Requirements

Your initial post must answer both of your chosen questions by 11:59 p.m., Thursday, CT.

You must complete your own posting and respond to at least one other student thread (different than your own) by 11:59 p.m., Sunday, CT.

Throughout the week, you must respond, to the best of your knowledge, the questions or requests made by Instructor and/or students, especially the Instructor’s requests for corrections.

Due Date

Initial post by 11:59 p.m., Thursday, CT

Respond to one or more classmates by 11:59 p.m., Sunday, CT

Directions 

After reading the assigned course material, you must select and answer any two (2) of the questions below.

Post your answers in this environment. Do not attach code, but copy and paste it onto the discussion thread. When you do that, you may lose some indentation. You need to restore this indentation manually to make the program readable.   

Please read what other students are posting and post all different examples. Do not repeat previous postings. Be Original. Also, do not write code containing material related to the Lab Activities/Homework. Homework is personal and it must not be shared with anyone but the Instructor.

Questions

Show a complete and syntactically correct piece of C/C++ code that contains a conditional expression that uses at least two (2) relational operators and three (3) logical operators. To be complete, the code must declare and initialize all the variables the conditional expression needs to be evaluated. After presenting the code, evaluate it, indicating the order of the operations in the conditional expression and their intermediate and final values.

Show a complete and syntactically correct example of C/C++ code that contains conditional statements to separate all integer numbers in four (4) or more ranges, and do something distinct in each range. To be complete, the code must declare and initialize all the variables it needs. For example, the conditional statements may divide all integer numbers into negative numbers smaller than -23, numbers from -23 to 100, numbers from 101 to 127, and numbers above 127. Students should chose and implement their own ranges, different from this example.

Show a complete and syntactically correct example of C/C++ code that contains a loop used to validate user input. To be complete, the code must declare and initialize all the variables it needs. For example, a loop may continuously request the user for a value within certain range. The code will only stop when this condition is satisfied.

Show a complete and syntactically correct example of C/C++ code that contains a loop to print a table. To be complete, the code must declare and initialize all the variables it needs. For example, a loop may print all rows of a addition or multiplication table. Add headers to the table.

Show a complete and syntactically correct example of a conditional statement in C/C++. This could be an if-else-if set of statements or a switch statement. To be complete, the code must declare and initialize all the variables it needs. After presenting the original code, convert it into the other conditional statement you did not chose. For example, if you originally wrote an if-else-if statement, you should show the same conditional expression converted into a switch. Be mindful that this is not possible in all cases, so chose an example where it is possible to do so.

Show a complete and syntactically correct example of a nested if-statement. To be complete, the code must declare and initialize all the variables it needs. After presenting the original code, convert it into a sequential if-else-statement. The conditional expressions in the sequential if-else-statement are a combination of the original conditional expressions in the nested if-statement using the AND relational operator (&&). Be mindful that it is not possible to do the conversion in all cases, so chose an example where it is possible to do so.

Show a complete and syntactically correct example of a C/C++ loop. This could be a while-loop, a do-while loop, or a for-loop. To be complete, the code must declare and initialize all the variables it needs. After presenting the original code, convert it into one of the other loops you did not chose. For example, if you originally wrote a for-loop, you may show the exact same loop written in either, a while loop, or a do-while loop.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2021-08-24T09:15:35Z

Hello class,

I am responding to prompts 3 and 4. If anyone knows a better way to print a header for my table, I would appreciate knowing a more efficient way.

/*******************************************************************************************************
Promp: 4 Show a complete and syntactically correct example of C/C++ code that contains a loop to print a table.
To be complete, the code must declare and initialize all the variables it needs. For example, a loop
may print all rows of a addition or multiplication table. Add headers to the table.

Prints a multiplication table
********************************************************************************************************/

#include 

int main()
{
    printf("   *******************************************\n");  //table header
    int column = 1;
    while (column < 10) { //interates through the columns of the table
        
        for (int row = 1; row < 10; row += 1)  //interates through the rows of the table
        {
            printf("%5d",row*column);   //multiplies the variables for the table
        }

        printf("\n"); //new line for each row of the table
        column += 1;
    }
    printf("   *******************************************\n");  //table footer
    return 0;
}

/********************************************************************************************
Promp 3: Show a complete and syntactically correct example of C/C++ code that contains a loop
used to validate user input. To be complete, the code must declare and initialize
all the variables it needs. For example, a loop may continuously request the user
for a value within certain range. The code will only stop when this condition is satisfied.

Has the user input data untill the correct answer is given.
*********************************************************************************************/
#include 

int main() {

int answer = 2;
int guess;
    do {
        printf("What does is 1+1?");
        scanf_s("%d", &guess);
}   while (guess != answer);
}

---
