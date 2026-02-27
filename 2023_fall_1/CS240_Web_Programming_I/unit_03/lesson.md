# Unit 3: Lesson

Working with HTML and CSS

Rather than provide separate lectures, we are going to ask you to read your textbook. We want you to read your book and take your own notes. Here are some notes we thought were most important or needed additional reinforcement or clarification. 

Chapter 5 Tables and CSS Layout

Chapter 6 Links and Images 

 [link: #top] Top

Table Elements

Tables are useful in showing data in a grid. Several of the textbook sample pages use table. 

While older web sites use tables to layout the page content, newer web sites do not because users with accessibility needs will have difficulty accessing your content in tables. The main table elements include table, th, tr and td. The elements include thead, tbody, tfoot, caption, col and colgroup. 

A caption element can be used to include a table caption.

The th element is used to configure the header cells for the column, which centers and bolds the text.  

The tr element is used to identify each row.

The td elements are used to identify the cells in the rows. 

Cells use the colspan and rowspan to merge cells across columns and rows.

You can use colgroup element to group two columns under one header cell column. 

The thead, tfoot and tbody elements can also be useful to configure the styles by separating the sections of the table so that they can be configured with different styles.

Older web pages used attributes such as align, width, bicolor cellspacing and cellpadding, that are now obsolete. You can use CSS styles to vertical-align, horizontal-align to center the text in the middle of the cell. Be careful because older editors will try to use valign as an attribute, but it’s obsolete. This is one way to determine if the page is html 5 compatible. The only local attribute that is supported still is border but it can only be set to “1”. However, using CSS is better for configuring table styles such as cell-spacing, border-collapse, and border-color. The other table-related properties commonly used include border-collapse, border-spacing, caption-side (specifies where the caption is placed), empty-cells (how the border on the empty cell is styled) and table-layout (how the size is determined.

You can set the empty-cell to show or hide the border. You'll sometimes see older web programs use nbsp; to hold open the cell to show the border which can now be avoided with the empty-cell attribute. The border-collapse collapses or separates the cell from the table. Separate will create the border around the cells and the table, creating a double border effect, which is usually not desired. So I usually set this property to collapse.

 [link: #top] Top

Hyperlinks and Navigation

Understanding hyperlinks are critical to your success in this course. 

HREF

Absolute URL

The href attribute identifies the URL or location you want to go to. Absolute URLs are easiest to understand. Include the protocol, http:// or https:// with the domain name and path to the object you want to link to. 

Notice can append a querystring with a question mark (?). A querystring is simply a list of name and value pairs. The names and values are separated by (=) and the pairs are separated by an ampersand (&). The name and value pairs must be URL encoded. So characters such as blank spaces are replaced with codes such as %20. Do not split strings in the line of your actual code. You can also specify a document or web page to open.

Go to <a href="http://google.com">Google</a>
Go to <a href="http://google.com?feedback=terrific">Google</a>
Go to <a href="http://mysite.com/pdf/bigreport.pdf">The big report</a>
Go to <a href="http://mysite.com/pages/home.html">Home</a>

MailTo

Mailto is used to open up the local email program. The querystring can contain the subject, cc, bcc and body of the email message. However, the subject and body must be URL encoded.  Do not split strings in the line of your actual code.

<a href="mailto:myname@mycompany.com">Email me</a>
<a href="mailto:myname@mycompany.com?Subject=Customer%20feedback" 
     target="_top">Send feedback!</a>
<a href="mailto:myname@mycompany.com?cc=thing1@mycompany.com&
     bcc=thing2@mycompany.com&subject=Customer%20feedback&
     body=Terrific%20web%20site!" target="_top">Send feedback!</a>

Target

Target attribute is the current window (_self) by default. If the target is an external web site, we usually use __blank which opens the page in a new window or tab.

Go to <a href="/pages/home.html" target="_blank">Home</a>
Go to <a href="/pages/home.html" target="_self">Home</a> 

Relative URL

Relative hyperlinks are used more often today. You do not specify the protocol or domain name. There are two types of relative addresses. 

1. Relative paths based on the path from the root folder. 

The web server is configured to map a folder as the 'root' of your web site. This can differ from your local web site.  

The / at the start of the href value indicates the path from the root folder. 

Go to <a href="/pages/home.html">Home</a>

Relative links can use the / indicating the path is relative to the root folder.

2. Relative paths based on the path from the current page. 

If the page is in the same folder, you do not need to specify any path, just page name. If the page is in a different folder use .. to go up to the parent folder, then navigate to the folder where the file is located. Often it's in a pages, html or other commonly named folder. You can use any combination of ../ as you would at the command line. 

Go to <a href="home.html">Home</a>
Go to <a href="../pages/home.html">Home</a>
Go to <a href="../../pages/home.html">Home</a>
Go to <a href="../samples/home.html">Home</a>
Go to <a href="../textbook/home.html">Home</a> 

TIP 

For our project in this course, the pages you create are all in the same folder and therefore no path is required.  Go to <a href="week1.html">Week 1</a>

Styling Hyperlinks

Hyperlinks can be styled for different states, a or a: (default), a:link (default), a:visited (previously visited page), a:hover (mouseover) and a:link (mousedown). Below you can see an example that was used last unit on creating the style rules for the main menu. When you mouse over the link, the color changes. You can change other properties too such as text-decoration (underline) and text-shadow. 

#leftAside a, #leftAside a:visited {
    font-family: Verdana, Geneva, sans-serif;
    text-decoration: none;
    color: #FFFFFF;
    text-shadow: 1px 1px #000000;
}
#leftAside a:hover {
    color: #E37222;
    text-shadow: 1px 1px #000000;
}

 [link: #top] Top

Images

Figures and images are important for web sites today.  We've already covered figures, which are containers for images and other content. Let's talk about web images and favicons and how they are used in your pages. 

Inserting Images in Web Pages

The image element is inserted with the IMG tag.

The source (src) attribute allows you to configure the absolute or relative path to the image.

The alternative text (alt) attribute is used to provide alternative text. Alternative text is important to support users with accessibility needs or when the image is not displayed.

Height and width provide the dimensions for the image displayed but you can set these in the style sheet. Most browsers support these attributes configures in CSS style rules. 

<img src="../images/imagename.png" alt="A description of the image" width="128" height="128">
<img src="https://www.mycompany.com/images/imagename.jpg" alt="A description of the image">

You can style the image in the style rules. As you see here you can modify the border, height and width, as well as the position. Using the float property you can have the image float to the right of the content, left or center. Border-radius can be used to change the shape from a rectangle to ellipse. In the first example you can see the image border radius is configured as an oval and floats on the right of the page. In the second image you can stretch the image but not larger than the original width and also centers the image. 

<img class = logo alt="A description of the image" >
<style>
.logo {
        src: url("../images/imagename.png");
        width:"128";
        height:"128"; 
        max-width: 100%;
        height: auto;
        border-radius: 50%; 
        border: 1px solid #ddd;
        border-radius: 4px;
        float:right;
}
.logo :hover {
        box-shadow: 0 0 2px 1px #FF3399;
} 
.logo2 {
        src: url("../images/imagename.png"); 
        max-width: 100%;
        height: auto;
        border: 1px solid #ddd;
        border-radius: 8px ;
        display: block;
        margin-left: auto;
        margin-right: auto;
}
</style>

Image File Formats

Types of images browsers natively support include JPG. PNG and GIF as well as SVG (scalable vector graphics). Browsers may support other formats using plug-ins and extensions. In this course, please only use the natively supported graphics. 

JPG 

Best for full color photographs because it supports millions of colors (24-bit).

can be compressed into smaller file sizes using “lossy” compression. Lossy means that there is always a loss of quality as you save or modify the image. Always keep copies of the original images! When you compress the photo you may lose fine details. Many editors allow you to control the compression methods and strengths. 

PNG

Can be compressed into smaller file sizes using “lossless” compression. Lossless means you can save the file and not lose any quality. This can result in larger file sizes.

Does not natively support a 4-color (CMYK) process so it's not useful for commercial print work.  

Best for screenshots, graphic elements such as buttons. 

Supports transparency and layers.

Can be saved as 8-bit supporting only 256 colors or 24-bit supporting millions of colors. 

GIF

Original format for images on the Web.

Used for images with less than 256 colors or shades of gray. (8-bit)

Useful for smaller size images needed limited colors such as icons, buttons and graphic elements. 

Supports layers and animation.  

How Images are Used in Web Pages

First, you can you insert the image into the web page using many methods:

basic image or picture 

image hyperlink

favicon

background of an element (such as a page, table, table cell, border, paragraph, div)

bullet icon in a bullet list

image buttons

imagemap

Hyperlinked Images

This is an important part of the lesson because we use this all the time. The key is create the link like you would any normal link. Then where you would normally put the text for the link, put the image. You can link another page or resource, including a larger version of the image. A thumbnail is a smaller version of the image linked to a larger version. While you can use the same image file, the larger image still is downloaded in the thumbnail. Therefore it is better to use a separate physical file for the smaller thumbnail than the larger image. Thumbnails can be easily created using graphic editing software such as GIMP (free) Adobe Photoshop.

<a href="page.html">
      <img src="../images/image.png" alt="A description of the image"  
         width="200" height="50"/>
</a>
<a href="imageLarge.png">
      <img src="../images/imageSmall.png" alt="A smaller image" width="200" height="50"/>
</a>

Background and Border Images

In the style sheet you can configure elements to have a background image. You can use the image for a border, if you set the border width to a width that is wide enough to see the image. List-style-image which allows an image to be used as a list marker.

div {
    border-image: 15px solid url("../images/border.png") repeat;
    background: #FF0000 url("../images/background.png") no-repeat center; 
}
ul {
    list-style: square inside url("../images/listbutton.png");
}

Image Button

The form input element is used to create form fields. Changing the type attribute to image will create an image button. Image buttons support image, height, width, alt and src (source) attributes. 

<form>
  Sign up on the email list. 
  <input type="text" name="email"><br>
  <input type="image" src="submit.png" id="btnSubmit" alt="Submit" >
</form> 

Tip

You will learn about image maps next unit.

 [link: #top] Top

CSS Positioning

Display

Display is used to help identify how to place the element on the page.

When display is none, the element will be hidden from the page, but not deleted. You can also hide an element by setting the visibility property to none, or opacity.

You can set the display of an element to block. Setting display to block means the element starts on a new line and the width of the element stretches to the full width of the container element. The heading, div, p, form, header, footer, and section elements are block level by default.

You can set the display of an element to inline. Inline elements cannot contain block level elements. Span is an inline element by default. You can make a list item inline in order to create a horizontal menu. You can configure the span element to block.

.hidden {
    visibility: hidden;
}
.hidden2 {
    display: none;
}

Absolute & Relative

We have had ways to position elements using absolute or relative values. You could set the position of the left, right, top and bottom and z-index (layering) of the elements. The smaller the z-index, the further back the element is in the layers.  

You can change the element position to static, relative, absolute or fixed and now 'sticky'. 

Static is normal flow.

Relative is relative to it's normal position. 

Absolute element stays in the same place relative to the nearest element or the body element. There is no gap in the page where the element normally would have been. The element will scroll with the page.  

Fixed means the element stays in the same place relative to the viewport, even when the page is scrolled in any direction. There is no gap in the page where the element normally would have been. You can set the top, right, bottom, and left properties to identify the position. 

Sticky can change from absolute to relative. Fixed and sticky very useful to create sticky menus, menus that do not scroll of the page. 

CSS 3 Column Layouts

Although we can float content on the page another page layout is to create multiple columns. This has been customized and referred to as  fluid grids. CSS 3 supports a 12 column responsive fluid grid. Columns can be set with shorthand properties.

The column-count is the number of columns, column-width is the width of the columns, column-gap is the distance between the columns. You can use fixed values for the width or relative (em) values.

You can configure the column-rule-color, column-rule-style and column-rule-width individually or at one time with the column-rule shorthand.

Column-fill is used to fill the columns sequentially, or use balance to minimize variations in column length. Column-span is how many columns an element should span (all or none).

p {
   column-count: 3;
   column-width: 10em;
   column-gap: 5.5em;
   column-fill: balance;
   column-rule: medium solid black;
   column-rule-color: black;
   column-rule-style:thin;
   column-rule-width:10px;
}  
<p> Column 1111111111111111111111.
    Column 2222222222222222222222.
    Column 3333333333333333333333.
</p>

Flexbox CSS 3 Layouts - Optional

Flexible Box Layout is used to help improve responsive layout structure without using float or positioning. There are many tools that are being developed that use flex to help improve responsive design. This is covered in another course, CS314 in greater detail. If you are interested in learning more about flex, you can read about it at  [link: https://www.w3schools.com/css/css3_flexbox.asp] https://www.w3schools.com/css/css3_flexbox.asp. 

 [link: #top] Top

Accessibility

We could cover a whole course on accessibility. But for now we'll keep it to the basics. 

American for Disabilities Act is a set of workplace regulations and requirements for accommodations in the workplace. It generally will not apply to web sites except those internally to organizations such as intranets. 

Section 508 of the Rehabilitation Act, §1194.22 contains the requirements for web sites for federal agencies. Previously these standards were minimal compared to the industry standards. While this was for federal agencies and a few other areas, it was used as the standards across states. While not law for private or public companies, this is an industry standard or what we call best practices. 

Industry standards developed by the W3 Web Accessibility Initiative (WAI), known as the Web Content Accessibility Guidelines (WCAG). WCAG has levels to identify different requirements. As of January 2018, Section 508 was brought up to WCAG 2.0 A and AA success criteria. 

 [link: https://www.section508.gov/] Section508.gov. IT Accessibility Program

 [link: https://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-ict-refresh/final-rule] Section 508 Final Rule 

 [link: https://www.w3.org/TR/WCAG20/] Web Content Accessibility Guidelines (WCAG) 2.0 (December 2008)

The primary organization for promoting web accessibility is  [link: https://webaim.org] WebAim.  Although their  [link: https://webaim.org/standards/wcag/checklist] checklist is admittedly not equivalent, it's a good starting point for beginners to understand some of the issues. The standards are organized into principals - four, knowns as POUR. 

Principle 1: Perceivable - Information and user interface components must be presentable to users in ways they can perceive.

Principle 2: Operable - User interface components and navigation must be operable.

Principle 3: Understandable - Information and the operation of user interface must be understandable.

Principle 4: Robust - Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.

One of the main aspects that developers should focus on is the providing of alternatives. So for example, the alt attribute used with images provides alternative text for users without vision. Closed captioning for videos provides transcripts for users without vision. 

There are evaluation tools that can help you with selecting contrasting colors, verifying links, and verifying some of the criteria. However, the entire review cannot be autogenerated, 

 [link: http://wave.webaim.org/] WAVE Toolbar

 [link: https://webaim.org/resources/contrastchecker/] Color Contrast Checker

Absolute positioning are difficult to comply with accessibility standards and mobile device requirements. So if you do use them you would want to think about alternative options. We do try to stay away from using tables for layout because of the accessibility requirements.

 [link: https://webaim.org/techniques/tables/] Creating Accessible Tables is an article that discusses some of the issues with tables. Tables can be used for data but remember they can be difficult for screen readers, so make sure to review the standards and best practices.  [link: https://webaim.org/techniques/tables/] 

 [link: #top] Top

Pseudo-Class Selectors and Elements 

Pseudo-Class Selectors ( : ) 

Pseudo-classes are prefixed with a single colon ( : ). Pseudo-classes can be combined with elements, classes or ID selectors. You could use :root but using the html element would have the same results in styling the entire page.

:root { background-color: white }

Links

By far the most common pseudo-classes are for the state of the hyperlinks which includes :hover, :active, :link, and :visited. You can change the default browser colors for links using these pseudo-classes and create a mouseover effect.

a:link, a:visited, a:active {color: yellow; background-color: black; text-decoration: none;}
a:hover { color: white; background-color: blue; text-decoration: underline; }

Child

Some of the common ways to select the child element based on the parent is by :first-child and :last-child.. 

p:first-child {
    color: blue;
}
p:last-child {
    color: red;
}

There is a negation selector so that you can choose the opposite such as 

a:not([href*=".com"]) { color: red; }

 element selects the default element from a group of similar elements.

These pseudo-classes are often used with forms, such as . :focus, :checked, :default, required, :optional, :enabled or :disabled. So for example if the button is disabled you could have a different style. 

<input type="text" id="txtName"></button>
<button value="submit" id="myButton"></button>
txtName:required { background-color: red; }
txtName:focus { background-color: green; }
myButton:enabled { background-color: green; }
myButton:disabled { background-color: gray; }

Disabled form fields are grayed out by the browser by default. You can change this with the :disabled pseudo-class.

The :valid, :invalid, :in-range, and :out-of-range can be helpful to indicate to users that there is a problem with the form data entered. 

:valid { border: thin solid green; }
:invalid { border: thin solid red; }

Pseudo-Elements ( : : ) 

Selecting Parts of an Element 

You can select parts of an element such as the first line of the block of text. You can select the ::first-line, ::first-letter or something selected by the user with ::selection.  You can can combine pseudo-elements with other selectors. Note that the browser will modify this when the window is resized. So it’s always the first line!  You can only change properties such as the font, color, background, word and letter spacing, text decoration and transform, line-height and vertical-align and clear. 

::first-line { color:red; } 
::first-letter { color:red; }
p::first-line { color:red; } 

Inserting Content Into Elements with CSS

You can use the ::before and ::after to insert content into an element using CSS. The example becomes Click here to visit Page 1! (Later you will learn to use JavaScript to change the InnerHTML property to change the contents inside an element such as the div element.)

a::before { content: "Click here to visit ” }
a::after { content: "!" }
<a href="page1">Page 1</a>

 [link: #top] Top

Attribute Selectors

You can use a class and attribute selectors for a single element or for all elements that match that class. For attribute selectors you can create multiple conditions.

Attribute selector is where a string value matches a pattern: 

If the elements have this attribute: [href] {color:red;}

The specific element selector has this attribute: a[href] {color:red;}

If any elements have this attribute with this specific value: [target="_blank"] {color:red;}

A specific element selector has a specific value: a[href = "page1.html"] {color:red;}

Starts with: [href ^= "www."] {color:red;}

Ends with: [href $= ".com"] {color:red;}

Any elements contains a specified word or string: [title~="Home Page"] {color:red;}

Any elements contains the substring listed: [href *= ".com"] {color:red;}

Compare from a pipe-separated list of values: [lang|"en"] {color:red;} where options for the list can be lang="en-us", lang="en-gb", lang="en". This ( | ) character is commonly known in computer science as a pipe. 

Attribute selector can contain multiple values and match the value. The Microsoft link would be blue.

[class ~= "class1"] {color:red;}
a[target="_blank"] {color:blue;}
<p>I like <span class="class2">flowers</span> 
<a class="class1 class2" href="http://www.google.com">Google</a>
<a href="http://www.google.com" target="_blank">Microsoft</a>

 [link: #top] Top 

 [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
