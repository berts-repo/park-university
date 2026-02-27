# Unit 8: Homework

**Due:** 2023-10-09T04:59:00Z
**Points Possible:** 60.0
**Submission Types:** online_upload

## Instructions

Unit 8: Homework 

        

    

    
Writing Web Programs with JavaScript

    
        
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

    
    

    

        

            
Practice - NOT GRADED

        

    

    
 

    

        

            
Review Chapter 12  (12.12)

        

    

    
 

    
The Canvas Object

    
Case Study Description:

    
The math calculations and some of the code in this program can be overwhelming to beginners. However, this is helpful to show the capability of the canvas object. Your homework is not to replicate this assignment! Make sure to review the directions carefully!

    
This section creates the chapter12.html Case Study 12.12 Solar Shadowing Dynamics page.In this chapter’s case study, we use a canvas drawing area to show a bird’s-eye view of two parallel arrays of photovoltaic solar collectors and the shadows they cast. If the arrays of collectors are close together and steeply sloped, the array closest to the sun may partially shade the array behind it. Because individual cells within a panel are wired in series to maximize that panel’s output voltage, and because shadowing increases series resistance, even a little shadowing substantially reduces a shaded panel’s electrical output. 

    
Figure 12.21 shows a typical presentation of this web page. When first displayed, input boxes for Latitude, Base Spacing / Panel Height, Clearance (between the lower ends of panels and the roof below) / Panel Height, Panel Slope, Month, and Hour are filled with default values. The rectangular canvas below the inputs displays a plain light-gray background, representing a light-colored flat rooftop. The user can modify any of the default inputs. The display in Figure 12.21 assumes the user changes the Base Spacing / Panel Height input from the default 1.8 to 1.4. 

    
Don't get caught up on the math in the textbook example. It's very easy to get caught up in the formulas and math. We are not looking for a replication of the math. You do not and should not just replicate their example. That is not the point.  

    
 [link: #top] Top

    
    

    

        

            
Homework - GRADED

        

    

    
 

    

        

            
Create homework12.html 

        

    

    
 

    
The Canvas Object

    
Case Study Description:

    
The goal of this project is to learn how to use JavaScript to build an interactive program using the Canvas element. You will not only insert the canvas element but you will also create a form, retrieve the form values with JavaScript and then interact with the content and drawing tools within the Canvas object.  

    
Break this into pieces. Try one step at a time! Always test that you can pass and return values from a function before coding inside the function!

    
 [link: #top] Top

    
    

        

            
Create the Form

        

    

    

Complete the assignment below.   

    
        

            
                

                    
                        
Create your web page, homework12.html as previously described in the other assignments.

                        
Add your text content about your web page as previously described in the other assignments.

                        
Format the content with a variety of HTML form elements and attributes as previously described in the other assignments. 

                        
Create a form in the web page. 

                        
Organize the form fields using:  labels that are the same width. 

                        
Add at least 4 form fields. 

                            
                                
Textbox - which is used to allow the user to input a message in the canvas

                                
Date Picker - to display the date in the canvas

                                
Color Picker - to change the color of the object you are drawing in the canvas. 

                                
Dropdown list - used to choose an image to be displayed in the canvas. The images must be in your images folder. The image must be small, such as 100 * 100, so that it does not take away from the rest of the canvas! (You need room for the message and drawing!) You can make the image smaller! The image should be used to display a small image or logo. 

                            
                        

                        
You need one button to submit and process the form.

                        
You need one button to clear the entire canvas and reset it back to the default settings. 

                        
Make sure to configure the attributes with the HTML form controls as you did last week.

                        
Format the content with CSS style rules as previously described in the other assignments.  

                        
Document the content and HTML code and form, per the class best practices as previously described in the other assignments.

                    
                

            
        

    
    
 [link: #top] Top

    
    

        

            
Create the Canvas

        

    

    
 

    
        

            
                

                    
                        
Create the external JS file called homework12.js. Store the file in the JS folder!
                            
                                

                                    
                                        
Link the external JS file to your web page. 

                                        
In the head section of the page, insert the code to link to an external JavaScript file. 

<script src="../js/homework.js"></script>

                                    
                                

                            
                        

                        
Remember to use the prefix ch12_ before any function name that you use in the page to keep your function calls from overlapping your other web pages!

                        
Process the form using JavaScript. Don't just re-use the elements and code from the example.    
                            
                                

                                    
                                        

                                            
Show the form data results to the user in an alert() dialogue window. This is also useful for debugging. Make sure the information is nicely formatted! 

                                        

                                        

                                            
When the use clicks the submit button, you will add content to the canvas element. You must use the data from the form. You can use the onclick( ) to call the main function, or event listeners. 

                                        

                                        

                                            
Insert the text message into the canvas. The message should be centered in the canvas.

                                        

                                        

                                            
Insert the date into the canvas below the message.

                                        

                                        
Create a drawing of a lamp in the canvas. 
                                            
                                                

                                                    
                                                        
Place the lamp below the image.  

                                                        
Color the lamp (or the lampshade or lamp base) based on the color passed from the form. 

                                                    
                                                

                                            
                                        

                                        
Insert the image into the canvas below the message.
                                            
                                                

                                                    
                                                        
The image should be centered in the canvas.

                                                    
                                                

                                            
                                        

                                        

                                            
When the user clicks on the reset button:

                                            
                                                

                                                    
                                                        

                                                            
Make sure to allow the user to clear the canvas when clicking on the reset button.

                                                        

                                                        

                                                            
Likewise, when the user clicks the reset button you want the user to be able to reset the form, which includes clearing out the canvas.

                                                        

                                                    
                                                

                                            
                                        

                                        

                                            
Creativity is part of the rubric. You can customize the canvas in many ways. Changing the text values, colors, images, moving objects and changing properties are examples of what you can do with the Canvas object. However, it's only required to do the steps above. Have fun! 

                                        

                                        
Thoroughly document all JavaScript!

                                    
                                

                            
                        

                        
Thoroughly document all JavaScript.

                        
Document what each of the functions and statements do in the program!

                        
Remember that creativity and originality counts.

                        
Save your changes to your files.

                        
Preview your web page in the browser.

                        
Validate your page code using  [link: http://validator.w3.org/] validator.w3.org 

                        
Follow the directions at the bottom of the page for submitting your work.  

                    
                

            
        

    
    
 [link: #top] Top

    
    

    

        

            
Submit the Assignment

        

    

    

Submit evidence of completion of the requirements.  Make sure to review the General Homework Requirements and document and submit your project using the directions provided on the page. Failure to submit the assignments according to these directions may result in a loss of points!  

    
IMPORTANT!

    
This week there is at least one or two more screen shot you need to add to the homework. 

    
        

            
                

                    
                        
Make sure to 'show' the JavaScript worked. We need to see the before and after screen shots! In other words, show the alert( ) message and then the canvas with your information showing. 

                        
Make sure to include your JavaScript code in the Word document!

                    
                

            
        

    
    
IMPORTANT! 

    

    
Also refer to the notes on the submission in Homework 1 as well as any instructions in the Course Announcements. 

    
 

    
Here is a brief reminder about the homework.  

    
        

            
                

                    
                        
Validate every web page code as previously described in the other assignments. 

                        
You will submit ONE (1) Word document, for the entire statement as previously described in the other assignments.

                        
SCREEN SHOTS as previously described in the other assignments.

                            
                                

                                    
                                        

                                            
Show the web page before you click on the submit button. 

                                        

                                        
Show the web page after you click on the submit button to show your code worked!

                                    
                                

                            
                        

                        
SOURCE CODE - homework12.html  files as previously described in the other assignments. 

                        
SOURCE CODE - External CSS file as previously described in the other assignments: homework.css.

                        
SOURCE CODE - External JS file as previously described in the other assignments: homework.js.

                        
Save the Word document as Week8.docx and upload it here in the classroom on this assignment page.

                    
                

            
        

    
    
 [link: #top] Top

    
    

    

        

            
Canvas Resources

        

    

    
Just some interesting points about Canvas. The main thing to remember is canvas allows you to do things we can't do in a normal web page such as draw and use the coordinate system. We used a coordinate system on web pages until about 2007, when I had to change from absolute positioning to relative. We can use absolute positioning in web pages, however, they don't work well across multiple devices, browsers, and resolutions of displays. So we use relative positioning. But this might be a fun thing to read! So I thought I'd share them!

    
Fun Demonstrations

    
Sometimes I will create the code in a vector drawing program and then copy the code from the SVG file to the canvas element. But those are for more complex drawing. Take a look at this one. It's at the level of an XBox game and this was a few years ago! This my favorite to show in class! This site also has some useful animation examples. It's what I use when I teach canvas. I don't expect anyone to have advance canvas animations but it's fun to just make something slide across the screen!

    
 [link: http://www.effectgames.com/demos/canvascycle/] http://www.effectgames.com/demos/canvascycle/ Links to an external site.

    
As you can see you are able to retrieve the height and width of the canvas dynamically as shown in your example. This can also be handy to 'clear' the canvas. However, always be careful as 'where' you create the context matters. If you have multiple functions, you might not be referring to the same context! (Similar to how the 'this' keyword works). 

    ctx2.clearRect(0, 0, canvas2.width, canvas2.height)
    
In this code snippet, although you could hard codes the text value you could use a variable as shown below. This gives you much more flexibility in your programming and you can more easily make changes on the fly.

    var message; 
message = "Bullseye";
ctx.fillText(message, canvas.width / 2, canvas.height / 2);
ctx.fillText("Bullseye", canvas.width / 2, canvas.height / 2);
    
Applying what you learned - Demonstration

    
In the extra credit, I show you a common game that someone else developed, that can be modified for that assignment. But you can read about other techniques. The key is that your homework should be your own. But you can see how the tools work together in some of these examples. 

    
        

            
                

                    
                        
 [link: https://canvasjs.com/html5-javascript-bar-chart/] CanvasJS. JavaScript Bar Charts & Graphs

                        
CanvasJS.  [link: https://canvasjs.com/docs/charts/basics-of-creating-html5-chart/] QuickStart: Your First Chart in under 5 minutes

                        
Negoita, John. (May 2017).  [link: https://code.tutsplus.com/tutorials/how-to-draw-bar-charts-using-javascript-and-html5-canvas--cms-28561] How to Draw Bar Charts Using JavaScript and HTML5 Canvas

                    
                

            
        

    
    
In some programs if you go off canvas, your content might disappear. So keeping the content in the center, and on the canvas is helpful. There are some excellent examples of rotation on the web. I prefer  [link: https://www.html5canvastutorials.com/advanced/html5-canvas-transform-rotate-tutorial/] HTML 5 Canvas Rotation Tutorials. Links to an external site.

    
Tutorials

    
These are the best canvas tutorials for beginners. 

    
        

            
                

                    
                        
 [link: http://www.w3schools.com/tags/ref_canvas.asp] HTML Canvas Links to an external site.

                        
HTML 5 Canvas Tutorials
                            
                                
 [link: http://www.html5canvastutorials.com/] Canvas HTML Links to an external site.

                                
 [link: http://www.html5canvastutorials.com/tutorials/html5-canvas-element/] Tutorials Links to an external site. 

                            
                        

                        
 [link: http://www.html5canvastutorials.com/tutorials/html5-canvas-element/]  Links to an external site. [link: http://diveintohtml5.info/canvas.html] Dive Into HTML Links to an external site. (Free!)  –  [link: http://diveintohtml5.info/table-of-contents.html] Table of Contents Links to an external site.

                        
 [link: http://www.brighthub.com/internet/web-development/articles/38744.aspx] Drawing an Image to the Canvas with JavaScript Links to an external site. 

                        
Mozilla
                            
                                
 [link: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations] Basic Animations Links to an external site.

                                
 [link: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API] Canvas API Links to an external site. 

                                
 [link: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Basic_animations] Animating the Solar System and Animated Clock Links to an external site.

                                
 [link: https://developer.mozilla.org/en-US/docs/Web/API/ImageData] Image Data Links to an external site. (Pixel Manipulation) 

                            
                        

                        
Dev.Opera.com
                            
                                
HTML 5 Canvas –  [link: https://dev.opera.com/articles/html5-canvas-basics/] The Basics Links to an external site. –  with  [link: https://dev.opera.com/articles/html5-canvas-basics/#pixelbasedmanipulation] pixel-based manipulation Links to an external site.  [link: https://dev.opera.com/articles/html5-canvas-basics/%23pixelbasedmanipulation]  Links to an external site.

                                
Creating an [link: https://dev.opera.com/articles/html5-canvas-painting/] HTML5 Canvas Painting Application Links to an external site.–  [link: https://dev.opera.com/articles/html5-canvas-painting/]  Links to an external site. and  [link: https://dev.opera.com/articles/html5-canvas-painting/example-5.html] painting demo Links to an external site. and just drawing with a  [link: https://dev.opera.com/articles/html5-canvas-painting/example-2.html] pencil demo Links to an external site. 

                            
                        

                    
                

            
        

    
    
More Examples

    
MSDN

    
        

            
                

                    
                        
 [link: https://msdn.microsoft.com/en-us/library/gg589490(v=vs.85).aspx] How to Use Canvas to Create a Space Game Links to an external site. 

                        
 [link: https://msdn.microsoft.com/en-us/library/gg589504(v=vs.85).aspx] How to Create Canvas Special Effects Links to an external site. 

                        
 [link: https://msdn.microsoft.com/en-us/library/jj635757(v=vs.85).aspx] How to Map Points Between 2D Coordinate Systems Links to an external site. 

                        
 [link: http:// https://msdn.microsoft.com/en-us/library/hh535759(v=vs.85).aspx] How to Create 3D Graphics Using Canvas Links to an external site.

                    
                

            
        

    
    
 [link: https://www.benjoffe.com/code] Ben Joffe Demos Links to an external site.  

    
        

            
                

                    
                        
 [link: https://www.benjoffe.com/code/demos/canvascape] CanvasScape 3D Walker Links to an external site. game 

                        
 [link: https://www.benjoffe.com/code/demos/canvascape/textures] Texture Version Links to an external site. (Very cool) 

                        
 [link: https://www.benjoffe.com/code/games/ninjamaze] Ninja Maze Links to an external site. 

                        
 [link: https://www.craftyball.com/] Crafty Ball Links to an external site. 

                    
                

            
        

    
    
 [link: https://davidwalsh.name/canvas-demos] Mind-blowing Canvas Demos Links to an external site. 

    
        

            
                

                    
                        
The  [link: http://github.com/suffick/Tearable-Cloth] Tearable Cloth Links to an external site. is terrific 

                        
 [link: https://www.freeriderhd.com/t/1016-layers] Free-Rider Links to an external site.is a fun game too 

                    
                

            
        

    
    
Other examples for fun

    
        

            
                

                    
                        
 [link: http://thecodeplayer.com/walkthrough/create-binary-trees-using-javascript-and-html5-canvas?s=rlt] Creating Binary Trees Links to an external site.

                    
                

            
        

    
    
        

            
                

                    
                        
 [link: http://fabricjs.com/] js Fabrics Links to an external site.

                        
 [link: http://www.blobsallad.se/] Interactive Blob Links to an external site.

                        
SitePoint –  [link: https://www.sitepoint.com/basic-animation-with-canvas-and-javascript/]  Links to an external site. with  [link: https://www.sitepoint.com/basic-animation-with-canvas-and-javascript/] Creating a Bouncing Ball Application Links to an external site.

                        
 [link: http://www.tutorialspoint.com/html5/canvas_animation.htm] Tutorials Point Rotates a small image repeatedly Links to an external site.

                        
 [link: http://javascript.info/tutorial/animation] JavaScript Tutorial Links to an external site.

                        
 [link: http://www.williammalone.com/articles/create-html5-canvas-javascript-sprite-animation/] Create A Sprite Animation With Html5 Canvas And JavaScript Links to an external site.

                        
 [link: http://jsfiddle.net/bDQ6b/2/] Fiddle Links to an external site.   

                        
 [link: http://stackoverflow.com/questions/9791904/animating-images-in-html5-and-canvas] StackOverflow animating images Links to an external site.
 [link: http://codetutorial.com/examples-canvas/canvas-examples-moving-along-the-line]  Links to an external site.

                        
 [link: http://codepen.io/ara_node/pen/EwfpL] Motion Graphic Typeface Links to an external site.

                        
 [link: http://code.tutsplus.com/articles/21-ridiculously-impressive-html5-canvas-experiments–net-14210 ] 21 Ridiculously Impressive HTML 5 Experiments Links to an external site. 

                        
 [link: http://cssdeck.com/labs/cool-canvas-particles-text-effect] Cool Text Particle Effects Links to an external site.

                    
                

            
        

    
    
 [link: #top] Top

---

## My Submission

**Score:** 60.0/60.0
**Grade:** 60

### Instructor Feedback

**[INSTRUCTOR]** (2023-10-10T02:28:53Z):

> Bert

You informed me that you were out sick in the hospital this week. 

If you have any questions please contact me in my inbox

**[INSTRUCTOR]** (2023-10-13T21:45:09Z):

> Bert

I have uploaded the file you submitted in the inbox 

Clever example of integrating shapes and an image in Canvas. 
Good documentation throughout. 

If you have any questions please contact me in my inbox
