# FAQ: Packet Tracer, Netlab

[link: #fragment-1] Packet Tracer

 [link: #fragment-2] Netlab

Questions about Netlab system and Netlab assignments

 [link: #q1] Q1: What is Netlab?
 [link: #q2] Q2: How do I access Netlab?
 [link: #q3] Q3: How do I get an account to access Netlab?
 [link: #q4] Q4: For a router or a switch, how do I save a configuration file
 [link: #q5] Q5: How do I save the result from a PC?
 [link: #q6] Q6: How do I finish a reservation?
 [link: #q7] Q7: What happens if I skip a Netlab project?
 [link: #q8] Q8: How many Netlab projects can I do per unit?
 [link: #q9] Q9: A router in Netlab uses an Fa0/0 interface, but the project description says to use G0/0 interface. What should I do?
 [link: #q10] Q10: I ran out of time to complete a project. How can I re-start a project where I left off?
 [link: #q11] Q11: What are the specific Netlab reservation rules at Park University?
 [link: #q12] Q12: The Time Limit only shows 1.0 hour. How much time can I reserve to do a project?
 [link: #q13] Q13: I reserved a 2-hour lab time. Do I get the full 2 hours to do the project?
 [link: #q14] Q14: How can I utilize the copy-and-paste features in Netlab?
 [link: #q15] Q15: Why and how to undock a device?

Q1: What is Netlab?
Answer: NETLAB provides a communication platform, allowing students to remote login into a set of physical networking equipment to perform the laboratory projects specified in Cisco Networking Academy. Netlab has different software versions. The one that we use for this course is Netlab+.

 

Q2: How do I access Netlab?
Answer: You will access Netlab via  [link: https://labs.fhsu.edu/] https://labs.fhsu.edu/.

 

Q3: How do I get an account to access Netlab?
Answer: Your instructor will email your id and password to you via your Park email account at the beginning of a term/semester. 

 [link: #top] BACK TO TOP

Q4: For a router or a switch, how do I save a configuration file
Answer: Please follow the following steps.

Figure 1 shows the option to save the configuration file.

Figure 2 shows where the configuration is saved. Click Manage > Configuration Files.

Figure 3 shows the list of saved configuration files.

Figure 4 opens a configuration file. Right click > Select All > Copy, and then paste into a .docx or .txt file.

Figure 1: Save Configuration

Figure 2: Manage > Configuration Files

Figure 3: List of saved configuration files

Figure 4: Right Click > Select All > Copy, and then paste into a .docx or .txt file. Then submit the file into the Canvas submission box.

 [link: #top] BACK TO TOP

Q5: How do I save the result from a PC?
Answer: From the PC, select "Take Screenshot" option, see Figure 5. Then, click "Submit" to log the screen shot in the Netlab system. 

 

Figure 5: Take a Screenshot from PC A.

Q6: How do I finish a reservation?
Answer: To finish a reservation, click Reservation > End Reservation Now. See figure 6.

Figure 6: End Reservation Now.

 

Q7: What happens if I skip a Netlab project?
Answer: Because of the accumulative nature of the computer networking concepts, skipping a required laboratory project in one unit may affect the performance of other laboratory projects in the subsequent units.

 

Q8: How many Netlab projects can I do per unit?
Answer: You can perform as many Netlab projects as you wish. However, only the result of the required Netlab projects will be graded.

 

Q9: A router in Netlab uses an Fa0/0 interface, but the project description says to use G0/0 interface. What should I do?
Answer: When executing the project, be sure to read the instruction under the Topology as the Netlab physical equipment setup may be different from the setup in the project description. In the router, issue a command such as “show ip interface brief”. It will show all available interface types.

 [link: #top] BACK TO TOP

Q10: I ran out of time to complete a project. How can I re-start a project where I left off?
Answer: For most the Netlab projects, by saving the configuration file using the command copy running-config startup-config in a router or a switch, you can restart the router or the switch where you left off if you wish to go back to the same project in the future. You can also save the configuration file for a device, and load the configuration later. For the final skills assessment, Netlab system will start from the initial system default configuration every time you take the assessment.

 

Q11: What are the specific Netlab reservation rules at Park University?
Answer: 

Maximum 2 hours per Netlab reservation.

The minimum duration between any two consecutive Netlab reservations is 2 hours.

The instructor reserves the right to adjust reservation limits to resolve capacity issues if they should develop, including tightening or loosening the time limits as needed.

During each lab reservation, you can work on only one NetLab project.

It is highly recommended that you do the lab project as early as possible in any given unit.

It is also recommended that early in a unit, you reserve a lab time.

Students should study and analyze a lab project ahead of time before their lab reservation time so that they don’t waste reserved lab time to study the project description and requirement.

 [link: #top] BACK TO TOP

Q12: The Time Limit only shows 1.0 hour. How much time can I reserve to do a project?
Answer: The “Time Limit” shown next to a project is the time limit recommended by the author of the project. See Figure 7. If your instructor allows a maximum of 2 hours per reservation, then you can set 2 hours per project. If you setup 5 hours per projects, the system will automatically set your reservation to 2 hours.

Figure 7: Project Time Limit

 

Q13: I reserved a 2-hour lab time. Do I get the full 2 hours to do the project?
Answer: Each lab takes several minutes to initialize the network setup, and takes several minutes to finish system operations. Be sure to allow ample of time (at least 10 minutes) for the system to save your work before the end of your lab reservation.

 

Q14: How can I utilize the copy-and-paste features in Netlab?
Answer: The configuration of the routers and switches has to be done in CLI (Command Line Interface) mode. When configuring a router/switch using CLI mode, it is suggested that you first write the configuration commands in a .txt or .docx file. You will then copy-and-paste into the router’s CLI. This allows for easy maintenance. For example, the following provides the sample commands for configuring a router or a switch which you will write in a .txt file. You then copy the commands, and paste into Netlab CLI mode. Specifically, open a device, right click the mouse and select paste. This saves you from typing line by line in the Netlab environment. 

config t

hostname Parkville

enable password itisfine       

banner motd #Security is enforced!#

 

 [link: #top] BACK TO TOP

Q15: Why and how to undock a device?
One student wrote “As we bounce between S1, S2,S3 PC-A,B,C to input assignment commands. The switch(s) prompts to hit enter which COMPLETELY removes any command history with a New S1# prompt. There is no way to "Scroll" up through the entire configuration window to see all the commands entered. Any ideas/suggestions?”

Answer from Netlab administrator: “Not sure why any history is being removed. You can undock the individual router/switch/pc. On scrollback, you can use a scroll wheel on a mouse, there just isn't a slider bar in the window yet. I know that is on the short list. But the scroll wheel does work both docked and undocked. Now when you move from docked to undocked or vice versa, history will be lost because it creates a new connection. So if a student liked the old style with different windows, I suggest they start by undocking all the devices they intend to use before starting to type.” Figure 8 shows where the undock option for a device.

Figure 8: Undock a device

 [link: #top] BACK TO TOP
