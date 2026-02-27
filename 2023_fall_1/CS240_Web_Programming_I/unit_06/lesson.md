# Unit 6: Lesson

Writing Web Programs with JavaScript

Rather than provide separate lectures, we are going to ask you to read your textbook. We want you to read your book and take your own notes. Here are some notes we thought were most important or needed additional reinforcement or clarification. 

Chapter 10 Loops, Additional Controls, Manipulating CSS with JavaScript 

 [link: #top] Top

Control Program Flow 

While Loop

Basic While Loop needs a condition indicating when to stop. In this case the counter stops at 10. On the i  = 10. 10 is not less than 10, so the loop stops before printing. Notice the counter i needs to increment.

Example 

var text = "";
var i = 0;
while (i < 10) {
    text += "<br>The count is " + i;
    i++;
}

This repeats for each element in the list. Notice the counter here would increment each time.

var fruit = ["apple", "banana", "apple", "strawberry", "orange"];
var text = "";
var i = 0;
while (i < fruit.length) {
    text += fruit[i] + "<br>";
    i++;
}

This would put a restriction on what value not to process or could be used to determine when to stop the loop.

var fruit = ["apple", "banana", "apple", "strawberry", "orange"];
var text = "";
var i = 0;
while (i < fruit.length) {
    text += fruit[i] + "<br>";
    i++;

    if (fruit[i] != 'apple'") {
        continue;
    }
}

Do While Loop

Example

You need the while loop to have a conditional expression that will evaluate to true or false, to determine when to stop the loop. 

do {
  quotient /= 2;
} while (quotient != Math.floor(quotient) && quotient > 1);

For Loop

Example shows the use of the counter incremented with the initialization. 

var text = "";
var i;
for (i = 0; i < 5; i++) {
    text += "The counter is " + i + "<br>";
}

 [link: #top] Top

Samples

TIP: We've covered this in lesson 4. However, it's useful to review the example in the book.

 

<script src="compoundInterest.js"></script>

Review the Samples from the chapter!

Notice the way the JS file is documented at the top of the page. 

Remember all JS files must be documented. Refer to the appendix for additional information. 

Notice the code uses a string to generate the table. There are other ways to do this. You can create table objects and other HTML elements on the fly. 

Fieldset and Legend form controls were also covered lesson 4.

Textarea and z-index were covered before too. 

The samples are sometimes browser dependent. Use Chrome if possible!

 [link: #top] Top

Debugging Issues

Chrome’s debugging tool is called “Developer Tools" are actually very useful. Not only the debugger but also in being able to inspect elements an temporarily change the code or values for testing on the client. This does not allow users to change the code on the server. The console log is just one tool. This information is not stored on the web server or across clients. 

console.log("cost = " + cost);

Security Issues

However, if a server 'receives' the form, the web server needs to validate the data received. It's possible to change data and modify HTML validation properties on the client using these Developer Tools. Fields that were 'readonly' can be changed to editable on the client too. So always remember that client-side validation does not replace server side validation of client data! [link: #top] 

 [link: #top] Top

Finding Elements

We are using two methods primarily to identify elements and what you should use in your homework. You may use other methods, but they are harder to work with for beginners.  

document.getElementById("controlID"); 

Other methods include by tag name, class name, any css selector

document.formName.elementName
document.getElementsByTagName("tagLowerCase");
getElementsByClassName("className");
querySelectorAll("tagLowerCase.className");

There are other methods to identify elements by index or name. Use the examples  in your book and on W3Schools and in your book!

document.forms[0]
document.forms[0].elements[0]
document.getElementById("myForm").elements[0].value;
document.getElementById("myForm").elements.item(0).value;
document.forms.namedItem("controlName")
document.getElementById("myForm").elements.namedItem("controlName").value;

 [link: #top] Top

Radio Buttons (Review)

The name is used to group the radio buttons together. By default you can only select 1 element in the group where they all have the same name but different IDs.  You can retrieve individual elements, and determine if they were selected.You have to check each one individually. You can write javascript to determine if they were checked using the checked property, to be executed when they are checked using onclicked. 

Radio Buttons

<input type="radio" name="fruit" id="apple" value="1">apple
<input type="radio" name="fruit" id="banana" value="2">banana
<input type="radio" name="fruit" id="strawberry" value="3">strawberry
<input type="button"name="fruit" id="Orange" value="4" 
       onclick="alert('Orange!')" text ="Choose Orange!">

Example

myfruit = document.form.elements["fruit"].value; 
document.getElementById("fruit").value;

 [link: #top] Top

Checkboxes (Review)

By default you can only select none, any or all checkbox elements with different IDs.  You can retrieve individual elements, and determine if they were selected. You can write javascript to determine if they were checked using the checked property, to be executed when they are checked using onclicked. You have to check each one individually.  

<input type="checkbox" name="fruit" id="apple" value="apple"> I have a apple<br>
<input type="checkbox" name="fruit" id="orange" value="orange"> I have a orange 

You can go through each one manually. Notice it's not an either or. Both or none can be selected so we used ( += ). 

if (document.getElementById("apple").checked) { 
      myfruit = document.getElementById("apple") + "<br>";
} 
if (document.getElementById("oranges").checked) { 
      myfruit += document.getElementById("oranges") + "<br>";
}   

If you have a name grouping the checkboxes you can iterate through them as a collection and refer to each element by it's index position. To retrieve the values with more than one element selected and no grouping, you could iterate through each one to determine if they are checked. 

This retrieves all checked elements in the form!

var fruit = document.forms[0];
var results = "";
var i;
for (i = 0; i <fruit.length; i++) {
  if (fruit[i].checked) {
   results =results + fruit[i].value + " ";
  }
}

 [link: #top] Top

Checking Form Validity

Make sure to review the sample pages. The checkValidity is used to determine if the form was valid for that field, before moving on. 

Let

Let will limit the scope of the index variable to just the loop. 

 

for (let skill of jobSkillsCBs) {
  if (!skill.checkValidity()) {
    message += "<br>" + skill.value;
  }
} // end for

You can also check the entire form validity. 

if (form.checkValidity()) {

 [link: #top] Top

DropDown Lists (Review)

We covered this before on creating the lists and the properties. 

<select id="dorm" required>
  <option label=" "></option>
  <option>Chesnut Hall</option>
  <option>Copley Quad</option>
  <option>Browning Hall</option>
  <option>Eaton Hall</option>
  <option>Melrose Hall</option>
  <option>Semple Hall</option>
</select>

Let's look at the JavaScript used to retrieve the values. This is only if 1 value can be selected. 

dorm = form.elements["dorm"];

If multiple values can be selected, as in a List box, then you need to iterate through the list like you did with checkboxes. 

<select id="dorm" multiple size="6" required>
 <option>Chesnut Hall</option>
 <option>Copley Quad</option>
 <option> Browning Hall</option>
 <option> Eaton Hall</option>
 <option> Melrose Hall</option>
 <option> Semple Hall</option>
</select>

Lets retrieve the values. Retrieve the form dorm element, then get the values selected. 

dorm = form.elements["dorm"];
for (let option of dorm.selectedOptions) {
  if (dorms != "") {
    dorms += ", ";
  }
  dorms += option.value;
} // end for

 [link: #top] Top

Manipulating CSS with JS 

Your book provides samples, but you can change any css or html with JS, even the entire page!You can have the html content and styles of the class change on the fly. We'll go through the book highlights. You have already changed the html property innerHTML. You'll want to review the additional examples in the sample pages. 

This changes the class name for an element. You can also change the style property for an element directly. 

document.getElementById("message").className = "bold small-caps";
document.getElementById("message").style.fontSize = "3em";
document.getElementById("demo").innerHTML = txt;
document.styleSheets[0].cssRules.item(1).style.width = "500px";
document.styleSheets[0].cssRules.item(1).style.paddingTop = "10px";

Important!

You can see the !important parameter will cause that property to overrule the other property values. 

 

<style title="core styles">
p {
     border: medium double black; 
     background-color: lightgray !important ;
} 
</style> 

 [link: #top] Top

Dynamic HTML and Style Elements

You can create elements dynamically as shown earlier. You can also set the HTML attributes and style properties dynamically.  There are many properties you have already worked with such as cssText, style and length. 

TIP: This is the general naming pattern for multiword CSS properties: remove the hyphens and capitalize the first letter of the second and subsequent words. 

<script>
// create the element variables
var myElement = document.getElementById("content");
var newBR = document.createElement("br");
var newElem = document.createElement("span");
// set the attributes for the newElem element
newElem.setAttribute("style", "color:#336699;"); 
newElem.setAttribute("style", "color:#336699;"); 
newElem.style.cssText = "color:black";
newElem.setAttribute("class", "yellow;"); 
newElem.setAttribute("title", "MY SPAN;"); 
newElem.textContent ="Adding content to the page";
// append parent element to the page. 
// append the child element to the parent. 
// add other elements as needed. 
myElement.appendChild(newBR); 
myElement.appendChild(newElem); 
</script>

Let's create another example with dynamic properties and set the attributes using those properties:

<p id="block1">Block 1</p>
<p id="block2">Block 2</p>
<div id="contents">Contents</div> 
<div id="results">Results</div>  
<script>
// retrieve the style sheet 
// create properties
var myStyle = document.styleSheets[0].cssRules[0].style; 
// set the property values - notice they are name and pair
myStyle.setProperty("color", "yellow", "important"); 
myStyle.setProperty("background-color", "green");
myStyle.setProperty("padding-top", "20px"); 
// create the html element
var newElem = document.createElement("p");
// set attributes with the property values
newElem.textContent = "This was dynamically inserted.";
newElem.setAttribute("style", "border:1;"); 
newElem.setAttribute("style", "color:" + myStyle.getPropertyValue("color")); 
newElem.setAttribute("style", "padding-top" + 
             myStyle.getPropertyValue("padding-top"));
newElem.setAttribute("style", "background-color" + 
            myStyle.getPropertyValue("background-color")); 
// . get the parent element
var myElement = document.getElementById("contents");
// add the new element to the parent element.
myElement.appendChild(newElem); 
</script>

Using this method you can generate the entire page on the fly if you wanted to! That means you can also retrieve the styles, properties and elements and use them or display them individually or as a list. We won't ask you do to that, but we can and do these kinds of manipulations on web sites. 

<script>
// retrieve properties - first get the html element
var myResults = document.getElementById("results");
// identify the style rule length
myResults.innerHTML = "Style Rule Length: " + myStyle.length + "<br>";
// you can retrieve individual properties 
myResults.innerHTML += "Color: " + myStyle.getPropertyValue("color") + "<br>"
    + "Priority: " + myStyle.getPropertyPriority("color") + "<br>"
    + "Background Color: " + myStyle.getPropertyValue("background-color") + "<br>"
    + "Border: " + myStyle.getPropertyValue("border") + "<br>"
    + "Padding-Top: " + myStyle.getPropertyValue("padding-top") + "<hr>"; 

// you can also iterate through the entire list of style rules for an element!
var myOtherStyle = document.styleSheets[0].cssRules[0].style; 
for (var i = 0; i < myOtherStyle.length; i++) {
    myResults.innerHTML += myOtherStyle[i] + " : " 
        + myOtherStyle.getPropertyValue(myOtherStyle[i]) + "<br>";
} 
</script>

Managing Attributes

This is a very useful section on how to use the attribute, getAttribute, setAttribute, removeAttribute and hasAttributes methods to manage HTMLElements (both get and set methods). 

<p id="textblock" class="myclass">
<pre id="results"></pre>
<script>
    var myresults = document.getElementById("results");
    var myElement = document.getElementById("textblock");
    myresults.innerHTML = "Language support: " + myElement.hasAttribute("lang") + "\n";
    myElement.setAttribute("lang", "en-US");
    myresults.innerHTML += "New language: " + myElement.getAttribute("lang") + "\n"; 
</script>

 [link: #top] Top

Working with Events

Simple Event Handlers

You know that you can configure the styles inline, or in the style rules when a function is called. But you can also call the code when an event occurs inline without creating the function. Use the keyword this to represent that object. Notice you can have a mouseover effect even if it's not a hyperlink! Notice the use of single quotes nested within double quotes. You can add style rules, as well as removeProperty with this method. 

<style title="core styles"> 
        p { background-color: gray; color:white; }
</style> 
<p onmouseover="this.style.background='white'; this.style.color='black'"
   onmouseout="this.style.removeProperty('color'); this.style.removeProperty('background')">

A more efficient way is to call a function. If you use the keyword 'this' then the object information is passed with the function call. 

<p onmouseover="handleMouseOver(this)" onmouseout="handleMouseOut(this)">Block 1</p>
<p onmouseover="handleMouseOver(this)" onmouseout="handleMouseOut(this)">Block 2</p> 
<script>
// the e is the element passed from the function call with the 'this' parameter. 
// so it's a way to identify the element being passed. 
// the element can then be easily represented in the script using 'e'. 
function handleMouseOver(e) {
      e.style.background='white';
      e.style.color='black';
}
function handleMouseOut(e) {
      e.style.removeProperty('color');
      e.style.removeProperty('background');
}
</script>

 [link: #top] Top

Using the DOM and Event Object

So the next step to be even more efficient is to not 'call' the function at all from within the element. Instead we'll call configure the call dynamically. The getElementsByTagName can help identify which elements to apply the event handlers. This makes your html code clean and easy to focus on the content. There is no difference from the other example in the output! 

<p>Block 1</p>
<p>Block 2</p> 
<script type="text/javascript">
var pElems = document.getElementsByTagName("p");
for (var i = 0; i < pElems.length; i++) {
     pElems[i].onmouseover = handleMouseOver;
     pElems[i].onmouseout = handleMouseOut;
}
function handleMouseOver(e) {
     e.target.style.background='white';
     e.target.style.color='black';
}
function handleMouseOut(e) {
     e.target.style.removeProperty('color');
     e.target.style.removeProperty('background');
}
</script>

Document.write

To write out content to the web page use document.write and document.writeln.  This allows you to completely rewrite the entire page or just send output to the page. Note that this does not necessarily write the content where you want it! Do it's mostly just used for testing.

<script type="text/javascript">
     document.writeln("Hello");
</script>

 [link: #top] Top 

 [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
