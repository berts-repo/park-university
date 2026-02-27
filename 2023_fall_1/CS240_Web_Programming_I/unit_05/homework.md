# Unit 5: Homework

**Due:** 2023-09-18T04:59:00Z
**Points Possible:** 60.0
**Submission Types:** online_upload

## Instructions

Unit 5: Homework

    

    
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

    
 

    
 [link: #top] 

    
 [link: #top] Top

    
 [link: #top] 

    
    
 [link: #top] 

    

        

            
Before You Get Started : 

        

    

    
 [link: #top] 

    
 

    
 [link: #top] 

    

        

            
Create and Process a Form with JavaScript

        

    

    
 [link: #top] 

    
 

    
You have only one chapter to read. However, you will incorporate what you learned last week in chapter 8 with this week chapter 9 readings. The example in the case study is complex, with complex calculations. You do not need that level of complexity in your form processing for the homework assignment. However, you will be creating a form with many different types of form elements, validating the form and displaying the results in the web page in a table and an alert window. 

    
Always start with just one form field. Get that to work first, with your functions. Then go back and add the second form field. If you create the entire form first, you will have a much harder time debugging your code! 

    
For the homework  show the results in the web page and in an alert message. 
You do NOT use a table yet! We will do that next week!!!

    
THOUGHT FOR THE DAY:  How to be Build an Inclusive Web Site

    
Your name is important. It identifies who you are. So make sure to name your homework project folder correctly. In web sites we also have to be respectful and sensitive to our visitors. 

    
Just as we follow netiquette guidelines in discussions, you should build them within your web sites too. Did you know that in the 2010 census, the top 50 surnames makeup 12.6% (37,192,142)  of the population (294,979,229)? When we create our forms and collect user data, always allow users to fill out their last name accurately. Our code can convert spaces to hyphens or underscores. But you should always allow them to insert their legal first and last name. 

    
        

            
                

                    
                        
Comenetz, Joshua.  (October 2016).  [link: https://www2.census.gov/topics/genealogy/2010surnames/surnames.pdf] Frequently Occurring Surnames in the 2010 Census 

                        
Moore Williams, John. (Oct 19, 2016). “Please enter a valid last name”  [link: https://medium.com/@johnamwill/please-enter-a-valid-last-name-c63dd5397a2a] Getting UX right starts with a name 

                    
                

            
        

    
    
 [link: #top] Top

    
    

        

            
Practice - NOT GRADED    

        

    

    
 

    

        

            
WaterBalloons Web Page

        

    

    
Chapter Examples: waterBalloons.html and waterBalloons2.html : Chapter 9 (9.15 and 9.20) 

    
The water balloons page is not the case study, but a useful start at learning about web forms and processing forms with JavaScript. In Chapter 8 you learned a little about JavaScript. Now, you will use JavaScript to process a basic form. It's a simple form that does a basic calculation using JavaScript. It's thoroughly covered in the chapter and will help you learn how to process a basic form.  

    
waterBalloons.html

    
What you will learn:

    
        

            
                

                    
                        

                            
                                

                                    
                                        
Creates a form with two textboxes and a button. 

                                        
Configures the button to call a function when the button is clicked. 

                                        
Creates a function that receives the form object, create variables, and retrieves the values from the form fields (the textboxes) sing the forms.elements collection. 

                                        
Performs a calculation. 

                                        
Outputs the results to the output html element.   

                                    
                                

                            
                        

                    
                

            
        

    
    
Steps

    
        

            
                

                    
                        

                            
                                

                                    
                                        
Read the instructions in 9.15 to create the form and process the results using JavaScript. 

                                        
Create the practice page as per the directions in the textbook. In your editor, insert the code as shown in the figures in the textbook. 

                                        
Follow the instructions in 9.15 to create the form and process the results using JavaScript. 

                                    
                                

                            
                        

                    
                

            
        

    
    
waterBalloons2.html

    
What you will learn:

    
        

            
                

                    
                        

                            
                                

                                    
                                        
Test the form fields to determine if they hold valid values. 

                                        
Create a program to display messages in the browser or an alert window. 

                                    
                                

                            
                        

                    
                

            
        

    
    
Steps 

    
        

            
                

                    
                        

                            
                                

                                    
                                        
Read the instructions in 9.20 to add JavaScript to  improve the input validation and display error messages after the user submits a form with invalid input. After the form is submitted (by clicking a button that executes an onclick event handler), you can use JavaScript to call the form object’s checkValidity method. If it returns false, that means at least one of the form’s control values is invalid, and you can then display an appropriate warning message.

                                        
Create the practice page as per the directions in the textbook. In your editor, insert the code as shown in the figures in the textbook. 

                                        
Follow the instructions in 9.20 to add JavaScript to  improve the input validation and display error messages.

                                    
                                

                            
                        

                    
                

            
        

    
    
Useful code snippets  to check for conditions such as an empty string, invalid value or null value. 

    if ((qty == "") || (diameter == null)) {
    output.value = "Invalid input";
}
else {  // do what you are planning to do
}
    
You can also check the validity for the form. 

    if (form.checkValidity() == false) {
    alert("Invalid input");
} 
    

        

            
Review Chapter 9 (9. 21) 

        

    

    

Remember practice pages are not submitted or graded. They are for your learning!

    
Please note this is a review of the activity. It is not going to be the same thing as the homework activity. Please read the homework activity directions carefully!

    
Chapter Example: areaDescription.html

    
In this example you will dynamically change the area description using JavaScript. In other words, rather than using HTML or CSS to change the figure position, you will change the properties in a script. This is a short script. 

    
Follow the directions in the book. 

    
        

            
                
First, add the code to call the script in the body tag so when the page is opened or the window is resized, the script will run. 

                    
           <body onload="alignFigure()" onresize="alignFigure()"> 

                

                
Then you can add your script to do whatever you want. In this case you retrieve the figure element. Then you can get the size of the window, and resize the figure. Refer to the figure in the readings and solution files for the code. Note that getElementById is an excellent way to retrieve an HTML element from the web page in JavaScript. 

The syntax to set a value of a property is elementName.style.propertyName = "value".

            
        

    
     var figure = document.getElementById("figure");
 figure.style.left = "-40px";
    
   You can consolidate this into one line of code.  [link: https://www.w3schools.com/js/js_htmldom_css.asp] W3Schools  provides examples of how to  [link: https://www.w3schools.com/js/js_htmldom_css.asp] Change HTML styles with JavaScript 

    document.getElementById(id).style.property = new style
    
   Example

    <p id="p2">Hello World!</p>

<script>
    document.getElementById("p2").style.color = "blue";
</script>
    
 

    

        

            
Review Chapter 9 (9.21, Figure 9.26) 

        

    

    
Collector Performance Web Page - PART 1

    
Case Study Description: 

    
Chapter 9 introduced the subject of solar collector performance by providing a calculator that computes noontime electric power generation of a photovoltaic solar panel as a function of latitude, panel slope, rated capacity, and time of year. In the first part you create the form and table. Figure 9.26 in the book shows what the result displays after the user performs calculations for January, March, June, and December. On the top of the page is a form. When the user clicks on the button, the contents displayed in the table will change. In the second part you create the JavaScript program to process the form and display the values in the table. 

    
Chapter 10 modifies the chapter 9 Solar Collector Performance page. You will add functions and pass values, do more calculations, and use the math library. Complete Case Study 10-17. But after reading this chapter, you should now be able to understand the JavaScript in those subordinate functions. The computeAngles function provides examples of using if statements and using members from the Math object—the Math.PI constant and various Math methods. All of the Math methods employed here are based on trigonometric functions used to describe the position of the sun in the sky at various latitudes, times of year, and times of day. The current application focuses on just one time of day—noon. That simplifies things, but only somewhat. We’ll use temporary alert statements to investigate details and confirm assertions about what’s going on.

    
Some of you might wonder why create the practice Solar page since it's not graded? It's imperative to understand how the script works, and the functions work together. You also need to work on debugging. Once you have the code working you can save a copy of the page for backup.  You also have the solutions. So it's something you can easily check as you go along. The book explains each step and provides the code in the figures.  

    
You can do the practice page for learning. However the practice page shows the output in a table. For the homework  show the results in the web page and in an alert message. You do NOT use a table yet! We will do that next week!!! I would much rather see you learn the basics first!

    
Summary

    
This section adds another web page to our case study website and you will update the home page. This is a 2-part activity that covers the case study in chapter 9 & 10. Therefore you will be saving the practice page and then in the chapter you will modify the page using the information from the chapter 10 case study. This chapter’s web page introduces the subject of solar collector performance by providing a calculator that computes noontime electric power generation of a photovoltaic solar panel as a function of latitude, panel slope, rated capacity, and time of year.

    
Figure 9.26 in the book shows what the result displays after the user performs calculations for January, March, June, and December. This works in the southern hemisphere as well as the northern hemisphere. Just negate the latitude, and negate the slope to specify a north-facing panel. 

    
On the left side of the page is a form. When the user clicks on the button, the content on the right will change. In the first part you create the form and table. In the second part you create the embedded JavaScript program to process the form and display the values in the table. 

    
Figure 9-22, 23, 24A and 24B provides the code modifications that you will make to modify the calculations in the computeAngles function. In the case study the top-level JavaScript code made calls to subordinate functions whose details were omitted initially because they employed features not yet described at that point. 

    
Follow the directions in the book for Chapter 9. 

    
Code Snippets - Summarizing some of the tasks in this page.  

    var form;                                             // Create some global variables
var variable1;    

// Inside the function: 
table = document.getElementById("performance");       // Create the table object 
row = table.insertRow(table.rows.length);             // Create the new row object 
form = solarForm;                                     // Create the new form object  
CallFunction1();                                      // Call a function to do calculations
   
row.insertCell(0).innerHTML = form.elements["textbox1"].value;      // Write out values to each table cell
row.insertCell(1).innerHTML = form.elements["textbox2"].value; 
var obj = document.getElementById("mySelect");                      // Get Create the dropdownlist object            
row.insertCell(2).innerHTML = obj.options[obj.selectedIndex].text;  // Write out the value to the cell 
row.insertCell(3).innerHTML = CallFunction2();                      // Write out a value returned by a function
    
 [link: #top] Top

    
    

        

            
Homework - GRADED 

        

    

    
 

    

        

            
Create the homework9.html 

        

    

    
Create and Process a Form with JavaScript  

    
You will create the form as well as process it this week. Therefore, you will only have one HTML file to create. You will continue to use the homework.css file, but you will also add the homework.js file this week in order to validate and process the form data. 

    
Note that you will have an assignment like this on the final exam that you have to write by hand. So please take the time to do this assignment carefully. Your documentation will help you to study what you did, why and how. 

    
The point of this activity is to show you can do the following tasks:

    
        

            
                
Create the form. 

                
Style the content and the controls on the form using CSS and JavaScript. 

                
Collect data from the form.

                
Do some calculations with the data.

                
Send output to the page with the results from the form. (Using an alert( ) and sending it to the actual web page using innerHTML)

                
Use functions, document and organize your code.  

            
        

    
    
 

    

        

            
Create the Form and Use HTML Validation

        

    

    
 

    
Create the Form

    
Complete the assignment below.

    
        

            
                

                    
                        
Create your web page, homework9.html as previously described in the other assignments.

                        
Add your text content about your web page as previously described in the other assignments

                        
Add the header/nav, main and footer sections as you did in previous assignments. Remove the content in the main section

                        
Add a heading to the page. 

                        
Add a short paragraph explaining any directions the user needs to fill out the form. 

                        
Format the content with a variety of HTML form elements and attributes as previously described in the other assignments. 

                        
Create a form.

                        
Organize the form fields using:  fieldset, legend and labels. 

                        
Add a variety of types of form fields to the form, one (1) of each type of form control below.

                        
There are 11 form controls listed.  Failure to add one of the form types will result in a deduction of 2 points on the assignment.  

                        
You may add more than one but at least one of each type of form control. 
                            
                                

                                    
                                        
Input Textbox

                                        
Email input textbox

                                        
Password input textbox

                                        
Hidden input textbox

                                        
Number input textbox 

                                        
Date Picker - uses input

                                        
Color Picker - uses input

                                        
Radio button list - uses input - Add 3 items in the list

                                        
DropDown List - Add 3 items in the list

                                        
TextArea

                                        
Submit Button

                                         
                                    
                                    
                                

                            
                        

                    
                

            
        

    
    
Validate the Form with Attributes and HTML Validation

    
Complete the assignment below.

    
        

            
                

                    
                        
Make sure to configure the attributes with the HTML form controls such as size, maxlength, selected, name, id. 

                        
Make sure to include the HTML validation attributes such as required, read only, pattern and type with some of the elements.  

                        
Document the content and HTML code and form, per the class best practices as previously described in the other assignments.

                        
Format the content with style rules as previously described in the other assignments.

                            
                                

                                    
                                        
Style the page content using CSS. Create original styles, don't just re-use the style rules from the example.

                                        
Only add or edit style rules inside the external CSS file, homework.css.

                                        
Document the 'new' style rules in the external css file, by placing them at the bottom of the CSS file.   

                                            
                                                
Provide a comment above the section saying that it's the CSS for week 5. 

                                            
                                        

                                    
                                

                            
                        

                    
                

            
        

    
    
 [link: #top] Top

    
    
 

    

        

            
Validate and Process the Form

        

    

    
 

    
TIPS:

    
        
Note there are many ways to retrieve the values in the form. It is useful to try out document.getElementById("formID").value first. You can use the forms[] collection but often students have challenges using this. Start with the basics first, make it work and then you can go back and improve the code. 

        
The other tip is to do this slowly. Gather the results from one field, and display that first, before going to add the code for the other fields. That way you can easily find out what issues you might have in the code. Debugging JavaScript is challenging. It's also useful to use alert() to send yourself message when you create and call functions and to find out what is in the variables. Many web sites use the console, in the browser, which is fine. However I find more students learn better by using alert(variablename) and passing the information to the alert method. 

    
    
Complete the assignment below.

    
        

            
                

                    
                        
Style the form controls using JavaScript, which modifies the CSS properties as mentioned above. 

                        
Process the form controls using JavaScript. You may use 1 or more functions in your program. 
                            
                                

                                    
                                        
Create an external JS file called homework.js. Store the file in the JS folder!

                                        
Link the external JS file to your web page. 

<script src="../js/homework.js"></script>

                                        
Create a function called processForm() to process your data.

                                        
Verify that the processForm() is called when the user clicks the submit button. 

                                        
Validate the user input. At minimum, make sure the values are not null, not empty strings. 

                                        
Show the results to the user in an alert dialogue window. 

                                        
Show the results to the user in an HTML control using the innerHTML attribute.  

                                        
Thoroughly document all JavaScript. 

                                    
                                

                            
                        

                        
Format the content with a variety of HTML elements and attributes as previously described in the other assignmentsDocument the content and code per the class best practices as previously described in the other assignments.

                        
Format the content with style rules as previously described in the other assignments.

                        
Remember that creativity and originality counts.

                        
Save your changes to your files.

                        
Preview your web page in the browser. 

                        
Validate your page code using  [link: http://validator.w3.org/] validator.w3.org

                        
Follow the directions at the bottom of the page for submitting your work.

                    
                

            
        

    
    
  [link: #top] Top

    
    

    

        

            
Submit the Assignment

        

    

    

Submit evidence of completion of the requirements.  Make sure to review the General Homework Requirements and document and submit your project using the directions provided on the page. Failure to submit the assignments according to these directions may result in a loss of points!  

    
IMPORTANT!

    
  This week there is at least two (2) screen shots you need to add to the homework. 

    
Failure to follow directions and submit all the required documentation may result in a 0 score. 

    
Make sure to 'show' the JavaScript worked. We need to see the before and after screen shots!  

    
IMPORTANT! 

    

    
Also refer to the notes on the submission in Homework 1 as well as any instructions in the Course Announcements. 

    
 

    
Here is a brief reminder about the homework.  

    
        

            
                

                    
                        
Validate every web page code as previously described in the other assignments. 

                        
You will submit ONE (1) Word document, for the entire statement as previously described in the other assignments.

                        
SCREEN SHOTS as previously described in the other assignments.

                            
                                

                                    
                                        
We need to see the before and after screen shots!

                                        
Provide a screen shot that shows your code validation worked!

                                        
Make sure to 'show' the JavaScript worked with 2 rows of data. 

                                    
                                

                            
                        

                        
SOURCE CODE - Homework9.html  files as previously described in the other assignments. 

                        
SOURCE CODE - External CSS file as previously described in the other assignments: homework.css.

                        
SOURCE CODE - External JS file as previously described in the other assignments: homework.js.

                        
Save the Word document as Week5.docx and upload it here in the classroom on this assignment page.

                    
                

            
        

    
    
 [link: #top] Top

---

## My Submission

**Score:** 60.0/60.0
**Grade:** 60
**Submitted:** 2023-09-25T21:20:13Z
**Late:** Yes

### Submitted Files

- **Week5-1.docx**
  - Downloaded: `files/Week5-1.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-09-24T23:22:58Z):

> Bert

Form looks good!

I see you made the form display a message if it's empty but not display the actual values. You did have validation but no documentation or comments in the JS code. 

Please review the course announcement. 

If you have any questions, please review the rubric, directions and contact me in my inbox.

**[INSTRUCTOR]** (2023-10-02T04:01:01Z):

> Bert 

It looks much better but I don’t know why you resubmitted it. I already graded the assignment. 

Please contact me in my inbox if you have any questions.

**[INSTRUCTOR]** (2023-10-02T04:02:30Z):

> Bert

I regraded the assignment. 

Please contact me in my inbox if you have any questions.
