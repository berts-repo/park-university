# Unit 2: Homework

**Due:** 2023-08-28T04:59:00Z
**Points Possible:** 60.0
**Submission Types:** online_upload

## Instructions

Unit 2: Homework

        

    

    
 

    
Working with HTML and CSS

    
        
Overview

        
Project Requirements 

    
    
    

    

        

            
Overview 

        

    

    
 

    
Learning Outcomes

    
The learning outcomes for all 8 assignments are the same.

    
        

            
                
Demonstrate creativity and problem-solving skills.

                
Analyze web programs in order to test, debug, and improve them. 

                
Evaluate web pages and web programs to ensure that they use proper coding conventions and documentation.

                
Create web pages and web programs that use: HTML5, cascading style sheets, dynamic HTML, JavaScript, forms with controls, and Canvas.

            
        

    
    
Project Topic

    
IMPORTANT! 

    

    
Use the same web site topic that was assigned in unit 1.

    
  

    
 [link: #top] Top

    
    
 [link: #top] 

    

    

        

            
Before You Get Started  

        

    

    
 

    
Format a Web Page with Style Rules

    
IMPORTANT! Simple Style Rules Refresher

    
The goal of this week is to layout the web page using HTML 5 elements and implement CSS style rules. The head section contains the meta data, title, embedded style rules and links to external files that contain style rules. Notice that the style rules can be located in the external CSS file or the embedded style tags.

    
IMPORTANT! Customize the homework page!

    
The textbook and Unit 2: Lesson has examples and information that you should read before you start the homework! Simple selectors select elements and style them based on the HTML element's name (such as h2) or the id and class attributes. We call these 'selectors'. There are other selectors, but we'll focus on just three this week. 

    
HTML Element, ID and Class Selectors

    
Here are some examples using html, id, and class selectors. Notice the 'property' in the style rule is the same and can have different values,  [link: https://www.w3schools.com/css/] W3Schools.com. has excellent tutorials and documentation to refer to in addition to the examples in the textbook and lesson. You'll notice in the homework you need to create a variety of style rules, with a  [link: https://www.w3schools.com/cssref/default.asp] variety of properties

    h2 {   
     color: #FF0000;    /* colors all h2 elements red */
} 
#green  {
     color: #00FF00;    /* colors only one element green */
}
.blue {
     color: #0000FF;    /* colors any element with the class set to blue */
}
    
Here is a refresher of how these style rules are identified in the HTML element. 

    <h2>Red Text</h2>
<p id="green">Green text</p>
<p class="blue">Blue text</p>
    
The Class Attribute

    
Note that the body of the page contains your content. The class attribute is used to identify the class which is defined either in the embedded style rules (in the style tags) or in the external style sheet file (the CSS file). You can see that the title and opportunity classes will only apply to span tags. They have no effect on other html element.  Notice the descriptive names of the classes in the style rule. In your homework project you must not use these names. Come up with your own class names that pertain to your homework web site!

    
Embedded Style Sheets 

    
If the style rules only apply to this page, then they belong in the style tags located in the head section of the web page. The embedded style rules will only apply to that page. 

    <style>
  h2 { 
      color: #FF0000; /* colors all h2 elements red */
  }
</style>
    
External Style Sheets and the Link Element  

    
If the style rules are going to be used for the entire web site, or more than one page, then they belong in the external CSS file. The external CSS file contains style rules that can also be applied to other pages. So you need a link to the style sheets on every web page in the site. 

    
Make sure to modify the link tag to reflect the correct path to the CSS file. 

    <link rel="stylesheet" href="[path]/[style sheet name]">
    
Practice Case Study Web Site

    
Note that in practice case study, the author puts the css files and the js files, (javascript files) in the same folder named library. Your book called this CSS file  lawrenceMicrogrid.css or Microgrid.css. Be consistent across the entire site. Make sure the style sheet is located in the css folder! DO NOT USE THE PRACTICE CSS FILES IN YOUR HOMEWORK PROJECT!

    <link rel="stylesheet" href="../library/Microgrid.css">
    
Homework Web Site

    
You are to reuse your CSS file, throughout your entire homework web site!

    
Notice how the relative path is identified as ../css because your web pages are located in the pages folder. So ../css/ is the relative path to the pages folder. Never use the absolute path. (/css/homework.css or css/homework or file://user/mydocuments/project/css/homework.css)

    <link rel="stylesheet" href="../css/homework.css">
    
 [link: #top] Top

    
    

    

        

            
Review - NOT GRADED

        

    

    
 

    

        

            
Review Chapter 3   (Case Study 3.22)

        

    

    

Case Study Description:

    
This section adds another web page to our case study/practice website. Complete Case Study 3-22 which is a Description of a Small City’s Core Area. This page describes the core area of Lawrence, Kansas: (1) downtown Lawrence; (2) East Lawrence, an old residential and industrial area east of downtown; (3) Old West Lawrence, an old residential area west of downtown; and (4) the University of Kansas (KU), a large university southwest of Old West Lawrence.  This page uses basic HTML elements as well as embedded style sheet rules.  

    
Refer to the chapter readings to see previews of the Microgrid web pages in the browser, as well as the source code. The textbook walks you through the purpose of each line of the program 

    
IMPORTANT

    

    
The link tag and style tags allow you to insert style rules to customize the web page. There is an error in chapter 3. The book refers to the lawrenceMicrogrid.css style sheet. This should be named Microgrid.css. 

    

        

            
 

            

                

                    
Review Chapter 4   (Case Study 4.12)

                

            

        

    

    

Case Study Description:

    
This section adds another web page to our case study website. Complete Case Study 4-12 which is a Microgrid Possibilities in a Small City. This web page illustrates local navigation, ordered and unordered lists, an aside box, and a footnote as well as external linked and embedded style sheet rules. 

    
 [link: #top] Top

    
    

    

        

            
Homework - GRADED

        

    

    
 

    

        

            
Create the Homework Page - Homework3.html

        

    

    

Complete the assignment below.  Use ONLY EMBEDDED CSS style rules!

    
        

            
                
Create your web page
                    
                        

                            
                                
Create homework3.html in the pages folder of your homework project folder. 

                                
Make sure to include the title and meta tags as described in the skeleton code in homework 1.

                            
                        

                    
                

                
Add your text content about your web page. 

                    
                        

                            
                                
Remember you need a FULL page of content.

                                
To give you an example, at minimum, you need the same amount of content that is in the case study. 

                            
                        

                    
                

                
Format the content with a variety of HTML elements and attributes. 

                    
                        

                            
                                
You must use a variety of elements and attributes from the lesson and lecture and case study!! 

                                
Use the practice case study as an example of how to implement different types of html elements.

                            
                        

                    
                

                
Document the content and HTML code.  

                    
                        

                            
                                
You must document your html code with comments. 

                                
Comments should be used to help organize your code and program logic. 

                                
<!--  Format for an HTML comment  -->

                            
                        

                    
                

                
Format the content with style rules in the EMBEDDED style sheet.

                    
                        

                            
                                
Do not just re-use the style rules from the example case study or you lose all points!

                                
Do not use the same style rules for these selectors! You have to use different properties.
                                    
                                        

                                            
                                                
If you used font-size on a style rule it doesn't count for points on the other style rules. 

                                            
                                        

                                    
                                

                                
Configure at least two (2) element selectors in the embedded style sheet
                                    
                                        

                                            
                                                
Each selector needs at least 3 style rules. (ie. font style, border-width, color, text-decoration, margin, padding) 

                                            
                                        

                                    
                                

                                
Configure at least two (2) class selectors in the embedded style sheet 
                                    
                                        

                                            
                                                
Each selector needs at least 3 different style rules. 

                                            
                                        

                                    
                                

                                
Configure at least two (2) id selectors in the embedded style sheet 
                                    
                                        

                                            
                                                
Each selector needs at least 3 different style rules. 

                                            
                                        

                                    
                                

                            
                        

                    
                

                
Document the CSS style rules with comments
                    
                        

                            
                                
/*  Format for the CSS comments */

                                
Organize the CSS comments. 

                                
Group and comment the html element selectors, id selectors and class selectors. 

                            
                        

                    
                

                
Remember that creativity and originality counts.

                
Save your changes to your files.

                
Preview your web page in the browser. 

                
Validate your page code using validator.w3.org. 

                
Follow the directions at the bottom of the page for submitting your work.

            
        

    
    
 [link: #top] Top

    

        

            
Create the Homework Page - Homework4.html

        

    

    

Complete the assignment below.  Use ONLY EXTERNAL CSS style rules!

    
        
Create your web page
            
                

                    
                        
Create homework4.html in the pages folder of your homework project folder. 

                        
Make sure to include the title and meta tags as described in the skeleton code in homework 1.

                    
                

            
        

        

            
External CSS Links 

            
                
Add the link to the external style sheet in every homework page you create.

                
Note the path is relative! If this does not work for you, then, you need to check your folder structure and file names!

                
This should be included in the skeleton page code of every other web page that you create in this web site. 

<link rel="stylesheet" href="../css/homework.css">

            
        

        

            
 

            Add your text content about your web page. 

            
                

                    
                        
Remember you need a FULL page of content.

                        
To give you an example, at minimum, you need the same amount of content that is in the case study. 

                    
                

            
        

        
Format the content with a variety of HTML elements and attributes. 

            
                

                    
                        
You must use a variety of elements and attributes from the lesson and lecture and case study!! 

                        
Use the practice case study as an example of how to implement different types of html elements.

                    
                

            
        

        
Document the content and HTML code.  

            
                

                    
                        
You must document your html code with comments. 

                        
Comments should be used to help organize your code and program logic. 

                        
<!--  Format for an HTML comment  -->
 

                    
                

            
        

        
Create an external  style sheet and save it as homework.css in the css folder. 

        
Copy all the embedded style rules and paste them in the external style sheet. 

        
Then delete all the embedded style rules. There should be NO embedded style sheet in this page!

        
Document your web site color scheme.
            
                

                    
                        
Keep track of your web site color scheme in a central location. 

                        
At the top of the CSS file, list all the colors used in your site in the hexadecimal values. 

                        
Use css comments to document the colors. 

                        
(Note: Advanced students may use variables if you read about them on W3Schools). 

                    
                

            
        

        
Format the content with style rules in the external style sheet.
Add NEW style rules:

            
                

                    
                        
Configure at least two (2) element selectors in the external style sheet
                            
                                

                                    
                                        
Each selector needs at least 3 style rules. (ie. font style, border-width, color, text-decoration, margin, padding)

                                    
                                

                            
                        

                        
Configure at least two (2) class selectors in the external style sheet 
                            
                                

                                    
                                        
Each selector needs at least 3 style rules. 

                                    
                                

                            
                        

                        
Configure at least two (2) id selectors in the external style sheet 
                            
                                

                                    
                                        
Each selector needs at least 3 style rules. 

                                    
                                

                            
                        

                    
                

            
        

        
Format the content with style rules from your external style sheet (homework.css)
            
                

                    
                        
You may add additional style rules as needed to enhance the web site. 

                    
                

            
        

        
Document the external CSS style rules with comments
            
                

                    
                        
/*  Format for the CSS comments */

                        
Organize the CSS comments. 

                        
Group and comment the html element selectors, id selectors and class selectors. For example, you can comment which style rules are for html elements, classes, ids (page specific). 

                    
                

            
        

        
Remember that creativity and originality counts.

        
Save your changes to your files.

        
Preview your web page in the browser. 

        
Validate your page code using  [link: http://validator.w3.org/] validator.w3.org. 

        
Follow the directions at the bottom of the page for submitting your work.

    
    
 [link: #top] Top

    
    

    

        

            
Submit the Assignment

        

    

    

Submit evidence of completion of the requirements.  Make sure to review the General Homework Requirements and document and submit your project using the directions provided on the page. Failure to submit the assignments according to these directions may result in a loss of points! Be consistent! The names of the chapter and homework pages and other files and folders in this project should be lower case. 

    
IMPORTANT! 

    

    
Also refer to the notes on the submission in Homework 1 as well as any instructions in the Course Announcements. 

    
 

    
Here is a brief reminder about the homework.  

    
        

            
                
Validate every web page code:
                    
                        

                            
                                
Copy the entire page of code. 

                                
Go to  [link: http://validator.w3.org/] validator.w3.org.  

                            
                        

                    
                

                
You will submit ONE (1) Word document, for the entire statement.

                
SCREEN SHOTS
                    
                        

                            
                                
The Word document will contain a screen shot of both web pages in the browser into the Word document.

                                
Put the screen shots at the first page. 

                            
                        

                    
                

                
SOURCE CODE - Both html files
                    
                        

                            
                                
Put a heading above the code, named homework#.html

                                
Just select everything in the code file, copy it and paste it into Word.

                                
Start each code file on a new page in the Word document, so that it's easy to locate!

                            
                        

                    
                

                
SOURCE CODE - External CSS file
                    
                        

                            
                                
The word document will contain a copy of the code from each of the homework.css file.

                                
Start each code file on a new page in the Word document, so that it's easy to locate!

                                
Put a heading above the code, named homework.css

                                
Just select everything in the code file, copy it and paste it into Word.

                            
                        

                    
                

                
Save the Word document as Week2.docx and upload it here in the classroom on this assignment page. 

                    
                        

                            
                                
Only Word documents (.docx and .pdf) files are accepted. 

                            
                        

                    
                

            
        

    
    
 [link: #top] Top

---

## My Submission

**Score:** 60.0/60.0
**Grade:** 60
**Submitted:** 2023-08-28T00:12:02Z

### Submitted Files

- **Week2.docx**
  - Downloaded: `files/Week2.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-09-02T15:32:15Z):

> Bert

Good work this week! Good documentation in the css. 

Please review the rubric as that's what I use to guide my grading. 

If you have any questions please contact me in my Inbox.
