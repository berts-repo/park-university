# Unit 2: Lesson

Working with HTML and CSS

You learned previously that some HTML elements like <center> and <font> are deprecated and can only be fixed by using style sheet rules. This week you will learn about style sheet rules. Browsers or user agents styles set the defaults for that browser. For example, links are blue and underlined by default. As web programmers, we can change these styles using style rules. 

We have already some style rules briefly in the previous chapter. We will spend more time on using style rules this unit to format your content. You should be thinking about how to use HTML elements and CSS style rules to to layout and format the content of your pages. 

Please make sure you read your textbook and review all of the samples in the chapter.  

We want you to read your book and take your own notes.  You are expected to view the sample code and take notes on your readings as you study. This page will help you to focus on the main parts that you will want to review. 

Chapter 3 Cascading Style Sheets (CSS)

Chapter 4 Organizing a Page's Content with Lists, Figures, and Various Organizational Elements 

 [link: #top] Top

Style Properties

Formatting Font Style Rules

A style rule is simply a description of how to format the content within the HTML elements. Text, tables, lists, images, hyperlinks and other HTML elements can all be formatted with style rules. 

The text of the style rule is formatted with various properties. There are several properties related to the appearance of the text. The color and font style rules are usually the first style rule to learn. Color is simply the color of the text. Background-color is the highlight color of the area behind the text. For fonts with spaces in the font-family name, make sure to use quotation marks. You may list more than one font if they are separated by commas. If the browser does not support the first font family, then the next font in the list will be used. Here are several examples of style properties. 

color: #FF0000;
text-decoration: underline;
font-size: 20pt;
font-family: "Times New Roman", serif;
font-style: italic;
font-weight: bold;
font-variant: small-caps;

It is not uncommon for beginners to make mistakes on syntax and use font-color instead of color or font-decoration instead of text-decoration when they want to underline text. Krzysztof Domański started a petition to W3 to  [link: https://www.change.org/p/world-wide-web-consortium-introduce-the-font-color-css-property?recruiter=238928026&utm_source=share_for_starters&utm_medium=copyLink] introduce the "font-color" css property but it only had 18 signers!   

 [link: #top] Top

3 Types of Style Rules

Make sure to review the difference and the syntax for inline, embedded (internal) and external (linked) style sheets.

Placement of Style Rules

The inline style rules uses the style property within the html element. (<p style="color:red;font-size:10pt;">Hello</p>)

Embedded style sheets use the <style> element and usually are in the head section within a single web page. The rules are places inside the style tags. <style>p { color:red; font-size:10pt; } </style>

External style sheets are CSS files that are linked to the web page using the <link> element. External CSS files do not use any style tags. Just the rules are stored in the external style sheet. The format of the style rules in external style sheets are the same as the format for embedded style rules. 

The rules inside the curly braces show the name and value pairs, separated by a colon, with each pair separated by a semi-colon. The rule name is the HTML element, class or other selector to indicate what element on the page you want to apply the style rule. The property is the style property, such as width, color, background-color, font-size, font-family, padding and margin. The value is the value you want to be configured. 

Rule name {
   property: value; 
   property: value;
} 

This is an example of a style rule where we set the property and value inside of an HTML element.

p { 
    color:red; 
    font-size:10pt; 
} 

Comments in embedded and external style sheets are written like this: 

/* comment goes here */

Notice the indentation in the style rules! This is important because it will help you to locate errors. Normally I put the braces on their own lines, to make it easier to locate. But in books and other places we sometimes put it on the same line as the class name, so that it's shorter code. For this class, please put the { } braces on separate lines.  Some elements such as font-size require a unit of measurement. Often font-size is measured in pixels or px. 

 [link: #top] Top

Inline Styles - Style Property

Style rules can be configured within an individual element, called an inline style rule. The tag uses a property called style. These styles would only apply to one element. 

Shorthand Properties

Some properties like background, border and font, can combine multiple property values into one rule called a shorthand property. 

h2 { font: #FF0000 20pt "Times New Roman"}

If you can't decide on a font, read  [link: https://design.google/library/choosing-web-fonts-beginners-guide/] Choosing Web Fonts: A Beginner’s Guide by Google Fonts. Always include a backup font. Serif fonts such as Times New Roman have small lines or decorations on some characters. Sans-serif such as Arial and Verdana do not have these decorations.

You can pass the color and font style rules as a string of name and value pairs as shown in the example below. These styles would only apply to that one tag. 

<h1 style=color:red; font-size:12pt; text-align: center">Hello world</h1>

Updating Obsolete Tags with Style Rules

Older HTML tags used to be used to format your content. Today instead of using <b> or <i>in this class, you should be using <strong> or <em>. Better yet, use CSS to format the style for bold and italic. 

<p style="font-style:italic; font-weight: bold;">Hello world</p>

Browser Support

You should be aware the browsers vary on support for some properties just as they do with HTML elements. The  [link: https://www.w3schools.com/cssref/css3_browsersupport.asp] W3Schools made a list that you should refer to if you are having issues displaying a rule in the browser.  

 [link: #top] 

 [link: #top] Top

Embedded Style Rules - Style Element

Style rules are more flexible than HTML properties and can be easily applied across multiple elements within the same page. Style rules can be configured for an entire page in an embedded style sheet. The embedded style rules for the entire page are grouped together within a style tag. 

These styles would only apply to any element that matches the selector within the web page. Later you will see that selectors can be configured to aggregate multiple HTML elements within the same rule if the selectors are separated by commas. 

<style>
h2 {
    color: red;
    font-size: 12pt;
    text-align: center;
}
h3, h4, h5 {
    color: green; 
}
</style>

Minimized Style Rules

Don't be surprised if you see code that is minimized where the spaces are removed. The browser can load these files faster. But editing them is not user friendly. In this class, do not minimize your code!

<style>.class1{text-align:center; color:#ff0000;/* Red */}</style>

 [link: #top] Top

External Style Sheets - Link Tag

Style rules can be configured within a separate file, called an external style sheet. 

This allows the selectors to configure the styles of elements on all of the pages within your web site if the web page is linked to the external style sheet. The link element is used mostly to link to a CSS or JavaScript file or a favicon. You may link the external style sheet with a <link> tag. You need to specify the location of the style sheet using an absolute or relative path to the file. An absolute path would be something like http://www.park.edu/css/project.css.  

Relative Paths

Note that below you can see that the path might be different. In your application, the CSS files are stored in the CSS folder. So for your href property you need to provide a relative path. The . . is like in the command line, representing the parent location. If you have not worked with file paths you should review that section of the book or read about  [link: https://www.w3schools.com/html/html_filepaths.asp] relative paths on the W3Schools site. The second example is how you will insert style rules into your homework web pages. Some editors may not include the type attribute!

<link rel="stylesheet" type="text/css" href="styles.css"   />
<link rel="stylesheet" type="text/css" href="../css/styles.css"   />

Then in the CSS file you would add the style rules, without the style tag. No script tags are used in this file. The syntax is otherwise identical. 

h2 {
    color: red;
    font-size: 12pt;
    text-align: center;
}

Select the Styles Based on the Media and Resolution

You can specify when to apply the style rules.  Simply specify the media type, to provide custom styles for different devices (media=“print”, media=“screen”). You can further customize the default resolution of the page with customize this with min-, max-. Properties which are helpful for customizing layout include device-width, device-height, resolution (600dpi), orientation (portrait or landscape) and others.  

<style media="screen AND (max-width:500px)" type="text/css">
     a {
        background-color: grey;
        color: white;
        padding: 0.5em;
     }
</style>
<style media="screen AND (min-width:500px)" type="text/css">
      a {
        color:red; 
        font-style:italic;
      }
</style>

 [link: #top] Top

CSS Selectors and Classes

Remember that selectors are used to identify which element(s) you want to style in the web page and there are several ways to locate these element(s). You can apply a style to multiple elements by separating them with a comma, saving you space and typing and time maintaining the code. These are the most important selectors that you should study!

Universal Selector:   * {color:red;}

Element Selector:   h2 {color:red;}

Combine Element Selectors:   h2, h3, h4 {color:red;}

ID Selectors:  #myImage {color:red;} 

Class Selector:   .class1 {color:red;}

Use generic class selector:   .class1 {color:red;}

Combine Class selector with specific element:   h1.class1 {color:red;}

Universal Selector

The universal selector ( * ) applies the style rule to all elements. You can select all of the elements using the universal selector (*) or some programmers use html or body element selectors since all the other elements will inherit from these two elements. More often, the body element is used to configure all of the elements within the page. This might be used to provide the default font and layout. Remember elements may inherit the style rules from the parent element. 

* {
    color: red; 
}
html {
    color: red; 
}
body {
    color: red; 
}

Element Selector

We first used basic tags in the style sheet to modify the styles. But then all of the h2 elements in the page were red! 

h2 {
    color: red; 
}
p {
    color: blue; 
}

ID Selector ( # )

So we moved to organize h2 elements based on ID properties. The ID selectors are identified by placing a hashtag ( # ) before the class name. 

<h2>My color is red</h2>
<h2 id="bluecolor">My color is blue</h2>
<h2 id="redcolor">My color is red</h2>

You could specify all of them to be red. But the h2 that has the id set to the "bluecolor" class would be blue.  But only 1 element would be styled blue!

h2 {
    color:green; 
}
#bluecolor {
    color:blue; 
} 
#redcolor {
    color:red; 
} 

Class Selector ( . )

This is a very important type of selector to learn how to use. Classes were a way to allow the style to be used for more elements, and for different types of elements. This is why using classes is so popular. Each class is a custom name of a set of stye rules as shown below. The class selectors are identified with a period ( . ) before the class name. Each class is a name of a set of stye rules as shown below. In other words you get to pick the name of the class, 

.bluecolor {
    color: blue; 
} 
.redcolor {
    color: blue; 
} 

To use this class rule, simply specify the class name using the class attribute inside the HTML element that you want to configure. You can then apply the style rules to a variety of HTML elements.

<h2 class="redcolor">My color is red.</h2>
<p class="redcolor">My color is red too!</h2>
<h2 class="bluecolor">My color is blue.</h2>
<p class="bluecolor">My color is blue too!</h2>

Combining Style Rules (   )

You can assign multiple classes to one element, by assigning them in the class property as shown below. The list of classes are loaded in order. So in this case class2 takes precedence over class1. Notice that a space is between the class names. 

<a class="class1 class2" href="http://mycompany.com">My web site</a>

In this example, all three classes are applied to the content. If there is a conflict in the styles, the last style value loaded override the other style rules.

<p class="red thinborder centeredtext defaultfont;">Welcome to our site!</p>

It's common to see companies use third party CSS style sheets which have common classes predesigned!

Union Selector: ( , )

Using selectors with a comma will create a list of selectors. You can combine multiple selectors and assign them to the same style rule, which will save you time. Just separate the selectors with a comma ( , ). You can mix and match selectors and assign them to the same style rule as shown below. 

h2, h3, h4, h5, h6 {
    color:red; 
} 
.mylinks, .mybookmarks {
    color:red; 
} 
h1, .bluecolor, #houseColor {
    color: blue; 
}  

Competing Style Rules

If the color of the element was set in these three places with different values there can be conflicts over which rule takes precedence.

Inheritance means that the element will take the style rule from the parent. Elements inherit styles from the parent, and the other style rules. 

p { color: inherits; }

We often use classes to group style rules that can be applied to many different elements at the same time. 

.myclass { color: green; }
<p class="myclass">Hello world</p>
<a class="myclass" href="http://helloworld.com">Hello world</a>

You can combine the element selector and the style name to be specific. The link would be black.

.myclass {  color: green; }
a.myclass {  background-color: blue; }
p.myclass { background-color: red; }
<a class="myclass1 myclass2" href="http://w3c.org">Visit the W3C website</a> 

Remember that cascading style rules are like a waterfall. The closest rule to the element usually wins. So inline style rules trump embedded style rules and embedded style rules trump external css file

Inline styles (styles that are defined using the style global property on an element)

Embedded styles (styles that are defined in a style element)

External styles (styles that are imported using the link element)

User styles (styles that have been defined by the user)

Browser styles (the default styles applied by the browser)

Overriding Style Rules

You can override the normal inline order using !important. The only thing that can overrule this is the !important in the user stylesheet.

a { color: black !important; }

There are many other selectors in the chapter you can review. However, the majority of your work in this class you will be using the selectors previously mentioned. Use the other information as a reference, especially when you are interpreting another programmer's style sheet!

 [link: #top] Top

Using Colors in Style Rules

Notice that the values for color may be one of the named colors, rgb values and hexadecimal values. Your book doesn't spend as much time on this so I'd like to explain this further. 

The good news is that many editors provide Color Pickers to select the color you want to display in the web page. Often, the colors are determined by the company marketing or public relations department to provide consistency with branding. 

Named Color Values

In the beginning we just used the 16 named colors in Windows. Over time we used the X11 colors distributed with the X Window System. If you are using an editor that supports IntelliSense the editor may provide a list of color names to choose from. Today you can view the  [link: https://www.w3schools.com/Colors/colors_names.asp] W3Schools list of supported color names. 

RGB Color Values

The RGB values range from 0 - 255 (8-bit) for each red, green and blue hue color. The first decimal value represents red, then green, then blue (Which explains the order of RGB). You have 256 shades of a color, from no color (0) to maximum color(255). You should know the major colors in RGB, hexadecimal and decimal values for the final exam. 

rgb(0, 0, 0) means no color, no red, no green, no blue so the color is black. The absence of color is black

rgb(255, 255, 255) The maximum colors together make white

rgb(255, 0, 0) means the maximum value for red, no green and no blue, so the color is red

rgb(0, 255, 0) means the maximum value for green, no red and no blue, so the color is green

rgb(0, 0, 255) means the no red, no green and the maximum value for blue, so the color is blue

Values in the middle are the hues or shades. So rgb(128, 0, 0) means the middle color value for red, no green and no blue, so the color is maroon. The same goes for blue and green. Lighter shades have higher color values. So rgb(128, 0, 0) is a darker color than rgb(192, 0, 0).

We can mix colors. You should know the major colors: white, black, red, blue, green, cyan, yellow and magenta. (color, hex and decimal values).

Mixing all red and green looks like rgb(255, 255, 0) and becomes yellow.

Mixing all green and blue looks like rgb(0, 255, 255) and becomes cyan (a bluish color).

Mixing all red and blue looks like rgb(255, 0, 255) and becomes magenta (a purplish color) 

You can specify the decimal values using rgb(r, g, b) or rgba(r, g, b, a), where a is alpha for opacity. Transparent is 0 and opaque is 1. Although Hue, Saturation and Lightness (HSL) is used with printing, it is not often used for web colors. 

Hexadecimal Color Values

Remember hexadecimal values represent 16 digits. So hexadecimal values have digits that range from 0 through 9 then A through F. We use hexadecimal values so more values can be represented in one digit. So 256 values can be represented in two hexadecimal digits, compared to the three values in decimal format.

So the decimal value 10 is represented as A in hexadecimal, and the value 16 is represented as F. 

Expanding this to two digits, 0C represents 12. We know that 0 means 0 and C means 12 because C is the 12th digit. The solution equation would be (0 * 161) + (12 * 160). So this resolve to (0 * 16) + (12 * 1) = 12

C0 represents  --> (12 * 16) + (0 * 1) = 192

AA represents  --> (10 * 16) + (10 * 1) = 170

AC represents  --> (10 * 16) + (12 * 1) = 172

FF represents  --> (15 * 16) + (15 * 1) = 255 

The first pair of digits in the hexadecimal value, represents red, then green then blue. You do not represent the hexadecimal value as a single digit. Why? There are 256*256*256 color combinations or 16,777,216 colors. No one would remember what color is 8,400,321.

Just evaluate each pair, not the entire hexadecimal number! For 00FF00 there is no red, no blue but all green, so the color is green. This can also be represented as rgb(0, 255, 0).  

A hashtag ( # ) precedes any hexadecimal color value. You can use upper or lower case.

If the hex value contains pairs such as #00CCDD you can minimize or shorten the value, in this case to #0CD. 

 [link: #top] Top

Using CSS Properties to Format Text

You learned already about how to create an inline and embedded style rule, classes and how to configure style rules. We’ve already discussed the color and font properties. It's important to know that usually when we talk about HTML we talk about elements and properties. Then we talk about those properties styled in CSS we call them properties. In many cases the attribute and property are the same name. 

Of course there are going to be many ways to format the text content. Text can be configured using CSS properties rather than the default. Instead of using the blockquote element, you can use the text-indent property in a style rule. 

There are many properties and we can’t cover them all here. We’ll cover the one’s most commonly used. Remember, some of the properties are useful to know, but we don’t necessarily memorize them because we don’t use them every day. So keep that in mind. 

Font allows you to configure the family, size, weight and style such as font-size, font-family, font-weight and font-style. 

Font-variant allows you to also use a font-variant, to allow you to use normal or small-caps.

 Text-align is used commonly to center the text (left, right, justify, center, start, end). 

Text-shadow is like the box-shadow but focuses on the text object only.

Text-decoration allows you to decorate the text. You can set the values to underline, blink, line-through and overline. Often we use text-decoration to remove the underline in hyperlinks. 

Text-indent is really helpful when you want to indent just the text within a container. 

Text-transform is also useful to change the default (none) to capitalized, uppercase and lowercase.

Direction is used to identify the direction to draw the line.You can change the word-wrap.

You can change directions from ltr to rtl.

Word-wrap controls word wrapping. The default (normal) words are not broken, and break-word the words are broken to fit the element.

Text-shadow let's you add a shadow to the text as opposed to a box or image. 

Line-height is commonly used to add spaces between lines to make the content more readable. It is common to use line-height with a relative value like 1.5em.

Justify allows you to modify the paragraph and text spacing. With justify you have expanded styles using text-justify. You can use the default (auto) or none, or, modify the distribution between the words (inter-word) and other methods (kashida, distribute, inter-ideograph and inter-cluster)

Whitespace is a property that allows you to change the default (normal) which collapses white space with content with more than one space. Before we talked about whitespace in the source code and how browsers ignore it.

Nowrap is used to collapse whitespace but not lines or pre, to preserve whitespace but only wrap on line breaks.

Other properties included letter-spacing and word-spacing. 

<style>
p {
   direction: rtl;
   letter-spacing: 2px;
   line-height: 3em;
   white-space: pre-line;
   word-spacing: 10px;
   word-wrap: break-word;
   text-indent: 15%;
   text-transform: uppercase;
   text-decoration: line-through;
   text-shadow: 5px 5px 20px black;
   font-family: "HelveticaNeue Condensed", monospace;
   font-size: medium;
   font-weight: bold;
   font-style: italic; 
   text-decoration: underline; 
}
</style>

Create shadows and glow effects with the text-shadow property.

To create a text-shadow you pass the values. from the text and blur is the degrees of blur. Values can be relative or absolute measurements (em or px).

The text-shadow syntax in order is the horizontal shadow-offset (h-shadow), the vertical shadow-offset (v-shadow), the blur-radius (blur) and the shadow color. The h-shadow and v-shadow are the shadow offset. Blur is the amount of blurring of the shadow. Change the shadow size and colors to the size and color of your choosing. 

.textshadow-dark {
    /* Create a class to create a text shadow */
    /* Text-shadow syntax: h-shadow-offset v-shadow-offset blur-radius color */
    text-shadow: 3px 3px 4px #333;
}

Notice for the glow effect, multiple layers of shadow are applied one after another, separated by commas. 

.textshadow-glow {
    /* Create a class to create a text shadow that glows */
    text-shadow: 2px 2px 4px #ffd800, 0 0 25px #ffd800, 0 0 5px #048703;
}

When you are just learning to program it's helpful to write the syntax in a comment above your code, to make sure you entered the right values in order.

 

 [link: #top] Top

Border Properties

The border, border-width, border-style, border-border-image and border-color are commonly used. 

Border-width can be expressed as a length in em or px units, a percentage based upon the area, or choose an option (thin, medium, thick).

Border-style can be set to none, solid double, dotted, dashed. Groove makes the border appear sunken while inset makes the content looks sunken.  Ridge make the border look sunken while outset makes the content look sunken. 

Border-image can be useful but has limited support across browsers. 

div {
   border-collapse:collapse;
   border-width:thin;
   border-style:solid; 
   border-color:#F30307;
   border-image: url(images/border.png) repeat;
}
p { border-width: 5px; border-style: solid; border-color: black; }

Shorthand Properties

Remember you can set properties for the entire border using the border propery, or you can specify a side (border-top, border-bottom, border-left, border-right). Many of the properties can also be set individually such as border-left-width, border-bottom-color and border-top-style.

Border allows you to use the shorthand property so you can save space typing and decrease maintenance. Below is an example using the shorthand property.

div { border: 5px;  solid;  black; }

Border Radius to Create Rounded Borders

Fun properties include the  border-radius which applies curved borders for one or more of the corners. You can use units or percentage for the radius. 

In the code below, the radius 20px is measured from the X (left margin) and 15px from the Y (from the top margin down into the content. This would create an oval effect.

div { border-top-left-radius: 20px 15px; }

The second example modifies all of the corners for a hand-drawn border effect.

div { border-radius: 50% 20px 25% 5em / 25% 15px 40px 55%; }

 [link: #top] Top

Background Properties

Background Color

The background-color is commonly used. Be careful! Many times if you set the background color you need to modify the text color with a contrasting color so the text shows up!

body {
   background: #000000 ; 
   color:#FFFFFF ; 
}
main {
   background: #FFFFFF ; 
   color: #000000; 
}

It's important to use contrasting colors so that your web page is compliant with accessibility standards. WebAIM provides a  [link: https://webaim.org/resources/contrastchecker/] Color Contrast Checker that can help you verify if your colors are compliant with accessibility standards.  

Background Image

You can set the background-image for the entire page, or an element. Note that the URL is required to identify the file based on the relative path. 

Beginning students often forget this!

body {
    background-image: url("background.png"); 
}
p {
    background-image: url("background.png"); 
}

You can set the background-size. The background-size can set the image to a specific size such as 100px by 100px, or relative size ( % ). By default the size is set to auto which is full size. You can set the image size to fix the size contain is the largest size so you can guarantee to see the picture inside the element and cover is the smallest size so not all of the image may be displayed) and preserve the aspect ratio. Using the cover value will scale the image and space to fill the space. 

header  {
   background-image: url("background.png");
   background-size: cover;
}

You can set the background-repeat to tile or repeat across the element. Specify if you want the image to repeat only horizontally using repeat-x or just vertically with repeat-y. You can repeat both horizontally and vertically using repeat. If you set the property to no-repeat then just one instance of the image will be displayed. 

You can set the background-attachment to fixed so the image stays in place or scroll so the image scrolls with the page content. 

You can also set where you want the image to be drawn. Background-position will let you change the position from the default x, y coordinates of 0,0 to other coordinates in the element or you can use a named position (left center, right top). Likewise, you can set the background-origin and background-clip properties to draw within the border (border-box), the padding (padding-box) or the content only (content-box).

p {
    background-image: url("background.png");
    background-position: center top;
}

Shorthand Properties

Background allows you to use the shorthand property so you can save space typing and decrease maintenance. Below is an example using the shorthand property.

div {
   background: #FF0000 url("background.png") no-repeat center; 
}

 [link: #top] Top

The Box Model

The box model is very important to understand. The main thing is you can change the attributes like margin, border, padding, and the content on one or all sides of the content using top, bottom, right and left attributes. Some of the attributes are not fully supported across all browsers yet such as overflow-style and marquee attributes such as marquee-direction, marquee-loop, marquee-play-count, marquee-speed and marquee-style). 

Each object has a box model. You can see in Figure 1, that the model includes padding, border, margin and the page offset. The values are different depending on the element and your style rules. The figure below is a graphical representation of the box model for an element as viewed in the Google Chrome browser. 

Margin is between the margin edge and the content.

Padding is between the border and the content. 

Figure 1 The Box Model

The Common Box Model properties include the margin (and for each margin- side), with the min-, max- and height, padding, width, overflow and visibility. These are properties that apply to most of the HTML elements. 

padding-top: 0.5em;
padding-bottom: 5em;
padding-right: 10px;
padding-left: 10px;

Remember that you can specify the values for each side or combination. You  can remember the order using the acronym 'TRouBL' which means top, right, bottom and left. 

padding: 5px 10px 15px 20px;      /* TRBL */
padding: 5px 10px;                /* TB LR */
margin: 10px;

You can modify the box-sizing (using content-box, padding-box; border-box, margin-box), with a properties such as width, right, max- and min- width and height. You can manipulate what to do with the overflow content using overflow, overflow-x and overflow-y. You can change the overflow to auto, hidden, no-content, no-display, scroll or visible. 

 [link: #top] Top

Margin and Padding

The margin and padding properties allow you to modify the position of the content separately for each area (left, right, top, or bottom or combinations). Students can be confused because these properties can have multiple ways to configure the values.

padding-top: 20px;
padding-bottom: 20px;
padding: 20px;                 // All 4 values are the same
padding:10px 5px 15px 20px;    // Top, Right, Bottom, Left   
                               // --> You can remember this is TRBL (TRouBLe!)
padding:10px 5px 15px;         // Top, Right=Left, Bottom
padding:10px 5px;              // Top=Bottom, Left=Right
margin-bottom:10px;
margin 0px auto;               // Use auto to center the body. 

 [link: #top] Top

Other Properties

Visible is also useful with dynamic sites where you can change the visibility attribute in JavaScript. You'll learn how to do that later in the course when we cover JavaScript. You can change the visibility to: visible, hidden (the element still occupies space) and collapse (no space required).

The display property is commonly used to set the type of box and is most often set to block. Block elements are vertically distinct, similar to the div element. You can set the values to block (default, like the p or div elements), inline (like a word in a paragraph, similar to the span element), inline-block (inline on the outside and block on the inside), run-in (varies with the elements around it) and none. Your book has some useful pictures and examples. There is also a new flexbox option which we'll cover later. 

Float is commonly used and very important because it lets you float the element on the left or right side of the page and the content can wrap around the element. We use it often for images as well as asides.

Clear is also commonly used to prevent a floating element from being next to another floating element. I often use this before the footer element to prevent the body of the page from impacting the footer.

<style> 
  aside {
    width: 75%;
    border: 10px double black;
    padding: 10px;
    background-color: lightgray;
    background-clip: content-box; 
    border-radius: 1em 4em 1em 4em; 
    box-sizing: border-box;
    height: 100px;
    width: 50%; 
    min-width: 100px; 
    max-width: 200px;
    overflow:hidden;
    float: right;
    clear: all;
  }
</style> 
<aside>Put an ad here.</aside> 
<p>This is the main part of the page.</p>

 [link: #top] Top

Box Shadow Property

The box-shadow  applies a drop shadow to one or more of the sides. 

You can change the horizontal and vertical offsets (hoffset, voffset) as well as the spread, blur, color and inset. Apply multiple shadows with a comma. This is useful for a 3D effect. The shorthand rule expects the properties in this order

box-shadow: hoffset voffset blur spread color inset;
box-shadow: 5px 4px 10px 2px gray, 4px 4px 6px gray inset;

Outlines are an alternative to border and can be useful to dynamically focus the user on an element and because outlines do not alter the page layout! You can change the outline-color, outline-offset, outline-sale (like border-style), outlines-width (thin, medium, thick or a relative length) such as outline: div { thick solid red; }.

 [link: #top] Top

Units 

Most of the units you will use are in pixels.

font-size: .8em;
td.width: 50%;
font-size: 2rem;
width: calc(80% - 20px);

Change the units could be relative where 1.0 is the same size.  Rem is relative to the root (html) stye rule. The vw and vh are relative percent to the viewport (browser) width and height. Other units are used for drawing with JavaScript. For example deg for degrees (1-360), s for seconds and ms for milliseconds (1/1000 second).You can also now use calc to  calculate the value in Internet Explorer only.

 [link: #top] Top

Browser Support

Some browsers don’t support all the new standards. So, browser specific prefixes were used to help provide a workaround.

So you could use border-radius in a style rule, but if you want it to work across other browsers like Chrome, you would use -webkit-border-radius.  Different browsers use different prefixes. The level of support for CSS3 and browsers varies. So please refer to the online CSS3 documentation for the most up to date support. 

Chrome and Safari use -webkit-

Opera uses -o-

Firefox uses -moz - 

Internet explorer uses -ms-

 [link: #top] Top

List Elements

List elements have similar properties and style rules to other elements, except they need additional properties to describe the bullet or numeric styles used.

The ol element (numeric and sequential) is for ordered lists and ul for unordered lists (bulleted). Both ol and ul include child list item elements, identified by the li element. Description lists are useful to show terms (dt) and the definition (dd) which is indented by default. The sample web site shows you examples with nested lists.

The type attribute allows the ordered list items to be numbers (type="1"), lowercase letters (type="a"), uppercase letters (type="A"), upper/lower case roman numerals (type="I" or type="i").

The type attribute can be set for unordered lists to none, disk (type = "disc"), circle (type = "circle"), or square (type = "square"). If you want to set the list items to use a bullet image set the property to none. In CSS you can configure the list item to use a specific image. 

The li element allows you to specify additional properties for individual list items within an ordered list, unordered list or menu. List items in ordered lists can also have a value assigned. 

DEBUGGING TIP: 
As you can see below, you can also nest lists. However, make sure that you properly nest the list within a list item element!

<ol type="A">
    <li>Monday</li>
    <li>Tuesday: 
          <ul>
             <li>Sunny</li>
             <li>Warm</li>
             <li>78 degrees</li>
         </ul>
    </li>
    <li>Wednesday</li>
    <li>Thursday:
         <ul>
             <li>Cold</li>
             <li>50% chance of rain</li>
             <li>66 degrees</li>
         </ul>
    </li>
    <li>Friday</li>
</ol>

List CSS Styles

List-items can be configures using CSS properties. Other list-related properties include list-style, list-style-image, list-style-position and list-style-type. The list-style-type property in CSS can set the list item marker to none, box, check, circle, diamond, disc, dash, square, decimal, binary, lower-alpha and upper alpha.

ul {
    list-style-type: circle;
} 
ol {
    list-style-type: lower-alpha;
}

The one that is interesting to most students is the list-style-image which allows an image to be used as a list marker. The list-style-image can also be a web image and can be a relative or absolute URL.

The list-position which sets the position marker in relation to the list item box, can be set to inside or outside. This has more of an impact when you are styling the list background and the position of the list to the other items in the page. 

Figure 2 Creating Image Bullets for a List

The HTML code to create the list is shown. 

<ul>
   <li>Sunny</li>
   <li>Warm</li>
   <li>78 degrees</li>
</ul>

The CSS rules are shown below. Make sure to reference the URL to the path using list-item-image in the LI element style rules: url(URLpath).   

ul {
   list-style-type: none;
   list-style-position: outside;
   margin: 0;
   padding: 0;
   overflow: hidden;
   background-color: #333333;
}
li {
   list-style-image: url('../images/smiley.gif');
}

The shorthand for list-style is: list-style: list-style-type list-style-position list-style-image.

 

ul {
     list-style: square inside url("sqpurple.gif");
}

 [link: #top] Top

Figure

Images are going to be covered next unit. Figures are simply optional containers for images. They make it easier to design boxes and captions with images, code blocks, video and audio and even advertisements.  You can have more than one element within the figure and even nest figures within figures! 

Here is the basic idea. The figure encapsulates the image and other child elements. The figcaption element is the figure caption. You can also include text and HTML tags within the figure caption!

<figure>
    <img src="../images/imagename.png" alt="Alternative text goes here">
    <figcaption>The Final HTML Tag</figcaption> 
</figure>

Here is how to modify the CSS style for the figure element.

figure {
  border: solid crimson;
  padding: 6px;
} 

To illustrate adding the border, we modified the CSS styles and figure content and placed it in the right aside. 

<div style="width:300px;">
    <figure>
        <img src="../images/clockTower.jpg" alt="Clock Tower">
        <figcaption>
            <h3>The Clock Tower</h3>
            <p>
                The clock tower has a long and storied history.
                Built in 800 A.D. by the ancient Parkite Indian tribe,
                it was originally used as a beacon for late-night buffalo-tipping parties.
            </p>
            <p>
                In 1865, because of its extraordinary time-keeping accuracy,
                it served as the world's first Coordinated Universal Time clock.
            </p>
        </figcaption>
    </figure>
</div>

Here is the CSS style rules to create the rounded corners on the border and the frame.  As you can see, the colors are shown on the border to help you see that you can configure the borders of figures, similar to other elements. 

/* =========== Figure =================*/
figure {
    margin: 0px auto;
    padding-top: 20px;
    text-align: center;
    background-color: #e9e9e9;
    border-radius: 0.25rem;
    border: 5px solid;
    border-color: red green blue;
}
figcaption {
    margin: 0px;
    padding: 15px;
    text-align: left;
    font-family: Verdana, Geneva, sans-serif;
    font-size: 10px;
}

Figure 3 The Clock Tower

 [link: #top] Top

Use Organizational Elements to Organize Content

Layout Elements

Elements you will work with in this chapter that group content into different parts, are new elements to HTML 5 and include aside, article, section, footer, header and nav. address, details, and summary. Other useful section elements include address, hgroup and h1 to h6. This chapter will allow us to layout the page content in a much more appealing way with asides, headers and footers.

Header and Footers are used commonly in web pages. Often the address element is used in the footer to show contact information, email or physical address and is in italic by default.

Nav elements are used to indicate navigation, which does not have to be hyperlinks. Today with Bootstrap, JQueryUI and other framework tools, we often use nested lists to represent the navigation hierarchy.

Sections are useful and commonly used today. Section elements can contain child section elements. I never assume browsers understand nested elements, other than lists. Instead use CSS style rules.

Articles are often discussed with sections. Like a newspaper you can break the content into sections.  Articles may have their own header, footer, aside and section within the article! Remember, articles are often meant to be independent of the reset of the page. Often articles are used through an RSS feed.

Asides are used for right and left sidebars. The location is often configured with the float property in the style sheet. Typically the nav and menu elements are located in the asides.  

The summary and details elements make building an interactive page easy.   The cool thing is you can click on the summary and the details is made visible. It’s a toggle so you can click again to hide the information.

<details>
 <summary>Click here to learn more about the animals in our zoo.</summary>
 There are many animals in our zoo :
 <ol>
     <li>bears</li>
     <li>elephants</li>
     <li>lions</li>
 </ol>
</details>

Layout CSS Properties

You can divide content containers like the div element into columns with the columns property. You can specify the column-count (and column-gap, width, -span and -fill) and the column-rule (with column-rule-color, -style and -width). The z-index property sets the layer order of the elements.

Resolution and Width

You will want to consider your resolution support. In the example, all of the horizontal items that spread across the page, are the same width, padding and margin. Setting the margin to 0 and auto will center that content in the page. 

header, footer, main 
{
    width:1028px; 
    height:100px; 
    padding:0px; 
    margin: 0px auto;
}

You should make sure the width, padding and margins of the 'nested' elements add up to the total width of the page. (300px + 728px = 1028px). 

<body style="width:1028px;">
    <header>
    </header>
    <main>  
            <!-- Left menu goes here -->
            <aside style="width:300px;">
            </aside>
            <!-- Main content goes here -->
            <section style="width:728px;">
            </section>
    </main>
    <footer style="width:1028px;">
    </footer>
</body>

You can see on  [link: http://gs.statcounter.com/screen-resolution-stats/mobile/worldwide] StatCounter, desktop, almost all have greater than 1024px by 768px.  Make sure to decide what your dimensions are for the different sections, before you start coding! You should use comments when you have complex layouts to help you locate main areas within the page during development. In a production site, we sometimes remove the comments if they impact performance. 

 [link: #top] Top [link: #top]  [link: #top]  [link: #top] 

 [link: #top] 

 [link: #top] 

Named Hyperlinks

 [link: #top] 

Understanding hyperlinks are critical to your success in this course. Image-based hyperlinks are covered in another chapter.   

 [link: #top] 

Internal or named hyperlinks hyperlinks are links that move the focus to another part of the same page. We use this same method as part of the course when you see the 'Top' links. 

 [link: #top] 

A link using (#) in the href property always reloads the current page. 

 [link: #top] 

<a href="#">Reload the page</a>

 [link: #top] 

The old way was to use <a name=“Top”></a> and then anywhere in the page add a link to the target using <a href=“#top”>Top</a> or simply type in the browser apples.html#top.

 [link: #top] 

The new way is to assign the ID to an element and link to that element by it’s ID.

 [link: #top] 

<h1 id="top">Overview</h1>
<a href="#top">Top</a>

 [link: #top] 

Hyperlinks can be styled for different states, a or a: (default), a:link (default), a:visited (previously visited page), a:hover (mouseover) and a:link (mousedown). You can see how this is implemented below. The color is white when the page is loaded and when the user mouses over the link, it changes color. 

 [link: #top] 

a, a:visited {
    font-family: Verdana, Geneva, sans-serif;
    text-decoration: none;
    color: #FFFFFF;
}
a:hover {
    color: #E37222;
}

 [link: #top] 

In the sample layout page, additional formatting is possible because we used the UL and LI elements in order to change the background color and add a bottom border. 

 [link: #top] 

At the top of the page right after the opening body tag you would have a named link. 

 [link: #top] 

<a id="top" />

 [link: #top] 

Insert the button at the bottom of the page using a link. I included this in the bottom of the content section. 

 [link: #top] 

<div style="text-align:center">
    <a href="#top" id="nav-pills">Go to the top of the page</a>
</div>

 [link: #top] 

In the CSS you may choose to set the properties to make the hyperlink look like a button.

 [link: #top] 

/* =========== TOP =================*/
#nav-pills {
    width: 200px;
    display:inline-block;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    color: #fff;
    background-color: #007bff;
    border-radius: 0.25rem;
    border: 1px solid;
    border-color: #dee2e6 #dee2e6 #fff;
}
#nav-pills:hover {
    color: #007bff;
    background-color: #ffffff;
    border-color: #007bff;
}

 [link: #top] Top [link: #top] 

Combinators and Selectors

There are different combinators in CSS3 that we can use today to simplify the markup code. Which one you use depends on what you want to format and the structure of your html! So, let's remove all the stye rules and just put in two.

Descendents

Descendant selector uses a space to show the hierarchy.  So in this case all h1 elements that are somewhere inside the div tag nested would be green. Select descending elements by using a space. So in this code snippet all children and their siblings and grandchildren would be green.

div h1 { color:green; }

In this code snippet all links inside a paragraph are styled red. All links inside an element with the ID mytable are styled red. 

p a {color:red;}
#mytable a {color:red;}

Child selector or Immediate Descendent selector uses a (>) to format the child in a parent-child hierarchy. The immediate descendent selectors are used to focus only on the immediate (first or child) descendants and not the sibling or nested elements. Select child elements using the > . This is used to indicate a parent-child relationship. 

#div >  h1 { color:green; }

Sibling Elements

The + and ~ allow you to choose sibling elements.

The adjacent sibling selector (+) will focus on sibling elements that are immediately after the element, but not nested elements further down the hierarchy.  So the + selects the sibling, immediately following the selector. 

h1 + h2 { color:green; }

The general sibling selector (~) choose all siblings of the element. The ~ selects the elements that follow the selector (it doesn’t have to be immediately after!) The formatting only applies to the siblings that are the same 'type' of element. For example, here only the siblings of h1 that are h2 elements would be selected but not p elements. 

h1 ~ h2 { color:green; }

Let's compare the two combinators in an example. The first style rule only configures the Page1 link because it is the first child immediately following the p element. The second style rule configures both the Page 1 and Page 2 links. 

p + a { color:red; }
p ~ a { color:blue; }
<p>Our <span>menu</span>.</p>
<a href="page1">Page 1</a>
<a href="page2">Page 2</a>

Chaining Selectors

You can combine the rules with a comma. Note the * means choose any link inside another element in the body. The other, only links inside a table cell are red.

body > * > a
td > a { color:red; } 
body > * > a, td > a { color:red; }

 [link: #top] Top

 [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
