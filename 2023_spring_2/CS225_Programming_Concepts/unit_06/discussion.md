# Unit 6: Discussion

Guidelines

Answer one of the  [link: https://canvas.park.edu/courses/73627/files/9959082/download?verifier=JxGYYXHdNbL6aLqx6VgirGsau1DrOz25Md36B9Cp&wrap=1] discussion questions. Whenever possible, pick a question that has not been answered, or has an incorrect/incomplete answer. 

Refer to  [link: https://canvas.park.edu/courses/73627/pages/assignment-grading-and-final-exam#discuss] Assignments and Grading for detailed guidelines.

Due Dates

Post initial response by Thursday at 11:59 pm, CT.

Respond to two or more classmates by Sunday at 11:59 pm, CT.

**My Score:** 15.0/?

---

## My Discussion Posts

**Posted:** 2023-04-21T00:43:10Z

6. [Practice #1 in ch12-ch13 Dynamic Data slides] Limited version newString class: Overload the +
operator to allow string concatenation with a c-string.
// driver code
newString str1("wonderful");
std::cout << "str1 is: " << str1 << "\n";
std::cout << "str1 + c-str: " << (str1 + " name") << "\n";

Class,
I had to first make a constructor for the newString object (str1). I also needed to overload the '<<' operator to print the output from the prompted driver file. When looking up some examples I ran across labeling private variables with and extra underscore at the end of the variable name 'data_' and 'size_' Does anyone know if this is common/good practice?

#include "disc.h"

newString::newString(const char* str) {
  // allocate memory for string
  size_ = std::strlen(str);
  data_ = new char[size_ + 1];

  std::strcpy(data_, str);    // copy data from C-string
}

// overload '+' operator to concatenate with C-string
newString newString::operator+(const char* str) const {
  // allocate memory for concatenated string
  size_t new_size = size_ + std::strlen(str);
  char* new_data = new char[new_size + 1];

  // concatenate strings
  std::strcpy(new_data, data_);   // copy data from first string
  std::strcat(new_data, str);   // append data from second string
  newString result(new_data);   // create new string object with concatenated data

  delete[] new_data;
  return result;
}

// overload stream output operator for printing
std::ostream& operator<<(std::ostream& os, const newString& str) {
  os << str.data_;
  return os;
}

Header:

#ifndef NEWSTRING_H
#define NEWSTRING_H

#include 
#include 

class newString {
public:
  newString(const char* str);

  newString operator+(const char* str) const;

  friend std::ostream& operator<<(std::ostream& os, const newString& str);

private:
  char* data_;
  size_t size_;
};

#endif

Output:

---


### Feedback

**[INSTRUCTOR]:** Bert,
You met the discussion requirements for this week.
