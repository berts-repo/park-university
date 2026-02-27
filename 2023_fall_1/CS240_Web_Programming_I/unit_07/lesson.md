# Unit 7: Lesson

Writing Web Programs with JavaScript

Rather than provide separate lectures, we are going to ask you to read your textbook. We want you to read your book and take your own notes. Here are some notes we thought were most important or needed additional reinforcement or clarification. 

Chapter 7 Object-Oriented Programming and Arrays 

Make sure to review this chapter closely if you have not worked with objects and arrays lately! [link: #top] 

 [link: #top] Top

 [link: #top] 

 [link: #top] 

 [link: #top] 

OOP

 [link: #top] 

Object oriented programming is part of JavaScript, although the code is not compiled. There are build-in objects, as well as methods to allow you to build your own custom objects. Our object will store data and methods to access that data, and the program that implements the class. The class is stored in an external JavaScript   file for convenience, maintenance and reusability.In the web page, you will need to import the JavaScript file that contains your class code as you have with other JavaScript files. 

TIP: The sample uses a prototype implementation in order to support legacy browsers. The constructor’s prototype holds the methods that the constructor can inherit from.  Legacy code is code that is used today even though it’s considered inefficient or inelegant. While legacy code is often supported in business situations you do not need to build support for legacy class for homework applications. Many of the issues with Microsoft IE will resolve as users move towards the Edge. 

This may be review for some students who have extensive OOP in school or in the workplace. However for some students they may have only seen the OOP programming in their one Java course. Please help eachother in the discussions as you talk about how we can use OOP with JavaScript to help build more robust, dynamic, user friendly web and mobile applications. 

The JavaScript Class File 

The JavaScript file implements a 'point' class and stores 'Point' objects which in this case contains the locations of the two most recent mouse clicks.  As you can see the constructor here requires 2 parameters. 

The book does a great job walking you through the Point class and creating an instance of the point class. So  make sure to review that section.

class Point { 
  constructor(x, y) {  // class constructor heading
        // assign values for the properties  
        this.x = x;
        this.y = y; 
        // create properties and assign values
        Point.count = 1;  
  } // end constructor 
  // Create methods that return values, or create properties. 
  // Create the value method and return the point in the format "(x, y)" 
  value() { 
        return "(" + this.x + ", " + this.y + ")";
  } // end value
} // end class Point  

Static Methods

Static methods are different than regular methods. These are three important characteristics of static methods. Below is an example of how to create a static method in JavaScript.

Static methods belongs to the class rather than object of a class. 

A static method can be invoked without the creating an instance of a class.

Static methods can access static data members and can change the value of them.

static getCount() {              // Return a count for the number of Point objects
static distance(pt1, pt2) {      // Return the distance between two points or null if one
                                 // or more of the points is missing. 
static reduceCount() {           // After removing a point, reduce the count.
var point1, point2;              // the most recently clicked points

// For Delete key functionality, remove element's onclick event handler & replace with: 
                                 // document.addEventListener("click", captureClick);
                                 // document.addEventListener("keydown", removePoint);

Regular Methods

function captureClick(e) {       // Stores a user's click location as a point.
function displayDistance(e) {    // Calculates and returns the distance between 2 points.
function removePoint(e) {         // Removes the most recently created point

So in the displayDistance one of the tasks is to calculate the distance. You can call the method and pass the points and the return value is stored in a variable (distance). 

distance = Point.distance(point1, point2);

 [link: #top] Top

 [link: #top] 

 [link: #top] 

 [link: #top] 

Primitive Values

 [link: #top] 

A JavaScript variable can hold a primitive value or an object. 

A primitive value can be a number, a string, a Boolean (true or false), null, or undefined.

Objects are inherently different from primitive values in that objects hold properties and methods. 

Another inherent difference is the way in which variables store primitive values versus objects.

Variables store primitive values directly and objects indirectly. 

You can think of an object’s reference as the address of where the object is stored in memory.

 [link: #top] Top

 [link: #top] 

 [link: #top] 

 [link: #top] 

Event Listeners

 [link: #top] 

The event listeners are not in the class but in the JavaScript that interacts with the web page. The event listeners are used instead for calling the event handler inline with the html code. 

You can bypass event-handler attributes (with accompanying JavaScript) altogether by instead using the addEventListener method. The html element is associated with the document object, so we just need to call document.addEventListener to add a listener for each event and object combination. 

There’s no absolute rule about where addEventListener method calls should be positioned, but it’s common to position them above the function definitions that they refer to. Notice that the events are thing such as click, keydown and mouseover. Some developers add all the event listeners in one group. Many times we code this interactively within the program. So when a user clicks on a button in an MP3 player we can disable the button so the song does not play on a separate thread. On the Stop button we can re-enable the event listener. 

document.addEventListener("click", captureClick);
document.addEventListener("keydown", removePoint);

Some other examples that use event listeners with different events. 

document.getElementById("myBtn").addEventListener("click",myFunction2);
document.getElementById("myBtn").addEventListener("mouseover", myFunction);
document.getElementById("myBtn").addEventListener("mouseout",myFunction3);
myBtn.addEventListener("mouseover", myFunction);
myBtn.addEventListener("mouseout", myThirdFunction);
myBtn.addEventListener("click", mySecondFunction);
myBtn.addEventListener("click", function(){ alert("Hello World!"); }); 
myBtn.addEventListener("click", function(){ myFunction(p1, p2); }); 

You can include  also add a method to remove an event listener from the controls.  So for example if the button has been clicked on a video you don't want them to click on the button and start another playmusic class, unless you like listening to "Row row row your boat!"

myBtn.removeEventListener("mousemove", myFunction);

The Web Page

On the button, when the onclick event handler is in action the displayDistance method is called passing the event to the function so that the function can retrieve the mouse click coordinates. 

<input type="button" id="btn" value="Distance apart"
           onclick="displayDistance(event);">

 [link: #top] 

 [link: #top] Top [link: #top] 

 [link: #top] 

 [link: #top] 

 [link: #top] 

Extending Classes 

We may be programming for the web, but good programming design and practices still apply! When you design your programs, remember your basic systems design skills and how you created  class diagrams. Think about what classes, functions you need. It may help you to write out the list of methods, properties that you will need to access, input and output parameters. 

Review the chapter class diagram for the Employee, PartTime, and FullTime classes.The class diagram’s format comes from the Unified Modeling Language (UML). UML is an industry standard for modeling OOP designs. It uses diagrammatic techniques in attempting to model a wide range of programming concepts. The top partition is for the class name, the middle partition is for the class’s properties (which are called attributes in UML), and the bottom partition is for the class’s methods (which are called operations in UML). 

Make sure to review the section on Inheritance Syntax. 

Class PartTime extends Employee {

For a subclass, you need to append the keyword extends and then the superclass name to the end of the subclass’s heading. For example, here’s the heading for the PartTime class, which is a subclass of Employee.

A subclass inherits its superclass’s members—its properties and methods. For a subclass method to access the properties inherited from its superclass, the syntax is easy. Just preface the property with this dot, which is the same way the object accesses properties defined in its own class. For a subclass method to call a method in its superclass, you preface the call with super dot.

class Dog extends Pet {
   constructor(name, trick) {
        super(name, "Woof! Woof!");
        this.trick = trick;
   } 
   confirm() {
       return super.confirm() + "<br>Favorite trick: " + this.trick;
   } // end confirm
} // end class Dog

Pet superclass and its two subclasses, Dog and Hedgehog
All pets have a name and a sound they make, so the Pet class defines name and sound properties. 

 [link: #top] 

 [link: #top] Top

 [link: #top]  [link: #top] 

 [link: #top] 

 [link: #top] 

 [link: #top] 

Mouse Events

The common ones are click, mouseover, mouseout, mouse enter, mouseleave, mousedown and dblclick.

 [link: #top] 

 [link: #top] 

 [link: #top] 

 [link: #top] 

Commonly used properties available with the mouse event include clientX and clientY coordinates relative to the viewport. You can also use screenX and screenY to identify the screen coordinates. You can use the altKey, shiftKey and ctrlKey which provide true if the key was pressed. Finally button will return 0 if main mouse button was clicked, 1 for the middle mouse button and 2 if the right mouse button was clicked.

if (e.eventPhase == Event.AT_TARGET) {
   typeCell.innerHTML = e.type;
   xCell.innerHTML = e.clientX;
   yCell.innerHTML = e.clientY;
   if (e.type == "mouseover") {
        e.target.style.background='black'; 
        e.target.style.color='white';
   } 
   else {
         e.target.style.removeProperty('color');
         e.target.style.removeProperty('background'); 
   }
} 

TIP: Events have three phases in the events life cycle: capture, target, and bubbling.  You can capture the event and work with events like stopPropagation and stopImmediatePropagation and event bubbling.

 [link: #top] Top

 [link: #top] 

 [link: #top] 

 [link: #top] 

Creating and Using Arrays

JavaScript like other languages, is zero-based, uses [ ] for index position, can have multiple data types and you don’t need to identify size when declaring the array.

As you can see the methods are syntactically similar to arrays in other programming languages. 

Create array

var myArray = new Array();
myArray[0] = 5;
myArray[1] = “Turkey”;
myArray[2] = true;

TIP:  Java supports exception handling. Exception handling uses error object to store error messages, name and number. Listing 5-30 Rotate through the array and retrieve each element. 

try {
     var myArray = [5, "Turkey", true];
     for (var i = 0; i < myArray.length; i++) {
             document.writeln("Index " + i + ": " + myArray[i]);
   }
} 
catch (e) {
     document.writeln("Error: " + e);
}
finally {
     document.writeln("Finish up the code");
} 

Array Methods 

concat(array1, array2) - return Array

join(“,”)  // specify delimiter - return string

reverse() - reverse order - return Array

sort() - sort array  - return Array

slice(start, end) - return sub-Array

shift() - append item in the first position - return object

pop() - remove and returns last item in stack  - return object

push(item) - append item to array - return void

unshift(item) - like push, insert at first position  - return Array

 [link: #top] Top 

 [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
