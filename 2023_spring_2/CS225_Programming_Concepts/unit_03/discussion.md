# Unit 3: Discussion

Guidelines

Answer one of the  [link: https://canvas.park.edu/courses/73627/files/9959111/download?verifier=vhzb5rARSImO3t0dDSQwSgSLCJpjj3lMgnA72fka&wrap=1] discussion questions. Whenever possible, pick a question that has not been answered, or has an incorrect/incomplete answer. 

Refer to  [link: https://canvas.park.edu/courses/73627/pages/assignment-grading-and-final-exam#discuss] Assignments and Grading for detailed guidelines.

Due Dates

Post initial response by Thursday at 11:59 pm, CT.

Respond to two or more classmates by Sunday at 11:59 pm, CT.

**My Score:** 15.0/?

---

## My Discussion Posts

**Posted:** 2023-03-29T01:39:09Z

5. [Practice #1 in ch8 Array slides] Write a function to count # of unique values in a sorted (non-
descending order) int array.

Testing case #1: arr {5, 7, 7, 8, 22, 22}, size 6  returns 4
Testing case #2: arr {5, 7, 8}, size 3  returns 3
Testing case #3: arr {5}, size 1  returns 1
Testing case #4: arr {}, size 0  returns 0

 

Class,

here is my function, but it does assume the list is sorted because it checks the current index to the last index.  I also added the test cases in main:

#include 

int countUnique(int arr[], int size) {

  int count = 0; // unique count variable

  for (int i = 0; i < size; i++) {
    if (arr[i] != arr[i-1]) { // checks current unique index to the last index in a sorted list
      count++; // unique counter
    }
  }
  return count;
}

int main() {
  int arr1[] = {5, 7, 7, 8, 22, 22};
  int size1 = sizeof(arr1) / sizeof(arr1[0]);
  std::cout << countUnique(arr1, size1) << std::endl;

  int arr2[] = {5, 7, 8};
  int size2 = sizeof(arr2) / sizeof(arr2[0]);
  std::cout << countUnique(arr2, size2) << std::endl;

  int arr3[] = {5};
  int size3 = sizeof(arr3) / sizeof(arr3[0]);
  std::cout << countUnique(arr3, size3) << std::endl;

  int arr4[] = {};
  int size4 = sizeof(arr4) / sizeof(arr4[0]);
  std::cout << countUnique(arr4, size4) << std::endl;

  return 0;
}

Output:

---


### Feedback

**[INSTRUCTOR]:** Bert,
You met all the requirements for the discussion this week. Thanks for posting the links and the output.
