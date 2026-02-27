# Unit 5: Digital Logic Project

**Due:** 2022-04-18T04:59:59Z
**Points Possible:** 16.0
**Submission Types:** online_upload

## Instructions

Purpose

The purpose of this exercise is to integrate our understanding of digital circuits and ROM to create a memory reading circuit. 

Project Description

We will build a memory reading circuit to simulate how a block of data is read out of a memory device and displayed on a screen.  The block of data will be a string, which is stored in memory character by character.  We will use a counter to generate memory addresses.  With proper control logic, each character will be read out from the memory device (simulated using a ROM in Logisim) sequentially and displayed on a user terminal (simulated with a TTY, TeleTYpewriter).

Step 1

Pick a string with at least 20 characters (could be more than one sentence). The string must include your first name and last name initial. Add a newline character at the end. The character count includes spaces and punctuations. Include your string and its length in your project report. For example, student John Doe picked a string of length 37 (including the newline character. Uppercase letters are highlighted):

No one knows that John D is a robot.↲

Step 2

Characters are stored in computers as unsigned binary integer following a character coding scheme such as ASCII. When you save a file in a Text only format, each character is saved in its ASCII value.

Translate each character in your string to ASCII in hexadecimal (Remember? Hex is a shorthand notation for binary). Reference an ASCII table showing Hex values, such as  [link: https://www.asciitable.com/] https://www.asciitable.com/.  Be aware that lowercase letters (0x61 ~ 0x7A) have different ASCII values than uppercase letters (0x41 ~ 0x5A). Newline character is the 11th character in the ASCII table with a value of 0x0A. The table below shows the first 8 characters of the example string translated to ASCII. 

Step 3

Each ASCII character will take a one-byte slot in a ROM component in Logisim and each slot needs a unique address. How many bits (n) does the memory address of this ROM component need in order to address each character of your string? Show your calculation. This n will be the [# of] data bits attribute of your counter as well as the address bit width attribute for your ROM.

Step 4

Build the circuit in Logisim. You need those components:

a clock signal.

a Counter (under the Memory folder) to generate memory address automatically. Set its “data bits” attribute to the n value you get in Step 3.

a ROM (under the Memory folder) to store read-only data i.e. your string. Set its “address bit width” attribute to the n value you get in Step 3. Use the default data bit width 8 (i.e. each stored value is 1 byte). Click the “Contents” attribute, which says “(click to edit)” to open a Hex Editor and enter the ASCII of your string in the ROM. When you’re done, click the “Close Window” button to save your edit and close the Hex Editor. See Help menu > User’s Guide > Memory components > Hex editor.

A Bit Selector (under the Plexers folder) to select the lower 7 bits of a byte (8 bits). Use the default “data bits” attribute of 8 but set “Output Bits” to 7. When connecting the component, connect a 0 (use a constant 0 wire) to its Select input pin.

A TTY (under the Input/Output folder), a dumb terminal acting as your “monitor”. TTY is short for TeleTYpewriter. Its input is a 7-bit ASCII code, which should come from the 7-bit output of the Bit Selector. An ASCII code actually only has 7 bits and TTY only works with those 7 bits per character. When we store an ASCII code in memory, an extra leading 0 is added to store it in an 8-bit slot.

Here is the example string in the Hex Editor. Take a screenshot of your Hex Editor when you're done editing and add it to the project document.

The basic connection will be: Q output of the counter (n-bit) --> address input of ROM. The data output of the ROM will be one character (1 byte) read out of the ROM --> the bit selector (input 8 bits, output 7 bits) --> TTY.  Both the counter and the TTY need a clock signal. Use the same clock signal. Your string should be displayed in the TTY character by character. You’re expected to read the Help menu > Library Reference to figure out how each component should be set up and connected. 

 

Use Simulate menu > Ticks Enabled to run your circuit so you don’t have to poke the clock non-stop. To stop the simulation, uncheck Ticks Enabled. To reset your circuit, use Simulate menu > Reset Simulation. If you want the circuit to run faster, use a faster clock through Simulate menu > Tick Frequency. Here is the example string displayed in the TTY during simulation: 

  

There is no credit on documenting testing for this project, but you should always test your circuit thoroughly before adding a new component.

Add your name, Park ID, and date to your circuit using the Text tool. Save your circuit as Unit5_YourLastName.circ.

Step 5.

Project feedback:

a. What’s the hardest part of this project for you? Please explain.

b. How’s your understanding of digital circuits after this project? Please explain. Feel free to comment on other aspects of this project.   

Submission

Submit two files: one circuit file and one project document (a Word/PDF file that includes all other required items).  

You may do your work on paper and scan or take a picture. Insert the pictures into your project document.

When submitting multiple files, you may turn in separate files as listed (preferred) or combine everything into a single .zip archive. Do NOT use any other archive format, as the instructor won’t be able to open them.

Rubric

Step 1. Your string and its length. Must be at least 20 characters long and include your first name, last name initial, and a newline character. 

1 pts

Step 2. Your string in ASCII (hex values)
2 pts

Step 3. The n value (# of address bits) needed for your string. Show your calculation.

1 pts

Step 4. A circuit file containing a working circuit as required.

Your circuit must match your Step 1 - Step 3 work, otherwise zero credit.

11 pts:

1 pts: a screenshot showing your string in the Hex editor of the ROM

10 pts: 2 pts for each of CLK, Counter, ROM, bit selector, TTY. The 2 pts cover all necessary attributes and connection.

Step 5. Project feedback
1 pts

Total: 

16 pts

---

## My Submission

**Score:** 16.0/16.0
**Grade:** 16
**Submitted:** 2022-04-18T02:26:23Z

### Submitted Files

- **Unit5_Bert.circ**
  - Downloaded: `files/Unit5_Bert.circ`
- **Unit5_documentation_bert.docx**
  - Downloaded: `files/Unit5_documentation_bert.docx`

### Instructor Feedback

**[INSTRUCTOR]** (2022-04-20T19:11:52Z):

> Total: 16 pts = 16 - 0 pts. Excellent!

[1 pts. Step 1. Your string and its length]
[2 pts. Step 2. Your string in ASCII (hex values)]
[1 pts. Step 3. The n value (# of address bits) needed for your string]
[11 pts. Step 4. A circuit file containing a working circuit as required] 
+ correct

[1 pts. Step 5. Project feedback]
+ Good job!
