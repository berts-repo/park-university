# Unit 1: Discussion

Due Date

First post due 11:59 p.m., Thursday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Directions  

Download the  [link: https://canvas.park.edu/courses/71018/files/9524453?verifier=DVBSwuO749siWE85alcVydhzpo28WzgnKNEkJrhr&wrap=1] Unit 1 Discussion Questions document. Follow the directions below for your initial post and replay posts. 

Initial Post

Answer one of the Unit 1 Discussion questions from the document. When possible, pick one that has not been answered or one that has not been answered correctly. Provide a copy of the original question in your response. 

In your post:

Do not just say the correct answer is x. You must also explain why your answer is correct or on the flip side why some other answers are wrong.  Your explanation also shouldn't be “this is how array works” or “this is the result I get when I run this program on the computer ”.  Rather it needs to be specific such as explaining the result of each block or even each line of the code. When appropriate you should also cite corresponding concepts from the book chapter or additional readings.

Example Post

Q0. If you declare an array double[] list = {3.4, 2.0, 3.5, 5.5}, what's the highest index in this array?

0          B. 1         C. 2         D. 3       E. 4

// Your initial post. Remember to provide a copy of the question
Q0. If you declare an array double[] list = {3.4, 2.0, 3.5, 5.5}, what's the highest index in this array?
        A. 0          B. 1         C. 2         D. 3       E. 4

The answer is D 3. Here the length of the array is determined by the number of values provided between braces and separated by commas.  There are 4 elements in the  declaration thus the size of this array is 4 and the last index is 3 (4 minus 1).  See Array Element Initialization section on p381 of ch9.3.

Coding question: following coding standards and add appropriate comments. It may be helpful to briefly explain your algorithm (standalone or in the comments).

Reply Post

Follow the same guideline for the initial post. Do not just say “you’re right/wrong” or “agree/disagree”, support your feedback with a reasonable explanation.  Your reply posts should continue or expand the discussion, not just repeat other students' posts.  You may have a different answer or a similar answer with a different/clearer reasoning.

Format Code

To display your code and indentation properly, change the text style of your code portion to "Preformatted" style. Use "Paragraph" tool, the 2nd tool in the tool menu right above the rich content editor

 

How to Format Code

Location in Canvas to Preformat

  

Example of Preformatted Code

  

 

Tips

 [link: https://cscircles.cemc.uwaterloo.ca/java_visualize/] Java Visualizer    may be helpful to visualize the execution of Java programs.

If you use Eclipse or similar IDEs, you should learn to use its Debug functionality which allows you to step through the code and inspect variables.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-10-21T03:33:53Z

#15

Class,

this program checks if a user input license number is in the correct Missouri format, by comparing the index of letters and digits. If anyone knows how to make my code better, please don't be afraid to point something out or correct me, for this assignment and the rest of the course. I want to learn and will not be offended for any amount of criticism. I don't just want my programs to run; I want to be good!

P.S. I found it much easier to read without comments. I think it cluttered my code in the discussion post format, but I will be glad to repost it with the proper comments.

import java.util.Scanner;

public class disc1{

   public static boolean isValid(String checkNumber) {

        String validNumber = "LLDLDL";
        char isDigit = 'D';
        char isLetter = 'L';
        int validLength = validNumber.length();

   for (int i = 0; i < validLength; i++) {
    
        char validDigit  = validNumber.charAt(i);
        char validLetter = validNumber.charAt(i);
        boolean checkDigit  = Character.isDigit ( checkNumber.charAt(i) );
        boolean checkLetter = Character.isLetter( checkNumber.charAt(i) );

        if      ( validDigit == 'D' ) {
                if (checkDigit == true);
                else return false;
        }

        else if ( validLetter == 'L' ) {
                if (checkLetter == true);
                else return false;
        }
   }
   return true;
   }

   public static void main(String[] args) {

    String checkNumber;
    Scanner scnr = new Scanner(System.in);
    checkNumber = scnr.nextLine();
    System.out.println( isValid(checkNumber) );
   }
}

---


### Feedback

**[INSTRUCTOR]:** You met the discussion requirements for this week.
