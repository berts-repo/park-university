# Unit 8: Discussion

Unit 8: Discussion

Writing Web Programs with JavaScript

Please review the general directions from Unit 1. In your discussion you will select and discuss the review questions and exercises at the end of the chapter. There will be some duplicates depending on how many students are enrolled.  So each question should be used at least once. 

Do not repeat a question that has already been answered until all questions have been answered!

Review Questions  

Your instructor will assign you one review question from chapter 12 

Copy the question number and the question at the top of your posting! 

Thoroughly explain the answer. 

Exercises   

Your instructor will assign you one exercise question from chapter 12

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

**Posted:** 2023-10-05T03:21:45Z

CH 12.10 Review Questions

#19

When you want to rotate something, why is it common to call translate before calling rotate?

When an object is originally drawn its point of origin is the top left of the object. This is also the point that that the object rotates around, so the top left.

In the code I added comments to show me translating to the center of the ‘canvas’ element (width: 300px, height 150px) to the center of the ‘canvas’ container, which is half of 300px and 150px. I also moved the point of origin of the rectangle by moving the it to the negative plane of the x,y axis by half of its height and width (100px).

<body>	
<canvas id="myCanvas" width="300" height="150" style="border: solid">

<script>
	var c = document.getElementById("myCanvas");
	var ctx = c.getContext("2d");

	// Translate to the center of the canvas
	ctx.translate(c.width / 2, c.height / 2);

	// Rotate 45 degrees clockwise
	ctx.rotate(45 * Math.PI / 180);

	// Set the rectangles x,y on a negative plane with the value of half the width and height
	ctx.rect(-50, -50, 100, 100);
	
	// Draw a rectangle whose is now centered in the element
	ctx.stroke();
</script>	
</body>

CH 12.4 Exercise

#2

If you want to display text with a border and filled interior, why should you normally call strokeText after fillText?

 This question is related to the wording and less right or wrong way of doing it; “If you want to display text with a boarder and filled interior." When I was testing the code I made an example of both using the code provided from WC3School for fillText(). Both outcomes look good but the second one does not have a boarder around filled text, but instead looks more like a shadow effect.

output:

code:

<body>	
<canvas id="after" width="300" height="150" style="border:1px solid grey">
<canvas id="before" width="300" height="150" style="border:1px solid grey">

<script>
	// Test 1: strokeText after fillText
	const c = document.getElementById("after");
	const context = c.getContext("2d");

	context.font = "30px Verdana";
	context.strokeStyle = "red";

	context.fillText("strokeText after", 10, 90);
	context.strokeText("strokeText after", 10, 90);

	// Test 2: strokeText after fillText
	const c2 = document.getElementById("before");
	const context2 = c2.getContext("2d");

	context2.font = "30px Verdana";
	context2.strokeStyle = "red";

	context2.strokeText("strokeText before", 10, 90);
	context2.fillText("strokeText before", 10, 90);

</script>
</body>

 

Work Cited:
Canvas filltext() method. W3School. (n.d.). https://www.w3schools.com/jsref//canvas_filltext.asp

---


### Feedback

**[INSTRUCTOR]:** Bert

Excellent! I'm glad you were able to complete the reply posting. 

Please contact me in my inbox if you have any questions.
