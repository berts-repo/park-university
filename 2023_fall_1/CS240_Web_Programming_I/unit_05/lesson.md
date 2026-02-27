# Unit 5: Lesson

Writing Web Programs with JavaScript

Rather than provide separate lectures, we are going to ask you to read your textbook. We want you to read your book and take your own notes. Here are some notes we thought were most important or needed additional reinforcement or clarification. 

Chapter 9 Additional JavaScript Basics: window Object, if Statement, Strings, Numbers, and Input Validation [link: #chapter28] 

 [link: #top] Top

Document Object Model Revisited

You've already covered the definition of the DOM. Now let's look inside the DOM at the major objects and methods and how we can use them in the web programs. 

As you learn the DOM elements you should mark them off. Some are more important than others.  The main objects are Document, Location, Navigator, Window, History and Screen. It can be a bit confusing at times. The DOM allows different ways to access some objects. Some objects like Location, can actually be referenced by document.location or window.location or window.document.location! 

You can learn more about the  [link: https://www.w3schools.com/jsref/obj_window.asp] Screen, Navigator, History and Location Objects on the W3Schools site. Just click on the object in the left menu that you want to learn more about. If you are really interested in the details of the DOM read  [link: https://www.w3.org/2003/01/dom2-javadoc/] DOM Version 2 Interactive Class Tree Hierarchy. DOM 3 is not fully supported across all browsers. There are many interactive games that can be created with JavaScript, HTML and CSS such as tic-tac-toe, rock, paper, scissors, card games. 

Often you can find old code that still worked today.  [link: https://msdn.microsoft.com/en-us/ie/ms533044(v=vs.94)] DHTML was first publicized by Microsoft in 1997 with release of the Internet Explorer version 4.0 browser at the World Wide Live developers event. You can still read archived content about DHTML on several Microsoft sites including  [link: https://technet.microsoft.com/en-us/windows/ms533022(v=vs.60)] Introduction to DHTML Behaviors. Check out the old documentation on  [link: https://msdn.microsoft.com/en-us/ie/hh772687(v=vs.94)] Microsoft DHTML web pages and  [link: https://msdn.microsoft.com/en-us/ie/hh772377(v=vs.94)] archived content.  [link: https://msdn.microsoft.com/en-us/ie/ms533044(v=vs.94)] Dynamic menus and flying text and   [link: https://msdn.microsoft.com/en-us/ie/ms533023(v=vs.94)] event handling, filters and transitions wasn't new but was all part of DHTML. 

Location Object

Location provides access to the location object and properties.

The URL is broken into the protocol, host, href, hostname, port and pathname, search and hash. Because the default port is 80 in the browser, you do not enter it. If you change the port number for a web site on the web server the users would have to enter it. You can read and set the values for these properties. If you set them, the web page will refresh in the browser to the new settings.

window.location.href
window.location.protocol
window.location.assign("url-value")

Location.assign will replace and remove the current document and go to the new one.  Location.href and location.assign do the same thing.

Location.reload will reload the current document)

Location.search provides access to the querystring 

Read more about the  [link: https://www.w3schools.com/jsref/obj_location.asp] location object on W3Schools.

Navigator Object

Window.navigator can the Screen object and properties such as availHeight, availWidth, colorDepth and width and height.

message.innerHTML = "User agent: " +window.navigator.usergent
message.innerHTML = "Cookie enabled: " +navigator.cookieEnabled
message.innerHTML = "Platform: " +navigator.platform
message.innerHTML = "Browser name: " +navigator.appName
message.innerHTML = "Browser code name: " +navigator.appCodeName

Screen Object

Window.screen can the Screen object and properties such as availHeight, availWidth, colorDepth and width and height.

window.screen.availWidth
window.screen.availHeight

History Object

Window history returns history object. You can move through the list of pages on the site that the user has visited using back( ) and forward( ) methods.  

Document Object

 [link: #top] 

All of the traditional HTML elements we see in the web page are child elements of the document object.  You can also access metadata about your page.

lastModified returns the document was changed which is helpful for web site maintenance

location provides the URL and domain of the page

referrer which is the page that the user clicked on to get to your page which is useful for web site analysis

title which can retrieve or set the page title (like the title element and used by search engined) 

message.innerHTML = "Last Modified: " + document.lastModified;
message.innerHTML = "Referrer: " + document.referrer;
message.innerHTML = "Title: " + document.title;

 [link: #top] Top

Window Object

Methods

Some window methods are useful.

window.print() prompts the user to print the page

window.close() close the window if allowed

window.atob() Decodes a base-64 encoded string

window.btoa() Encodes a string in base-64

Alert, Prompt, Confirm and ShowModalDialog Methods

There are 3 methods you need to know and will use in your homework and exams. You can pass the literal string, or a variable. 

Alert displays a message and does not return a value.

 Confirm also includes an OK/Cancel button which return a boolean value.

Prompt allows users to enter a value and returns the value as a string.

Examples

window.alert("mystring");
var response1 = window.confirm("mystring?"); 
var response2 = window.prompt("Directions", "Default placeholder");

The showModalDialog(url) is not as common because of the browser compatibility issues, but can be useful. This method shows the url in a popup window and does not return a value.  Hit escape to close the window. 

window.showModalDialog("http://www.mycompany.com"); 

Example

<button onclick="showDialog()">Show the window</button>
<dialog id="myDialog">This is a dialog window</dialog>
<script>
function showDialog() { 
      document.getElementById("myDialog").showModal(); 
} 
</script>

 [link: #top] 

 [link: #top] Top

 [link: #top] 

 [link: #top] 

JavaScript Syntax

In JavaScript you test two objects for and inequality using (==, !=). They may have different data types. JavaScript converts to the same type then compares values. It only compares the values. 

if (firstVal == secondVal)

Use (===, !==) to determine if the data types are the same and if they have the same value. 

if (firstVal === secondVal) 

NULL

One area beginners often forget to test for is null or undefined.  

If you want to differentiate between null and undefined, use the identity operator (===). The identity operator will verify if they are the same data type and have same value. 

Null means that no value is yet assigned or the object does not exist. 

You can determine if a variable is null or not null.

if (name != null) 

Undefined is a bit tricky. Undefined can be returned when the object you are trying to create does not have a definition, or doesn't exist. 

An undefined variable will be regarded as being equal to a null variable. Use the equality operator (==) and JavaScript to convert the type and complete the comparison. 

The program may detect that the property does not exist yet and cannot be used until it is defined. 

 [link: #top] Top

Controlling Program Flow: If-Else

You have already taken a programming language. So we'll just include the syntax here for common methods used to control the flow of a program in JavaScript. 

You can review the conditional expressions and methods on  [link: https://www.w3schools.com/js/js_if_else.asp] W3Schools.

if (condition is true) {
      do this
} else if (condition is true) {
     do this
} else {
       do this
}

 [link: #top] Top

Working with Strings

String Comparison

String comparison operators (<, >, <=, >=, ==, !=) use lexicographical ordering.

Test for Empty Strings

if (name == "") 

String Concatenation

Make sure to . use some pattern so you are not missing ( + ) signs and the spaces at the end of  each line.

var message;
message = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem " + 
"accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab " + 
"illo inventore veritatis et quasi architecto beatae vitae dicta sunt " + 
"explicabo.";

Compound Concatenation Operator

Another alternative. Be careful to make sure to use (+=) starting on the second line.

var message;
message = "Quis autem vel eum iure reprehenderit qui in ea voluptate velit "; 
message += "esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat ";  
message += "quo voluptas nulla pariatur?";

You can use the concat method to concatenate multiple strings together. You can include spaces and use variables and literal strings. 

text1.concat("text1", text2, " " , text3);

Escape Characters

You need to use the ( \ ) character for ( " ), ( ' ), ( \ ) characters. 

message = "'That\'s pretty fast, Jordan.'";
message = "C:\\Users\\John\\Music";

Special Characters (\n \t)

You can use \t for tabs, but it's tricky in terms of the browser output. The \n will work as a new line character. But this only shows up in the source code. If you want a new line in the browser view use the <br /> element. 

var message;
message = "Quis autem vel eum iure reprehenderit qui in ea voluptate velit\n"; 
message += "esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat\n"; 
message += "quo voluptas nulla pariatur?";
var message2;
message2 = "Quis autem vel eum iure reprehenderit qui in ea voluptate velit<br/>"; 
message2 += "esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat<br/>"; 
message2 += "quo voluptas nulla pariatur?";

 [link: #top] Top

String Properties and Methods

There are many string methods available that you might want to try out. W3Schools provides a list of  [link: https://www.w3schools.com/js/js_string_methods.asp] string methods. JavaScript is 0 based so lists and arrays start with 0 for the first index position. If nothing is found (-1) is returned.  

var password = "Mo(2H^*2$6dB&R@0"
var mystring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var myfruit = "apple, orange, apple"

The toUpperCase/toLocaleUpperCase, toLowercase/toLocaleLowerCase methods convert strings to upper and lower case in the user's locale. Unicode values start with 65 for "A", 97 for "a" and 48 for "0".  

mystring.toLowercase;             // returns "abcdefghijklmnopqrstuvwxyz"
mystring.charAt(0);               // returns character at first index position, A
mystring.charCodeAt(0);           // returns  [link: https://en.wikipedia.org/wiki/List_of_Unicode_characters#Latin_script] unicode value at first index position, 65
var mylength = mystring.length;   // returns 26 (starts 0 - 25)

Trim()

Return a string with all whitespace removed from the start and end. Do not change the calling string.

var myfruit = "  apple  "
myfruit.trim                      // returns "apple"

Splitting a String into an Array

myfruit.split(",");       // splits on commas and returns an array
myfruit[0]                // returns 'apple'
myfruit[2]                // returns 'apple' 

Replace ( ) 

Returns a new string. You can use use regular expressions ( /  / ), case insensitive flag ( /i ) to ignore case and global match flags ( /g ) to replace all matches.

mylist.replace("apple", "strawberry");     // Replaces 1st match  // case sensitive
mylist.replace(/apple/i, "strawberry");    // Case sensitive
mylist.replace(/apple/g, "strawberry");    // Replaces all matches globally

Learn more about regular expressions and the replace( ) method at  [link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace] Mozilla’s description of replace. 

Finding a String in a String

Search ( ) 

Searches a string for the value and returns the 1st position of the first letter of the match.

mystring.search("C");          // returns 2

IndexOf

Returns index position of the 1st occurrence of the search string. If nothing is found (-1) is returned. Cannot take use regular expressions. The 2nd parameter as the starting position for the search.

mystring.indexOf("C");          // returns 2, the starting point 
myfruit.indexOf("apple");       // returns 0, the starting point 
myfruit.indexOf("apple", 5);    // returns 15, the starting point 

LastIndexOf

Returns index position of the last occurrence. If nothing is found (-1) is returned. Cannot take use regular expressions. The 2nd parameter as the starting position for the search.

myfruit.indexOf("apple");          // returns 15 
myfruit.indexOf("apple", 5);       // returns 15  

Extracting Part of a String

Slice ( ) extracts a part of a string and returns the extracted part in a new string. Negative positions count starting from the end of the string at 0, but then start with the first character. Omit the second parameter, returns the rest of the string.  

slice(begin-index,  after-end-index)
mystring.slice(2, 6);    // returns "CDEF" // stop at 6, do not return 6!
mystring.slice(-6, -2);  // returns "UVWX" 
mystring.slice(24);      // returns "XYZ"  
mystring.slice(-2);      // returns "XYZ"  

Substring ( ) 

Similar to slice( ), but cannot accept negative indexes. Omit the second parameter, returns the rest of the string.

substring(begin-index, after-end-index)
mystring.substring(2, 6);    // returns "CDEF"

Substr ( ) 

Similar to slice( ). Second parameter specifies the length of the extracted part. Omit the second parameter, returns the rest of the string.

substr(begin-index, length)
mystring.substr(2, 4);    // returns "CDEF"
mystring.substr(24);      // returns "XYZ" 
mystring.substr(-2);      // returns "XYZ" 

 [link: #top] Top

Manipulating Text

You can modify the text of elements directly using methods. Caution! This can include the whitespace characters! 

The wholeText returns the text string while data gets or sets the text and returns a strong.

Length returns the number of characters.

While substringData(offset, count) returns the substring as a string object, the splitText(number) splits the text and returns a Text object. 

While insertData(offset, string) will insert the string at the offset the replaceData(offset, count, string) will replace the region with the string.

ReplaceWholeText replaces all the text and returns a text object.

The appendData adds the string at the end of the text, and deleteData (offset, count) removes the text including the first character in the offset for the specified count of characters).

TIP: You can either, create a new variable so store the firstChild which contains the text, or access it directly as shown below!

<p id="message">ABCDEFGHIJKLMNOPQRSTUVWXYZ</p> 
<pre id="results"></pre>
<script>
     var myResults = document.getElementById("results");
     var myMessage = document.getElementById("message").firstChild; 
     myResults.innerHTML = "The message has " + myMessage.length + " characters\n";
     myMessage.replaceWholeText("abcdefghijklmnopqrstuvwxyz");
</script>

 [link: #top] Top

Working with Numbers 

 [link: https://www.w3schools.com/js/js_arithmetic.asp] Arithmetic Expressions include operators ( + - / * ), increment and decrement operators ( ++, -- ) and the modulus operator (%) which returns the division remainder.The division operator returns the quotient and a remainder. Arithmetic operations follow the same order of operations as in other languages ( ** * / + - ) which can be reorganized using parentheses ( ). The compound assignment operators combines assignment and arithmetic functions ( +=, -=, *=, /=, %=, **= )

Exponents are indicated with ** and executed in order from right to left.  For example, 2**3 = 23

count++;       // count = count + 1;
count--;       // count = count - 1;
count += 10;   // count = count + 10

The modulus can be useful to determine if a value is odd or even.  

if (document.getElementById("myNumber") % 2) == 0)

 [link: #top] Top

Math Library

The  [link: https://www.w3schools.com/jsref/jsref_obj_math.asp] Math constants and methods is well documented on the W3Schools site. 

Math Constants

Math.E         // returns Euler's number
Math.PI        // returns PI3.141592653589793
Math.SQRT2     // returns the square root of 2
Math.SQRT1_2   // returns the square root of 1/2
Math.LN2       // returns the natural logarithm of 2
Math.LN10      // returns the natural logarithm of 10
Math.LOG2E     // returns base 2 logarithm of E
Math.LOG10E    // returns base 10 logarithm of E

Math Built-in Methods 

Example

numQuarters = Math.floor(vendingChange / 25);
numDims = Math.floor(vendingChange / 10);

Examples 

x = 2;
y = 4;
z = 2.5;
Math.abs(x);        // returns absolute positive value of x
Math.round(x)       // returns x rounded to the nearest integer 
Math.sqrt(x)        // returns square root of x:
Math.pow(x, y)      // returns value of base x to the power of y 
x**y                // returns value of base x to the power of y (faster than POW)
Math.ceil(z)        // returns value of x rounded up to its nearest integer:
Math.floor(z)       // returns value of x rounded down to its nearest integer:
Math.min(x, y, z)   // find lowest value in a list. No limit to the number of parameters)
Math.max(x, y, z)   // find highest value in a list 
Math.random()       // returns random number between 0.0 - 1.0 not including 1.0 (exclusive)

Trigonometric functions

Angles, Degrees and Radians

You will use this information in Unit 8 with the Canvas object. You will also use this information in other CS courses. 

Circumference of a circle is given by 

Radius = r

Diameter of a circle is 2r

There are 360 degrees in a circle, but some methods use radians.  

Convert  [link: https://upload.wikimedia.org/wikipedia/commons/9/9a/Degree-Radian_Conversion.svg] degrees to radians: 1 radian is equal to 180/π degrees

0 degrees = 0 rad

57.3 degrees = 1 rad

90 degrees = π/2 rad

180 degrees = π rad

270 degrees = 3π/2 rad

360 degrees = 2π rad

To convert degrees to radians:

Angle in Radians (rad) = Angle in Degrees * π/180

Angle in Degree (deg) = Angle in Radians * 180/π

The hypotenuse is always the longest side of a right-angled triangle across from the 90 degree angle. So there are 2 acute angles and one 90 degree angle. 

Sine is used with right triangles and is a value between -1 and 1. Sine is the ratio of the side opposite one of the acute angles to the hypotenuse. 

Math.sin(x)                      // You need to convert degrees to radians. 
Math.sin(90 * Math.PI/180);      // x = 90 degrees * Math.PI / 180
Math.sin(90 * Math.PI/180);      // returns 1, sine (90 degrees) = 1

Cosine is also a value between -1 and 1. Sine is the ratio of the side adjacent one of the acute angles to the hypotenuse. 

Math.cos(x)                      // x = 0 degrees * Math.PI / 180);
Math.cos(0 * Math.PI/180);       // returns 1, cos (0 degrees) = 1  

TIP: In most methods if there is no answer you will return either -1 or NaN if the value is empty or not a valid number.

 [link: #top] Top

Convert Data Types

 [link: https://www.w3schools.com/js/js_datatypes.asp] Data types are described in the book and W3Schools site. JavaScript has dynamic data types that are not strict and allow various data types to be stored in the same variable at different times.  Explicitly converting data types is the most common error on the final exam because students forget to convert data types on order forms! You have to convert values you receive from a form to a number before you can perform calculations. 

Here are some additional JavaScript constants. These may be important to use if you believe you have an issue with overflow. 

MAX_VALUE              // Largest number possible in JavaScript
MIN_VALUE              // Smallest number possible in JavaScript
NEGATIVE_INFINITY      // Negative infinity (returned on overflow)
POSITIVE_INFINITY      // Infinity (returned on overflow)

Convert Number to String  

Use String or toString to convert the number to a string. It assumes the string is a base 10 number. 

myNumber.toString() 
(5).toString() 
String(5)

Converts String to Number  

The radix is a number from 2 - 36, used to determine if the number system. Set it to 16 for hexadecimal, 8 if octal. If there is no radix, and the string begins with "0x" then it's classified as hexadecimal, otherwise it's base 10 (decimal). The syntax is: 

parseInt(string, radix)

Examples

Number("8.9")           // converts String to a Number (real or integer)
Number("8")             // converts String to a Number (real or integer)
parseInt("9.8")         // converts to integer - 9
parseFloat("8.9")       // converts to real
toFixed(n)              // convert to real number with n digits after decimal point

Examples

balloons = parseInt(prompt("Number of water balloons:", ""));
diameter = parseFloat(prompt("Diameter of each balloon in inches:", ""));

 [link: #top] Top

Water Balloons Textbook Sample 

Review the Water Balloons example in section 9.15 in the book. Note that the form="myform" in the input is useful if you have multiple forms on the page or not form element. Use this activity to review pseudoclasses such as :first-child and :not from the lesson on CSS. 

 [link: #top] Top

Sample Shopping Cart Form and Processing the Data

The example below is similar to the Solar Collector Performance in Case Study. 

In this project you are allowing the user to select products for purchase and rate the products. The page will calculate the subtotal cost as well as the total cost of the shopping cart similar to the Microgrid Solar Collector Performance page.

Create the Files

Create a web page ShoppingCart.html and save it in the Pages folder

Create a JavaScript file named ShoppingCart.js and save it in the JS folder. 

Insert the JS file into your web page at the bottom of the ShoppingCart.html file using the script tag. Note that you no longer need to insert the type="text/javascript" in the script tag. JavaScript is the default type. 

<script src="../js/ShoppingCart.js"></script>

Create the Web Form

Modify the ShoppingCart.html page.  

At the top of the page, above the Bootstrap style sheet, import the Font Awesome Font Icons style sheet. You will display some image to represent your rating. This cannot be a star! Pick another image from the Font Awesome collection at  [link: https://fontawesome.com/v4.7.0/icons/] https://fontawesome.com/v4.7.0/icons/. 

<!-- Insert the Font Awesome Font Icons style sheet -->
<link rel="stylesheet" 
  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

  3. In the web page, provide directions to the user on how to fill out the form. 

<h1>Order Form</h1>
<p class="pl-5"><strong>Directions: </strong>
If the table gets too big, scroll to the bottom of the page to view the data. </p>
<hr />

Insert the Web Form Element

Insert the Form Elements

Insert the form tags.

The id and name the form is myOrderForm.

When the user clicks on the submit button, the onsubmit event handler attribute in the form tag should return false. 

Here is what the code looks like.

      <!-- Insert the beginning form tag below -->
        <form id="myOrderForm" name="myOrderForm"
              onsubmit="return false" class="form signup-form">
      </form>

Insert the Form Controls (Form Fields)

Insert several fields. 

Make sure to change the tabindex to 0 for all of the fields. 

Here are some guidelines: 

In the first control, insert a dropdown list where the user can select the product. 

Display the product name in the list. 

The value should be the price of the product with no dollar ($) sign.

The field id and name is products.  

The first option should be disabled, selected by default, have a value of "" and display, Select a Product. 

Here is what the code looks like.
<!-- Insert the dropdown list of the products -->
<select class="form-control" name="products" id="products"
        style="width:250px;display:inline;" size="1"
        tabindex="0">
    <option value="" selected disabled>Select a Product</option>
    <option value="139.95">Waterford West Hampton Glassware</option>
    <option value="24.99">Belleek Galway Vase</option>
    <option value="79.99">Belleek Shamrock Dinner Plate</option>
    <option value="36.99">Royal Tara Shamrock Saucer</option>
    <option value="8.95">Barry's Classic Blend 80 Tea Bags</option>
</select><br /><br />

The second control is a textbox used to allow users to identify the quantity many items they are ordering.

Provide a label before the radio button list that says Quantity (0-100):

This should be an input control that has the type set to range.

The default value is 1. 

You may change the attributes to be appropriate for your store. 

The field id and name is quantity. 

<label for="quantity">Quantity (0-100):</label><br /> 
<input type="text" value="1" name="quantity" id="quantity" required><br /><br />

The third form control is a radio button list that should allow the user to select a number of stars for the product.

Provide a label before the radio button list that says Star Rating (1-5):

The values for the five options are are 1 - 5. 

The field id and name is ratings. 

Rating 5 is checked by default. 

You are to display some image to represent your rating. This cannot be a star! Pick another image from the Font Awesome collection at  [link: https://fontawesome.com/v4.7.0/icons/] https://fontawesome.com/v4.7.0/icons/. 

You will need to configure the font image color using a style rule. In this example the class is named checkedStars. You can see in the span tag, the class name is used to change the color of the font image icon. Insert this style rule at the top of the page inside a style tag. You may later add other styles to enhance your web page appearance!

.checkedStars {
    color: deeppink;
}

The snippet shows an example of how to insert the stars. Do this for each of the 5 radio buttons. Make sure the number of spans matches the number for the value for that radio button. Here is what the code looks like.

<!-- Insert the 2nd radio button -->
<label>Star Rating (1-5):</label><br />
<!-- Insert the 1st radio button -->
<input type="radio" name="ratings" title="Ratings" id="1star" value="1" tabindex="0"> &nbsp;
<span class="fa fa-star checkedStars"></span> <br />
<!-- Insert the 2nd radio button -->
<input type="radio" name="ratings" title="Ratings" id="2star" value="2" tabindex="0"> &nbsp;
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span> <br />
<!-- Insert the 3rd radio button -->
<input type="radio" name="ratings" title="Ratings" id="3star" value="3" tabindex="0"> &nbsp;
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span> <br />
<!-- Insert the 4th radio button -->
<input type="radio" name="ratings" title="Ratings" id="4star" value="4" tabindex="0"> &nbsp;
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span> <br />
<!-- Insert the 5th radio button -->
<input type="radio" name="ratings" title="Ratings" id="5star" value="5" tabindex="0" checked> &nbsp;
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span>
<span class="fa fa-star checkedStars"></span>
<br /><br />

The fourth form control is a radio button list that should indicate if the user is adding the product to their wish list or shopping cart. 

The name is listing. The id's are cart and shoppingCart and wishList. 

Cart is checked by default.

<!-- Insert the first radio button --> 
<input type="radio" name="listing" title="Wish List" id="wishList" 
     value="Wish List" tabindex="0"> &nbsp; Wish List<br />
<!-- Insert the Cart radio button --> 
<input type="radio" name="listing" title="Cart" checked id="shoppingCart" 
     value="Cart" tabindex="0"> &nbsp; Cart <br /> 

The last form control is a reset button and a button that is used to submit the form.

The submit button should say Place My Order.

When the button is pressed, a function named "processOrder" is called. 

Notice how the onclick event handler is calling the function when the button is clicked. 

<input type="submit" id="btnSubmit" class="btn btn-primary" tabindex="0"
     value="Place My Order" onclick="processOrder();">

 [link: #top] Top

Create the The Wish List and Shopping Cart Table

The table will display both the shopping cart and the wish list. In practice these would likely be different pages. However, it's helpful to see that you can read the data and display different information in the table based on the contents of the data. 

Insert a pair of div tags. Set the class to center. 

Inside the div tags, insert the table element.

You may want to create a sample of the table to make sure the table fits on the page. If it does not, you can alter the style attributes for the text and table and rearrange the form controls.

Set the class name for the table to "table-dark w-100"

Set the id to tableShoppingCart. 

Configure the table heading row.

The table heading row should remain always on the page. 

Note that the quantity is price * quantity. 

The Ratings displays a number of images that represents the rating selected.

The Grand Total is the previous grand total plus the current subtotal. 

The table include the following column names:

Product

Price

Quantity  

Subtotal (Price * number)

Ratings

Listing

Subtotal

Grand Total

Here is what the code looks like.

<h3 class="text-center">Calculation Results:</h3>
<div class="center">
    <table id="tableShoppingCart" class="table-dark w-100">
        <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Ratings</th>
            <th>Listing</th>
            <th>Subtotal</th>
            <th>Total</th>
        </tr>
    </table>
</div>

You may alter the CSS style rules and enhance your form. This is the code used in figure 1 that was used to format the stars and the table. This was embedded into the web page. 

<style>
/* Configure the Stars in the form in unit 5 */
.checkedStars {
    color: deeppink;
}
form, input:last-child {
    margin: 10px 20px;
}
/* position the table */
table.center {
    margin: 10px 0;
    display: flex;
    justify-content: center;
}
th {
    text-align: right;
    text-decoration: underline;
    padding-left: 10px; 
}
    th:nth-child(1) {
        text-align: left;
        padding-right: 10px;
    }
    th:nth-last-child(1) { 
        padding-right: 10px;
    }
td {
    text-align: right;
}
    td:nth-child(1) {
        text-align: left;
        padding-right: 10px;
    }
    td:nth-last-child(1) {
        padding-right: 10px;
    }
</style>

In figure 1 you can see a sample of what the form might look like in a browser.

Figure 1 Sample Form

 [link: #top] Top

Create the JavaScript Program

Define the Variables in the JavaScript File

When the user clicks on the button, the external JavaScript file is called.

Define the variables that you will need for the product name, price, quantity, listing, ratings, subtotal and grand total.

You will also need variables to store the font icon string that is displayed in the web page (starString) and a string to store the code that creates one font image icon (star).

You may need to assign default variables such as "" to starString.

You will also want to set the global subtotal and grand total variables to 0 when they are declared.

Be consistent and descriptive in your variable names. You  may  add additional variables if you need to. 

var star = '<span class="fa fa-star checkedStars"></span>';

Create the Variables

Create the variables function. Notice the comments.

/* Created by John Smith, 9/1/2019, ShoppingCart.js */
// alert("Defining variables");
var pr;             // product name
var p;              // price for the item
var q;              // quantity of the item
var l;              // shopping cart or wish list
var sr;             // star ratings
var st = 0;         // subtotal
var gt = 0;         // grand total 
var starString =""; // stores the star string
var star = '<span class="fa fa-star checkedStars"></span>';

I left the 'alert' messages in for you to see that you can use the alert() method to test if the button is able to call the JS file. Always test while you are programming and do not wait until the end to start testing!

Create the processOrder Function

Create the processOrder function.

Retrieve the value from the products field in the form. This is to make sure that the user selected a product from the dropdown list before processing the form. Form validation is important to complete before processing the data!

Only if the user has a product selected, then, call the calculate function. 

function processOrder() {
    // alert("OrderForm function called");
    var products = document.getElementById("products");
    pr = products.options[products.selectedIndex].text;
    if (products.value == null ||
        products.value == "" ||
        products.value == "undefined") {
        // No product was selected
    }
    else {
        // alert("Calling calculate function");
        calculate();
    }
}

Retrieve values of the form controls using getElementByID and the value property. 

Create the OrderForm Function in the JavaScript File

Create a function called orderForm. This will let you determine if the user selected a product. 

Create a variable called products. Assign this value to products: document.getElementById("products").

Set the value of your global product variable to the selected item's text property. To do this you need to retrieve the index position of the option that was selected. 

pr = products.options[products.selectedIndex].text

You  can then use an if statement to determine if the value is null, an empty string or undefined.

TIP: You can combine conditional expressions using && and ||. 

If there is no value, then no product was selected. Do nothing. 

If there is a value, then call the calculate() function. 

 Create the Calculate Function

There are three parts to this function.

First, retrieve the values from the form  and store them in the global variables. (You should be able to do this with getElementById or getElementsByName. There are ways to do this with limited scope, but I'd like you to work with global variables so you can see how the local scope and global scope works in Javascript).

Second complete the calculations.

Third, you will display the results in the table by inserting a new row and creating cells for each value that you are inserting. 

Retrieve the Products Value and Text 

Retrieve the text of the products form control as you did in the orderForm function. Store the product name in your global variable.  

Retrieve the Values of the Price and Quantity  

Retrieve values of the price and quantity form controls using getElementByID and the value property. 

function calculate() { 
    // alert("Calculate function called");
    // Retrieve the selected index and then get the text value
    var products = document.getElementById("products");
    pr = products.options[products.selectedIndex].text;
    // Retrieve the price and quantity fields
    p = document.getElementById("products").value;
    q = document.getElementById("quantity").value;
}

Syntax to retrieve a value from a form control. 

var VariableName = document.getElementsByName("formControlID");

Retrieve the Ratings and Convert the Value to Image Font Icons

To retrieve the ratings value, you need to determine which option was checked. This is similar to the code you used in the last unit. Assign the ratings control value using getElementsByName to a temporary local variable. 

// Retrieve the ratings based on the checked values
var rbRatings = document.getElementsByName("ratings");

Use a for loop to iterate through each option. If the option is checked, then set the global ratings variable to the value of that option. This will simply provide the value of the option that was selected. 

for (var i = 0, length = rbRatings.length; i < length; i++) {
    if (rbRatings[i].checked) { sr = rbRatings[i].value; }
    else { }
}   

To turn the value of the ratings option to a string of image font icons you need to create a string, that displays the image n times.

You can use multiple techniques such as a for loop, while, do-while or switch-case. The while loop is the shortest code. Remember star contains the string that displays one image. StarString contains one or more star strings to display one or more images. So the starString is made up of one or more star(s). You can simply concatenate the star(s) to return the starString. 

You have to convert the global ratings variable (sr) to a number using the Number method.

Store the new value in a variable such as starNum. 

Reset your variable that stores the string such as startString to empty strings. 

In the while loop, continue executing the code as long as the starNum is greater than 0. 

Assign starString to the results from concatenating the old starString and a single star.

Decrement the starNum by one.

Retrieve the Listings Value

To retrieve the listing value, you need to determine which option was checked. This is similar to the code you used in the last unit.

Retrieve the listing form control. 

Use the for loop to iterate through each option in the listing. 

If the option is checked, set the global listing variable to the value of that option.      

starNum = Number(sr);
// Reset variables 
starString = "";
while (starNum > 0 ) {
    starString = starString + star;
    starNum--;
}
// alert("Starting Switch statement");
// switch (starNum) {
//    case 1:
//        starString = star
//        break;
//    case 2:
//        starString = star + star;
//        break;
//    case 3:
//        starString = star + star + star;
//        break;
//    case 4:
//        starString = star + star + star + star;
//        break;
//    case 5:
//        starString = star + star + star + star + star;
//        break;
//    default:
//        starString = star;
//}   
// alert("Retreiving the Listing");
// Retrieve the listing based on the checked values
var rbListing = document.getElementsByName("listing");
for (var j = 0, length = rbListing.length; j < length; j++) {
    if (rbListing[j].checked) { l = rbListing[j].value; }
    else { }
}

Calculate the Subtotal and Grand Total Values

Convert the price and quantity global variables to numbers using parseFloat() or Number() methods.

Multiply the new numeric price and quantity variables.  

Set the global grand total variable to the previous grand total variable plus the subtotal.  

Create the Table and Insert the Data in a New Row

To retrieve the listing value, you need to determine which option was checked. This is similar to the code you used in the last unit.

Create the variables 

// Create variables that calculate the subtotal and grand total (a global variable)
st = Number(p) * Number(q);    // calculate the subtotal
gt = gt + st;                  // calculate the grand total

Create a variable named table to store the table object. 

// Display the results in a new table row
// alert("Displaying the results in a table");
var table;        // table of computed values

Create a variable named row to store the new row object. 

var row;          // current row in the displayed table   

Assign the table variable to the tableShoppingCart table in the web page using the getElementById method.
table = document.getElementById("tableShoppingCart");

Insert a new row. 

row = table.insertRow(table.rows.length);  // creates the row 

Insert a cell and assign the innerHTML to the value to be displayed in the cell. Remember that for the ratings, to display the starString and not the numeric value for the ratings. 

row.insertCell(0).innerHTML = pr;
row.insertCell(1).innerHTML = "$" + p;
row.insertCell(2).innerHTML = q;
row.insertCell(3).innerHTML = starString;
row.insertCell(4).innerHTML = l;

You can format the values by concatenating "$" for currency as well as use the fixed or toLocaleString methods. The toLocaleString will also insert the commas. Here are snipped of how each might be used. 

row.insertCell(5).innerHTML = "$" + st.toLocaleString(2).toString();
row.insertCell(6).innerHTML = "$" + gt.toLocaleString(2).toString(); 
// alternative is to use gt.toFixed(2).toString(); 

 

Save both pages. Preview the pages in the browser. Below is figure 2 that shows what the page might look like after testing your form. Your form may look different depending on the CSS styles and formatting that you choose. 

Figure 2 A Completed Order Form

 

 [link: #top] Top 

 [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
