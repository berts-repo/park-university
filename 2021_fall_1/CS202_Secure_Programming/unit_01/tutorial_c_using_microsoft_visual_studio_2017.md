# Unit 1: Tutorial: C++ Using Microsoft Visual Studio 2017

[link: #fragment-1]  Start Here

 [link: #fragment-2] Setting Visual Studio 2017 Before Use

 [link: #fragment-3] Creating a C++ Visual Studio 2017 Project

 [link: #fragment-4] Saving the C/C++ Project from Citrix Environment to a Local Drive

 [link: #fragment-5] Restoring a Saved C/C++ Project from a Local Drive to the Citrix Environment

 [link: #fragment-6] Debbuging a C++ program in Visual Studio 2017

 [link: #fragment-7] Adding an existing C/C++ file to a Project 

OBTAINING AND INSTALLING VISUAL STUDIO FOR YOUR HOME COMPUTER:

This course uses Visual Studio on the Citrix Park Virtual Lab environment. This document will explain how to use this environment to create and run C/C++ Projects. However, students may download versions of Microsoft’s Visual Studio Community Edition in their own machines, but they will have to adapt the instructions in this document to their own configuration. Microsoft’s Visual Studio Community Edition is free. Its functionality is virtually identical to Microsoft’s Visual Studio Professional, but it’s oriented towards individual developers and small teams, rather than large collaborative projects used in industry. To download it, go to  [link: https://www.visualstudio.com/downloads/] Microsoft Visual Studio Downloads and click on the Community option. During the installation, when you’re prompted to select your “workloads,” you’ll want to select Universal Windows Platform development and Desktop development with C++, plus whatever else you think you might want.

After the download and installation completes, go ahead and launch Visual Studio. When asked whether you’d like to sign up for a Microsoft account, feel free to decline.

If the installation above doesn’t work or you don’t want to install, you can always use Visual Studio in the Citrix Park Virtual Lab environment to be found at  [link: https://citrix.park.edu/Citrix/ParkWeb/] https://citrix.park.edu. The tutorial “Accessing Visual Studio in Citrix.park.edu”, explains how to access that environment (read that document first). If you have problems, contact Park’s ITS help desk at support_technology@park.edu.

SAVING FILES:

If you're compiling using Visual Studio installed on your home computer, you should save your project files on your computer’s hard disk or USBs. If you're at the school's lab, do not use the hard disks! Instead, use a USB flash drive storage device.

However, you must be aware that when working with C/C++ projects in Visual Studio on the Citrix Park Virtual Lab, there is a bug that prevents successful compilation when project files are stored on your local devices. The work-around is to initially create and work your projects within the Desktop of the Citrix Park Virtual Lab, and when finished, before closing the Citrix environment, make a copy of the whole project folders to a local drive. Be mindful that projects may be deleted from the Citrix environment between sessions, so you may need to upload them again from your local copies when a new working session begins. You may find instructions on how to make a copy of a project to a local drive under How to restore backups of Project saved in Citrix in the reference document How to Use Microsoft Visual Studio 2017 for C/C++.

VISUAL STUDIO TUTORIAL:

This tutorial uses x: to refer to the drive that you're saving your work on. In the lab, x: should be replaced by the USB drive (do not specify the hard drive!). At home, x: should be replaced by the USB drive or the hard drive, whichever you prefer.

Whenever the tutorial asks to perform an action (left column below) that students have previously done, it will refrain from providing the supplemental information (right column below). If a student doesn't remember the details of how to do something, they should look for it earlier in the tutorial or consult the document How to Use Microsoft Visual Studio 2017 for C/C++. Students may have to look up a lot of previously covered material. This is an attempt to force them to start remembering how to do things.

Setting Visual Studio 2017 Before Use

The following commands will set up Visual Studio to enhance the programming experience in this environment. This may have to be set the first time you use Visual Studio in the Citrix environment, or every time the settings are lost (not an infrequent occurrence).

Commands to Set-Up Visual Studio to Enhance the Programming Experience 

Actions

Supplemental Information 

Load Visual Studio.

Search for the Microsoft Visual Studio 2017 Icon and double click it.

Alternatively,

Click on the Start button.

Search for Microsoft Visual Studio 2017 and click it.

 

Set C++-specific coding-style preferences.

In the Tools menu, select Options.

In the options tree at the left, expand the Text Editor container.

Inside the Text Editor container, expand the C/C++ sub-container.

Select the General option.

Make sure the Line numbers box is checked.

In the C/C++ sub-container, select the Tabs option.

In the Indenting area, select the Block option.

If the Insert spaces radio button is unchecked, check it.

Click OK to close the Options dialog.

Display build toolbar.

Select Tools / Customize.

In the Customize window, select the Commands tab.

Select Toolbar, and then, using the pull-down menu to its right, select Debug.

Click Add Command.

In the Add Command window, under the Categories Panel, select Debug.

If you see the Control: Start Without Debugging, Click the Close button.

If you do not see it, then, under the Commands Panel to the right, select Start Without Debugging.

After clicking OK, you should return to the Customize window and see this:

 

Click Close.

 

 

Creating a C++ Visual Studio 2017 Project

sing Microsoft Visual Studio 2017

Actions
Supplemental Information 

Create a new project.

Select File / New / Project…

That should cause a New Project dialog to appear.

In the Installed panel on the left, select Visual C++.

In the middle panel, select Empty Project.

In the Name box, enter test.

To the left of the Location box, click the Browse button, then find and select the Desktop as shown in the red ellipse below:

Some screen similar to the following will show up:

Select and click your name or Park ID in the folders displayed, the following screen will be displayed:

Select and click the Desktop Icon show above,

Click the Select Folder button

Make sure the Create directory for solution box is unchecked.

If the box is unchecked, the IDE automatically creates a directory named 225pgms\test and stores the project and C++ files in that directory. If the Create directory for solution box is checked, then the IDE creates a directory named test inside 225pgms\test (a test directory inside a test directory), and that's inappropriate.

The screen will look something like this:

Click OK.

The following Screen may show up in the Citrix environment:

If so, just click OK and wait until the project is created:

Proceed with the Application Wizard.

Clicking OK should cause an empty project to appear that will enable you to create “console applications.” Console application” refers to a program that runs in a black and white text environment, not in a graphical user interface (GUI) environment.

Saving the project.

You should see a Solution Explorer panel within your Visual Studio window on the right. If you don’t see it, select View / Solution Explorer.

Within the Solution Explorer panel, make sure that your test project is selected.

Click on the save icon on the Toolbar (). That should save the item that’s highlighted in the Solution Explorer panel (i.e., that should save the test project).

Verify the project is saved.

Go to File Explorer and locate the test folder in Citrix environment’s Desktop.

Prevent console window from disappearing.

When you create an empty project, unfortunately, the IDE’s default behavior is to immediately close the console window after the program runs. That prevents you from seeing the program’s output. Change that behavior by doing this:

 

In the Solution Explorer, right click on your project (test) and select Properties. That should cause a Property window to display.

In the Configuration Properties tree, expand Linker and select System. Find the Subsystem field in the right panel, click it and click the down arrow on its right:

In the drop-down menu, select Console. Click OK.

Add a .cpp program file to your project.

Select Project / Add New Item…

That should cause an Add New Item dialog to appear.

 

In the left panel, under the Visual C++ heading, select Code.

In the middle panel, select C++ File (.cpp).

In the Name box, enter hello.

In the Location box, the test folder should appear by default.

The screen should look like this:

Click Add to close the dialog.

Writing a C/C++ program.

Enter this text in the hello.cpp panel such that <your name> is replaced with your actual name.

/****************************************
* HelloWorld.cpp
* <your name>
*
* This program says "hello" to the world.
****************************************/

#include <stdio.h>

int main()
{
  printf("Hello, world!\n")
} // end main

In the hello.cpp source code panel, enter this text:

The top section is known as the prologue section. It provides documentation for human readers. The compiler ignores everything between the opening /* and the closing */.

The prologue section.

Make sure that the hello.cpp file is highlighted in the Solution Explorer panel. Click on the save icon.

Save the source file.

Select Build / Build Solution.

That should cause a compilation error message to appear in the Output panel at the bottom of your Visual Studio window.

Compile your program.

The error message should be something like:

If you double click on a compilation error message, your cursor should jump to a statement that is involved in the compilation error. For this example, if you click on the error message, your cursor should jump to the last curly bracket. To fix the problem, add a semicolon to the end of the previous statement, like this:

printf("Hello, world!\n");

Fix the compilation error.

 

Recompiling should generate a success message in the Output panel at the bottom of your Visual Studio window. Something like this:

Recompile your program.

 

Select Debug / Start Without Debugging.

That should cause a console window to appear with your program’s output (Hello, world!) inside it.

Press the Enter key and the console window should close.

Run your program.

If necessary, fix runtime errors.

 

 

When completed, save your Project and close it.

 

Within the Solution Explorer panel, make sure that your test project is selected.

 

Click on the save icon on the Toolbar (). That should save the item that’s highlighted in the Solution Explorer panel (i.e., that should save the test project).

Select File / Close Solution

Exit from Visual Studio.

Select File / Exit

Saving the C/C++ Project from Citrix Environment to a Local Drive

sing Microsoft Visual Studio 2017

Actions
Supplemental Information 

Start File Explorer.

Start File Explorer.

This will open the Start Panel:

Click “This PC” Icon or “File Explorer” Icon. File Explorer will show up:

Search and Copy the Project to be saved

Search the Folder structure to find the project folder for test.

If you stored the Project in Citrix’s Desktop, follow the Desktop Icon until you find the  project:

Copy the project folder test.

Search the destination Folder for the Project backup

Use the File Explorer to find the local devices where the backup will be stored. Local devices will be listed under “This PC” on the left side of the File Explorer:

 

Once you find the destination for the Project save the previously copied folder.

 

Once you find the destination for the Project save the previously copied folder.

 

Once you are certain the project was copied to a local drive you must delete it from the Citrix environment.

 

Locate the Folder for the test Project in the Citrix environment.

Right Click over its icon, select Delete.

The project folder and all its files are deleted from Citrix.

 

Restoring a Saved C/C++ Project from a Local Drive to the Citrix Environment

sing Microsoft Visual Studio 2017

Actions

Supplemental Information 

Start File Explorer.

Click the Windows icon in the bottom left corner of the Student Lab Desktop:

This will open the Start Panel:

Click “This PC” Icon or “File Explorer” Icon. File Explorer will show up:

Search in your local drives the Project to be restored and Copy it.

Search the Folder structure to find the saved copy of the project folder for test.

This should be in one of your local drives listed under “This PC” on the left side of the File Explorer:

Copy the project folder test.

Search the destination Folder for the Project backup

Use the File Explorer to find your desktop the local devices where the backup will be stored. Local devices will be listed under “This PC” on the left side of the File Explorer:

 

 

Once you find your desktop save the previously copied folder test.

 

Start the Project

To start the project open the test folder in File Explorer.

You will notice that there are a couple of files with the same name as the project folder: test.

If you move your mouse over the files, you will see information about them.
Find the file test.sln in the folder

Double-click the icon for the file test.sln.  This should open the project in Microsoft Visual Studio. If this is the first time this option was used the following Window may show up:

Select Visual Studio 2017 and the project will appear:

Debbuging a C++ program in Visual Studio 2017

sing Microsoft Visual Studio 2017

Actions

Supplemental Information 

Start Visual Studio.

 

 

Open your test project.

Remove hello.cpp from your project.

In the Solution Explorer frame, right click on your hello.cpp file, and in the pop-up menu, select Remove. A window will appear giving you the following choices:

Select Remove.
Don't worry – that doesn't delete the file, it only removes it from the project. And you need to remove it from the project so that a different program can be in charge. If you actually want to delete the file the option Delete would have perform a permanent deletion.

Add a new countUp.cpp source code file to your test project.

In the countUp.cpp source code panel, enter this text:

/****************************************
* countUp.cpp
* <your name>
*
* This program counts up to a user-entered value.
****************************************/

#include <stdio.h>

int getNumber()
{
  int number;
  printf("Enter an integer: ");
  scanf(“%d”, &number);
  return number;
} // end getNumber

//****************************************

int main()
{
  int number = getNumber();
  for (int i=-number; i<=number; i++)
  {
    printf(“%d “, i );
    if (i = 0)
    {
      printf(“\nhalf way there!\n);
    }
  } // end for

} // end main

Save your countUp.cpp source file.

Compile your program.

 

When compiling, you may see an error in the bottom panel that says something like this:

This is a Warning indicating that the program cannot compile because it is using the function scanf that is deprecated by Microsoft Visual Studio.

To overcome this problem in the Solution Explorer, right click on your project (test) and select Properties. That should cause a Property window to display.

In the Configuration Properties tree, expand Configuration Properties and then expand C/C++, select the General item as shown:

In the right panel, be sure to set the following properties, if they are not already set:

Treat Warning As Errors No (/WX-)

   And

SDL Checks No (/sdl-)

To modify these options you may click on them and a drop-down arrow will appear to their right. Select No from the options provided as shown below:

Click OK to close this window and re-compile.

Run the program.

You should see a prompt to enter an integer. Enter 5.

After pressing enter, your Console panel should be filled with multiple lines of 1 1 1 1 1 …

Terminate the program.

Your program is experiencing an infinite loop.

To stop the infinite loop, click the console window’s X button.

 

Understand how to walk through your program using the 3 stepping modes.

 

To walk through your code one line at a time, you can use the debugger’s Step Into, Step Over, and Step Out commands. Step Into will take you into a called function, Step Over will execute a called function with one step, thus skipping the function body. Step Out will execute the entire remainder of the current function and jump back to one line after the original function call.

Walk through your program using the Step Into mode.

Select Debug / Step Into.

That should cause a yellow arrow to appear next to the first line in main.

 

Click the Debug menu. Notice F11 next to the Step Into option.

The F11 function key is a hot key. Pressing a hot key provides a shortcut alternative to using a menu.

After closing the Debug menu, press F11.

That should cause the arrow to move down to the next line.

Press F11 several times and stop after the arrow has stepped inside the getNumber function definition code.

Step into and out of the << operator definition.

Press F11 several more times and stop when the arrow resides on this line:

printf("Enter an integer: ");

 

Press F11.

That should cause the arrow to step inside the printf function definition code. There’s no need to step through this function code because it came from Microsoft and it’s bug-free.

To step out of the printf function definition, select Debug / Step Out.

Use the Step Over mode.

To avoid stepping into the printf function definition code again, select Debug / Step Over.

Press F10 (which is the hot key for stepping over).

When you are prompted to enter an integer, enter 3.

 

Continue to press F10 until the arrow resides on this line:

if (i = 0)

Examine main’s local variables.

In the Visual Studio window, note the variables panel below the source code panel. The Autos and Locals tabs at the bottom of the variables panel indicate types of variables that can be examined.

 

Click on the Locals tab, which displays the values for the current function’s local variables.

 

In the variables panel, note that i has the value -3 and number has the value 3. That should make sense.

Figure out the problem.

Press F10.

Note in the variables panel that i now has the value 0. Why? The purpose of if (i = 0) is to ask “Is i equal to 0?”, but that’s not what happens. Since the assignment operator is used (single =) rather than the equality operator (double ==), the i = 0 code assigns 0 to i.

Stop the debugger and fix the bug.

Select Debug / Stop Debugging.

Change if (i = 0) to if (i == 0) in the program.

 

Save your program and recompile it.

Set a break point.

To see whether the changed code works, you could step through the program one line at a time. But to avoid that tedium, this time you should skip the first part of the program and step through the code starting at the if statement. To do that, you need to first set a break point at the if statement.

 

Click somewhere on the line if (i == 0).

Select Debug / Toggle Breakpoint.

That should cause a red ball to appear at the left of the if (i == 0) line.

 

Run your program to the breakpoint.

Select Debug / Start Debugging.

As an alternative to using the menu, you could have pressed F5 (the start debugging hot key) or clicked the right-facing green triangle button near the top of the Visual Studio window.

 

When you are prompted to enter an integer, enter 3.

That should cause the arrow to appear on the if (i == 0) line.

Execute the fixed code.

 

Press F10 to execute the if (i == 0) line.

In the variables panel, notice that i has retained its value of -3.  Yeah!

 

Run your program to the next breakpoint.

Click the continue button, which is the right-facing green-triangle button near the top of the Visual Studio window.

That should cause the arrow to appear once again on the if (i == 0) line.

Remove the breakpoint.

You could click the continue button for each iteration of the for loop, but to save time, you can remove the breakpoint.

 

To toggle the breakpoint off, click anywhere on the breakpoint line and then select Debug / Toggle Breakpoint.

Run to the end of the program.

Click the continue button.

Since there are no breakpoints, that should cause the program to run to completion.

Unfortunately, “running to completion” includes shutting down the console window, so you won’t be able to see the final output.

View the program’s output.

To see the final output, you could of course select Debug / Start Without Debugging. But if you’re in the middle of a debugging session, that doesn’t work. Instead, what you can do is insert a breakpoint on the last line of the program. Then, if you want to see the final output, simply click the continue button and the program will stop at the remaining breakpoints (including the one at the very end).

 

Insert a breakpoint on the last line of the program.

Select Debug / Start Debugging.

When you are prompted to enter an integer, enter 3.

 

Click the continue button to run to the program’s last line.

View the output in the console window.

Click the continue button to complete the program’s execution.

Save the Project and Exit from Visual Studio.

 

 

Adding an existing C/C++ file to a Project

This course provides a number of C/C++ files with examples of programs that illustrate the contents of the course. Students should create projects for them to compile, run, and modify in their learning process. Students should create a project with Microsoft Visual Studio and add the file or files to be studied to this project. In this exercise we assume that the student obtained the source file from the course and save it in the test project folder

sing Microsoft Visual Studio 2017

Actions

Supplemental Information 

Obtain a source file from the course and save it in the folder for the test Project.

The file ACheckSizes.cpp was obtained from the course files and was saved in the folder of the test project:

Start File Explorer and open the test Project.

Remove countUp.cpp from your project.

In the Solution Explorer frame, right click on your countUp.cpp file, and in the pop-up menu, select Remove. And press the Remove button.

Add ACheckSizes.cpp to the test Project

Select Project / Add Existing Item…

That should cause a File Selection dialog to appear. Select the file ACheckSizes.cpp and click Add.

The file will be added to the list of Files in the Solution Explorer Panel on the right.

Double-click its name for the source code to appear.

Compile and Run the Program

 

Save the Project and Exit from Visual Studio.
