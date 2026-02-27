# Unit 2: Discussion

Due Date

First post due 11:59 p.m., Thursday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Directions  

Download the  [link: https://canvas.park.edu/courses/71018/files/9524213?verifier=7zymRu4Np6vTW6UrF78msVbA4Tjw0wWhJFvn5Wtj&wrap=1] Unit 2 Discussion Questions document. Follow the directions below for your initial post and replay posts. 

Initial Post

Answer one of the Unit 2 Discussion questions from the document. When possible, pick one that has not been answered or one that has not been answered correctly. Provide a copy of the original question in your response. 

Follow the guidelines of the  [link: https://canvas.park.edu/courses/71018/discussion_topics/1489774] Unit 1 Discussion.

Reply Post

Follow the same guideline for the initial post. Do not just say “you’re right/wrong” or “agree/disagree”, support your feedback with a reasonable explanation.  Your reply posts should continue or expand the discussion, not just repeat other students' posts.  You may have a different answer or a similar answer with a different/clearer reasoning.

Tips

 [link: https://cscircles.cemc.uwaterloo.ca/java_visualize/] Java Visualizer   may be helpful to visualize the execution of Java programs.

If you use Eclipse or similar IDEs, you should learn to use its Debug functionality which allows you to step through the code and inspect variables.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-10-25T05:29:37Z

#16. Write a method which takes two parameters, an ArrayList of Integer list and an int target, and 
return an ArrayList which stores the indexes of all occurrences of target in list. Do not modify 
list.

 

Class,

I tackled this by creating a return array, the same size as list, that loops through list and stores the index of the target and sets the un-matched indexes of indexList to -1.

 public static int[] findIndexList( int[] list, int target ){
                int[] indexList = new int[list.length];
                for (int i = 0; i < list.length; ++i ){

                        if ( target == list[i] ){
                                indexList[i] = list[i];
                        }
                        else indexList[i] = -1;
                }
                return indexList;
        }

---


### Feedback

**[INSTRUCTOR]:** You met the discussion requirements.
