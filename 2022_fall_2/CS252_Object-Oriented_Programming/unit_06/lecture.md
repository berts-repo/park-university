# Unit 6: Lecture

Select the tabs below to view each topic

 [link: #fragment-0] Configure JavaFX

 [link: #fragment-1] GUI Basics

 [link: #fragment-2] Event Handling

 [link: #fragment-3] GUI Program Design

 [link: #fragment-4] More on GUI

We need to configure JavaFX with our IDE before building GUI programs. See  [link: https://canvas.park.edu/courses/71018/files/9524373?verifier=J4x3RefTS4wQvBzZIzSMzgmmP71ZANISiUtlEupU&wrap=1] Install_OpenJDK_JavaFX.docx on how to install JavaFX. Next see  [link: https://canvas.park.edu/courses/71018/files/9524130?verifier=LyilrCxQiLKtyLnfvclgoeKdEiLDf5IpRWj8rBlz&wrap=1] ConfigureJavaFX.docx on configuring JavaFX with Eclipse (If you use VS Code, at least read the first two pages to get a basic idea and then follow the video below).

This tutorial uses JavaFX 17 (for OpenJDK17). However, older versions are fine as long as your JavaFX version matches that of your OpenJDK/JDK (just the main version number). For example, if you have OpenJDK/JDK 11, install JavaFX 11.

Here is a video demonstrating the steps with Eclipse on a Windows 10 machine:

VM arguments (modify the path if you have a different version or if your JavaFX library files are at a different location):
--module-path "C:\Program Files\javafx-sdk-17.0.0.1\lib" --add-modules javafx.controls,javafx.fxml 
Mac users: the VM arguments may be something like this (without "" and uses /):
--module-path C:/Path/to/your-javafx-sdk-17/lib --add-modules javafx.controls,javafx.fxml

A video demonstrating the steps with VS Code on a Windows 10 machine:

Add the following line to launch.json of your VS Code project (modify the path if you have a different version or if your JavaFX library files are at a different location). Be sure to add a ,  after the existing lines in launch.json before our "vmArgs" line: 
xxx,
"projectName": xxx, 
"vmArgs": "--module-path \"C:\\Program Files\\javafx-sdk-17.0.0.1\\lib\" --add-modules javafx.controls,javafx.fxml"
Mac users: the vmArgs line may be something like this (without "" and uses /):
xxx,
"projectName": xxx, 
"vmArgs": "--module-path C:/Path/to/your-javafx-sdk-17/lib --add-modules javafx.controls,javafx.fxml"

 [link: https://canvas.park.edu/courses/71018/files/9523879?verifier=bgOA40APkRWSWNEiW1IJyL8M2bBvXZvgkC5D5fPj&wrap=1] Unit6_1_PPT_Code.zip

 [link: https://canvas.park.edu/courses/71018/files/9524107?verifier=xHGxPN3OHZv73lVbMDFHD98ZdoJ8WK7g3EvgiqSg&wrap=1] Unit6_1_GUIbasics.pptx

 [link: https://canvas.park.edu/courses/71018/files/9523877?verifier=Izbkio0yRt4KES8rdflEMH9EpTpo9vIK1QTM83wn&wrap=1] Unit6_2_PPT_Code.zip

 [link: https://canvas.park.edu/courses/71018/files/9523769?verifier=gd16QmjL3SE1aB2qAuhwwdd9OAYccerywkc5ORBg&wrap=1] Unit6_2_EventHandling.pptx

 [link: https://canvas.park.edu/courses/71018/files/9523966?verifier=sW3AvrQXz8EwnvShs1yYEjUZrn3dcJcl5lHMX2it&wrap=1] Unit6_3_PPT_Code.zip

 [link: https://canvas.park.edu/courses/71018/files/9523866?verifier=D6oEn3xCaPFWGRf2spMHY82CZgqd22HYqDLthK5w&wrap=1] Unit6_3_ProgDesign.pptx

 [link: https://canvas.park.edu/courses/71018/files/9524104?verifier=pvCh1R8JaIkIxiidEf07tu9E040LILIuSBCawHcO&wrap=1] Unit6_4_MoreOnGUI.pptx
