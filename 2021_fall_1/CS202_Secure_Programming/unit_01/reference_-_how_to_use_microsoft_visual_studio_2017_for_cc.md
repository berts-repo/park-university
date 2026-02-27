# Unit 1: Reference - How to Use Microsoft Visual Studio 2017 for C/C++

This document contains guidance on how to perform various tasks in Microsoft Visual Studio to write, compile, debug, run and store C/C++ projects and files. It is intended as a reference document when students want to obtain quick answers on How-To-Do things in Microsoft Visual Studio. They include the following topics:

 [link: #fragment-1] How to obtain Microsoft Visual Studio in your computer

 [link: #fragment-2] How to access Microsoft Visual Studio in Citrix Park Virtual Lab

 [link: #fragment-3] How to set Microsoft Visual Studio to work on C/C++ projects for first time

 [link: #fragment-4] How to create a New C/C++ Project from scratch

 [link: #fragment-5] How to enable a C/C++ Project to work with a Window Console

 [link: #fragment-6] How to create/add a new source file in a C/C++ Project

 [link: #fragment-7] How to compile a C/C++ Project (a.k.a Building a C/C++ Project)

 [link: #fragment-8] How to run a C/C++ Project

 [link: #fragment-9] How to disable Warnings as Errors when Compiling>

 [link: #fragment-10] How to add an existing source file to a C/C++ Project

 [link: #fragment-11] How to create a C/C++ Project from an existing source file(s)

 [link: #fragment-12] How to save a C/C++ file

 [link: #fragment-13] How to remove/delete a C/C++ file from a Project

 [link: #fragment-14] How to save a C/C++ Project

 [link: #fragment-15] How to close a C/C++ Project

 [link: #fragment-16] How to exit Microsoft Visual Studio

 [link: #fragment-17] How to re-open a previously saved C/C++ Project

 [link: #fragment-18] How to create backups of a Project saved in Citrix

 [link: #fragment-19] How to restore a saved Project from backup to Citrix.

How to obtain Microsoft Visual Studio in your computer

This course uses Visual Studio on the Citrix Park Virtual Lab environment. Here we will explain how to use this environment to create and run C/C++ Projects. However, students may download versions of Microsoft’s Visual Studio Community Edition in their own machines, but they will have to adapt the instructions in this document to their own configuration. Microsoft’s Visual Studio Community Edition is free. Its functionality is virtually identical to Microsoft’s Visual Studio Professional, but it’s oriented towards individual developers and small teams, rather than large collaborative projects used in industry. To download it, go to:

 [link: https://www.visualstudio.com/downloads/] https://www.visualstudio.com/downloads/

and click on the Community option. During the installation, when you’re prompted to select your “workloads,” you’ll want to select Universal Windows Platform development and Desktop development with C++, plus whatever else you think you might want.

After the download and installation completes, you should launch Visual Studio. When asked whether you’d like to sign up for a Microsoft account, feel free to decline.

How to access Microsoft Visual Studio in Citrix Park Virtual Lab

The tutorial “Accessing Visual Studio in Citrix.park.edu” in this course, explains how to access that environment (read that document first). If you have problems, contact Park’s ITS help desk at support_technology@park.edu.

How to set Microsoft Visual Studio to work on C/C++ projects for first time

If this is your first time using this software, or the settings in Citrix are lost, the following screen may display:

There is no need to Sign in or Sign Up, just click the message below (Not now, maybe later) to enter the software. The following window may appear:

Click the button labeled “Start Visual Studio” at the bottom right corner of the window. A screen similar to the following one should show up, indicating a successful opening of Visual Studio:

Microsoft Visual Studio is ready to work all sort of projects in various languages, but we will use it to work on C/C++ projects. For these it would be good to set two features:

Displaying line numbers on code. Having numbers in the lines of code makes them easy to recognize when debugging a program.

Using spaces for indentation. Having spaces rather than tabs in indentation will eliminate many misalignment problems between platforms.

Follow the next steps to set these two features. If the features were already set as indicated, keep them that way.

Inside Microsoft Visual Studio 2017, select Tools menu in the Toolbar, and select Options.

In the options tree at the left, expand the Text Editor container.

Inside the Text Editor container, expand the C/C++ sub-container.

Select the General option.

Make sure the Line numbers box is checked.

The window should appear as shown below:

In the same Options dialog, in the same Text Editor container, C/C++ sub-container:

Select the Tabs option.

In the Indenting area, select the Block option.

If the Insert spaces radio button is unchecked, check it.

The window should appear as shown below.

How to create a New C/C++ Project from scratch

To create a new C/C++ Project in the Citrix environment do the following:

In Microsoft Visual Studio Menu select File / New / Project…

That should cause a New Project dialog to appear.

In the Installed panel on the left, select Visual C++.

In the middle panel, select Empty Project.

In the Name box, enter a name for your Project. The system automatically provides a name for you, usually ProjectX, where X is a number. You may choose any name you want, or use the proposed name.

To the left of the Location box, click the Browse button.

A File explorer Windows will show up. Find and select the Desktop as shown in the red ellipse below:

(It is recommended that you create and work projects on the Desktop in Citrix. It is faster. Before ending a Citrix session you will need to save your files in your local drives for future use) :

Once the Folder is found, click the Select Folder button.

Make sure the Create directory for solution box is unchecked.

If the box is unchecked, the IDE automatically creates a directory named test and stores the project and C++ files in that directory. If the Create directory for solution box is checked, then the IDE creates a directory named test inside test (a test directory inside a test directory), and that's inappropriate.

The Dialog box should look like this:

Click OK.

The following Screen may show up:

If so, just click OK and wait until the project is created as shown below. The figure shows an empty Project1:

How to enable a C/C++ Project to work with a Window Console

A newly created project will enable you to build “console applications”. A “console application” is a program that runs in a black and white text-based window, known as a console, a.k.a. command line. However, a problem with a new console is that it is set so that after the program runs, it immediately closes the console window, preventing you from seeing the program’s output. To change this behavior, one must set a new project as follows:

You should see a Solution Explorer panel within your Visual Studio window. If you don’t see it, select View / Solution Explorer.

In the Solution Explorer, right click on your project (test) and select Properties. That should cause a Property window to display.

In the Configuration Properties tree, expand Linker and select System. Find the Subsystem field in the right panel, and click the down arrow on its right:

In the drop-down menu, select Console. The screen will appear like the following:

Click OK.

The new project was created in the Desktop of the Citrix environment because it will be easier to handle it in that location. Be aware that if you create the project in any other directory in the Citrix environment you may have trouble to find it later on, and if you create it in your local drives (USB or hard drives) they may not compile. That is another reason for using the desktop.

To create a new C/C++ project in your own environment, you may follow the same instructions, but you will need to decide on the location for your projects.

How to create/add a new source file in a C/C++ Project

To add a source file (.cpp or .hpp extension) to a C/C++ Project do the following:

You should have the Project on which you are adding the file opened.

Select Project / Add New Item…

That should cause an Add New Item dialog to appear:

In the left panel, under the Visual C++ heading, select Code.

To write a C/C++ source file, in the middle panel, select C++ File (.cpp).
   OR

To write a C/C++ header file, in the middle panel, select HeaderFile (.h).

In the Name box, enter the name of the file, for example hello.

In the Location box, the Project’s folder should appear by default (for example test, or ProjectX).

Click Add to close the dialog. A new panel will appear where C/C++ code could be written. Notice that the name of the file appears at the top of the new panel and in the Solution Explorer under the project:

After writing code for in the new file it should be saved by clicking the Save Icon ()or selecting the File Menu and the Menu Item ‘Save filename’  (with filename replaced by the name given to the file, for example hello.cpp):

How to compile a C/C++ Project (a.k.a Building a C/C++ Project)

Once a project has a program that includes a main function it can be compiled to translate it into machine code (compilation). If the project consists of more than one file, or it it has #include statements inside its files, there is an additional linking process in which all external references to names in other files are resolved. Microsoft Visual Studio will compile all files in the project and will link all references.

To compile and link (a.k.a. build a project) select from the menu the options Build / Build Solution as shown below:

If there are problems with the compilation or the linking they will be described in a new panel, named Error List, that will appear at the bottom of Microsoft Visual Studio:

All problems shown should be corrected before the file produces a runnable version of the program. When all problems are fixed the project is ready to be run.

Sometimes a program may not compile, because it shows Warnings, but not real errors. In those case you will need to disable Warnings as Errors when Compiling. See this section for details.

How to run a C/C++ Project

To run a C/C++ Project the program must be free of syntax errors discovered while compiling and it should have resolved all its references thru the linking process. Without successful compilation and linking no project can be run. See How to compile a C/C++ Project (a.k.a Building a C/C++ Project) above for directions on this regard.

Once a project is successfully compiled and linked, one can run it by selecting from the menu the options Debug / Start without Debugging, as shown below:

These options will generate a Console Window where the project will run, displaying all printing done by the program, and, if the program expects input, receiving it from the user’s keyboard.

If the project was compiled and linked successfully and no Console Window appears when the project is run, or it appears and disappears quickly, it is an indication that the Project has not set properly the option to work with the Console. This option needs to be enabled. See How to enable a C/C++ Project to work with a Window Console. above for directions on this regard.

How to disable Warnings as Errors when Compiling

Sometimes when trying to compile a C/C++ Project, Microsoft Visual Studio will issue Warnings instead of Errors. Warnings should not prevent the program from running. They are only cautionary advice the compiler or linker give regarding possible vulnerabilities with the code. A typical example of a warning is when the program is using a library function that has been deprecated. This means that the function is still available in the language, but there is another version of the function that is currently preferred. For example, the following warning prevents the program for compiling because the program is using the scanf function (a legitimate function that is deprecated by Microsoft Visual Studio):

The default setting for Microsoft Visual Studio is to prevent the final compilation and linking of a project if there are Errors or Warnings. If we know that the program has no Errors and we want to run the code, despite of the Warnings we need to modify the default setting.

To disable Warnings to be treated as Errors when compiling, you should see a Solution Explorer panel within your Visual Studio window. If you don’t see it, select View / Solution Explorer.

In the Solution Explorer, right click on your project (test) and select Properties. That should cause a Property window to display.

In the Configuration Properties tree, expand Configuration Properties and then expand C/C++, select the General item as shown:

In the right panel, be sure to set the following properties, if they are not already set:

Treat Warning As Errors No (/WX-)

   And

SDL Checks No (/sdl-)

To modify these options you may click on them and a drop-down arrow will appear to their right. Select No from the options provided as shown below:

Click OK to finish.

How to add an existing source file to a C/C++ Project

If a C/C++ program file is written/obtained from outside the Microsoft Visual Studio, it can be incorporated in a C/C++ Project. The Project has to be created first. Refer to the topic How to create a New C/C++ Project from scratch for information on this regard. Once the Project is created it will have a Folder. To add a C/C++ file to the Project, follow the next steps:

Copy or move the C/C++ file (.cpp, .h or .hpp) inside the Projects Folder.

You may use the File Explorer to do so. If necessary, you may consult the document Accessing Visual Studio in Citrix.park.edu for instructions on how to access the File Explorer in Citrix (under Accessing your Local Drive From the Citrix Environment).

Have your Project opened in Microsoft Visual Studio.
You may consult the topic How to re-open a previously saved C/C++ Project for information on this regard.

Select Project / Add Existing Item…

That should cause a File Selection dialog to appear. Select the file to be added to the Project and click Add.

The file will be added to the list of Files in the Solution Explorer Panel on the right.

How to create a C/C++ Project from an existing source file(s)

This course provides a number of C/C++ files with examples of programs that illustrate the contents of the course. Students should create projects for them to compile, run, and modify in their learning process. Students should create a project with Microsoft Visual Studio and add the file or files to be studied to this project. Once added they can be compiled, linked and run. The steps to do are as follows:

Create a C/C++ Project with Microsoft Visual Studio.
You may consult the topic How to create a New C/C++ Project from scratch for information on this regard.

Add the C/C++ file(s) to the Project..
You may consult the topic How to add an existing source file to a C/C++ Project. for information on this regard.

The Project is then ready to be compiled and run.
You may consult the topics How to compile a C/C++ Project (a.k.a Building a C/C++ Project) and How to run a C/C++ Project for information on this regard.

Students may keep separated projects for each of the provided programs. An alternative and recommended strategy would be to create and have an empty C/C++ Project in Microsoft Visual Studio. Every time the student wants to test new programs s/he may delete any previous code from the project (you may consult How to remove/delete a C/C++ file from a Project), and add the new code for compilation, running and testing. Student should decide what is the best strategy for them in this regard.

How to save a C/C++ file

Files inside projects are automatically saved when the project is compiled and run (building). When writing code to a file it is also advisable to save it from time to time, in the eventuality that a power or connectivity failure erases all our efforts. To save a single file already in a Project do the following:

Select the File to be saved by clicking its Panel.

Click the Save Icon () or select it from the File Menu and the Menu Item ‘Save filename’  (with filename replaced by the name given to the file, for example hello.cpp):

How to remove/delete a C/C++ file from a Project

A file inside a Project may be Removed or Deleted. Removal means that the file is taken out of the Project, but it still remains in the Project folder (or wherever location where the file is). Deletion implies that the file is both, removed from the Project and also permanently deleted from the file system.  To remove or delete a file from a C/C++ project do the following:

Select the File to be removed/deleted by right-clicking its name in the Solution Explorer Panel.

For example, to delete the hello.cpp file from the current Project, right-click its file name where indicated:

A menu will appear. Select the Remove menu item:

A Window with choices will appear. Select the Remove button to remove the file or the Delete button to delete the file:

How to save a C/C++ Project

A Project can be saved as follows:

Click the Save All Icon () or select it from the File Menu and the Menu Item ‘Save All’:

How to close a C/C++ Project

A Project can be closed as follows:

Select ‘Close Solution’ from the File Menu. If the Project has files that need saved, Microsoft Visual Studio will ask your approval to save the files:

How to exit Microsoft Visual Studio

To exit Microsoft Visual Studio, do the following:

Select ‘Exit’ from the File Menu. If any Project has files that need saved, Microsoft Visual Studio will ask your approval to save the files:

 

How to re-open a previously saved C/C++ Project

A previously saved C/C++ Project can be re-opened by double-clicking its Solution File. The Solution File is a file that manages the Project. It can be found inside the folder where the Project is located. It usually has the same filename as the Project with file extension .sln. The following shows an example:

The following figure shows the contents of the folder where all files from Project1 are stored.

By double-clicking the file Project1.sln (shown), Microsoft Visual Studio will open the project.

How to create backups of a Project saved in Citrix

Projects stored in Citrix must be saved to a local drive (a hrd drive or USB drive) before ending a Citrix session. Files stored in Citrix may be deleted from session to session, that is why it is important to keep backups of the Projects in local drives. To create a backup do the following:

Use the File Explorer to locate the Project Folder in the Citrix Environment. As explained in the document. Accessing Visual Studio in Citrix.park.edu, you will click the Windows icon in the bottom left corner of the Student Lab Desktop:

This will open the Start Panel:

By clicking the “This PC” Icon or the “File Explorer” Icon you will obtain a File Explorer Windows that will show both, the folders in the Citrix environment, as well as all the local file sources attached to your computer:

If you stored the Project in Citrix’s Desktop, click the Desktop in the panel to the left of the window to start searching your project. The following screen will show up:

Select and click your name or Park ID in the folders displayed, the following screen will be displayed:

Select and click the Desktop Icon show above, the folders in your desktop should be displayed, for example:

Copy the project that you are going to save.

Use the File Explorer to find the local devices where the backup will be stored. Local devices will be listed under “This PC” on the left side of the File Explorer:

Their labels may appear a little odd, but the first letter is the drive letter that it has been assigned on your local computer. For example, in the figure below, drive C$ (\\Client) (V:), is the hard drive of your local machine C:. Do not confuse it with Local Disk (C:), that is the Virtual hard drive in the Citrix Environment. In a similar manner, drives D$ (\\Client) (U:), and E$ (\\Client) (E:) in the figure below, correspond to the local drives D and E, possibly USB drives in the user’s computer.

Select the destination and paste the copied folder. Avoid erasing previous work.

How to restore a saved Project from backup to Citrix.

Use the same process described in How to create backups of a Project saved in Citrix in reverse. That process described how to copy from the Citrix environment to a local drive. Just do the opposite, and copy the project from a local drive to your Desktop in the Citrix environment.
