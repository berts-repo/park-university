# Extra Credit

**Points Possible:** 30.0
**Submission Types:** online_upload

## Instructions

Extra Credit - Writing Web Programs with JavaScript and Canvas

 [link: #overview] Overview

 [link: #projectrequirements] Project Requirements

Overview

Learning Outcomes

The learning outcomes for all 8 assignments are the same.

Demonstrate creativity and problem-solving skills.

Analyze web programs in order to test, debug, and improve them. 

Evaluate web pages and web programs to ensure that they use proper coding conventions and documentation.

Create web pages and web programs that use: HTML5, cascading style sheets, dynamic HTML, JavaScript, forms with controls, and Canvas.

Project Topic

This is an extra credit assignment which is only made available by the instructor!

The amount of points will be announced in the  [link: https://canvas.park.edu/courses/75721/announcements] Announcements by your  instructor. 

 [link: #top] Top

Project Requirements

The goal of this project is to work with the the canvas object. Remember you can review the sample umbrella and face drawing activities in the chapter readings. That will help you learn about the tools used to draw on the canvas. But the canvas object does much more than provide a place for static drawings. You can also create animations and even games which require users to provide keyboard input. 

This project is different from the previous assignments. It's shorter since it's your final activity. But is't also lot's of fun. One of the learning outcomes is to Demonstrate creativity and problem-solving skills. So you are going to use these skills during this activity. You will be graded on your ability to implement HTML, CSS, JavaScript, and the canvas object, document your program properly, use proper coding conventions, and write correct code. 

Follow these guidelines:

In this project you are allowing the user to select products for purchase and rate the products.  You will be modifying one of the oldest electronic games in this homework assignment.

The snake game origins stem from the 1976 arcade game Blockade. The snake game was simple to implement across languages and platforms and was quickly applied to other genres and topics. 

Visit the Google Snake Game

Google today provides a free snake game to play.

As you can see in figure 1, the object is for the snake to eat the apple without crashing in the walls! Notice the quality of the graphics and ease to move the snake using the arrow keys. 

Go to  [link: http://www.google.com] www.google.com.

Type in snake game in the search form. 

At the top of the page returned, click on the Click to Play button. 

Play the game.  

Figure 1 The Google Snake Game

In your snake game you will start with the skeleton code.  You could create this from scratch, but this is the last unit of the course and we want you to focus on applying what you learned. 

This edition of snake game is based off the Snake Game created January  29, 2013 by Caio Paiola. With over 80,000 views, this game has been officially forked, over 400 times! 

The home page of the games is  [link: https://codepen.io/CaioPaiola/pen/GFpuK] https://codepen.io/CaioPaiola/pen/GFpuK. Go to this page. You can see in figure 2 that you can edit the HTML, CSS and JavaScript directly in the web page. However, this doesn't let you save your changes unless you are logged into the web site. We don't want to do that. You will need to insert the content into your own web site in Visual Studio!

You can see in figure 2 that the base game is bland with no color or graphics. The game does keep one score or tally of how many items are captured (and eaten) by the snake. The screen is setup so each part of the page allows users to edit the HTML, CSS and JS files. This is helpful for working with writing code remotely. More web sites like CodePen.io are popping up. CodePen.io has many more examples on their web site. 

Figure 2 The Snake Game on CodePen

It's important to understand and respect copyright. As you can see in figure 3, the copyright permits users to create forks of the original code. Forking is when you are using someone else's code as a base and modifying their code. 

Figure 3 Copyright Permissions to Fork the Snake Game

 

 [link: #top] Top

Setup the Files

Open the template.html and copy code to the week8.html web page. 

Save your file. 

You will need to flip the rows so that the first row consists of the two columns. 

Add some fun content to the page! Add links to other snake games and resources. 

In the left column, insert a heading and document the original snake game at  [link: https://codepen.io/CaioPaiola/pen/GFpuK] https://codepen.io/CaioPaiola/pen/GFpuK. 

On the right column when you are finished with your coding, insert a screen shot of your finished game!

Copy the code from the HTML section into the snake game web page to your second column. 

<h3>Simple Snake Game</h3>
<canvas id="stage" height="400" width="520"></canvas>

Copy the code from the CSS section into the top of your web page, This is the embedded style sheet rules because they are embedded in the web page. 

body {
text-align:center;
font-family: helvetica;
}
canvas {
border: 2px solid rgb(151, 149, 149);
}

 [link: #top] Top

Change the HTML Code that Inserts the Canvas Element

Make the following changes in the HTML content. 

Change the Jumbotron to say “My Snake Game”.

Change the heading to say “A Modified Snake Game”.

Change the heading to be size h2 instead of h3.

Did the text get bigger or smaller?

Note the ending HTML tag, too!

Increase the difficulty of the game

Change the canvas tag height and width both to 200.

What happens?

Change it back to the default 400 by 520 or a size you prefer.

Change the CSS Code

Make the following changes in the CSS content. 

Align the text to the right instead of the center. What happens? You can choose right or center

You can also change the background color if you like as shown.

If you want to see a list of color names, visit this web site:

 [link: http://www.99colors.net/color-names] Color Names

 [link: https://www.w3schools.com/colors/colors_rgb.asp] W3Schools RBG Calculator

 [link: http://www.cloford.com/resources/colours/namedcol.htm] Named Colors

 [link: http://rgb.to/html-color-names/1] RGB to HTML Color Codes – On this web site you can choose your color and click on it to see the RGB values. 

RGB means the colors are defined by a combination of red/green/blue, Any color can be expressed by specifying the amount of each color component between 0 (none) and 255 (fullest).

This is what your CSS code now looks like.

   body {
      background-color: pink;
      text-align:center;
      font-family: helvetica;
 }

Change the thickness of the border to 5 pixels instead of 2.

Change the border color of the canvas to a blue color, Red = 0, Green = 63, Blue = 165 or any color of your choosing!

This is what your code looks like:

  canvas {
    border: 5px solid rgb(0, 63, 165);
}

 [link: #top] Top

Change the JavaScript Code

Step 1 – Make the Game More Challenging or Easier (Slower)

Locate the code under “Window Load” at the bottom of the JavaScript code:

Find the line that says: “var snake = new Game.Snake(‘stage’, {fps: 150, size:4});”

Change that line to match the code shown below.

1) This will change the speed of the game by editing the frames per second, fps, from 100 to 150.

2) Change the size of the snake from 4 to 6.

What happens in the game? 

Your code should look like this:

var snake = new Game.Snake('stagefps: 150, size:6}); 

Step 2 – Add the highScore global variable to the game

Under the “* Namespace” section, add a global variable:Add a global variable called highestScore and set it to 0.

var highestScore = 0; 

Under the comment “* Game Component Stage”:

Under where this.score is set to 0, insert a new line.

Then enter a similar line that sets this.highscore to highestScore.

Change the direction of the snake to start down instead of right.

this.highscore = highestScore;
this.direction = 'down';

Under the comment “* Restart Stage”:

Under where this.stage.score = 0; insert a new line.

Enter a similar line that sets this.stage.highscore to highestScore.

this.stage.highscore = highestScore;

Step 3 – Change the canvas properties

Under the comment “// Draw White Stage”

Change the fillStyle from white to antiquewhite

context.fillStyle = "antiquewhite";

Step 4 – If the score eats food, check and see if it’s a high score

Under the comment “// Logic of Snake food”:

Right after the line of code that says “snake.stage.score++;” where the score is incremented, add an if statement that checks if the scores is greater than the high score.

If it is, increment the highscore.

Set the highestScore to new high score stored in snake.stage.highscore;

if (snake.stage.score > snake.stage.highscore) {
     snake.stage.highscore++;
     highestScore = snake.stage.highscore;
 }

Step 5 – Change the color of the snake to Laker Gold

Under the comment “//Draw Snake“

Insert a blank line

Enter the code on the blank line as shown:

context.fillStyle = 'rgb(255, 198, 30)';  

Step 6 – Change the color of the food to Lake red

Under the comment “//Draw Food“

Insert a blank line

Enter the code on the blank line as shown:

context.fillStyle = 'rgb(255, 0, 0)';  

Step 7 – Change the color of the brush and center any text

Under the comment “//Draw Score“.

Delete this entire line of code:

context.fillText(‘Score: ‘ + snake.stage.score, 5, (snake.stage.height – 5));

Make sure not to delete the next line that has “ };“

Add the code as shown. This code will to these three things:

Changes the “score” color to Laker Blue, rgb(0, 63, 165)

context.fillStyle = ‘rgb(0, 63, 165)’;

Centers the “score”  in the center of the canvas

context.textAlign = “center”;

Create a variable to center the text on the canvas. To get the center we just divided the width by 2.

var stageCenter = snake.stage.width/2;

 context.fillStyle = 'rgb(0, 63, 165)'; 
 context.textAlign = "center";
 var stageCenter = snake.stage.width/2;

Step 8 – Move the score in the center of the page 

On the next line, add the code to move the score to the center of the page.

 context.fillText('Score: ' + 
       snake.stage.score, stageCenter, (snake.stage.height - 25));

Note that you can also just ‘hard code’ where you want the score to be.

Just assign values to x, y

// context.fillText(‘Score: ‘ + snake.stage.score, x, y);

// context.fillText(‘Score: ‘ + snake.stage.score, 5, 350);

// To get near the bottom you use the snake.stage.height – 25

Step 9 – Show the highest Score in the center

On the next line, add the code to show the highestScore to the center of the page.  

 context.fillText('Highest Score: ' + 
     highestScore, stageCenter, (snake.stage.height - 5)); 

Step 10 – Show the highest Score in the center

Under the comment “// Draw Cell” delete this line of code.

 context.fillStyle = 'rgb(170, 170, 170)';

Step 11 – Save and preview your page in the browser!

 [link: #top] Top

Finishing Up the Assignment

This is what the sample output might look like in the browser if you chose the same color scheme.

You should of course choose a different color scheme!

Figure 4 Sample Modified Snake Game

Save your web page in the pages folder and the JavaScript file in the JS folder.

Make sure you have thoroughly documented all of your code in all files. 

Preview the page in the browser.

Analyze and evaluate the web page. Use the W3C’s Markup Validation Service ( [link: https://validator.w3.org/] validator.w3.org (Links to an external site.) to analyze the code. If there are errors, correct the errors now. 

 

“CHALLENGE” IDEAS 

Can you change the placement of the food such that it always is placed at x, y = 5, 5?

Hint: Locate where you add food on stage. Comment out the old code and set x to 5 and then set y to 5.

Can you cause the game to end when the snake runs into itself?

Hints: The “for” loop that draws the snake might be useful to examine; a modified version can be used in the collision Also, make sure the initially snake size is 1 for simplicity for starters.

Can you speed up the snake each time a food dot is collected?

Can you force the user to have to enter a key to [re]start the game when it ends?

CSS Game: 

Other Snake Games:

 [link: http://cssgridgarden.com/] CSS Grid Garden is another example of how to modify the game. ( [link: http://cssgridgarden.com/] http://cssgridgarden.com/). Here are some other examples of snake games:

 [link: http://www.andrespagella.com/snake-game] Andres Pagella

 [link: https://www.samclarke.com/js-snake-game/] Sam Clarke

 [link: http://thecodeplayer.com/walkthrough/html5-game-tutorial-make-a-snake-game-using-html5-canvas-jquery] The Code Player

 [link: http://patorjk.com/games/snake/] patorjk.com

 [link: #top] Top

Submit the Assignment

Submit evidence of completion of the requirements.  Make sure to review the  [link: https://canvas.park.edu/courses/75721/pages/general-homework-requirements] General Homework Requirements and document and submit your project using the directions provided on the page. Failure to submit the assignments according to these directions may result in a loss of points!  

Take the screen shot of your web page as it appears in your browser after you play the game so it shows values in the Score and Highest Score! 

 [link: #top] Top

---

## My Submission

**Score:** 0.0/30.0
**Grade:** 0
**Submitted:** 2023-10-16T03:49:45Z

### Submitted Files

- **extra_credit.docx**
  - Downloaded: `files/extra_credit.docx`
