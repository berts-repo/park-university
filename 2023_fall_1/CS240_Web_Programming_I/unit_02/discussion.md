# Unit 2: Discussion

Unit 2: Discussion

Working with HTML and CSS

Please review the general directions from Unit 1. In your discussion you will select and discuss the review questions and exercises at the end of the chapter. There will be some duplicates depending on how many students are enrolled.  So each question should be used at least once. 

Do not repeat a question that has already been answered until all questions have been answered!

Review Questions  

Your instructor will assign you one review question from chapter 3 or chapter 4   

Copy the question number and the question at the top of your posting! 

Thoroughly explain the answer. 

Exercises   

Your instructor will assign you one exercise question from chapter 3 or chapter 4   

Copy the question number and the question at the top of your posting! 

Thoroughly explain the answer. 

Reply Postings

Please provide a total of 2 reply posts.

In your reply post to 2 other students:

Respond to each student by name.

Identify if the answer was correct or incorrect. If it's incorrect, identify the correct answer and where you found the answer. 

Students should review the other students post for clarity and correct explanation of concepts, terminology accuracy and correctness of code and evaluates the post for use or proper coding conventions and documentation.

Cite a reference to support your statements.

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2023-08-22T21:10:57Z

Review #5

For the ul element, what does the start attribute do?

Class, I have a little confusion for this review question. The review question is listed in section “4.4 Ordered List” in the review questions list section, and I also can’t find any documentation in the book or on the web about the start attribute for unsorted-list. The start attribute is used in ordered-list and not with the unordered-lists (bullets). Please correct me if I missed something.

The start attribute can be used to set the starting point for the numbered bullets in the ul tag, so instead of labeling the bullets starting at 1,2,3, it allows the user to set bullet at a start point say 5, so the bullets would be 5,6,7.

Example:

<ol start="5">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>

Output:

First item

Second item

Third item

Exercise #1

Provide a type selector CSS rule for the ul element that causes list items to be displayed with check mark symbols at the left. The list-style-type­ property does not include a value for the check mark symbol. To display check marks symbols, you will need to use the list-style-image property, which was not covered in the book. In your answer, use the filename checkMark.gif.

To accomplish this there first needs to be a file named ‘checkMark.gif’ with the path to its location on the computer, or it can just be in the same folder as the .html file, which will be the example in my demonstration. In the header tag add the fallowing style:

<style>
ul {
  list-style-image: url('checkMark.gif');
}
</style>

Output view:

If I remember correctly I don't need to post my source from W3School but here is the url incase: https://www.w3schools.com/cssref/pr_list-style-image.php

---


### Feedback

**[INSTRUCTOR]:** Bert

Fantastic!

If you have any questions please contact me in my Inbox.
