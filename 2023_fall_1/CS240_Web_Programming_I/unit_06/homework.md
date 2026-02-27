# Unit 6: Homework

**Due:** 2023-09-25T04:59:00Z
**Points Possible:** 60.0
**Submission Types:** online_upload

## Instructions

Unit 6: Homework 

        

    

    
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

    
    
 [link: #top] 

    

    

        

            
Before You Get Started : 

        

    

    
 

    

        

            
 Validate and Process a Form (Notes)

        

    

    
 

    
Just a reminder. You will be creating another form this week, but you will focus on validating the form data, creating functions and passing parameters to functions. You will also see how you can use functions to organize your code. The examples in the book have more advanced calculations than you need in the homework! This will also be a week where you will likely spend time debugging your code. It's much better to document your code, and what you are going to code, at the start of the project. That way you can slowly add your code and test it at each step. 

    
 [link: #top] 

    
 [link: #top] Top 

    
 [link: #top] 

    
    
 [link: #top] 

    

    
 [link: #top] 

    

        

            
Review - NOT GRADED

        

    

    
 [link: #top] 

    
 

    
 [link: #top] 

    

        

            

                

                    
Review Chapter 10 (10.17) 

                

            

        

    

    
 [link: #top] 

    

    
Process the Collector Performance Form - PART 2

    
This example outputs the values in the table which is why I continue to include this in the readings. However it is more complex than the last activity. Please note this is a review of the activity. It is not going to be the same thing as the homework activity. Please read the homework activity directions carefully!

    
Case Study Description: 

    
 [link: #top] 

    
The Case Study  of the chapter 9 and 10 page is about solar panels and energy and contains multiple formulas that might not be something you are interested in.  This is a 2-part activity that covers the case study in chapter 9 & 10.

    
Chapter 9 introduced the subject of solar collector performance by providing a calculator that computes noontime electric power generation of a photovoltaic solar panel as a function of latitude, panel slope, rated capacity, and time of year. In the first part you create the form and table. Figure 9.26 in the book shows what the result displays after the user performs calculations for January, March, June, and December. On the top of the page is a form. When the user clicks on the button, the contents displayed in the table will change. In the second part you create the JavaScript program to process the form and display the values in the table. 

    
Chapter 10 modifies the chapter 9 Solar Collector Performance page. You will add functions and pass values, do more calculations, and use the math library. Complete Case Study 10-17. But after reading this chapter, you should now be able to understand the JavaScript in those subordinate functions. The computeAngles function provides examples of using if statements and using members from the Math object—the Math.PI constant and various Math methods. All of the Math methods employed here are based on trigonometric functions used to describe the position of the sun in the sky at various latitudes, times of year, and times of day. The current application focuses on just one time of day—noon. That simplifies things, but only somewhat. We’ll use temporary alert statements to investigate details and confirm assertions about what’s going on.

    
Some of you might wonder why create the practice Solar page since it's not graded? It's imperative to understand how the script works, and the functions work together. You also need to work on debugging. Once you have the code working you can save a copy of the page for backup.  You also have the solutions. So it's something you can easily check as you go along. The book explains each step and provides the code in the figures.  

    
 [link: #top] Top

    
    
 

    

        

            
Homework - GRADED

        

    

    
 

    

        
Create the Form 

    

    
The point of this activity is to show you can do the following tasks:

    
        

            
                
Create the form. 

                
Style the content and the controls on the form using CSS and JavaScript. 

                
Collect data from the form.

                
Do some calculations with the data.

                
Send output to the page with the results from the form. 

                
Use functions and organize your code.  

            
        

    
    
Complete the assignment below.

    
        

            
                

                    
                        
Create your web page, homework10.html as previously described in the other assignments.

                        
Add your text content about your web page as previously described in the other assignments

                        
Add the header/nav, main and footer sections as you did in previous assignments. Remove the content in the main section

                        
Add a heading to the page. 

                        
Add your text content about your web page as previously described in the other assignments.

                        
Copy the form from the previous week. 

                        
You will only need the following form controls below this week. Delete the other fields that are not going to be used.   
                            
                                

                                    
                                        
Input Textbox (1) 

                                        
Email input textbox (1) 

                                        
Password input textbox (1) 

                                        
Date Picker - uses input (1) 

                                        
Color Picker - uses input (1) 

                                        
Dropdown list - uses input - Add 3 items in the list (3 items) 

                                        
Checkbox list - uses input - Add 3 items in the list (3 items) 

                                        
Radio button list - uses input - Add 3 items in the list (3 items)

                                        
Submit Button (1)

                                    
                                

                            
                        

                        
Make sure that you have at least one field has a number as a value, so that you can do some calculation. 
Be aware when you create the form, that you will need to have some calculation in your web page. 
Here are some ideas. Your form will vary with your particular project!

                            
                                

                                    
                                        
Total value in your shopping cart
                                            
                                                

                                                    
                                                        
Total ordered * price of the product + total tax

                                                    
                                                

                                            
                                        

                                        
 There are other ways to do this!

                                    
                                

                            
                        

                        
You should already have from the last assignment:
                            
                                

                                    
                                        
configured the attributes with the HTML form controls such as size, maxlength, selected, name, id. 

                                        
configured the HTML validation attributes such as required, read only, pattern and type with some of the elements. 

                                        
styled the form control using CSS. 

                                        
documented the content and HTML code and form, per the class best practices as previously described in the other assignments.

                                        
If you add css styles, provide a comment above the section saying that it's the CSS for week 7. 

                                        
You do not need to use JavaScript to configure the styles in your page this week!
 

                                    
                                

                            
                        

                    
                

            
        

    
    
 [link: #top] Top

    
    
 

    

        
Validate and Process the Form 

    

    
 

    
Overview: The point of this activity is to show you can do the following tasks. The goal is that each time the user submits the form with valid values, a calculation is performed and the output with all the field values are appended as a new row of values in a table in the web page. Process the form controls using JavaScript. 

    
Complete the assignment below.

    
        
You will use at least 3 or more functions in your program. 

            
                

                    
                        
hw10_processForm ( ) function will be called by the form. The function controls the main flow of the program. 

                        
hw10_validateForm ( ) function will verify that all of the form fields have values. If they do, then call the next function. If not, alert the user that they need to complete the form, and which field need to be completed. 

                        
hw10_calc( ) function will perform some basic calculations needed. (see the directions for details). If the calculations are valid, then the hw10_processForm( ) is called. 

                        
hw10_displayResults( ) function will create the table object, and the rows, and add a row of data using the data passed by the form. 

                        
Students may add other functions such as a function to reset the entire form. 

                    
                

            
        

    
    
Complete the assignment below. 

    
        

            
                
You can use the external JS file called homework.js, in the JS folder, as you will be naming your functions using different names.  

                
Link the external JS file to your web page. (TIP: Make sure it's relative "../js/homework10.js")

<script src="../js/homework.js"></script>

                
Create a function called hw10_processForm() to collect the form data. 
                    
                        
Verify that the hw10_processForm() is called when the user clicks the submit button. 

                        

                            

                                
There are two types of buttons that can be used to submit the form. 

                            

                            
                        

                        
Read about  [link: https://www.w3schools.com/js/js_events.asp] events .
                            
                                
<button onclick="hw10_processForm()">Submit Form</button> 

                                
<input type="submit" onclick="hw10_processForm()" value="Submit Form" />

                            
                        

                        
Read about  [link: https://www.w3schools.com/js/js_popup.asp] alert() 
                            
                                
alert("It worked"); 

                            
                        

                        
Call the validateForm() function. 
                            
                                
Read about  [link: https://www.w3schools.com/js/js_function_parameters.asp] Parameters

                                
The form function will need the values from the form!

                            
                        

                        
If the entire form returns true and is valid, call the hw10_calc([pass some value]) function.
                            
                                
 [link: https://www.w3schools.com/js/js_function_parameters.asp] Pass at least one value to the function  (Read about  [link: https://www.w3schools.com/js/js_function_parameters.asp] Parameters)

                            
                        

                        
If the hw10_calc was successful, call the hw10_displayResults( ) function. 

                        
If there is an issue with the display, send an error message to the user. Otherwise end the program. 

                    
                

                
In the hw10_validateForm function, validate the user input. (Read about  [link: https://www.w3schools.com/js/js_validation.asp] validate )
                    
                        
At minimum, make sure each of the values are not null, and not empty strings. 

                        
If the form data is valid, return true to the hw10_processForm() function. 

                        
If the form data is not valid, return false. 

                        
If the validateForm() returns false: 
                            
                                
Send an alert() message to the user. (Read about  [link: https://www.w3schools.com/js/js_popup.asp] alert )

                            
                        

                        
Inform the user that the form is not filled out correctly.

                        
Return the results back to the calling function. 

                    
                

                
In the hw10_calc() function, retrieve the value that was passed.
                    
                        
Show the value that was passed and the results to the user in an alert() dialogue window. 

                        
Do some calculation with the value.

                        
If the calculation was successful display the results in an alert( ) message for testing.

                        
Then, return the results back to the calling function function. 

                        
If there is an error, display the error message and return to the calling function. 

                    
                

                
In the hw10_displayResults() function,
                    
                        
If there is no error, display the results of the form to the user, including the calculated values.
                            
                                

                                    
                                        
Display them in a table. Make sure to follow the directions from the book on how to display values on the page. 

                                        
Use the value from the color picker on the form, to change the background color on the table. 

                                    
                                

                            
                        

                        
Note that each time the user submits the form, the data must be appended to the table so that all values are displayed. 

                        
Return a value to the hw10_processForm( ) function. 

                            
                                
If the validateForm() returns false: 

                                
Send an alert() message to the user indicating the problem. (Read about  [link: https://www.w3schools.com/js/js_popup.asp] alert )

                            
                        

                    
                

                
Thoroughly document all JavaScript. 

                
Remember that creativity and originality counts.

                
Save your changes to your files.

                
Preview your web page in the browser. 

                
Validate your page code using  [link: http://validator.w3.org/] validator.w3.org

                
Follow the directions at the bottom of the page for submitting your work.

            
        

    
    
 [link: #top] Top

    
    

    

        

            
Submit the Assignment

        

    

    

Submit evidence of completion of the requirements.  Make sure to review the General Homework Requirements and document and submit your project using the directions provided on the page. Failure to submit the assignments according to these directions may result in a loss of points!  

    
IMPORTANT! 

    

    
Also refer to the notes on the submission in Homework 1 as well as any instructions in the Course Announcements. 

    
 

    
Here is a brief reminder about the homework.  

    
        

            
                

                    
                        
Validate every web page code as previously described in the other assignments. 

                        
You will submit ONE (1) Word document, for the entire statement as previously described in the other assignments.

                        
SCREEN SHOTS as previously described in the other assignments.
                            
                                
Show the results displayed to the user in a table. You need to show at least 2 rows of data!

                            
                        

                        
SOURCE CODE - homework10.html  files as previously described in the other assignments. 

                        
SOURCE CODE - External CSS file as previously described in the other assignments: homework.css.

                        
SOURCE CODE - External JS file as previously described in the other assignments: homework.js.

                        
Save the Word document as Week6.docx and upload it here in the classroom on this assignment page.

                    
                

            
        

    
    
 [link: #top] Top

---

## My Submission

**Score:** 60.0/60.0
**Grade:** 60
**Submitted:** 2023-09-25T23:09:39Z
**Late:** Yes

### Submitted Files

- **Week6-1.docx**
  - Downloaded: `files/Week6-1.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-10-02T04:13:43Z):

> Bert

Very nice work creating the table and even playing with the colors. 

Please contact me in my inbox if you have any questions.
