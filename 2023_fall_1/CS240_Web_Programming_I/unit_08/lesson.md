# Unit 8: Lesson

Writing Web Programs with JavaScript and the Canvas Element

Rather than provide separate lectures, we are going to ask you to read your textbook. We want you to read your book and take your own notes. Here are some notes we thought were most important or needed additional reinforcement or clarification. 

There are some excellent examples in the book, such as the umbrella, smiley and Microgrid examples. Please review all of them. 

Chapter 12 Using Canvas

 [link: #top] Top

Canvas  

This chapter is very easy to review. You'll find that drawing with 2D and 3D elements is very similar to other programming languages. That's the beautify of using JavaScript. This chapter shows you the basics of the canvas element. Some of the basic shapes we draw include rectangles, squares, circles, and ellipses. We fill them with solid colors, linear gradients and patterns. You can also include images, canvas or video as your output.  

So how does the canvas compare to other drawing tools? Look at this waterfall example from effect games by  [link: http://www.effectgames.com/effect/article-Old_School_Color_Cycling_with_HTML5.html] Canvas Cycle: True 8-bit Color Cycling with HTML5. Art by  [link: http://www.markferrari.com/] Mark Ferrari Code by  [link: https://twitter.com/jhuckaby] Joseph Huckaby.  [link: http://www.effectgames.com/demos/canvascycle/]   [link: https://twitter.com/jhuckaby] Ben Joffe Demos at  [link: https://www.benjoffe.com/code] https://www.benjoffe.com/code [link: https://twitter.com/jhuckaby]  has several examples including the Ninja Maze and CanvasScape 3D Walker. The example of the Waterfall is beautiful. Retrieved from  [link: http://www.effectgames.com/demos/canvascycle/] http://www.effectgames.com/demos/canvascycle/. Other useful (optional) resources include:

Canvas  [link: http://www.html5canvastutorials.com/] http://www.html5canvastutorials.com/HTML

Tutorials  [link: http://www.html5canvastutorials.com/tutorials/html5-canvas-element/] http://www.html5canvastutorials.com/tutorials/html5-canvas-element/

 [link: http://www.html5canvastutorials.com/tutorials/html5-canvas-element/] Dive Into HTML (Free!)  [link: http://diveintohtml5.info/canvas.html] http://diveintohtml5.info/canvas.html –  [link: http://diveintohtml5.info/table-of-contents.html] http://diveintohtml5.info/table-of-contents.html

HTML Canvas –  [link: http://www.w3schools.com/tags/ref_canvas.asp] http://www.w3schools.com/tags/ref_canvas.asp

 [link: #top] Top

Canvas Element

The canvas is just like a painting canvas, an identified space to put your content. Canvas properties include the height and width as well as alternative content for browsers that don’t support canvas. Most modern browsers do support canvas. You can set style rules such as border because canvas is an html element. So the canvas has access to many of the global HTML properties. 

<canvas id="canvas" width="480" height="250">
  Sorry - This page uses <code>canvas</code> and your browser doesn't support it.
</canvas>

In the JavaScript, you can access the canvas. The HTMLCanvasObject provides access to a canvas object through the getContext method, where you can insert and manipulate images, text and custom drawings and animations. The drawImage method will help you draw your content on the page. To draw you need to use the getContext method to create a context object (2D or 3D) to expose the graphics tools.

<script>
var canvas = document.getElementById("canvas");
var ctx = document.getElementById("canvas").getContext("2d"); 
</script>

 [link: #top] Top

Canvas Drawing Tools  

Drawing Elements: Rectangles and Squares

When you draw shapes you pass the values used by the mathematical formula to draw the shape. Squares are simply height * width. So the program needs the x, y coordinates and height and width property. You need to watch how you pass the variables. For all the rectangles pass the values as (x, y, w, h).

You can create a filled (fillRect) or unfilled (strokeRect) or clear an area in the shape of a rectangle (clearRect). When you are ready to draw use stroke which draws the outline of the shape, and fill which draws and fills the shape. 

context.fillRect(x, y, width, height);

By using clearRect you can remove any shape anywhere on the canvas. Just set the rectangle coordinates to the entire canvas dimensions! Here are two different ways to clear the canvas. 

ctx.clearRect(top-left-x, top-left-y, width, height);
ctx.clearRect(0, 0, canvas.width, canvas.height);

You can pass values as variables, expressions or numeric values.  

ctx.fillRect(20, 80, 70, 140);

Properties that you can configure include lineWidth, lineJoin (such as miter, bevel and round), lineWidth, strokeStyle and fillStyle (which provide color options). Usually call strokeStyle before fillStyle. 

context.strokeRect(x, y, width, height);

Here is an example.

ctx.lineWidth = 20; 
ctx.strokeStyle = "red";
ctx.fillStyle = "deepskyblue";
ctx.strokeRect(140, 80, 70, 140);

Colors and Gradients

Colors can be configured as solid colors or gradients (linear, radial). Pass colors using RGB values, rgb(r, g, b) or a CanvasGradient object. So first, you create the gradient object, than assign that gradient object to the style. 

You can create linear gradients using createLinearGradient (x1, y1, x2, y2) or radial gradiants using  createRadialGradient (x1, y1, r, x2, y2). You also will use the addColorStop (position, color) methods to identify when the changes in color should occur.

The ‘stops’ are relative (0-1) based on the whole selected area. So it’s a percentage. You can add additional stops. This is the syntax. 

gradient.addColorStop(offset, color);

Here is an example that applies the gradient to the fill style. 

gradient = ctx.createLinearGradient(0, 50, 0, 250);
gradient.addColorStop(0, "green");
gradient.addColorStop(0.5, "yellow");
gradient.addColorStop(1, "blue");
ctx.fillStyle = gradient;

Drawing Text

Text is also drawn to the canvas. Stroke and fill do the same thing except the strokeSyntax will provide outline of the text. Here is the  syntax. 

context.fillText(text, x, y, max-width);
context.strokeText(text, x, y, max-width);

You can set the properties of the font.

ctx.font = "2em 'Times New Roman', serif";
ctx.font = "100px sans-serif";

You can use the fillStyle and lineWidth and other properties too. Draw the text with filltext(text, x, y, w) and strokeText(text, x, y, w).

ctx.fillText("Hello", 50, 100);
ctx.strokeText("Hello", 50, 100);

Other properties include textAlign (start, end, left, right, center) and textBaseline (top, hanging, middle, alphabetic, ideographic, bottom).

ctx.textAlign = "center";

Drawing a Line

Here is the syntax for a line. MoveTo moves to the coordinates without drawing a subpath. LineTo keeps drawing the line as the pen moves. The syntax is lineTo(x,y) 

context.moveTo(starting-x, starting-y);

Example

ctx.strokeStyle = "red";
ctx.lineWidth = 4;
ctx.beginPath();
ctx.moveTo(40, 20);
ctx.lineTo(80, 20);
ctx.moveTo(90, 20);
ctx.lineTo(130, 20);
ctx.moveTo(140, 20);
ctx.lineTo(180, 20);
ctx.closePath();
ctx.stroke();

Drawing a Images

You can draw an image on the canvas using drawImage and pass the image element, and parameters. You can pass different parameters. 

The arguments passed can be just the image and the x, y coordinates of where you want the image. In other words, how offset do you want the image to be drawn from the 0,0 coordinate? The second example code, you add the height and width of the image. 

ctx.drawImage(imageElement, 10, 10);
ctx.drawImage(imageElement, 120, 10, 100, 120);

You might be thinking of how the other tools could enhance your canvas application. You can draw lines, rectangles, arcs, bezierCurves and quadratic curves, clip drawings, draw text with fillText or strokeText, add shadows, and transform the canvas with rotate or scale.

 [link: #top] Top

Drawing a Line using a Path Object

You might have experience using programs like Adobe Illustrator or Photoshop. When you use the pen tool in these programs you are creating a path. In HTML we also work with paths, which are just individual lines connected.

So path methods are just the same as we have when we use the pen. All of these methods and properties are accessible via the context object using the getContext method of the canvas object. 

We have beginPath to start a new path, and closePath to draw the last line to the starting coordinates. In between you might use tools to draw subpaths such as and rect(x, y, w, h) and arc. Here are some additional methods. 

The isPointInPath(x,y) returns a boolean value if the coordinates is within the shape created by the path.

The lineCap sets the shape at the end of the line (butt, round or square).

You also use stroke and fill methods. You still have access to things like fillStyle, strokeStyle and lineWidth.

Drawing circles, ellipses and angles using Arcs 

You can draw arcs as your path. The x, y coordinates are the coordinates for the center point. 

context.arc(x, y, radius, start-angle, end-angle, counterclockwise);
context.stroke();

This example draws half a circle. 

ctx.arc(80, 35, 25, .5 * Math.PI, 1.5 * Math.PI);
ctx.fill();
ctx.stroke();

Effects and Transformations

The two most common effects are shadows and transparency.

 

Shadows

Shadows can be modified by setting the degree (number) of the blur (shadowBlur), and the x,y offsets (shadowOffsetX, shadowOffsetY) and the shadowColor. Shadow can be applied to lines, paths, arcs, shaped and text.

ctx.shadowOffsetX = 5;
ctx.shadowOffsetY = 5;
ctx.shadowBlur = 5;
ctx.shadowColor = "grey";

Transparency

In the reba function, RGB sets the color and Alpha sets the transparency level. Alternatively you can use the globalAlpha property of the context object. The values are relative from 0 - 1, where 1 is completely opaque. It’s a context property so, the settings are saved until you change them back.

ctx.globalAlpha = 0.5;

 [link: #top] Top 

 [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
