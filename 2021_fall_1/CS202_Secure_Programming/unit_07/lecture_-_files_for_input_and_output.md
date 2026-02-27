# Unit 7: Lecture - Files for Input and Output

Until now we have been providing data to our programs thru the keyboard and obtaining results in the monitor. In this unit we will review how to use files to become either the input or the output in our programs. We will talk about creating, opening, reading, writing, updating and closing files. We will also see two classes of files: text files (or ASCII) and binary files, and we will pinpoint the things that can go wrong handling files and how to prevent them from happening.

As with other units, to highlight the main security points, in this document you will see paragraphs prefaced by the initials SPR. They indicate an important Secure Programming Rule that you must keep in mind when programming. This will be particularly important when a code and a number follows the initials SPR. They are the code and number assigned to this recommendation by the Software Engineering Institute at Carnegie Mellon University, a source of authoritative information on the discipline ( [link: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard] SEI CERT Coding STandard). You will also be directed to more information from the textbook and course material in paragraphs marked as Read more. References to companion C/C++ programs will also be prefaced by: “You may review the attached program(s).”

 

 [link: #fragment-1] File Types

 [link: #fragment-2] File Opening and Closing

 [link: #fragment-3] Text File Reading and Writing

 [link: #fragment-4] Binary File Reading and Writing

 [link: #fragment-5] Additional Secure Programing Rules

File Types

We will review two types of files with C/C++: text files and binary files.

Text files contain characters. Because we are using the ASCII code to represent characters, these files are also known as ASCII files. There are other ways to represent characters that may lead to different kind of text files, but we will not talk about them in this unit. Text files can be opened and reviewed with text processors, and can be displayed in computer’s screens. Because they are written in ASCII code, they are easily understandable by humans inspecting them. They are usually organized in lines separated by next line characters (‘\n’). Most Internet communications are based on this kind of files.

On the other hand, binary files do not store values as characters, but as binary values. For example, an integer number usually takes 32 bits (4 bytes) to be held in RAM. This same pattern of 4 byes would be stored in a binary file as a representation of the number. A binary file cannot be manipulated with text processors or viewed on a screen. If one tries to do any of these activities, the computer will not show anything easy to understand because one would need an interpreter of the binary code onto ASCII code, or something similar. A binary file is more compact, it may contain more information than a text file of the same size, but it is slightly more difficult to handle.

File Opening and Closing

Regardless of file types, all files are to be handled using similar operations, albeit with slightly different commands.

To represent a file in a program we will use the FILE data type. However, rather than using this data type directly we will use a pointer to it. This will be a pointer to a physical file that is stored in secondary memory (hard drives, disks, flash memory, and optical devices). All file operations will use this pointer to perform operations in the file.  The FILE data type is defined in the C header file stdio.h, and it needs to be included in the program to work with files. A pointer to the FILE data type can be declared as follows:

FILE *f;

Like any other variable, the FILE pointer needs to be initialized for use, by assigning it to a specific file with a fopen function. This function opens the file and sets the value of the pointer. The syntax for this function is:

FILE* fopen (char *filename, char *mode) ;

where filename is a string with the name of the file, and preceded by its path if necessary, and  mode is a string indicated the kind of access that is required on the file.

For text files, the mode could be either “r” for read, “w” for write, or “a” for append. In case the file is to be updated, the mode could also be “r+” to be able to read and the write on the same file, “w+” to be able to create the file and be able to read it also, or “a+” to be able to read and append data on the file.

For binary files we have the same modes, but the letter ‘b’ must be added after the first character on the mode. This provides the following options: “rb”, “wb”, “ab”, “rb+”, “wb+” and “ab+”.

Some examples of file opening:

//opening test.txt for reading
FILE fr = fopen(“test.txt”, “r”); 
//opening outfile.txt in the images subfolder for writing
FILE fw = fopen(“images/outfile.txt”, “w”);
//opening append.txt in the D: drive for reading and append
FILE fa = fopen(“D://append.txt”, “a+”);
//opening bin.txt in the parent folder for binary reading and writing
FILE fb = fopen(“../bin.txt”, “rb+”);

If successful, the fopen function returns a pointer to the designated file, but if it fails, it returns a NULL pointer. This situation must be handled before continuing with a program. Something like the following could be appropriate:

f = fopen(filename,"r");
if (f == NULL) {
     // Handle the error
}

 

It is important to emphasize, that opening a file, like any other operation designed for files should only be performed on files. Operating systems may treat certain Input/Output devices as files. These include the screen (known as CON), printers (with names like PRN or LPT followed by a number), network cards (named COM or AUX), Internet addresses, other devices that begin with the characters ‘\\.\’,  or the NUL file (used to discard content that is not needed). However, C/C++ file commands may not be used on these devices. This is prescribed by the following secure programming rule:

SPR FIO32-C

Do not perform operations on devices that are only appropriate for files.

 

 

 

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205053/download?verifier=3EnSX7JHh05xwLteTZLLlQcDmUbZnW7qi5zhU13f&wrap=1] ASPRFIO032.cpp for an example on how to identify devices that should not be treated as C/C++ files.

After a program finishes using a file, it must be closed. This is done with the  fclose function which takes the FILE pointer and attempts to close it. If it is successful, this function returns an integer value of zero, or EOF if it fails. The correct way to close the file pointed by f would be:

if (fclose(f) == EOF) {
     // Handle the error
}

Even if the closing of a file is not successful, the pointer should no longer be used to reference the file again.

Closing files is particularly important on functions that receive the name of a file to be opened and used for a task. The convention is to let the function finish all the activities it has to do and then close all files it opened before return, because the function cannot guarantee the behavior of other programs after it returns. It is also customary to return indications of the success in opening or closing a file. The following code shows a typical use of a file in a function:

int goodUseofFile(const char *filename) {
  FILE *f = fopen(filename, "r");
  if (NULL == f) {  // file was not opened 
    return -1;
  }
  // Performing activities with the file ...
  if (fclose(f) == EOF) {    // Attempt to close the file
    return -2;  
       // If the file could not be closed an error code is reported
  }
  return 0;  
// Return an error code of zero after all operations are concluded,
// including the closing of the file.
}

Notice that the integer values returned by the function may indicate the reason why the call to the function fail. The following secure programming rule highlights the importance of closing files:

SPR FIO46-C

Do not access a closed file.

 

 

Text File Reading and Writing

Once a text file is opened, data can be read or written in three different ways:

 [link: #tab-1] Character by Character

 [link: #tab-2] Line by Line

 [link: #tab-3] Using a Format

Character by Character

The functions to read and write single characters in a file are  fgetc and fputc respectively. They read and write one character at the time, sequentially. Both functions require a pointer to the file they are accessing. The  fputc function also needs the character it is writing. The following will read a character from a file pointed by  fi and print the character  c to the file pointed by  fo:

 char c = fgetc(fi);
 if (c!=EOF) {
      putc(c,fo);
}

fgetc will receive a character from the file is reading and advance to the next position within that file. When it reaches the file’s end, it will retrieve the character EOF (end-of-file), a situation that must be expected, as shown above.  fputc will also receive back the character it just wrote, and will get EOF if there is any problem that prevents writing, however, these situations may or may not be monitored.

Line by Line

If a file is organized in lines, they will end each line with the end of line character (‘\n’). The function fgets uses this fact to read an input file until the ‘\n’ character is read or a limit on the number of characters is reached, whatever comes first. The syntax is as follows:

char* fgets(char *t, int count, FILE * f);

 fgets reads lines of characters from the file pointed by f on a string t. The string t must have enough space to receive up to count characters. The function will read up to count-1 characters from the file and add a null character (‘\0’) to the end. The string t will include any characters read, including the end of line character (‘\n’), if read. The function also returns the string read, or the NULL pointer if nothing is read, leaving string t untouched.

The function fputs is used to write a string onto a file. Every character on the string will be written into the file, up to, and not including the null character (‘\0’) at the end of the string. The size of the writing is only limited by the size of the string. The syntax is as follows:

char* fputs(char *t, FILE * f);

fputs writes the contents of string t onto the file pointed by f. The function returns a non-negative integer value on success, and EOF if it fails.

Using a Format

We can also use the same formats described for scanf and printf functions in their versions for file writing: fscanf and fprintf. The syntax for fscanf is:

int fscanf(FILE *f, char *format,...list_of_addresses ...);

fscanf reads values for variables from the file pointed by f, directly into their memory addresses (listed), using the format in the string format. The function returns the number of expressions being read, and if the number is smaller than the number of placeholders (%) for variables in the format, it is an indication that something went wrong.

Equivalently the function fprintf prints the values of a list of expressions onto a file using a format.  It has the following syntax:

int fprintf(FILE *f, char *format,...list_of_expressions ...);

 fprintf is printing the values of a list of expressions onto the file pointed by f, using the format in the string format. It returns the number of characters printed or a negative integer value if it fails.

Review the Code

You may review the attached programs  [link: https://canvas.park.edu/courses/62124/files/8205422/download?verifier=FEwJPLIRYGAimAwYYBXmurfUzcfVaUUKgksa2hB8&wrap=1] BReadingASCIIFiles.cpp, and [link: https://canvas.park.edu/courses/62124/files/8205425/download?verifier=N5zpEAWTqXkoAdo2PYKYH9dLvEmxc5MOrLvNlsOs&wrap=1]  CWritingASCIIFiles.cpp for examples on the use of this functions. They also require the input files [link: https://canvas.park.edu/courses/62124/files/8205324/download?verifier=CW2D3WLs26uo3dh4nm3idAUh7leVadHW3mmhBaih&wrap=1]  Input1.txt,  [link: https://canvas.park.edu/courses/62124/files/8205433/download?verifier=adgJmsDlH4hv6TpKuIF5OcLlOvWO5TlDMh2SYZqW&wrap=1] Input2.txt and  [link: https://canvas.park.edu/courses/62124/files/8205052/download?verifier=0peTs7WTAplNFoh7vCk3tA8pH6RYMsbdiV0S33G9&wrap=1] Input3.txt.The program BReadingASCIIFiles.cpp contains 3 functions to show how each reading method works. Function  readFileWfgetc reads a file character by character and displays its contents in the screen. Function  readFileWfgets reads a file line by line and it also displays it in the screen. Because the lines read contain the end of line character (‘\n’) they move automatically to the next line when displayed. The file is opened a second time to show a mechanism to eliminate the end of line character (‘\n’) by replacing it with the null character (‘\0’). This replacement is widely recommended when processing of the text does not require line separations, as we will highlight in the following paragraph. Function  readFileWfscanf reads a file in which each line has a previously known format.

As indicated before, the function fgets returns the string that it read if successful, or the NULL pointer if nothing was read. However, there is the possibility that the file contains an empty line, a line in which the only character is the next line character (‘\n’). For these situations, the fgets function will return a string containing only this next line character (‘\n’). If the program is eliminating this characters from the string, this amounts to obtaining an empty line. This situation prompts the issuing of the following secure programming rule:

SPR FIO37

Do not assume that fgets() or fgetws() returns a nonempty string when successful.

We are not concerned in this course with the fgetws function, designed for strings unlike the ones we are studying in this course. However, we presented an earlier method to replace next line characters (‘\n’) with null characters (‘\0’) when using the fgets function. That method will take care of the problems associated with this secure programming rule. The same technique can be used if an error is detected when using the fgets function. The following code is an example to clear the string where the information from fgets is being stored if something fails:

char buf[BUFFER_SIZE];
if (fgets(buf, sizeof(buf), file) == NULL) {
    /* Set error flag and continue */
   *buf = '\0';
}

Doing that will satisfy the prescriptions of the previous secure programming rule, and the following one:

SPR FIO40-C

Reset strings on fgets() or fgetws() failure.

The program BWritingASCIIFiles.cpp contains 3 functions, each reads an input file and produces an output file created with each of the three writing techniques previously described. Function writeFileWfputc creates its output file by converting every character it reads from the input file into upper case. Function writeFileWfputs does something similar, but process both files line by line while function writeFileWfprintf uses formats to read and print.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205428/download?verifier=tVjAL975Px5vEzZXmuHrS3BtmglqCNQNl3vuAWmu&wrap=1] DAppendingASCIIFiles.cpp which shows the use of opening a file for append. It also requires the input file  [link: https://canvas.park.edu/courses/62124/files/8205056/download?verifier=EAvjsA2QbdNe1U2HrE92jN5FSmawLSN9V8myUXBK&wrap=1] Input4.txt. The program opens a file and displays its contents on the screen. The displayed text ends with a questions for the user. The user may respond and her/his answer is appended to the end of the file. This example shows two important ideas. First, opening the file with the “a” mode would not allow to display the file contents.  When opening a file with “a”, a program goes directly to the end of the file for appending. If one needs to read the file and then append, one must open the file in the extended mode “a+”. In second place, notice that the program uses the keywords  stdin and  stderr. Let us talk a bit about these keywords.

C/C++ has designated three files as standard files, accessible thru their pointers: stdin, stdout and stderr. stdin is the pointer to the default file from where programs can receive input. So far, we have been receiving input from our programs from the keyboard. This is the file pointed by  stdin. We can always use the keyboard as an input in all our file commands, if we use the keyword stdin.  This means that the following two commands are equivalent:

scanf(“%s”,buffer);
fscanf(stdin,“%s”,buffer);

 

Something similar happens with stdout. Everything we have been printing until now went to the screen. This is stdout, the pointer to the default output file.  We can obtain the same results from the following commands:

printf(“This is 2 + 3 = %d”, 2+3);
fprintf(stdout, “This is 2 + 3 = %d”, 2+3);

stderr is a pointer to a new file we are introducing here, and it is the file where the program will write any error message that might have happened while running the program. By default, this file is also the screen, but the operating system has the ability to change its destination and print errors in another file, like a reporting log.

Binary File Reading and Writing

Because binary files cannot be easily inspected, programmers must be aware of the structure of their files. Generally, they tend to store similar objects, so that recovering and handling their values is less taxing. A binary file usually contains all integers, or all float values, although more complicated data types, like structures, may also be used. We will limit the discussion on this topic to simpler numeric values that can be stored in an array.

A binary file can be created, by opening it for writing in the “wb” mode. An array of numbers can be written on this file using the fwrite function. This function has the following syntax:

size_t fwrite(const void *anAarray, size_t size, 
              size_t count, FILE *f);

 fwrite function will attempt to write the contents of the array anArray in the file pointed by f. The array may point to any location in memory containing the values and from that point on, the function will take count positions of size bytes to be stored in the file. size_t is the data type that may contain the largest size for any object in C/C++, and it is usually unsigned integer. The function will return the number of values it successfully wrote, and it will be less than count if something went wrong while writing.

The corresponding function fread allows for a binary file opened with the “rb” mode to be read. The syntax for this function is:

 size_t fread(const void *anAarray, size_t size, 
              size_t count, FILE *f);

 The parameters are similar to fwrite. The fread function will attempt to read count*size bytes from the file pointed by f onto a location in memory that begins at anArray. anArray should have enough space to receive the bytes.

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205430/download?verifier=tnmmbGTs2He1vGVuHvdOA65HC3gIQ7dLqDfFQaS1&wrap=1]  EUsingBinaryFiles.cpp which creates a binary file in the WriteBinaryFile function and reads and displays its contents in the ReadBinaryFile function. It also requires the input file Input5.txt. This program also includes the UpdateBinaryFile functions that shows how to access a binary file at random.

In this unit so far, we have been accessing all files in a sequential mode. We begin reading the file from the top and we access every character, every line, or every value from the beginning to the end. In the UpdateBinaryFile function on the latest example we are not accessing the file in this fashion, but we jump to specific locations using the fseek function. This functions allow us to jump to a given position within the file and proceed with operations from that point on.  This is the syntax for the fseek function:

      int fseek(FILE *f, long count, int origin);

fseek function will jump count bytes from the origin in file f. origin could be one of three possible values: SEEK_SET (the beginning of the file), SEEK_CUR (the current position in the file) or SEEK_END (the end of the file).  The function will return zero if successful, any other number otherwise. Accessing files in this fashion is known as random access for files. While random access can be implemented in text files, using it in binary files appears to be more natural, since movement within the file is based on a number of bytes.

The UpdateBinaryFile function on the latest example opens a binary file in “rb+” mode. This allows it to read the binary file from the beginning, but also to update it:

     fb = fopen(fBin,"rb+");

The example will search for the last integer in each row of data, increase its value by 10 and save it again in the same position it was on the file. To do so, it has a loop that positions the file in the last value of each row with fseek:

while ((ok==1) &&
       (fseek(fb,7*sizeof(int),SEEK_CUR) == 0) &&
       (fread(value, sizeof(int), 1, fb) == 1)) {

Because each row in the file has 8 integers and we are always looking for the last one, the fseek function will always be called from the first integer to advance 7 more (7*sizeof(int)). Within the while, and after the fseek move is successful, the loop uses fread to read one and only one integer value inside the array value in memory. This variable value  was declared as an array of one element to be able to use the reading and writing functions that require arrays. The value inside value[0] is increased by ten and then saved to the same place using the fwrite function:

if ((fseek(fb,-1L*sizeof(int),SEEK_CUR)!=0) || 
    (fwrite(value, sizeof(int), 1, fb) != 1)) { 
    ok = 0;
} 

When we read the value to be modified, the position in the file advances to the next integer (the first element in the next row). Because we want to modify the same location where we read the value, we must to go back one integer in the file. This is the reason why before using fwrite we must use fseek to move –1L*sizeof(int) bytes. If either of the functions calls fails, the variable ok will stop the loop and the finish the function call in this program.

Having to call the fseek function after using the fread function and before using the fwrite function is a requirement for the correct use of random access files. This is so important that requires the following secure programming rule:

SPR FIO39-C

Do not alternately input and output from a stream without an intervening flush or positioning call.

This rule indicates that when opening a file for update (reading and writing within the same opening), one must not change from reading to writing or vice versa without using in between a call to a function to reset the position in the file. Not doing that my produce undefined behavior. In particular, when updating, if we are reading a file and we must perform a write on the same file, this must be preceded by calls to fseek, fsetpos or rewind functions, unless we have read the whole file and we arrived to EOF. If on the other hand, we are writing to a file, and we must perform a read operation on the same file, we must call first the fflush, fseek, fsetpos or rewind functions.

We have seen that fseek resets the position in a file. The fflush function clears the buffer used in memory to represent a file and finalizes any writing operation to a file that is still pending. The rewind function moves the current position to the beginning of the file. Both require only the pointer to the file as a parameter. For example:

fflush(f);
rewind(f);

The fsetpos function is coupled to the fgetpos function. The fgetpos function may store the current position in a file when requested. This position is stored in a special fpost_t data type solely used for this purpose. If one has saved such position, the fsetpos function may move the position of the file to that stored location. For example, the following will save the location at the beginning of a file:

fpost_t p;
FILE f = fopen(“file.bin”, “rb”);
if (fgetpos(f,&p) !=0) {  // saving current position in p
    printf(“Error storing position\n”);
}

The program may move about the file, but when it requires to return to its beginning, it can do the following:

 if (fsetpos(f,&p) !=0) { // returning to position p
    printf(“Error returning to position\n”);
}

Programs should not attempt to clone or copy a variable with  fpost_t data type. They should only use it to store and retrieve locations in a file using  fgetpos and  fsetpos, as indicated in the following secure programming rule:

SPR FIO44-C

Only use values for fsetpos() that are returned from fgetpos().

The positions in a file should also not be used to locate or move about into another file.

 

 

Additional Secure Programming Rules

Besides the secure programming rules already mentioned for files, there are a few additional ones that require some attention:

This is a general warning to check that standard error messages from library functions are properly handled. It applies to all functions, but especially to I/O and memory allocation functions. We have seen that these functions return valid values when successful, or a value that indicates that there was some problem when executing the functions. Programmers should always check the values returned and take actions accordingly. Assuming that all operations have performed correctly without checking may lead to undefined behavior. For example, trying to access a file when the fopen function returned a NULL pointer may cause problems. The secure programming rule for this advice is as follows:

 

ERR33-C

Detect and handle standard library errors.

When using formatted input or output (with fscanf, fprintf or similar functions), do not use user provided input as the format without checking it, or mitigating its effect. A user may provide any kind of input for programs. And programs should always validate this input before using it. In the situation we are specifically addressing, formats for input and output may be used for attackers to obtain information. For example, the placeholder %n when printed, rather than formatting a variable, stores the number of characters being printed into that variable. For example:

  printf(“I have printed %n variables”, &i);

The previous sentence would print the string “ I have printed variables” and record the number 15 in the variable i, since the statement printed 15 characters before the %n symbol. This is the kind of statements that can be avoided when we have complete control of the program, but suppose that instead of using the explicit format, the program obtains it from a string parameter named  format and uses it in the print statement, like this:

 printf(format, &i);

An attacker may provide a  format like the one shown above to obtain information. For this reason, the following secure programming rule prescribes the exclusion of user provided formats:

 

SPR FIO30-C

 Exclude user input from format strings.

 

Due to this concern, Microsoft Visual Studio prevents the use of %n when executing programs.

 

Still, when using formatted input or output, use the correct format for a given data type: numeric placeholders (like %d and %f) for numbers, %c for characters, %s for strings, and so on. Using the wrong format may produce undefined behavior. For example, in some environments, using %d to print strings may cause the runtime environment to think that the string is a pointer and may try to read a number from the address being pointed by the string. It is likely that the program may stop if this happens, but it should be prevented by following the given secure programming rule:

SPR FIO47-C

Use valid format strings.

 

When accessing files, they are usually opened first, checking if they actually exist or not. This is what is called the “Time of check”. Later the file is accessed either for reading or writing in what is called the “Time of use”. In an environment where files are shared among multiple users, this process to access files may generate a race with a potential attacker in what is known as the “Time of check - Time of Use” race, or TOCTOU race. An attacker may replace an opened file (after the time of check) with another of his making before the time of use, with ill-fated consequences. Because of this problem, some implementations of C/C++ allow a new mode of operation that includes the letter “x” for exclusive access to the file. The file would be opened as follows and the race condition is avoided:

   FILE *f = fopen(filename,"rx");

The TOCTOU race condition generated the following secure programming rule:

 

SPR FIO45-C

Avoid TOCTOU race conditions while accessing files.

Finally, we should emphasize that when using the pointer to a FILE, even though it is a pointer, its contents should not be de-referenced, but access to the file should be solely thru the pointer. For example, the following sentence tries unsuccessfully to copy the contents of stdout to a FILE data type:

   FILE f = *stdout; // Wrong use of de-referencing 

The sentence above will generate a runtime error. On the other hand, the following is allowed:

   FILE *f = stdout; // Correct copy of a pointer to FILE 

 

The sentence is copying a pointer to the standard output file. Programs should not copy FILE objects, but use FILE pointers. The following secure programming rule summarizes this point:

SPR FIO38-C

Do not copy a FILE object.

 

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205432/download?verifier=20lAtMAKJ3IHGF7SAUEiAEXPNn6easjkybxS212V&wrap=1] FSPRFIO038.cpp that illustrates this point.

 

Read More

Read more about Files in Chapter 7 and Appendix B1.1 thru B1.6 of the textbook.

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
