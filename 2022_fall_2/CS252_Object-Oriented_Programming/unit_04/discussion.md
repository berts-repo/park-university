# Unit 4: Discussion

Due Date

First post due 11:59 p.m., Thursday CT

Respond to two or more classmates by 11:59 p.m., Sunday, CT.

Directions  

Download the  [link: https://canvas.park.edu/courses/71018/files/9524067?verifier=bMwYMp2NLOcBgUcoOlHZPFUKEJYgGf27vB38WUTy&wrap=1] Unit 4 Discussion Questions document. Follow the directions below for your initial post and replay posts. 

Initial Post

Answer one of the Unit 4 Discussion questions from the document. When possible, pick one that has not been answered or one that has not been answered correctly. Provide a copy of the original question in your response. 

Follow the guidelines of the  [link: https://canvas.park.edu/courses/71018/discussion_topics/1489774] Unit 1 Discussion.

Reply Post

Follow the same guideline for the initial post. Do not just say “you’re right/wrong” or “agree/disagree”, support your feedback with a reasonable explanation.  Your reply posts should continue or expand the discussion, not just repeat other students' posts.  You may have a different answer or a similar answer with a different/clearer reasoning.

Tips

 [link: https://cscircles.cemc.uwaterloo.ca/java_visualize/] Java Visualizer   may be helpful to visualize the execution of Java programs.

If you use Eclipse or similar IDEs, you should learn to use its Debug functionality which allows you to step through the code and inspect variables.

**My Score:** 10.0/?

---

## My Discussion Posts

**Posted:** 2022-11-09T00:51:08Z

16. Read source code of ArrayList and answer the following questions (pick one). 
http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/util/ArrayList.java 

16.a. What’re the purposes of the instance data member size, internally and externally? 

 

Class,

'size' is a private helper in the 'ArrayList' class. It is declared on line 134:

private int size;

The variable is used throughout the different methods in the class, but I first notice it on line 169 in the conductor, which I believe is still a conductor, because it has no return type, but where I am uncertain is that it has unfamiliar syntax as a parameter. 

public ArrayList(Collection<? extends E> c) { [link: http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/util/ArrayList.java#l167] 
        elementData = c.toArray(); [link: http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/util/ArrayList.java#l168] 
        size = elementData.length; [link: http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/util/ArrayList.java#l169] 
        // c.toArray might (incorrectly) not return Object[] (see 6260652) [link: http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/util/ArrayList.java#l170] 
        if (elementData.getClass() != Object[].class) [link: http://hg.openjdk.java.net/jdk8/jdk8/jdk/file/687fd7c7986d/src/share/classes/java/util/ArrayList.java#l171] 
            elementData = Arrays.copyOf(elementData, size, Object[].class);

It is used to initialize the length of the array, and can be found in some other methods including: trimToSize() line 180, and 'public void ensureCapacity(int minCapacity)' on line 194.

It is used externally with the method 'size()' on line 263 and that would be a public return of 'size'

---


### Feedback

**[INSTRUCTOR]:** You met the discussion requirements.
