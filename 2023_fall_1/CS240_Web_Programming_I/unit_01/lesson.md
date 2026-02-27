# Unit 1: Lesson

Part I: Introduction to Web Programming

The textbook readings this week will give you an introduction to HTML and the World Wide Web. Rather than provide separate lectures, we are going to ask you to read your textbook. So this truly is to supplement your readings and help fill in the gaps. 

We want you to read your book and take your own notes.You are expected to view the sample code and take notes on your readings as you study.

Chapter 1 Introduction to Web Programming

Chapter 2 Coding Standards, Block Elements, Text Elements, and Character References

Topics

 [link: #link1] Why Web Programming is Important Today

 [link: #link2] HTML Structure

 [link: #link3] Grouping Content

 [link: #link4] Basic Text Elements

 [link: #link5] Validating HTML Syntax

 [link: #link6] The Sample Website

 [link: #link10] Next: Creating a Web Page

Why Web Programming is Important Today

The web is evolving as new technologies emerge. The semantic web and programmatic content such as content management servers (CMS) such as WordPress and Weebly, have helped grow the web even more. End users can create their own content using these add-ons and CMS systems and social media such as Facebook pages. However, we also need to know how to create web pages, manually as we'll be using this knowledge in future courses.

All computer science majors should have a strong grasp of client-server programs. If you look up  [link: https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf] OWASP Top Ten list you will see that most of them are preventable by having developers educated in proper web programming. That is why the learning outcomes below, involve not only how to create web pages but also how to apply your knowledge to solve problems and properly document and debug your web programs.

 [link: #top] Top

The First Web Site

The first web site is attributed to Tim Berners-Lee. Tim Berners-Lee was responsible for the WWW, HTML and HTTP and is now the Director of the W3, the World Wide Web Consortium that maintains the web standards. The earliest web site known has been republished online.

View the  [link: http://line-mode.cern.ch/www/hypertext/WWW/TheProject.html] first web site using a simulated line-mode browser.

 [link: http://info.cern.ch/hypertext/WWW/TheProject.html] Browse the first web site.

The history of the web and XHTML are also important to learn about.The browser wars are an important part of the history of the web, because they set a process in motion where companies varied in how they supported standards, and the need for having professional standards became evident.

You can learn about the  [link: https://home.cern/topics/birth-web] Birth of the Web from CERN.

Learn about how the  [link: http://www.netvalley.com/cgi-bin/intval/net_history.pl?chapter=4] Web was born and the Browser Wars as part of the  [link: http://www.netvalley.com/internet/history_of_internet.pdf] History of the Internet ( [link: http://www.netvalley.com/internet/history_of_internet.pdf] PDF) by Gregory Gromov at Netvalley.com.

Notice that the first web site is void of images, color, animation, video and interactivity. It's basically content (the text) and the presentation of the text using HTML. In later versions of HTML, we see more tags introduced and browsers that support these interactive and design features and enhance the layout and the appearance or style of the web page.

Web Site Resources

All of the HTML and CSS tags and styles are maintained by standards governed by the  [link: http://www.w3.org] W3. The World Wide Web Consortium (W3C) is an international community led by Web inventor and Director Tim Berners-Lee. 

 [link: https://www.w3.org/TR/html52/index.html#contents] HTML 5.2 standards are available online. They are not as easy to read for beginners. 

So for this course, you will want to bookmark  [link: https://www.w3schools.com] W3Schools. You can look up many topics on the this web site related to web programming and will find that this is the best reference for many of the activities you will complete in this course. Some users also find  [link: https://developer.mozilla.org] Mozilla Developer Networks equally useful for  [link: https://developer.mozilla.org/en-US/docs/Web/html/Reference] HTML and  [link: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference] CSS. 

 [link: #top] Top

HTML Structure

HTML is a hierarchical structure.  Each of the elements is inserted using a set of beginning and closing tags (<tag></tag>). The elements can be further customized using one or more attributes. The attribute name and value is inserted into the tag. The content goes before the beginning and closing tag. Notice that tags and attributes are always lower case with quotes used for the values!

<tag attribute1="value1" attribute2="value2" >Content goes here.</tag>

There are 2 major parts to the web page: <head> and <body> sections. The root node is the <html> tags. The <doctype> indicates what type of document and version of html is used in the page. We'll talk about the meta and viewport tags further down this page. 

The doctype is used by validation tools such as validator.w3.org, to identify what rules to apply when validating the code in your web page. Students should always validate their code before they submit the homework. Remember that the doctype does not use the /. 

The head section is used to contain data about the page such as meta data and links to external resources. You can think of this section is the information and resources about the page. 

The title tag is used to display the name of the page in the tab in the browser, in history lists and favorite lists in browsers. So it's important to include the title in each page.

The body section is used to contain the content that the users see in the page, the actual text, images, media and items you see in the page. 

This is the default skeleton code when you create a page. In some editors they may leave the lang attribute off.  For our web sites, all students must show the nesting of these tags, using indentation as shown in the example.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
</body>
</html>

Here are some important tips about the doctype and head section.

All web pages in this course are required to use HTML 5.

Your doctype will always be the same for this course.

All web pages are required to have a descriptive title.

All web pages are required to have meta tags for: author, description, keywords and viewport.

Web browsers allow you to view the source code of the web page. Minimizing the source code means is implemented so that the web page code can load faster in the browser. If you visit park.edu, and view the source code of the web page, you can see about half of the page is minimized. All the code is written on one line that wraps, like a word-processing document. For our web sites, we will not minimize the code.

 [link: https://www.w3schools.com/tags/tag_meta.asp] Meta and Viewport Tags

Your author didn't mention the  [link: https://www.w3schools.com/tags/tag_meta.asp] meta tags for keywords or viewport tags. Meta tags are used to indicate information about the page - meta data. For example, the meta tag can be used to provide keywords which is  just a set of comma-delimited words describing the page.  In the past, Search Engines like Yahoo! and Google, used the title tag, keywords and description heavily for search engine optimization (SEO). They used the information to help classify and rank the web pages and web sites. While they are not heavily used for search engine ranking, they are still important as they can confirm with search engines what your page is all about. 

Today we can use the meta tag for any number of meta data that we want to track on the page. This may include the description, keywords, author, last modified date and sometimes the editor used to create the page. 

<meta name="author" content="John Smith">
<meta name="keywords" content="John Smith">
<meta name="generator" content="WordPress 5.0.2" />
<meta name="description" content="Park University is a private, nonprofit, liberal arts institution 
founded in 1875, headquartered in Parkville, Mo., with more than 40 locations nationwide."/

The robots and refresh are also useful to know. Robots help tell search engines if they should index the page but this can't be enforced. Some software programs will even allow users to download the entire site and ignore the robots settings. 

<meta name="robots" content="noindex, nofollow, noarchive">

Note that the refresh option is useful when we have content that changes often or we want to redirect them to a new page. This passes the information to the server in the HTTP headers and therefore uses the http-equiv property. (You might have learned about HTTP headers in a basic networking course.)

<meta http-equiv="refresh" content="5; http://www.park.edu"/>

Sometimes web sites use an extension of the meta tag using the  [link: http://ogp.me/] Open Graph protocol. This classification system helps provide additional information in the meta tags. For this course, you do not need to implement any Open Graph classifications.

<meta property="og:locale" content="en_US" />
<meta property="og:title" content="Welcome | Park University" />
<meta property="og:url" content="https://www.park.edu/" />
<meta property="og:site_name" content="Park University" />

 [link: #top] Top

Grouping Content 

Grouping elements used in the body section include p, blockquote, div, figure and figcaption, hr, ol and ul, li, p, div, pre, dd, dl and dt. 

The body element is used typically to include all the content that is displayed in the web page. 

Paragraph elements are commonly used. Later you will use a variety of style properties such as margins for styling the paragraph. The margin style allows you to indent the paragraph. 

The concept of whitespace in a web page is important. Adding white space in code view by pressing the space bar has no effect beyond a single space. You can't just hit the spacebar for blank spaces in html. Additional spaces are only added using &nbsp; which stands for the non-breaking space entity. 

The div element groups content.

Sometimes we use the display attribute with the div tag and set the value to block by default so that by default a line break/carriage return is added at the end of the content.

We often assign an id attribute to the div tag in order to manipulate the contents with JavaScript. 

We often assign a style or class attribute so that we can customize the appearance and layout of the contents with CSS. Many other HTML 5 elements tags act like a div tag, but the semantics help us recognize what they are used for, such as the header, footer, and section elements.

Preformatted content is configured with the pre element.

Often the content displayed using the Courier font a monospace typeface. Preformatted content is displayed in a block format. That means that after the content is displayed, a line break/carriage return is inserted. We used the pre element for formatting the code snippets in this class on the web pages. 

The blockquote element is used to indent your content.

The purpose of this element is to identify a block of quoted text. You can include the cite attribute to identify the URL for the original source. 

The hr element is used to provide a logical break by inserting a horizontal rule (a horizontal line). In older versions of HTML we modified the hr element with color, align, width, color and noshade. Today it is still used to help provide a logical separation of content, especially in longer web pages. 

Today we use CSS to modify the  styles of many  elements. You will learn more about styles in a future lesson. For example, the margin style is used to indent a paragraph. You can customize the indentation by modifying the margin-start and margin-after and margin-end attributes.  

 [link: #top] Top

Basic Text Elements

Some elements are used to provide emphasis or highlighting of the content and other elements are helpful to indicate editing such as insertion, deletion and markup of content. You’ll see these elements often used with content management systems where editing and versioning of content is required.

Commonly used text elements which are used in the body section include: a, br and wbr, em, mark, q, spam, strong, sup and time.  

I would like <strong>more</strong> salt in my <em>soup</em>.

As this  [link: https://www.w3.org/International/questions/qa-b-and-i-tags] W3 article points out, some tags like <i> and <b> have had changes in their meanings. So be careful! The W3 does not recommend using the tags for bold or italic anymore. Just because a tag 'works' in the browser doesn't mean it's valid for class purposes or will be valid in the future. You should avoid the B, U and I elements in your web pages for this class. Instead use strong, em, and q. (Later you will learn how to make content appear as bold or italic using CSS style rules.)

Review the other elements in the chapter:  br and wbr, em, mark, q, spam, strong, sup and time. Note that code, samp and kbd all show the user input in monospaced font, while var shows it in italic. Many developers and editors just use code or the pre elements for monospaced fonts. 

<pre> var userName = "Fred"; </pre>
<code> var userName = "Fred"; </code>

By default the mark element will display the highlighted text with the color yellow.

I would like more <mark>salt</mark> in my <mark>soup</mark>.

The q, dnf, abbr and cite elements can be used in combination with the title attribute and cite attributes. 

The <abbr title="United States">US</abbr> flag has 50 stars and 13 stripes. 
<p><q cite="https://www.whitehouse.gov/">The <dfn title="Homeland Security">DHS</dfn> GOP</q></p>
You can read about <cite>DHS Key Laws</cite>at https://www.dhs.gov/key-dhs-laws

Span

Span is allows you to group content inline, within a sentence without having a line break. We often use the span tag so that later we can modify the style of just that portion of the sentence or paragraph using style rules. So the display of the content is often described as block or inline. Recall the div tag is a block tag, that adds a line break at the end of the content. 

Special Characters (< > & )

Because tags are identified with < > you need to convert them into another format in order to actually display them in the web page. So if you are creating a page that has a math formula such as 1 < 5 you need to convert the < in the code to a character entity. For < replace that character with &lt; and > would be replaced with &gt;. More information on character entities is located in chapter 2 and the book samples. 

Here is an example of what you want to actually display in the web page. 

<h1>The creator of the WWW is Tim Berners-Lee.</h1>

Here is the code you would write in your code file. 

&lt;h1&gt;The creator of the WWW is Tim Berners-Lee.&lt;/h1&gt;

 

If you plan to work with non-Western languages you can review the section on ruby, rt and rp. 

 

 STUDY TIP

One way to keep track of the elements is to create sample pages that use the elements and attributes. Another way is to create a 'HTML syntax sheet' where you list each tag and what it does. A third way is to learn how to use web sites that reference the tags and attributes. The site below contains syntax help, samples and even allows you try out the examples online. 

 [link: https://www.w3schools.com/html/default.asp] HTML 5 Tutorial with details on all of the tags.

 [link: https://www.w3schools.com/tags/default.asp] HTML Reference and  [link: https://www.w3schools.com/tags/default.asp] Tag list and  [link: https://www.w3schools.com/tags/ref_standardattributes.asp] attribute list. 

 [link: #top] Top

 

Validating HTML Syntax

There are many editors. It is possible to use any text editor or web page editor to create a web page. However, web page editors often have syntax checking or what Microsoft calls Intellisense that can help you detect syntax related errors in real time. 

Validation Tools

Not all errors are detected in the editors. One option is to use a validation service that checks to see if your HTML code is compliant with the version of HTML identified in your <doctype>. If your doctype is for HTML 5, the validation service will compare your code to the HTML 5 standards and identify any errors detected. 

 [link: http://validator.w3.org] W3C Validation Markup Service is the tool we recommend. W3 is known as the World Wide Web Consortium or W3C or just W3 ( [link: http://www.w3.org] http://www.w3.org).

Each time you create a web page in this course, you are required to validate the code in the page to ensure that it is compliant with HTML 5 standards. 

Supported and Obsolete Tags and Attributes

The  [link: https://www.w3.org/TR/html52/dom.html#htmlelement] HTML Element standards are online but are challenging for beginners to read. Students should not use any deprecated or obsolete HTML tags or attributes in any web page. A better solution is to view the list of approved HTML tags at  [link: https://www.w3schools.com/tags/default.asp] W3Schools HTML Element Reference page.  You can also view the entire list of deprecated elements also at the  [link: https://www.w3.org/TR/2010/WD-html5-20100304/obsolete.html] W3C Obsolete Features page. 

Some elements such as group and cite are not commonly used or deprecated. Some browsers continue to support the <blink> tag which has been deprecated for many years. However, developers should not be using the blink element today. Editors can help verify the syntax to ensure you are not using deprecated or obsolete tags. Or, you can memorize the list! 

Common deprecated and obsolete elements include <center>, <applet>, <font>, <frame>, <frameset>, <big>, <blink>, <u>, <marquee>, <noscript> and <strike>. 

Common deprecated or obsolete attributes include: align, bgcolor, bgsound, color, border, cellpadding, cellspacing, valign, datasrc, link, text, noshade and vlink. Some attributes are deprecated when applied to certain tags, like name on <a> and <img> elements.

Debug this Code

Do you see why this is incorrect code? What could you do to fix this?

Example 1

// The Constitution  
<H1>The Constitution of the United States</H1>
<p>We the People of the United States, in Order to form a more perfect Union, <br>
establish <b>Justice</b>, insure domestic <i>Tranquility<i>, </br>
provide for the common defence, promote the general Welfare, <br/>
and secure the Blessings of Liberty to ourselves and our Posterity, <br />
do ordain and establish this Constitution for the United States of America.<p/> 
<img src="../images/constitution.bmp" width=400 height=250>

This is why using an editor is so helpful. Here would be the solution.

You can see that you had to fix the H1 tags to use lower case. All tags and elements are lowercase and all values are in quotes. The p closing tags have the / in the wrong place. The closing tag should be </p>. This is true for some of the </br> tags that should be either <br> or <br />. The space in <br /> does not matter. Replacement of deprecated or obsolete tags are also required. The image path is correct for this project but the file type is not a valid web graphic. Only gif, png, and jpg should be used. The values for the image size should be in quotation marks. 

<!-- The Constitution. -->
<h1>The Constitution of the United States</h1>
<p>We the People of the United States, in Order to form a more perfect Union, <br>
establish <strong>Justice</strong>, insure domestic <em>Tranquility</em>, <br>
provide for the common defence, promote the general Welfare, <br/>
and secure the Blessings of Liberty to ourselves and our Posterity, <br />
do ordain and establish this Constitution for the United States of America.</p>
<img src="../images/constitution.gif" width="400" height="250">

Only add images and resources that are open source, royalty free in the public domain, or that you own. You are expected to document the sources of your content, images and media in the web site as directed on the  [link: https://canvas.park.edu/courses/75721/pages/general-homework-requirements] General Homework Requirements page. 

Example 2 

This is a more advanced solution that shows that you cannot solve all the HTML syntax problems with HTML alone.

<body bgColor="red">
<p align="center">"But man is not made for defeat. A man can be destroyed but not defeated." 
By Ernest Hemingway</p>
<center>"The price of greatness is <u>responsibility</u>." By Winston Churchill</center>
<table>
<tr><td cellpadding="0"cellspacing="0"></tr></td>
</table>

Here would be the solution. Notice, that the HTML alone will not 'fix' the code. You will not be able to  'fix' the center tag error until you learn how to work with style sheet rules in a later chapter. Many of the attributes when they were deprecated, were added as properties that we can set using style rules. You'll learn more about style rules in a future lesson!

Again, this is just an example to show you that not all HTML syntax are 'fixable' with HTML alone. 

<body style="background-color:red;" >
  <p style="text-align:center;">"But man is not made for defeat. 
  A man can be destroyed but not defeated." By Ernest Hemingway</p>
  <p style="text-align:center;">"The price of greatness is 
  <span style="text-decoration:underline;">responsibility</span>." By Winston Churchill</p>
  <table>
    <tr> 
       <td style="padding: 0px; border-spacing: 0px; border-collapse:collapse; "> 
       </td>
    </tr>
  </table>
</body>

 

  DEBUGGING TIP: 

Common mistakes students make are copying code from online web sites that users post deprecated or obsolete tags. Some students are tempted to use web sites such as like Course Hero, Chegg, and Stack Overflow and copy code or web page editors. Resist the urge. May times they use older versions of HTML. You can recognize this by looking at the DocType and meta tags. Resist the urge. Write your own code and follow the standards! The code below is deprecated!

 [link: #top] Top [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
