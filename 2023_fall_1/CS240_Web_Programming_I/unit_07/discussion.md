# Unit 7: Discussion

Unit 7: Discussion

Writing Web Programs with JavaScript

Please review the general directions from Unit 1. In your discussion you will select and discuss the review questions and exercises at the end of the chapter. There will be some duplicates depending on how many students are enrolled.  So each question should be used at least once. 

Do not repeat a question that has already been answered until all questions have been answered!

Review Questions  

Your instructor will assign you one review question from chapter 11  

Copy the question number and the question at the top of your posting! 

Thoroughly explain the answer. 

Exercises   

Your instructor will assign you one exercise question from chapter 11

Copy the question number and the question at the top of your posting! 

Thoroughly explain the answer. 

Reply Postings

Please provide a total of 2 reply posts.

In your reply post to 2 other students:

Respond to each student by name.

Identify if the answer was correct or incorrect. If it's incorrect, identify the correct answer and where you found the answer. 

Students should review the other students post for clarity and correct explanation of concepts, terminology accuracy and correctness of code and evaluates the post for use or proper coding conventions and documentation.

Cite a reference to support your statements.

**My Score:** 20.0/?

---

## My Discussion Posts

**Posted:** 2023-09-27T00:48:39Z

CH 11 Review Questions: #22

The following code attempts to declare an empty array and then add an element to the array. Does it work? Yes or No.

Prices = new Array();

Prices[0] = 22.35;

Yes, ‘Prices’ is assigned to the JavaScript method to create an array. The second line then initializes the first element in the array to ’22.35’

CH 11 Exercises: #9

[After Section 11.14] The fallowing code implements a simple web page that creates a list of cheerleader names and sorts the names. Provide an improved version of the web page that stores each cheerleader’s height in centimeters and sorts the cheerleaders by height. Among other things, you’ll need to implement a Cheerleader class with name and height properties.

Class, I found this question to use more advanced programming concepts. The other programming classes I have taken didn’t work with OOP objects until later in the chapters. The JavaScript really ramped up fast for this class.

I found this sort function on W3School, and is defined as:

“A function that defines a sort order. The function should return a negative, zero, or positive value, depending on the arguments:

    
function(a, b){return a-b}

When sort() compares two values, it sends the values to the compare function, and sorts the values according to the returned (negative, zero, positive) value.”

Code:

<script>
// Global array to hold cheerleader object
var stuntGroup = new Array();

function driver(){
	// Gets height and name from html
	var name = document.getElementById("cheerleader-name").value;
	var height = document.getElementById("cheerleader-height").value;

	// Creates Chearleader object, by calling Cheerleader constructor
	var cheerleader = new Cheerleader(name, height);

	// Adds Cheerleader object to end of array
	stuntGroup.push(cheerleader);

	// Sort function by comparison, if first height value comes before the second
	stuntGroup.sort(function(a, b){return a.height - b.height});
	
	// Calls function to display output in html
	displayStuntGroup();

} // end driver function

// Cheerleader class constructor
class Cheerleader {
	constructor(name, height) {
		this.name = name;
		this.height = height;
	}
}

function displayStuntGroup() {
	var namesColumn = ""; // string to display output

	// Iterates through stuntGroup array to print name and height
	for (let i=0; i<stuntGroup.length; i++) {
		namesColumn += stuntGroup[i].name + ": " + stuntGroup[i].height + "<br>";
	}
	// Where to display output in html
	document.getElementById("stunt-group").innerHTML = namesColumn;
} // end displayStuntGroup

</script>
</head>
<body>	
	<input type="text" id="cheerleader-name" placeholder="Name">
	<input type="text" id="cheerleader-height" placeholder="Height in cm">
	<br>
	<input type="button" value="Add cheerleader" onclick="driver();">
	<div id="stunt-group">
</body>
</html>

Output:

Work Cited:

JavaScript array sort(). W3School. (n.d.). https://www.w3schools.com/jsref/jsref_sort.asp

---


### Feedback

**[INSTRUCTOR]:** Bert

Good work!

Please contact me in my inbox if you have any questions.
