# Unit 8: Lecture - Miscellaneous Secure Programming Rules

In this very short lecture we will complete our set of secure programming rules, introducing a couple of miscellaneous rules.

The first SPR we will review is related to the environment where a program executes. It indicates:

SPR ENV33-C

Do not call system()

The system function from the stdlib.h C library allows a C/C++ program to invoke and run commands from the computer’s operating system. These commands are not C/C++ commands, but are specific to the operating system hosting the running program. Once the command finish execution, control returns to the C/C++ program. The system function receives a string with a command, and if the operating system understands the command, it may execute it. This function may be useful when the operating system provides commands that simplify certain operations. For example, rather than writing a program that open and inspects the files in a folder, a C/C++ program may use the Windows command “dir” that produces this result, as follows:

 system(“dir”);

This mechanism is safe, unless the parameter string contains unsafe commands. For example, the following set of instructions is an invitation for an attacker to access the system:

char command[100] ;
printf("Enter a command:");
scanf(“%s”,command);
system(command); 

 An attacker may include commands to access the system in any possible way. If the program is run with privileges, the damage may be extensive. That is why this secure programming rule recommends not to use this function. However, using hard coded commands with caution (like “dir”), may also avoid problems with this function.

On the other hand, sensitive information should not be hard-coded in a program. This is the recommendation of the last secure programming rule of this course:

SPR MSC41-C

Never hard code sensitive information

Codes, passwords, personal and company information should not be hard coded directly in a program. Attackers may analyze the contents of the executable file and easily obtain this information. This information should be obtained from an external source, like a user, a file, or a database system and be held in variables during the program’s operation. Once these variables are no longer needed, it is a good practice also to erase them from memory, to prevent attackers from gaining this information by inspecting the computer’s memory after execution. To do so, the program may use the memset function.

The memset function from the string.h C library replaces an area of memory with a character. The syntax is as follows:

memset(void *ptr, int x, size_t n)

where ptr is a pointer to the start of a piece of memory to be filled with

                        x the value to replace every byte in memory, and

                        n is the number of bytes to be filled starting in ptr.

It is important to note that even though the value to be copied (x) is an integer, the function will treated as an unsigned char, so it will replace exactly one character.

As an example, the following code erases a user-provide password from memory after it is used to access some resource:

char password[100] ;
printf("Enter a password:");
scanf(“%s”,password);
   // use password to access a resource 
memset(password,0,sizeof(password));

The memset function call in the example above is replacing every character in the password array with zeroes.

This completes the set of rules covered in this course. The document  [link: https://canvas.park.edu/courses/62124/files/8205449/download?verifier=EvUivlDEcZm47Ulnlk8q1B2Y9cXzyiBwt3IELWle&wrap=1] “Summary of Secure Programming Rules in C/C++” contains the complete list. You should take a look at this document. It will be used in the discussion thread this week.
