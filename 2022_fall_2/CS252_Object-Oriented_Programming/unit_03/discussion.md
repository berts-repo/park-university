# Unit 3: Discussion

Due Date

First post due 11:59 p.m., Thursday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Directions  

Download the  [link: https://canvas.park.edu/courses/71018/files/9524072?verifier=nDJGVEIkdrGMa86VXZuODu0q5450jNH8i6fh01Kh&wrap=1] Unit 3 Discussion Questions document. Follow the directions below for your initial post and replay posts. 

Initial Post

Answer one of the Unit 3 Discussion questions from the document. When possible, pick one that has not been answered or one that has not been answered correctly. Provide a copy of the original question in your response. 

Follow the guidelines of the  [link: https://canvas.park.edu/courses/71018/discussion_topics/1489774] Unit 1 Discussion.

Reply Post

Follow the same guideline for the initial post. Do not just say “you’re right/wrong” or “agree/disagree”, support your feedback with a reasonable explanation.  Your reply posts should continue or expand the discussion, not just repeat other students' posts.  You may have a different answer or a similar answer with a different/clearer reasoning.

Tips

 [link: https://cscircles.cemc.uwaterloo.ca/java_visualize/] Java Visualizer   may be helpful to visualize the execution of Java programs.

If you use Eclipse or similar IDEs, you should learn to use its Debug functionality which allows you to step through the code and inspect variables.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-11-02T00:27:22Z

#17

Class,

This method creates a masked 2d-array that represents negative numbers with a "0", and positive numbers with a "1" which is derived from a sample array that is passed into the method. It then returns the new masked array.

The hardest part, and my notable discovery, was that you have to initialize the row length for the table array in the outer nested loop. This way the inner loop as a length for each of the rows.

import java.util.Arrays;
public class disc {
        public static int[][] getMask ( int origArray[][] ){

                // Initialize the number of rows.
                int[][] maskedArray = new int[origArray.length][];

                for ( int row = 0; row < origArray.length; ++row ){

                        // Initializes the row length for each iteration.
                        maskedArray[row] = new int[ origArray[row].length ];

                        for ( int elem = 0; elem < origArray[row].length; ++elem ){
                                if ( origArray[row][elem] > 0 )
                                        maskedArray[row][elem] = 0;
                                else {
                                        maskedArray[row][elem] = 1;
                                }
                        }
                }
          return maskedArray;
        }

        public static void main(String[] args){

                int arr[][] ={{ 1,2,3 }, {-1,-2,-3}};
                System.out.println( Arrays.deepToString( getMask(arr) ) );
        }
}

---


### Feedback

**[INSTRUCTOR]:** You met this weeks discussion requirements.
