# Unit 7: Discussion

Guidelines

Answer one of the  [link: https://canvas.park.edu/courses/73627/files/9959074/download?verifier=NT8LfmIHdm84Qcd2yYI53ACxLxmroge9Bupsmbfq&wrap=1] discussion questions. Whenever possible, pick a question that has not been answered, or has an incorrect/incomplete answer. 

Refer to  [link: https://canvas.park.edu/courses/73627/pages/assignment-grading-and-final-exam#discuss] Assignments and Grading for detailed guidelines.

Due Dates

Post initial response by Thursday at 11:59 pm, CT.

Respond to two or more classmates by Sunday at 11:59 pm, CT.

**My Score:** 15.0/?

---

## My Discussion Posts

**Posted:** 2023-04-28T00:23:56Z

14. [Practice #1-1 in ch11-ch12 Composition] Implement the isEligibleToRetire() function.

Class,

I did not get the entire program to work properly. I do not have the output for you. From the criteria I believe I solved the implementation of the function:

bool Company::isEligibleToRetire(const Employee& emp) const {
  int age = emp.getAge();
  int yearsOnJob = emp.getYearsOnJob();
  double salary = emp.getSalary();

  int count = 0;
  if (age >= retireAge) count++;
  if (yearsOnJob >= retireYears) count++;
  if (salary >= retireSalary) count++;

  if (count >= 2 ) { return true; }
  else { return false} ;
}

---


### Feedback

**[INSTRUCTOR]:** You met the discussion requirements for this week.
