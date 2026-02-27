# Unit 3: Homework

**Due:** 2023-09-04T04:59:00Z
**Points Possible:** 60.0
**Submission Types:** online_upload

## Instructions

Unit 3: Homework 

 

Working with HTML and CSS

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

IMPORTANT!  Use the same web site topic that was assigned in unit 1.

PLEASE NOTE: The page directions are NOT the same as the practice pages in the case study. 
While the case study will help you learn different techniques, I have arranged the directions in a specific way.

Please pay attention to the directions here!

 [link: #top] Top

Before You Get Started 

 

Hyperlinks and Style Sheets - Example Menus

This week you will work with hyperlinks and menus as well as images. Notice that this menu uses the header tag to separate out the main heading and menu, That is common in web sites. You also see h1 for a page heading. Then you see the nav tag used to identify that the links are for navigation purposes. Some web sites use the menu tag. In this example an unordered list is also used with list items (LI) for each link in the menu. The # is used as a placeholder url, for links that reload or refresh the page. 

Here is a sample code snippet from the case study. 

<header>
  <h1>Microgrid Development in Lawrence KS</h1>
  <nav>
    <ul>
      <li><a href="lawrenceHydropower.html">Lawrence Hydropower</a></li>  
      <li><a href="typicalProperty.html">Typical Property</a></li>
      <li><a href="localEnergy.html">Local Energy</a></li>
      <li><a href="#">Collector Performance</a></li>
      <li><a href="#">Electric Power Services</a></li> 
      <li><a href="http://www.w3schools.com">W3Schools.com</a></li>
      <li><a href="https://www.w3schools.com/cssref/default.asp">CSS Reference</a></li>
      <li><a href="../images/property.png">Link to view the property!</a></li>
      <li><a href="https://www.whitehouse.gov/wp-content/uploads/2021/01/white_house_grounds.jpg">Link to the White House image</a></li> 
    </ul>
  </nav>
</header>

Then you use CSS to modify the links. This is the example from the case study. 

/* Rules for interpage navigation */ 
nav ul {
  list-style-type: none;
  text-align: center;
  padding-left: 0px; 
}
nav li {
  display: inline-block;
  padding: 0px 4px 2px 4px;
  margin: 2px 4px 2px 4px;
  background-color: lightgoldenrodyellow;
  border: outset;
  border-color: lightgreen;
}
nav a {text-decoration: none;}

You can also add style rules for the W3Schools  [link: https://www.w3schools.com/css/css_link.asp] hyperlink states example. 

a:link, a:visited {
  background-color: #f44336;
  color: white;
  padding: 14px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: red;
}

Images are fun to play with and extensively covered in the book and lesson. 

Look at  [link: https://www.w3schools.com/html/html_images.asp] W3Schools Images as well as  [link: https://www.w3schools.com/html/html_images_picture.asp] W3Schools Picture Element for reference. 

Look at the  [link: https://www.w3schools.com/css/css_link.asp] W3Schools CSS Reference.for advanced CSS styles to play with. 

The  [link: https://www.w3schools.com/css/css_image_gallery.asp] W3Schools Image Gallery. will help you learn to use the figure tag and captions. 

 

Read about Navigation menus

Some web sites use different methods to create navigation menus, which are well beyond what we can do here at this stage of your learning. Some us unordered lists, which leave a bullet. You then have to remove the bullet using the list-style-type css property.

Many of the menu examples require JavaScript to handle the drop-down and mega menus. Here are some links to examples that are something you can implement. In the homework I will share with you examples of how you can do this. 

 [link: https://www.w3schools.com/howto/howto_js_topnav.asp] Create A Top Navigation Bar

 [link: https://www.w3schools.com/howto/howto_js_topnav.asp] Tip: To create mobile-friendly, responsive navigation bars, read our  [link: https://www.w3schools.com/howto/howto_js_topnav_responsive.asp] How To - Responsive Top Navigation tutorial.

Tip: Go to our  [link: https://www.w3schools.com/css/css_navbar.asp] CSS Navbar Tutorial to learn more about navigation bars.

 [link: #top] Top

Review - NOT GRADED

 

Review Chapter 5  (Case Study 5.11)

 

Case Study Description:

This section adds another web page to our case study website. Case Study 5-11 is a A Downtown Store’s Electrical Generation and Consumption. Figure 5-11 shows a preview of the web page.  This page uses basic HTML elements as well as external style sheet rules to format columns of text as well as a table and columns.  You will also be using classes to format the element styles.   

 

Review Chapter 6 (Case Study 6.11)

 

Case Study Description:

This section adds another web page to our case study website and you will update the home page. Case Study 6-11 is the Local Energy and Home Page with Website Navigation. This page describes some of the technology and benefits of local energy generation and storage. Then we present a home page for the case study website that includes links to the new local energy web page, plus links to web pages introduced in earlier chapters’ case study sections. You will be working with links and lists throughout the activity. 

 [link: #top] Top

Homework - GRADED

 

Create homework5.html  

 

External CSS Links

Complete the assignment below. 

Add the link to the external style sheet in every homework page you create.

Create your web page, homework5.html as previously described in the other assignments. 

Add the link to the external style sheet in every homework page you create.

Note the path is relative! If this does not work for you, then, you need to check your folder structure and file names!

This should be included in the skeleton page code of every other web page that you create in this web site. 

<link rel="stylesheet" href="../css/homework.css">

Create a Top Navigation Bar

Read how to create a top navigation menu:  [link: https://www.w3schools.com/howto/howto_js_topnav.asp] https://www.w3schools.com/howto/howto_js_topnav.asp 

Create a menu at the top of the page that you will reuse on every web page in your site. You do not need to change week 1 homework. However, all future homework will use this menu. Note that the case study used an index page. This is a simpler method, but you need to copy this onto every page in your homework site. 

Use the header, and nav tags to create the menu

Include links to all the html pages you have created. 

The list should be a list of each homework page. (homework1.html .... homework8.html)

Set the link to homework1.html to "homework1.html" 

For pages that don't exist yet, set the href ="#".

The current page can have a class assigned such as "active" so that the style rule can be different for that current page. 
 <a class="active" href="homework1.html">homework1.html</a>

You would need to make this change on each individual page. So on homework2 page you would change the link for homework2.html to use the active class and remove it from homework1.html. .    
<a class="active" href="homework2.html">homework2.html</a>

Sample code snippet to add to the body section:

<header>
    <nav> 
          <a href="class="active" homework1.html">homework1.html</a>
          <a href="homework2.html">homework2.html</a>
           . . . 
          <a href="#">homework7.html</a>  
          <a href="#">homework8.html</a>
          <a href="http://www/w3schools.com" target="_blank">W3Schools</a> 
          . . . 
    </nav>
</header>

Include links to 3 external web sites in your menu (see example above)!

Use the target attribute for each link to open the link in a new tab or window. 

Example: 

<a href="http://www/w3schools.com" target="_blank">W3Schools</a>

 [link: #top] Top

Style the menu

Add style rules to format the navigation menu ! 

Add the CSS styles only to the External CSS file!

Make sure to set the margin to 0 so the menu starts at the top of the page. 

body {
  margin: 0; 
}

Format the menu.

Do not show the bullets. 

Format the text and background color different than other links in the page.

The links should be next to each other, horizontally, not vertically. 

You can configure other styles for the menu as desired.  

Use different styles for mouseover effects. with the hover state. 

Change the styles for each state:  default, hover, visited and active.

Here is an example of a code snippet on how you might approach this problem.

Notice that this did not require a class, because I used a nav tag instead of a div tag. Some examples use a div tag. In that case you have to do more work and configure the menu with class selectors. It's not needed if you simply use the nav tag as I did here.

Change at least 2 different properties for each hyperlink state. (ie. underline, text color, font) See the example below.   

nav {
    overflow: hidden;
    background-color: #333;
}

nav a {
    float: left;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
}

nav a:hover {
    background-color: #ddd;
    color: black;
}

nav a.active {
    background-color: #04AA6D;
    color: white;
}

 [link: #top] Top

Working with the Main Tag   

Create the Main Content Area

Insert a main tag, and then insert 1 headings and 1 paragraphs after your menu. 

<main class="container">
           <h1> . . . </h1>
            <p> . . . </p>
            <p> . . . </p>
            <!-- table will go here -->
</main> 

Add at least 2 hyperlinks to other web sites in the paragraphs.

The hyperlinks should be integrated into the paragraph text, not just a list of links.  

Make sure that you are using hyperlinks and not just pasting the URLs in the web page.

Set the target for each link to open in a new tab or window.  

 [link: #top] Top

 [link: #top] 

Working with Images 

In the main content area, add your text content about your web page as previously described in the other assignments.

Insert headings and several paragraphs into the <main> tags. 
 

Insert images in the page. Images all have the alt, height and width attributes set.

You can resize the image so it is not taking up the entire page (or use a photo editor)

Images are only stored in the images directory. 

Images are only to use a relative URL in the src attribute. (ie. src="../images/mypicture.png")

Use only web formats: JPG, PNG, GIF

Images all have a descriptive text in the alt attribute with an appropriate description. 

Images all have the height and width attributes set.

You can resize the image so it is not taking up the entire page (or use a photo editor)

Images should not be larger than 200 * 200 px. 

Remember you don't include px for the size as its pixels by default!

Make sure you use quotes for the values.

Insert the images into the page and configure the image styles: 

Image 1 - insert into homework5.html

Image should be displayed using the figure and figcaption html elements. 

Use a figure caption to add a text to the figure caption. 

Style the figure, caption and image using only to the External CSS file!

Align the figure to the right side of the page.

Set the padding to the paragraph text does is not right next to the figure. 

Image 2 - insert into homework5.html

Insert an image and add style rules to format the images.

Format the images in different ways such as rounded borders, circle, opacity, framing, etc.

Style the image using only to the External CSS file!

  [link: #top] Top

 [link: #top] 

Working with the Footer Tag 

Create the Footer Area

Below the closing main tag, insert a footer tag.

Then insert hyperlinks to a privacy page and terms of use page as well as your contact information. 

A <footer> element typically contains author, date and copyright information, contact information, sitemap, back to the top links and other links. 

Privacy pages are often required in the EU and other countries.

You can format the footer, contents and address and even the links in the footer using CSS.    

<footer class="container"> 
    <p>Email the author: John Smith at <a href="mailto:jsmith@MyCompany.com">jsmith@MyCompany.com</a></p>
    <p><address>Visit us at: MyCompany.com, Box 123, Main Street, Galapagos, TX, USA<br> 
    </address></p>
    <p><a href="privacy.html">Privacy Policy</a> | 
           <a href="contact.html">Contact Us Form </a>  | 
           <a href="terms.html">Terms of Use</a>
     </p> 
</footer> 

 [link: #top] Top

Create homework6.html 

 

Working with Tables

Complete the assignment below.   

Create your web page, homework6.html as previously described in the other assignments. 

Copy the header/navigation, the main section and footer from the previous page. 

Remove the content from the page. 

Add the link to the external style sheet in every homework page you create.

In the <main> area insert 1 heading and 1 paragraph summarizing your table. 

In the <main> area insert a table  

Insert a table under the comment <!-- table will go here -->

Add a table with 6 columns, 6 rows

Add a table 'header' row. (which makes the total of 7 rows)

Add a caption and summary

The last row will store an image 

Edit the external CSS file.

Add style rules to enhance the table appearance

overall appearance of your site as previously described in the other assignment.

Add style rules to format the table and the contents inside the table! 

The heading row should be a different text and background color. 

Every other row should have a different background color. 

Working with Images in a Table

Add your text content about your web page as previously described in the other assignments.

Insert headings and several paragraphs in the <main> section of the page!
 

Copy and paste the menu, main tags and footer that you created in the previous page. Remove the content in the main section.

Insert 6 Images - insert these images into the table  

The image should be given a 'class' name that can be used to style all 6 images at one time.

Insert the images and configure the class. 

Add style rules to format the images by configuring the class style rules. 

Format the images in different ways such as image size, rounded borders, circle, opacity, framing, etc.

You will definitely want to alter the image size or use CSS to set the size so they are consistent and reasonable (no bigger than 80*80px). 

Add the CSS styles only to the External CSS file!

<td>
       <img src="../images/row1.png" class="tableImage" alt="Row 1 image description" width="80" height="80">
</td>

Images all have the alt, height and width attributes set.

You can resize the image so it is not taking up the entire page (or use a photo editor)

Images are only stored in the images directory. 

Images are only to use a relative URL in the src attribute. (ie. src="../images/mypicture.png")

Use only web formats: JPG, PNG, GIF

Images all have a descriptive text in the alt attribute with an appropriate description. 

Images all have the height and width attributes set.

You can resize the image so it is not taking up the entire page (or use a photo editor)

Images should not be larger than 80 * 80 px for the table!

Note that in the HTML code you don't need px units, but with CSS you do!

Make sure you use quotes for the values.

Format the images with CSS. I have many examples here, though they don't look great together!

.tableImage {
      height: 80px;
       width: 80px;
      border-radius: 50%;
      border: 1px solid #ddd; 
      padding: 5px;
      width: 150px; 
      opacity: 0.5;
      filter: grayscale(100%);
      transform: scaleX(-1);
}

Check out the W3School web site for many examples on CSS properties for images!

 [link: http://w3schools.com/css/css3_images.asp] CSS Style Images

 [link: https://www.w3schools.com/css/css3_image_reflection.asp] CSS Reflestion

 [link: https://www.w3schools.com/css/css_image_gallery.asp] Image Gallery

 [link: #top] Top

Finish Styling the Content and Documentation

Format the content with a variety of HTML elements, attributes, and CSS styles as previously described in the other assignments.

Add the CSS styles only to the External CSS file.

Style rules to enhance the overall appearance of your site.

Only add or edit style rules inside the external CSS file.

Document the program:

Document the content and HTML and CSS code per the class best practices as previously described in the other assignments.

Document the CSS style rules with comments as previously described in the other assignments. 

Document the 'new' style rules in the external css file that you created last week, by placing them at the bottom of the CSS file.

Provide a comment above the section saying that it's the CSS for week 3. 

Remember that creativity and originality counts.

Save your changes to your files.

Preview your web page in the browser. 

Validate your page code using  [link: http://validator.w3.org/] validator.w3.org. Remember this is required for all html files!

Follow the directions at the bottom of the page for submitting your work.

 [link: #top] Top

Submit the Assignment

Submit evidence of completion of the requirements.  Make sure to review the General Homework Requirements and document and submit your project using the directions provided on the page. Failure to submit the assignments according to these directions may result in a loss of points!  

IMPORTANT! 

Also refer to the notes on the submission in Homework 1 as well as any instructions in the Course Announcements. 

Here is a brief reminder about the homework.  

Validate every web page code as previously described in the other assignments. 

You will submit ONE (1) Word document, for the entire statement as previously described in the other assignments.

SCREEN SHOTS as previously described in the other assignments.

SOURCE CODE - homework5.html, homework6.html files as previously described in the other assignments. 

SOURCE CODE - External CSS file as previously described in the other assignments: homework.css.

Save the Word document as Week3.docx and upload it here in the classroom on this assignment page.

 [link: #top] Top

---

## My Submission

**Score:** 60.0/60.0
**Grade:** 60
**Submitted:** 2023-09-04T02:17:00Z

### Submitted Files

- **Week3.docx**
  - Downloaded: `files/Week3.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2023-09-08T02:30:39Z):

> Bert

Excellent.

If you have any questions or need help please contact me in my inbox.
