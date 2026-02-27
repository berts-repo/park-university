# Unit 4: Lesson

Using Multimedia, IFrames and Forms, and Processing Forms with JavaScript Programs

Rather than provide separate lectures, we are going to ask you to read your textbook. We want you to read your book and take your own notes. Here are some notes we thought were most important or needed additional reinforcement or clarification. 

Chapter 7 Image Manipulations, Audio, and Video

Chapter 8 Organizing a Page's Content with Lists, Figures, and Various Organizational Elements 

Appendix B JavaScript Coding Conventions

 [link: #top] Top

IFrames

You can embed content with elements. You have already seen how to embed images with <img>. This unit we'll talk about image map, and iframe, audio and video elements. 

Web sites like YouTube used the embed element but are now using the iFrame element to share content. With YouTube you can use the full URL (https://www.youtube.com/watch?v=xJqSu1IbcHg) or a short URL (https://youtu.be/xJqSu1IbcHg) And to be honest, the iframe is really easy to work with.

IFrame Element

The iframe element is useful to insert other content and web pages into the page. It is possible to use server side includes but only if you use a server side technology such as PHP or ASP. The iframe creates a browsing context that contains the embedded content. Use a source (src) attribute to identify the web resource to insert.You can modify the source of the page loaded in the frame using JavaScript. The width and height attributes identify the dimensions of the page are identified before the page is loaded. The srcdoc attribute is used as an alternative, if you want to provide the raw html instead of a separate physical file. Use title for accessibility compliance. The seamless attribute displays the page as part of the main web page. A border is applied by default if the page is larger than the size attribute values, a scrollbar appears. Use CSS styles to modify the frame border, margin-height and margin-width and scrolling on the page. 

<iframe id="Example2"
    title="Example2" 
    allowfullscreen
    frameborder="0" 
 width="400" height="300" 
 src="URL"> 
</iframe>   

Do not use frames or framesets. These older methods are deprecated but still used by some web sites and content management systems. 

Here is an example of inserting a YouTube video using the iFrame. You can configure the properties of the page to enhance the appearance. Figure 1 shows an example of how the video might look inserted into your page.  

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/w9eqh_kGg-Q" 
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe> 

Figure 1 Displaying a Video in a Web Page

Here is the basic format for citing a YouTube video. The title is italicized.

Screen name. (year, month day). Title of video [Video file]. Retrieved from URL

TIP: Web sites such as  [link: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe] Mozilla Developer Network and W3Schools contain information on HTML 5 standards and support across browsers. Only  Chrome supports most of the sandbox features. The sandbox attribute will apply restrictions. This is to provide security between web sites.  

 

 [link: #top] 

 [link: #top] Top

 [link: #top] 

Shortcut Icons - Favicon

Favicon’s are useful for inserting images into the favorites, tab and history lists in the browser.  They can be used to help reinforce your brand. Browsers look for the favicon at /favicon.ico by default. You can use png or ico file formats. However, the syntax to insert the favicon will vary because icons can store more than one image in the file, of different sizes. 

For your web pages, use this syntax:

<link rel="icon" href="../images/m-favicon.ico">

However you might see other variations such as: 

<link rel="shortcut icon" href="favicon.ico" />
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
<link rel="icon" href="favicon.png" sizes="16x16" type="image/png"> (1 size)
<link rel="icon" href="favicon.png" sizes="16x16 32x32" type="image/png"> (2 sizes)
<link rel="icon" href="favicon.svg" sizes="any" type="image/svg+xml">

TIP: You can convert your images to favicons using the  [link: http://www.xiconeditor.com/] X-Icon Editor.
You can also download icons from  [link: https://www.freefavicon.com/freefavicons/] Free Icons.

 [link: #top] Top 

Video Media

A long, long time ago . . .

How we have worked with media in web pages has changed over the years. Just like how we have moved from using html attributes to css properties, we have changed the html elements and attributes we use to insert multimedia. In the past, we used bgsound as an attribute of the body element to insert a background sound. But the sound played and didn’t stop. You’d have to write JavaScript to enable a button to stop the sound. Alternatives were to insert sound in the page using the object or embed tags. Java Applets and Adobe Flash gained popularity as a way to insert multimedia into pages with controls in the page that could be used by the user to manage the media. Applets used the <applet> tag which was later deprecated.  Older browsers may use these older methods to manage media.

Today . . .

So what do we use today in HTML 5? New elements such as video and sound.

Video Sample

The video element has multiple properties you can configure.Provide default content for users without audio support. 

<video width="360" height="240" poster="poster.png" src="myvideo.mp4" preload="none" 
    autoplay controls muted> Your browser does not support this video format (MP4).
</video>

Video Properties

The width and height attributes control the size of the video on the screen. The browser preserves the video's aspect ratio and pads the sides of the video. 

The source (src) attribute identifies the location of the video which can be a relative or absolute URL. 

The controls attribute will display controls to manage the playback of the video.

The autoplay attribute indicates that the browser should start to play the video as soon as it is able to.

The loop attribute is a boolean value that indicates that the playback should repeat the video.

The poster attribute identifies the placeholder image that is displayed while the video is being loaded.

The muted attribute indicates that initially the video will be be muted.  

The preload indicates that the browser should download the video to reduce the delay when playing the video. However, if the user doesn’t view the video, this is a waste of bandwidth. The values are none, meta (which loads only the metadata and the first frame) and auto (the default behavior).

The track element is another child element of the video tag. The track element used by the video and audio elements, can help manage the chapter title (chapters), description, metadata, subtitles and captions, but is not widely supported.

Video Formats

There are no universal video formats. Browsers vary with the video support. All the new versions of the major browsers support MP4/H.264. Chrome supports MP4/H.264, Ogg/Theora and WebM. You need to understand that the video is encoded with a codec, which is stored within a container. Your system must have the proper codec and container to actually play the video.

We can use the source element to manage different video formats. The source element is a child element of the video and audio elements. In the source element use the source (src), type and media attributes to identify the individual formatted media. Type is the mime type such as video/webm, video/ogg and video/mp4. Media can be used to help customize the source selected based on the type of device. 

As you can see, the first version that matches a supported version on the client's system will win and play the video. So try to put the widely supported video tags first. 

<video controls width="360" height="240">
     <source src="timessquare.webm" type="video/webm" />
     <source src="timessquare.ogv" type="video/ogg" />
     <source src="timessquare.mp4" type="video/mp4" />
     <track src="subtitles_en.vtt" kind="subtitles" srclang="en" label="English">
     <track src="subtitles_ga.vtt" kind="subtitles" srclang="ga" label="Irish">
     <track src="subtitles_gd.vtt" kind="subtitles" srclang="gd" label="Gaelic (Scottish)">
     <track src="subtitles_gv.vtt" kind="subtitles" srclang="gv" label="Gaelic (Manx)">
     <track src="subtitles_fr.vtt" kind="subtitles" srclang="fr" label="French"> 
     Your browser does not support any of these video formats (WEBM, OGG, MP4)
</video>

TIP: The video and audio elements both inherit properties from HTMLMediaElements.  That is why the attributes are similar across elements. If you use JavaScript, you can get or set the defaults using the HTMLMediaElement. 

You can create interactive programs using JavaScript that modify and set properties and call methods to play, pause, resume, stop, louder and softer and restart media. You can read more about the interface for the video and audio elements on the  [link: https://www.w3schools.com/tags/ref_av_dom.asp] W3schools site. 

The HTMLAudioElement class provides access to the <audio> element. The HTMLMediaElement can also get or set the volume level using the volume attribute. 

The HTMLVideoElement class provides access to the <video> element. You can even play audio with the video control. The HTMLVideoElement can also get the intrinsic height and width of the video using videoHeight and videoWidth. The currentSource of the HTMLMedia element gets the current source of the video or audio element.  

 

 [link: #top] Top 

 [link: #top] 

 [link: #top] 

Audio Media

The audio element is used to insert audio media. The audio element also uses the width, height and source (src) attributes. You can use the audio control to play the audio portion of a video. Provide default content for users without audio support. 

<audio controls src="mytrack.mp3" autoplay>
     Your browser does not support this audio format (MP3).
</audio>

While MP3 format is widely supported by all major desktop browsers, no format is supported by all browsers on all platforms natively. So you’ll want to use the source child element to identify multiple formats.

<audio controls autoplay>
     <source src="mytrack.ogg" />
     <source src="mytrack.mp3" />
     <source src="mytrack.wav" />
     Your browser does not support any common audio formats (MP3, WAV, OGG).
</audio>

 [link: #top] Top

Image Maps

Image Maps

In the past . . .

Server-side image used the the ismap attribute, retrieved the coordinates of the position in the image you clicked on and appended the coordinates on the URL. Server-side image maps are not easily accessible and are not popular for many users. So we'll cover client-side image maps only.

Today . . .

Client-side image maps are useful. For example, in an election year you might indicate provide a map where you can click on a state and then you would go to the page with information about that state. Client-side maps use the map element with the image element. The image element has an attribute called usemap that identifies the name of the map in the map element. Make sure to include the pound sign (#) before the name! 

Nested in the map element are area elements.You should use the alt attribute for alternative text to support accessibility standards. Each area defines the coordinates with the coords attribute. Potential shapes include default, rect, circle and poly. If the shape is set to default, the area element does not require any coordinates.  Three values available for the shape element are: 

The rect attribute needs the coordinates of each corner (x, y, x, y).

The circle attribute needs the coordinates of the center of the circle and the radius (x, y, r).

The poly attribute needs the coordinates of each point on the polygon. (x1, y1, x2, y2 . . .)

<img src="myimage.png" usemap="#mymap" alt="My Image" width="200px" height="80px" />
<map name="mymap">
    <area href="page1.html" shape="rect" coords="0,0,100,100" alt="Left Side"/>
    <area href="page2.html" shape="rect" coords="100,0,200,100" alt="Right Side"/>
    <area href="page3.html" shape="circle" coords="100, 350, 50" alt="Circle"/>
    <area href="page4.html" shape="poly" coords="100,500,100,400,50,450" alt="Triangle"/>
    <area href="default.html" shape="default" alt="default"/>
</map>

Finding the Mouse Coordinates Using JavaScript (OPTIONAL)

You could retrieve the coordinates with JavaScript. The default 0 is displayed when the page is loaded. Notice how the JavaScript split method of the href attribute of the location object is used to split the querystring based on the commas and puts the results into an array. The first coordinate is the first value represented by [0]. The getElementById will retrieve the element based on the ID of that element. That is why it's so important to configure the ID of elements. The innerHTML attribute is used to change the text of the element. 

<p>X-coordinate: <span id="x">0</span></p>
<p>Y-coordinate: <span id="y">0</span></p>
<a href="mypage.html">
     <img src="myimage.png" ismap alt="My Image" width="200" height="80"/> 
</a>
<script>
    var coords = window.location.href.split('?')[1].split(',');
    document.getElementById('x').innerHTML = coords[0];
    document.getElementById('y').innerHTML = coords[1]; 
</script>

For more examples on the syntax of the image map, review the  [link: https://www.w3schools.com/tags/tag_map.asp] W3Schools Map tag page. The hardest part about the image map is to identify the coordinates in the picture that represent your image.The most difficult is working with a polygon. All you need is an image editing program that lets you see what the coordinates are where you click on your page. You just need to write them down in order for polygons. Image map editing programs simply record the coordinates for you. 

There are many online and free resources which can help you with this task.

How to make an image map using GIMP. Technology Websites.  [link: http://www.instructables.com/id/How-to-Make-an-Image-Map-Using-GIMP/] http://www.instructables.com/id/How-to-Make-an-Image-Map-Using-GIMP/ 

Image-Maps.  [link: https://www.image-maps.com/] https://www.image-maps.com/ 

 

 [link: #top] Top

CSS Icon Fonts vs SVG Icons?  

A long, long time ago . . .

Icons have been used since graphics were first supported on the web. Icons represent an idea or concept or resemble a physical object. They were often used to represent the home page, and email link or a help page. In the past, we used images for icon or font-families such as Wing-Dings and DingBats.  

JPG are bitmap images (rasterized or flat images) which do not support transparency and the images are often aliased by browsers, so they are not as crisp as the originals. So most of the icons were created in GIF format, because GIF supported transparency as well as layers and animations. More complex images used the Adobe Flash/Animate SWF format. Later a format called PNG provided both transparency and support for millions of colors. 

Today . . .

We use icons to enhance our page features by connecting us with other web sites, using a small amount of space. It is not unusual to see web sites with a number of icons used link users to their social media pages. 

We want the images used in these icons to be crisp and small file sizes. Today we used icon fonts and SVG graphics to create reusable icons. These are different from the original 'picture' icons which we created in graphics programs in how the images are created, saved and accessed. While icon fonts remain very popular, SVG icons are gaining in popularity because of their performance, appearance, customization and accessibility support. 

SVG Fonts

We can use native vector images (images in SVG format). SVG images can be styles with CSS. Because the content is stored in the web page and not in the font file, the SVG can change any part of the icons colors or have multi-colored icons using the stroke property. SVG fonts have better  [link: https://developer.paciellogroup.com/blog/2013/12/using-aria-enhance-svg-accessibility/] accessibility support. Many font providers specify a folder name. If you change the folder name you must use a local copy of the CSS files and change the path in the @font-face style rule. [link: https://developer.paciellogroup.com/blog/2013/12/using-aria-enhance-svg-accessibility/] 

If you are interested in making custom fonts, read about  [link: https://www.w3schools.com/graphics/svg_intro.asp] SVG from W3Schools and from  [link: https://css-tricks.com/svg-sprites-use-better-icon-fonts/] css-tricks.com   You can build and customize your own SVG files or obtain them from an online source. If you build them you can write the code directly to the web page. However it's more efficient to have separate SVG files and store the in your images directory or other location.

You can use a vector graphics editing program such as Adobe Illustrator to change an icon font glyph into an SVG file. According to  [link: https://css-tricks.com/svg-sprites-use-better-icon-fonts/] Chris Coyier you create the new document, select the icon font you want to use such as Webdings or Wingdings and then type the character on the document. Then you simply convert the text to outline format and save as a .SVG format. 

Icon libraries are available for free and commercially. Icon fonts are also known as glyphs, glyphicons or font-icons. These icons have to be a single color. But they can be customized with CSS style sheets, including changing the color and size. There are also issues with icon fonts such as  [link: https://www.filamentgroup.com/lab/bulletproof_icon_fonts.html] accessibility support  

Coyier, C. (APRIL 3, 2012).  [link: https://css-tricks.com/flat-icons-icon-fonts/] The Big List of Flat Icons & Icon Fonts (Links to an external site.)

 [link: https://fontawesome.com/] Font Awesome   and  [link: https://fontawesome.com/icons] Font-Awesome Icons (Links to an external site.) and  [link: https://fontawesome.com/cheatsheet] Cheatsheet List of Icons  

Bootstrap Version 3.37 uses 250  [link: https://getbootstrap.com/docs/3.3/components/] Glyphicons   from  [link: http://glyphicons.com/] Glyphicon Halflings (Links to an external site.). a commercial provider

 [link: https://octicons.github.com/] GitHub Octicons  

 [link: http://icomoon.io/app/] IcoMoon  provides icon fonts and SVG sprites 

Font Awesome is currently supported in Bootstrap 4 and the new version 5. The process for the other icon font providers is the same. Review their documentation as the syntax is slightly different. 

Here is how you would use the icon font in your web page. First import the CSS file into your web page. If the version changes, you need to download the new link from the  [link: https://fontawesome.com/get-started] Getting Started page.  You could alternatively download the fontawesome-all.css file and reference a local copy as shown below. You may see link with additional attributes. Type is the MIME type and rel is the relationship. 

<link rel="stylesheet"crossorigin="anonymous" 
  href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" 
  integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp">
<link rel="stylesheet href="../css/fontawesome-all.css" type='text/css'>

Then in any element or CSS style rule you can use the fonts.  Notice how many  [link: https://fontawesome.com/icons?d=gallery&s=brands] brands are available!

<span class="fa fa-cloud"></span>
<span class="fa fa-heart"></span>
<span class="fa fa-spinner fa-spin"></span>
<span class="fa-spinner fa-pulse"></span>

You can preview the brand design and layouts, such as  [link: https://fontawesome.com/icons/apple?style=brands] Apple. 

<span class="fab fa-apple"></span>
<span class="fab fa-github-square"></span>
<span class="fab fa-twitter"></span>
<span class="fab fa-facebook"></span>
<span class="fab fa-dropbox"></span>
<span class="fab fa-amazon"></span>

Notice here you can stack the icon fonts using fa-stack. So you can have add a circle, square or other shape behind another icon as well as layers. Here is the Twitter icon in a circle, square and an email icon with a counter displayed in the upper right corner. 

<span class="fa-stack fa-2x">
    <i class="fas fa-square fa-stack-2x"></i>
    <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
</span>
    <span class="fa-stack fa-2x">
    <i class="fas fa-circle fa-stack-2x"></i>
    <i class="fas fa-twitter fa-stack-1x fa-inverse"></i>
</span>
<span class="fa-layers fa-fw" style="background-color:pink">
    <i class="fas fa-envelope"></i>
    <span class="fa-layers-counter" style="background:Tomato">1,001</span>
</span>

You can customize the icons in CSS style rules as well as with JavaScript. You can rotate, flip, scale, position, add borders, bold, invert colors, alignment and even fill-in shapes of icons. If you actually look at the Font Awesome CSS file you'll see the code to access the font, is just the font number that matches the picture in the font file. 

.fa-heart:before {
     content: "\f004"; 
}

Google Fonts 

 [link: https://fonts.google.com/] Google fonts are open source and there are many free fonts online from sites such as  [link: https://www.urbanfonts.com/] Urban Fonts. But Google actually collects data on font usage and the data is published and accessible in the  [link: https://goo.gl/5HeqYf] Google Fonts BigQuery database. If the font has already been downloaded by the user, the page will use the copy available in the users cache. 

Let's look at  [link: https://fonts.google.com/specimen/Dancing+Script] Google's Dancing Script font. Data about the font such as the author and where the font is used is displayed. It is most popular in the US and used on over 760,000 web sites. It's easy to get started with Google fonts. Just link to the font style sheet. Then use the new font in your style sheet. Notice that spaces are replaced with ( + ) plus signs. You can import the font or link it to a style sheet. 

@import url(//fonts.googleapis.com/css?family=Dancing+Script);

Here is an example:

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Dancing+Script">
<script>
.p {
     font-family: 'Dancing+Script', serif;
} 
</script>

TIP: References and other services that provide the ability to download commercial fonts include:

 

Google Information page for a specific Google font:  [link: https://fonts.google.com/specimen/Dancing+Script?selection.family=Dancing+Script] https://fonts.google.com/specimen/Dancing+Script?selection.family=Dancing+Script 

CSS Page for a specific Google font:  [link: https://fonts.googleapis.com/css?family=Dancing+Script] https://fonts.googleapis.com/css?family=Dancing+Script 

 [link: http://www.typography.com/] Cloud Typography 

 [link: https://typekit.com/] Typekit 

 [link: http://www.fonts.com/] Fonts.com 

 [link: http://www.google.com/fonts] Google Fonts 

 [link: http://www.fontsquirrel.com/] Font Squirrel [link: http://www.fontsquirrel.com/]   

The Form Element

Forms allow you to collect input from the user. For class purposes, keep all the form controls together, within the form tags. Remember that all form data is sent as clear text, unless you use HTTPS with SSL to encrypt the data.   

Forms contain the form controls, such as textbooks and dropdown lists. Form elements commonly that create the form controls include form, input, select, texture, label, and button. Other useful form elements include optgroup, option, output, keygen legend and fieldset. 

The form element has several attributes you need to be aware of. Name and ID attributes of the form element are used to identify and distinguish forms. Having form elements outside the form might be useful in web pages that are spliced together from different sources. While it’s possible to have more than one form on a page, don’t include more than one set of form tags in a single web page. 

<form id="myRegForm" name="myRegForm" onsubmit="return false" class="form signup-form">

Sending Form Data

A form must be submitted to be processed.The form element properties help identify how to validate and process the form data. There are sometimes reasons not to use form elements around the form controls. For now, assume in your homework, you need the form element unless otherwise told! The action attribute identifies the location of the program that will process the form on the web server.

TIP: To stop the form from being submitted, you can intercept action="javascript:void(0);" and then send the program to a JavaScript function using onSubmit="processForm()". We can also automate the submission in JavaScript by returning false (onSubmit="processForm(),  return false;)" in the function or function call, or calling the submit function in JavaScript.  

The method attribute is either post or get. Post appends the data to the page request. Get appends the data to the URL in the address bar, as a QueryString. The QueryString is separated from the URL by a question mark (?).

The enctype element is used identify how the data is encoded and transmitted.  

The default value is application/x-www-form-urlencoded, which converts the form field named and values using URL encoding. That means that the data is sent as a single string with spaces converted to plus (+) signs. The string contains pairs of the names of the controls and the values, separated by equal (=) sign. The pairs are separated by the ampersand (&). These can be confusing but it's important to remember as you study for the exam! 

The multimart/form-data encoding method is only used for uploading files to the web server.

The text/plain encoding places the name and value pairs on separate lines with no encoding of special characters. 

Remember any URL is public over the Internet and TCP/IP provides ways to identify the routing information of the user and web site they are accessing. Only use get when you are using public read-only data. 

You can override the form element attributes by setting similar attributes for the submit button (such as form, formmethod, formaction, formenctype attributes). If you have form controls outside the form, you can use the form method to identify which form element the controls belong to. 

 [link: #top] Top

The Form Controls 

The web today is all about collecting data. To accomplish this we need forms and form controls to allow the user to enter their data. Different types of data need different form controls. We also want to organize the form controls so they are easy to complete. The form controls are also referred to as form fields. 

For all of the controls, you can customize them with global attributes and CSS style rules such as color, background-color, font properties, size and more. The form elements also support a range of  [link: https://www.w3schools.com/tags/ref_eventattributes.asp] global events which can be intercepted with event handlers. This means when the user types in something in a text box or clicks a button, we can intercept that event, and execute our own custom code. Let's describe the basic form controls first.

TIP: You will learn more about these form controls as you read through the book. This is an overview of the form controls. You may format the page with CSS Style rules to enhance your web page appearance. Use the template.css external style sheet to store your style rules. You can style the input element using CSS. Check out the  [link: https://www.w3schools.com/Css/css_form.asp] W3Schools CSS Forms page for additional methods to style form controls with style rules. For example, you can modify the text box border color, background color or image, font size, family and other font characteristics. 

Figure 2 Previewing an Example Form in a Browser

Legend and Fieldset

To help organize your form you can create groupings of form elements with the fieldset element, which puts a box around the elements and the legend element which adds a text heading on the box. The fieldset is useful to control how a user fills out a form. You can disable the shipping information controls until the user completes the billing information, by using the disabled attribute for the fieldset. 

Label

The label control is use to insert text which can be used to help the user identify the textbox and what they should enter. The label element is useful because you can set the field size in the style rules, making the form labels consistent. Use the for attribute to indicate which control the label is connected with. Some developers prefer to use placeholder rather than labels. This saves you space in your form layout which is useful for mobile devices. 

 [link: #top] Top

The Input Element 

The input element is used to create most of the form controls such as the textbox, radio button and checkbox. 

The text attribute allows alphanumeric characters. 

The size attribute is used to identify the length or number of characters displayed.

The maxlength limits the fixed number of characters that can be entered in the field.  

<input type="text" class="form-control"  id="txtFirstName" placeholder="First name"
tabindex="0" size="20" maxlength="20"required autofocusstyle="width:250px;display: inline;" >

Type Attribute

The type attribute is used to identify the type of data collected. The type is used to identify what kind of data is in the input field (text, number, date, email, color, range, password, URL, time, week, date, datetime-local and month). Other input types such as button, submit, reset, file, image radio, checkbox also are used in forms. The type attribute restricts the data type and format expected and often provide custom input methods such as color picker and calendar pickers. The type will attempt to validate the contents in the form matches the set of rules for that type. For example number must match a numeric value. 

Name: <input type="text" size="30" maxlength="30"/> 
Email: <input type="email" size="100"/> 
Telephone Number: <input type="tel" size="12" />
Color Preference: <input type="color" />
Date of birth: <input type="date" size="10" />
<input type="text" id="ssn" placeholder="#########" size="9" maxlength="9">
<input type="reset" value="Reset">
<input type="submit" value="Submit">

Common Form Input Types: 

The password type hides the characters from the user with asterisks ( * )

The checkbox type allows only a true/false response by using the checked attribute. The value attribute is on by default, which means that the value is only sent to the server if the user checks on the checkbox. 

<input type="checkbox" name="ckNewsletter" id="ckNewsletter" title ="Newsletter" 
value="You are signed up!" checked tabindex="0">

The radiobutton (radio button) type allows a single response from a limited number of choices and also uses the checked attribute. The name attribute identifies the radiobutton as a group and the id of each element is used to identify which radiobutton was selected. You can assign a default value by using the checked attribute. 

<input type="radio" name="rdMember" title="Member ($180)" id="rdMember" 
value="Member" tabindex="0">

We can use a button element or use a submit button to submit the form. The button element and the input element allow the type attribute to be set to submit, reset and button. There are several types of buttons that are customized based on the type attribute.

The button element is often used to call a function or act as a link or menu item

The reset type returns the form controls to their default state (usually empty). 

The submit type allows the user to submit the form when the button is pressed.

<button type="submit" id="btnSubmit" class="btn btn-primary" tabindex="0" 
onclick="processMyForm(this.form");">Place my order</button> 

The number type only allows numeric values (integer or real).

For both range and number controls, you will often specify a minimum and maximum value with the min and max attributes. 

The step attribute allows you to identify the granularity of the increments or decrements to the values. 

The range type is used to specify a range of values using a scrollbar. W3 provides examples of how to customize the  [link: https://www.w3schools.com/howto/howto_js_rangeslider.asp] range as a slider element using CSS style rules. It's a great way to enhance the appearance of your form.

<!-- Insert the zip code -->
<input type="number" class="form-control" id="txtPostalCode" 
placeholder="Zip code (02134)"  min="0" max="99999" pattern="[0-9]{5}"
style="width:150px;display: inline;" required tabindex="0">

Additional Input Types: 

The email, tel and url types requires the format in a specific string. Mobile devices will open the email program when you click on the email value, open the browser with the URL value and make a phone call when you click on the tel value.

The hidden type will hide the value in the browser. However the data is not hidden in the source code and therefore this should only used for data known to the client. Hiding values does not protect the data when it is transmitted to the web server program. The value of the hidden control is available in the source code file and should never be used to pass personal identifiable information, credit card, health care, educational records or financial data unless the entire web page is encrypted. 

   <input type="hidden" id="txtMySecret" value="Your name" />

The color type will display a color picker and return a color value in hexadecimal format. The color picker chosen will be based on the users operating system. Remember the color type may not be supported across all browsers. You will want to set the color attributes so that you can more easily see the color. You can also turn off the border and box-shadow of the color input control using style rules. Notice that the hashtag (#) is used to identify only this one control. However, an alternative is to use something like this code input[type=color] rather than #txtColor. However this would affect all color controls.

<input type="color" class="form-control" tabindex="0" id="txtColor" 
style="width:200px;display: inline;" title="Select your favorite color!">

Date provides a calendar picker. 

There are several date related input types such as date, month, time, week

Datetime-local is independent of the time-zone. 

You can have a field for users to select a date. The input type attribute can be set to date. The date control is not supported across browsers. This will bring up a calendar or date picker in the browser window, similar to the color picker. Several element such as datetime which included the timezone information are deprecated! So use date! Many  [link: https://www.w3schools.com/html/html_form_input_types.asp] new types were added with HTML 5 and described on the  [link: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input] W3Schools site. You may want to refer to the documentation and standards or use the validation tool at validator.w3.org to verify you are only using valid elements. 

The file type will allow the user to browse and select a file on the local system and set the enctype attribute to multipart/form-data. TWhile multiple is an attribute to allow multiple files, no browser supports this. 

The image type will create an image button. Because this is an image, height, width, and src (source) attributes are supported. The alt attribute is used to provide alternative text. 

The url type will restrict the user to entering a valid formatted URL. 

The search type will restrict the user to entering terms for a search. No real major differences here. But browsers can choose to display the textbox in different ways. 

Output

The output element can be used to display the results of a calculation. The oninput is helpful to cause the calculation to occur, when the user starts typing.

 

Datalist Element and List Attribute

The datalist is a field element, also used to create a list of options. The list attribute of a the input field, indicates which datalist to use to provide suggested values. The option elements can have a value and label assigned. 

TIP: You can also place the value displayed between the beginning and ending option tags. For both the select and datalist elements, if no value was provided the text between the option would also be the value. Often students forget that the value and label can be different such as the employee ID and the employee name.

 [link: #top] Top [link: #top] 

Other Form Elements

TextArea

The textarea control is not an input control. The textarea element is a multiline textbox. Identify the rows and columns with the rows and cols attributes. The wrap can be set to hard or soft to control the line breaks. The textarea control is used to allow users to enter more than one line of text.  You can identify the number of rows and columns to display using the rows and cols attributes.

<textarea id="txtComments" tabindex="0" class="form-control" rows="3"
placeholder="Enter any questions or comments here"></textarea>

Select, Option, and OptGroup

This chapter covers several form elements. Review listing 14-3. The select element is used to create the dropdown list or listbox. The size indicates how many items to show, and multiple attribute allows you to select multiple values. If you select multiple values, they are passed to the web server in a comma separated list. 

The option element provides the options in the dropdown list. The selected attribute lets you choose a default selected value. The value and label attributes work like the datalist. 

The optgroup element is used to group the options. Just nest the option elements within the optgroup beginning and ending tags.

<select class="form-control" name="txtState" id="txtState" size="1" required tabindex="0"
style="width:250px;display:inline;" >
     <option value="0" selected disabled>Select a State</option>
     <option value="AL">Alabama</option>
     <option value="AK">Alaska</option> 
</select>  

TIP: A useful site to locate the list of 50 states formatted as a dropdown list is available at  [link: http://lab.artlung.com/50states/] http://lab.artlung.com/50states/.

 [link: #top] Top

Commonly Used Global Attributes 

Most of the form controls have similar attributes such as autofocus, type, value, readonly and disabled.

The value attribute identifies an initial default value. Note that if you use the value attribute to identify a default value, the user can alter that value. If the user does not enter a value, the default value is then passed.

The placeholder attribute are grayed out because the placeholder provides context to help the user. (An example could be placeholder="(XXX)-XXX-XXXX"). The placeholder attribute is used to explain or show an example  on how the user needs to format the text. This helps the user to know what to type in the box, without the need for a label control. 

The readonly attribute means the user cannot edit the content and required means the user must enter a value (or a default value is entered) but readonly doesn’t provide any visual cues to the user.

The disabled attribute will not allow the field to be used and provides a visual cue to the user such as graying out the textbox. Disabled controls are usually grayed out. 

The autofocus attribute to configure which field should have autofocus.

The tabindex global attribute sets the order of the tabs so that the user can use the keyboard to tab through each field. 

 [link: #top] Top

Form Example

<form onsubmit="return false" 
      oninput="results.value = document.getElementById("customerName").value + 
           " " +document.getElementById("selFood").value;">
    <fieldset>
         <legend>Foods</legend> 
         <label for="food">Choose your favorite foods</label>
         <select id="selFood" size="1" multiple required autofocus>
              <optgroup label="Fruit">
                   <option value="1">Apple</option>
                   <option value="2">Orange</option>
                   <option value="3">Banana</option>
                   <option value="4" selected>Pear</option>
              </optgroup>
              <optgroup label="Meat">
                   <option value="5">Fish</option>
                   <option value="6">Steak</option>
                   <option value="7">Chicken</option>
              </optgroup>
          </select>
          <datalist id="customerName">
                   <option value="111" label="Smith, John">
                   <option value="222">Smith, Sara Jane</option>
                   <option value="333" />
          </datalist>
          <textarea rows="4" cols="50" id="txtFeedback">Write your feedback here</textarea>
          <button id="btnFood" type="button" value="Submit"></button>
          <output name="results"/> 
    </fieldset>
</form>

Example Using Styles to Format Form Controls

<style>
* { 
     color: #4CAF50; 
     font-size: 16px;
     font-weight: bold;
}
button {
    background-color: #4CAF50; /* Green */
    color: white;
    border: none;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
}
</style>

 [link: #top] Top

Input Validation

Using the Pattern Attribute with Regular Expressions

Students are requested in the assignment to use HTML validation. That means to use the HTML attributes and elements previously described to validate the data format without JavaScript. The type attribute will automatically verify that the data is in a valid format for email, tel, number, range and other elements. Many of the new form elements and attributes previously described, are useful to help in client-side validation of the data. 

Another attribute provides additional flexibility with form field validation on the client-side. The pattern attribute allows you to specify a regular expression that can be used to validate the data. This is often used to provide more comprehensive input requirements. For example "[0-9]{5}" means that you can only enter 5 digits. So, you have to make a choice, for a zip code. Use the pattern, or set the type to number. But you can't do both. 

What's awesome about this is you can use any valid regular expression. So check out the web sites online for valid expressions, like, an email address, web site address, social security number, telephone number, zip code, credit card number. You can also learn how to create custom expressions for things like your employee numbers.

 [link: https://www.regular-expressions.info/] regular-expressions.info

 [link: https://www.regular-expressions.info/creditcard.html] Finding or Verifying Credit Card Numbers at Regular-Expressions.Info

 [link: http://regexlib.com/REDetails.aspx?regexp_id=340] RegExLib.com

Here you have a pattern to match the email address for any user within your companies domain. 

pattern=".*@mydomain.com$"
pattern=".*@mydomain.$"

The pattern attribute is only allowed when the input type is one of the following:

email

password

search

tel

text

url

In the country textbox the pattern is set to [A-Za-z]{2}. the user can only enter 2 alphabetic characters from A - Z, either upper or lower case. In the phone textbox, the pattern is set to ^\d{3}-\d{3}-\d{4}$. So the format must be 999-999-9999. You do not use parenthesis ( ) with this textbox.  

In the email textbox the type is set to email. So the web page will validate the contents. However, an alternative is to use the pattern and set that to a regular expression such as [a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$. The reason developers prefer the regular expressions is that they can customize the rule. For example, the email pattern could have been set to[a-z0-9._%+-]+@[a-z0-9.-]+\..edu $. This rule is similar, but will validate that the email address ends in .edu. 

Likewise when the type is set to password the rule sets the minimum to 8 characters minimum. You can also set this in the pattern attribute. ?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}. However you may want to increase the required number of digits or change the complexity to help prevent bruce force and dictionary attacks. 

TIP: Notice the NaN may be returned from a form when the form calculations do not have the appropriate numerical input. NaN means not a number. You would want to really do the calculation in a script and include additional validation so that errors will not show up to the client. We will do this in JavaScript later in this lesson. 

Credit Card Processing

Please remember that validating using HTML or JavaScript is client-side and is not meant to replace security.  It is important to have example numbers that are valid and invalid. 

In the example, please use this number as a valid credit card number: 3711-078176-01234. You can use alternate 'fake' card numbers as shown:

Matches

3711-078176-01234

4123 5123 6123 7123

5123412361237123

Non-Matches

3711-4123-5123-6112 

Here is an example regular expression for credit card numbers. You do not need to memorize these patterns or write regular expressions beyond the  basics (zip code, state, phone, zip code).

pattern="^((4\d{3})|(5[1-5]\d{2}))[ -]?(\d{4}[ -]?){3}$|^(3[4,7]\d{2})[ -]?\d{6}[ -]?\d{5}$"

Regular expressions on credit card valid numbers can be found on many web sites such as  [link: http://www.regular-expressions.info/creditcard.html] http://www.regular-expressions.info/creditcard.html and  [link: http://regexlib.com/REDetails.aspx?regexp_id=340&AspxAutoDetectCookieSupport=1] http://regexlib.com/REDetails.aspx?regexp_id=340&AspxAutoDetectCookieSupport=1.

 [link: #top] Top 

Introduction to JavaScript

Overview

So you made a form. Now what? We need to process that form and JavaScripts are one way to process data on the client. JavaScripts or 'scripts' are not compiled into machine language; they are interpreted by the runtime environment in the browser. They are scripts are stored within <script> tags in the head section, body of the web page. Scripts can also be stored in an external file. 

Client-side programs written in JavaScript can collect, validate and process data on the client's computer and do not need an Internet connection for testing. For real applications you will want to be online to submit the form data to the web server. 

You will want to have a div tag or other element to insert your results in the web page if you want the user to see what they entered. This is also helpful for debugging. 

<!-- The form results will be displayed here -->
<div id="results" style="float:right; width: 500px; "> </div>

TIP:  You can view samples at the  [link: https://www.w3schools.com/js/default.asp] W3Schools JavaScript Tutorials and the   [link: https://www.w3schools.com/js/js_examples.asp] JavaScript Examples.

 

Script Element 

Most of the syntax, basic programming skills, working with objects and arrays will be the similar to other languages that you have studied. But they are not the same language! (We'll come back to language issues later.) Scripts are interpreted inline. That means that the script is loaded and run, when the browser encounters the script tag.

There are built-in objects, but they only make sense in the browser. You don't use JavaScript to create a native Windows or mobile application. JavaScripts may have counterparts in other languages. For example instead of MessageBox.Show("Hi") that we use in C# we could use window.alert("hi") in JavaScript. The browser creates the window dialog box for you.

TIP: JavaScript is case sensitive!

 

TIP: The type property can be set to "text/javascript". Since JavaScript is the default version we do not need the type property anymore. It is possible to put a version number but again, unnecessary because the browser defaults to a version of JavaScript for that browser. 

External JavaScript Files 

You can embed JavaScript programs using the script tag in the web page. However, you can also link to an external JavaScript program using the script tag. External JavaScripts are linked to the page with <script> tag where the src property is set to the URL of the external JS file. The script is in the head section, or at the bottom of the page, just above the closing body tag. 

<script src="Chapter7.js"></script>

Basic JavaScript Syntax  

You are not new to programming. So I'll just review a few important points. Creating and calling functions with function keyword and passing parameters is similar to other languages. Put the function keyword first.

Here are some other syntax rules with JavaScript. 

 

The plus ( + ) sign is the concatenation operator.

The equals ( = ) sign is the assignment operator.

Each statement is separated by a semi-colon (;). While it's easier to read one statement per line it is not a language requirement. However, for class, please use 1 statement per line. 

Only Strings have values passed in quotation marks. 

Do not break quoted literal string across lines unless you concatenate them.

Functions

In these examples alert() is a method used to display an alert window in the browser with a message.  This example just calls the function that displays the message. 

function function1() { 
      alert("hello world");
}
function1() 

This example calls the function and sends actual values as arguments to the function. The function uses them as parameters in it's own code block.

function function2(parameter1, parameter2) { 
      alert(parameter1 + " " + parameter2); 
}
function2("hello", "world");

This code uses variables as the arguments. This is preferred for class because it will be easier for you to debug. As you can see you can comment out the variable values and the function code would not have to change. 

// p1 = "hello"; p2="world"; 
p1 = "goodnight"; p2="goodbye"; 
function2(p1, p2);

In some cases you would call the function when the user clicks on a button. When that event happens, the function is called. Parameters may or may not be passed. If you are processing a form you may pass the form as a parameter. The keyword 'this' is used to identify the current form. 

<input type="button" value="Say Hello" onclick="function1();">
<input type="button" value="Submit the form"
    onclick="sendForm(this.form);">

Variables

JavaScript doesn’t have traditional fixed variable types so it's called a loosely typed language. You don’t have to explicitly declare variables before use. You can assign different data types to the same variable at different times. You can have local and global variables.  

The first statement is the variable declaration. When the variable is first defined, there is no value. Therefore if you try to use it you will get an error that the variable is undefined. 

Data Type Values:

String

Number (int, float, hexadecimal: 0xFFFF)

Boolean 

Object

Function

You can determine a variable's data type using typeof. 

typeof "story"                       // Returns "string" 
typeof 3.14                          // Returns "number"
typeof true                          // Returns "boolean"
typeof undefined                     // undefined
typeof x                             // Returns "undefined" (if x has no value)
typeof null                          // Returns "object"
typeof {product:'Chair', Price:20}   // Returns "object"
typeof undefined                     // undefined

The second statement is the variable assignment. Add a description comment next to the variable declaration. An initialization statement is a combination of a variable declaration and an assignment. 

Let's see some examples of how to define the variables of different data types.

 [link: #top] Top 

Data Types

Strings

For literal strings, you need to nest them within a pair of quotes.

var p1;  // Represents the first message
p1 = "hello"; p2="world";   
p1 = "Good 'Luck'"; 
p1 = 'Good "Luck"';  
p1 = 'Good "Luck""; // incorrect

Caution. Do not nest single quote literal values inside single quotes or double quote literal values within double quotes. 

Null and Undefined Values

Strings not assigned a value are undefined. Objects with no valid values are NULL. 

if (mystring.count == undefined)  
if (null === undefined)          // false 
if (null == undefined)           // true 

Determine if a number is null.

 

if (name != null) {
if (name == "") {

Determine if the number is an integer.

Number. isInteger ( ) determines if the value is an integer

Number.isSafeInteger( ) determines if integer is in the range from (253 - 1) to -(253 - 1)

Determine if a variable is a number. We can test whether a value is arithmetically processable or usable "like" a number. If it is not, you do not want to use that value in a function or expression. You might instead use another value or provide a default value.  Use Number.isNaN() to determine if a variable (or expression) is a number or able to be used in an expression. Returns true for any value that is not of the type Number.   [link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN] MDN Web Docs isNaN documentation explains this the best. You will want to consult the documentation if you rely solely on isNaN.  

Number.isNaN(123)                     // false so it's a number
Number.isNaN(0)                       // false so it's a number 

Reset Variables

After you are finished with a variable, you can reset it to conserve memory.

 

p1 = null;        // Now value is null, but type is still an object 
p1 = undefined;   // Now both value and type is undefined

Boolean

Boolean variables represent only true or false with no quotes and are often used in conditional expressions. You can use ! to represent the opposite. 

Boolean(10 > 9)     // returns true
(10 > 9)            // returns true
10 > 9              // returns true 
!(10 > 9)           // returns false

Constants

You can create your own custom constant values that do not change in your program. They are like variables but do not change values. Notice they are all in upper case. 

const CUBIC_INCHES_PER_GALLON = 231;

Numbers

There is only one number data type. You can write numbers as integers, in decimal or scientific notation.

x = 34.00
x = 34
x = 123e5
x = 123d-5

Operators are the same as in other languages.  Make sure to use parenthesis!

Logical AND and OR (&&, ||)

Tests for equality and identity are the same

 [link: #top] Top 

Documentation

For your homework you are expected to conform to documentation requirements and best practices as described in the  [link: https://canvas.park.edu/courses/75721/pages/general-homework-requirements] General Homework Requirements. 

Identifiers (IDs)

Follow the book directions. Use descriptive names. Usually functions and variables the first letter is lower case as in displayHello. Each additional word in the function starts with upper case. With form controls, describe the form element using a prefix such as tLastName or txtLastName or btnSubmit. 

Comments 

Use single line comments and multiple line comments

// Comment 
/* Comment */  

Coding Conventions

These conventions should be used in each homework assignment. Your instructor may have additional requirements or modifications that they will share in the  [link: https://canvas.park.edu/courses/75721/announcements] Announcements.

Include a comment above every function to describe the function’s purpose

For 2 or more functions, separate each adjacent pair of functions with a line of *’s surrounded by blank lines.

Put all variable declarations at the top of a function’s body, and for each variable declaration, provide a comment that describes the variable.

Provide an “end …” comment for each function’s closing brace.

Position a function’s opening brace ({) at the right of the function heading, separated by a space.

Position a function’s closing brace (}) in the same column as the function heading’s first character.

Between a function’s opening and closing braces, indent each statement with two spaces. [link: #top] 

 

 

 [link: #top] Top

Beginning JavaScript

The first example is important because it shows how events and functions work together. 

<script> 
function displayHello() { 
      var msg; msg = document.getElementById("message"); 
      msg.outerHTML = "<h1>Hello, world!</h1>"; 
} 
</script> 

In this case no arguments were passed to the function. 

In the body we have a block or container element where we will store the message.  When the user clicks on the button, the click event triggers the onclick event handler. But, we intercepted the event using the onclick property in the button. The onclick event handler now calls instead, the displayHello() function. 

<body> 
    <h3 id="message"> To see the traditional first-program greeting, click below. </h3> 
    <input type="button" value="Click Me!" onclick="displayHello();"> 
</body>  

Because the JavaScript was loaded already in the page, the page knows about the function and executes the function. The function retrieves the element you want to write to, the message element and assigns it to a variable. To retrieve the element, pass the ID of the element to the getElementById method. 

We can then change the contents and even the HTML tags!  OuterHTML replaces the outer tags and the content. InnerHTML would replace just the content. 

Sometimes you will see programmers shorten this code. However, using variables will help you later as our programs get longer!

<script> 
function displayHello() { 
      document.getElementById("message").outerHTML = "<h1>Hello, world!</h1>";  
} 
</script> 

Try this!

<script> 
function displayHello() { 
   document.getElementById("message").outerHTML = "<h1>Hello, world!</h1>"; 
} 
function displayGoodbye() { 
   document.getElementById("message").innerHTML = "Goodbye!"; 
} 
</script>

 [link: #top] 

In the body enter this:

<body> 
<h3 id="message">Click a button below. </h3> 
<input type="button" value="Say Hello!" onclick="displayHello();"><br />
<input type="button" value="Say Goodbye!" onclick="displayGoodbye();"> 
</body> 

 [link: #top] Top

Creating a Basic Function in JavaScript to Process Form Data

You will use some basic JavaScript to return the results to the user. 

At the very bottom of the page you will create your basic JavaScript. Later in the course you will learn how to write the code in an external file. 

Insert the script tags. 

Create a function called processMyForm. This must match the name of the function listed in the onclick event handler in the submit button. 

Insert an alert method to test to see if the function is called when the user fills out the form and clicks the submit button. You must pass a string to the alert method. If the alert message does not work, review your JavaScript syntax. If there is any error, the script will not run. 

Get the current date and store is in the variable d. The date is needed to display the date on the receipt. 

Retrieve the results object you created earlier. Use document.getElementById and pass the ID of the control you want to retrieve. Notice that the getElementById is case sensitive. 

<script> 
function processMyForm() {
  alert("Thank you for joining our team!"); 
  // Check to see if the fields are empty
  // Get the current date
  var d = new Date();
  // Get the results control
  var results = document.getElementById("results"); 
}
 </script> 

TIP: W3Schools provides examples of other page and commonly used  [link: https://www.w3schools.com/tags/ref_eventattributes.asp] form event attributes that you can use to customize your programs. For example, there is onclick, onchange, onselected, onsubmit, onload and onunload, onmouseover and onmouseout, and onfocus,events that can be intercepted. These are also listed in your book readings!

 [link: #top] Top

Retrieve Form Control Values in JavaScript

You can retrieve values from a form multiple ways. Each one of these are methods built into the document object. They are also case sensitive. Most of the time you will use document.getElementById("id"). 

The getElementByID can retrieve the control if you pass the ID of the control. 

The getElementsByName will retrieve all elements with the name you specify such as txtName

The getElementsByTagName will retrieve all elements with a tag name you specify such as h2.

The getElementsByClassName will retrieve all elements with the same class name you specify.

TIP: Another option is to work with the forms collection. The forms collection includes all the form controls that are nested within the form. The document.forms[0] will retrieve the first form. From there you can use the name to retrieve the form field value. The document.forms[0].elements.namedItem("id").value will retrieve the form control value. However, document.getElementById("id").value is shorter. There are times though that you may want to create programs to iterate through the forms collection. In that case you could reference each element within the collection based on it's index in the collection. 

Retrieve the Radio Buttons and Checkbox Values

Now you will need to retrieve the values of the radio boxes and checkboxes. Notice that you can't just get the value directly. You need to retrieve all of the elements together using getElementsByName. Then you have to determine if the element is checked, and then getting the value.  

TIP: The programming syntax to create variables, concatenate values, create for-loops and if-else statements is very similar to other programming languages. That is why there is a programming prerequisite in this course. 

Insert a few blank lines after the line of code that reads: 

var results = document.getElementById("results");

Type the code shown below in those blank lines. Notice the syntax of the comment is different than HTML comments. 

// retrieve the values of the radio button and checkbox
var message = "";
var rb = document.getElementsByName("rdMemberStatus");
for (var i = 0, length = rb.length; i < length; i++) {
    if (rb[i].checked) {
        message = "Member Status: " + rb[i].value + "<br />\n";
    }
    else {
    }
}
var ck = document.getElementsByName("ckNewsletter");
for (var i = 0, length = ck.length; i < length; i++) {
    if (ck[i].checked) {
        message = message + "Newsletter: " + ck[i].value + "<br />\n";
    }
    else {
    }
} 

Retrieve the Radio Buttons and Checkbox Values

Now you can retrieve the rest of the values from the form controls. You are going to concatenate the values and some text that you will display in the web page. There is a pattern that you should pay attention to. 

Insert the comment. 

Set the results.innerHTML to the long string that you will create. 

// Display the results control
results.innerHTML = "Here is your receipt: <br /><br />\n" +
   "Name: " + " " + document.getElementById("txtFirstName").value + " " +
        document.getElementById("txtLastName").value + "<br />\n" +
   "Address: " + " " + document.getElementById("txtStreet").value + ", " +
        document.getElementById("txtCity").value + ", " +
        document.getElementById("txtPostalCode").value + ", " +
        document.getElementById("txtState").value + ", " +
        document.getElementById("txtCountry").value + "<br />\n" +
   "Phone: " + " " + document.getElementById("txtPhone").value + "<br />\n" +

Now comes the challenge. You need to write the rest of the code.

Retrieve the rest of the form field values using the same pattern. You can combine values such as the credit card information onto one line. 

On the line after your retrieve the password, insert the message variable. 

message +

On the last line you will then need to display the the current date that you retrieved earlier and stored in the variable "d". 

After retrieving all of the form fields, insert a line of code that will display the current date in the coordinated universal time format (UTC). 

"Date Submitted: " + d.toUTCString() + "<br />\n"  ; 

Figure 3 Viewing the Results

 [link: #top] Top

Document Object Model (DOM)

Your book has a good overview of the DOM node tree and how to refer to elements.  Nodes are arranged in a hierarchical fashion with the root node (document) at the top of the tree. Dynamic HTML refers to updating the web page’s content by manipulating the DOM’s nodes. 

TIP: The 'root' node of the HTML code in a web page is html. 

 

We will use this code format to retrieve elements from our page. 

document.getElementById(elementID)

NOTE

The  [link: http://teach.park.edu/~jdean322/phoneManager/phoneManager.aspx] Employee Phone Manager Form in the example, does not use JavaScript. It uses a server side program technology called Active Server Pages (ASP). Server-side programs sends data to a local or remote web server, where it is processed, and the results returned and displayed in the client. 

MouseOver

The onclick event is used often with buttons. With hyperlinks, the onclick event is used as well as the mouseover and mouseout, to create a hover effect with images. Use the keyword this to represent the current object (the image element). 

<img src="../images/image1.jpg" width="130" height="100" alt="Alternate Text"
        onmouseover = "this.src='../images/image2.jpg';"
        onmouseout = "this.src='../images/image1.jpg';">

But you can also use CSS with no JavaScript to create a similar effect. 

<img class="mouse" src="../images/image1.jpg" alt="Alternate Text" width="130" height="100">
<style>
/* Configure the hover style using pseudo-element, for any valid properties */
img:hover { 
        src: url('../images/image1.jpg');
}
img:hover { 
        -webkit-transform: scaleX(-1); // Flips the image
        transform: scaleX(-1);
        src: url('../images/image2.jpg'); // Can also use different image
}
</style>

TIP: More information on how to use  [link: https://www.w3schools.com/css/css3_images.asp] CSS Styling with Images is found on the  [link: https://www.w3schools.com/css/css3_images.asp] W3Schools.com site. 

 

 [link: #top] Top 

Email Generator

Make sure to review the email generator in the book and samples, as well as the common event and event handlers in the readings. 

Displaying the Results

What's also different is that we use the web page as the default standard output.

We can send output to a separate web page, or 'pop-up' window. 

We can send output to a separate special browser window. 

We can write directly to the browser and force the browser to reload the page with the new content. This is more helpful for debugging.

We can modify the content or HTML on the web page itself. We often display the results or content returned from the script within a container or block element such as a <p> or <div> element.  

So for now,  we'll use these basic steps to retrieve the values and display the results.

Form controls gather data from the user

<input type="text" id="txtControlID"> 

Block or container control for the results output

<p id="results"> 

Call the function 

<input type="button" value="Click Me!" onclick="functionName(this.form);"> 

Create the function

function functionName(form) {   // don't forget your comments!    }

Use one of these to access the form value

document.object (document.getElementById("txtControlID").value

form.elements["txtControlID"].value

Do something with the value, such as a calculation or setting a property in the page. 

document.object (document.getElementById("txtControlID").value

form.elements["username"].value = "admin";

form.elements["password"].readOnly = true;

Assign the output to a block or container control or a dialog window.

document.getElementById("results").innerHTML = value;

alert(value);

 [link: #top] Top 

CSS Image Sprites  

Sprites let you use one file, and identify selected parts of the image to display. So it's commonly used for animation and games. Sprite sheets can be used for buttons, and other graphic elements on your web site. These are also used when the web page needs raster or bitmap images. 

The book includes an example of how to implement sprites. However, your homework will not require  you to implement a sprite within a web page. 

Sprites are commonly used with div, a and img tags. The key is to modify the styles to use a different background image when the user mouses over the image or clicks on the image. If you have a gap between the images make sure to include that in your measurements.

<a id="myimage"></a>
#myimage {
  display: block;
  width: 300px;
  height: 200px;
  background-image: url(../images/myimage.png);
  background-position: 0 0;
}
#myimage:hover {background-position: 0 -200px;}
#myimage:active {background-position: 0 -400px;}

 [link: https://www.giftofspeed.com/sprite-generator/] CSS Sprites Generator (Links to an external site.)Links to an external site. tool is useful to assemble multiple images into one image.  You can also use graphic editors such as GIMP or Adobe Photoshop or Illustrator. [link: #top] 

 [link: #top] Top 

 [link: #top] 

Next:  

Now please go to the discussion page and participate in the discussions and then complete the homework activity.

 [link: #top] Top
