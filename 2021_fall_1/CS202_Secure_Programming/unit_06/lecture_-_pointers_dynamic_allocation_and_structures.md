# Unit 6: Lecture - Pointers, Dynamic Allocation, and Structures 

In this unit we will describe and use a concept we have seen previously, but that we will review in detail just now: pointers. We have already seen their use with arrays and functions. Pointers are also used extensively in C/C++ for other applications, in particular, to allocate memory and to handle all sort of data structures. These would be the topics of this unit.

As with other units, to highlight the main security points, in this document you will see paragraphs prefaced by the initials SPR. They indicate an important Secure Programming Rule that you must keep in mind when programming. This will be particularly important when a code and a number follows the initials SPR. They are the code and number assigned to this recommendation by the Software Engineering Institute at Carnegie Mellon University, a source of authoritative information on the discipline ( [link: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard] SEI CERT Coding STandard). You will also be directed to more information from the textbook and course material in paragraphs marked as Read more. References to companion C/C++ programs will also be prefaced by: “

You may review the attached program(s).”

 

 [link: #fragment-1] Pointers

 [link: #fragment-2] Pointers and Functions

 [link: #fragment-3] Pointers and Arrays: Pointer Arithmetic

 [link: #fragment-4] Dynamic Allocation

 [link: #fragment-5] Using Dynamic Allocation

 [link: #fragment-6] Structures

 [link: #fragment-7] Additional Secure Programming Rules

Pointers

Pointers are variables that hold addresses of memory as their values. So far we have had variables that hold numbers and characters, so this is a new kind of variable that holds the address of a piece of RAM in the computer.

When we bought RAM we usually bought it by its size. Depending on the era when we bought it, it would have been in kilobytes, in megabytes, or in gigabytes. Whichever the size it was, each of these bytes had a consecutive number when installed in the computer. This number goes from 0 to the maximum size we bought. This number is the memory address for a byte. Values for variables are stored on those bytes. For example, let us say that the number 123 is stored in a char variable named c. The following shows the command used and the effect it may cause in memory:

char c = 123;  

The variable c could be anywhere in RAM. For the purpose of this explanation, let us assume that it landed in the byte numbered 5634. We will use a hash symbol to indicate that the number 5634 refers to a memory address, so variable c is located in address #5634 in RAM. This memory address can itself be stored in a pointer. To do so, we will use a variable that is a pointer to a character. The following shows a C/C++ command that creates this pointer and takes the address of variable c as its value:

char *pC = &c;  

Variable pC is declared as a pointer to char. The asterisk (*) before its name in the declaration indicates that pC is a pointer. Its value is the address of the char variable p, obtained using the ampersand operator. An ampersand (&) before any variable name produces its memory address. We actually do not need to know that absolute value of the address in memory. We only need to be able to hold its value in a pointer.

The last diagram above showed a hypothetical creation of pointer pC in memory. The size of a pointer in memory depends of the compiler’s implementation, but in most of them it usually takes 4 bytes per pointer. The diagram assumes that the content of the pointer, the address #5634, is stored in RAM from address #7646 to address #7649 (4 bytes altogether).Pointers take their name from the fact that they point to the location where a variable is to be found. They are pointing to the other variable, as the red line in the diagram shows: variable pC is pointing to variable c.

Let us define the syntax to create a pointer in C/C++ more precisely. We can create a pointer to a data type by adding an asterisk before the name of the variable declared as pointer:

dataType *variableName;

The type of the variable is not dataType, but pointer to dataType.  This means that variableName will hold an address of memory where a value of that kind of data type will reside. The data type matters, because, even though all pointers have the same size and they all contain memory addresses, the compiler treats them differently. A pointer to char is not the same as a pointer to int, because the compiler knows that if the variable being pointed at is a char, it only uses one byte of storage. On the other hand, the compiler also knows that an int uses 4 bytes of memory, so a pointer to int is only pointing at the first of the 4 bytes that make up the integer.

As with other variables, we may declare more than one pointer with one command. For example, the following command declares three different pointers to int variables:

int *p, *q, *r;

One could also declare variables and pointers to variables of the same kind in the same line as follows:

int *p, s*, *q, *r;

The command above declares the integer variables s and t and the pointers to integer variables p, q, and r. Each pointer has the asterisk next to its name to indicate they are declared as pointers. Specifically, the asterisk next to the variable p means that p is declared as a pointer to an integer, in contrast to variable s that is only an integer.

Like any other variable, pointers must be initialized before they are used in a program. They could be initialized with the address of any compatible variable, like we saw before:

car *pC = &c;

An ampersand (&) next to a variable means “the address of that variable”.

Alternatively, pointers may also be initialized with NULL. This is a constant defined by C/C++ that indicates that the pointer has no assigned value:

car *pC = NULL;

The value of the NULL is usually zero, but it is compiler dependent, so it is best to use the constant name when comparing the value of any pointer, as follows:

if(pC == NULL) {// checking if the pointer is NULL}

Or

(if(pC !=NULL) {//checking if the pointer is not NULL}

 

If a pointer was initialized and it is pointing to a memory address, we can obtain the contents of that variable with the de-referencing symbol (*). This is an asterisk next to a pointer’s name. For example, if we want to print the value of the char variable c, as defined above, and the variable pC is a pointer to this variable, we can do either of the following:

cprintf("The value of c is %d",c);
cprintf("The value of c is %d",*pC);

The first printf uses the name of the variable c, while the second one uses a de-referencing (*) of the pointer pC. Both statements do the same thing, and for all purposes, they are completely interchangeable.

Do not confuse the asterisk used in de-referencing with the asterisk used at pointer declarations. In declarations, asterisks are used to indicate which variables are pointers. Everywhere else, the asterisk next to a pointer is a de-referencing symbol and it means “the contents of the memory pointed by”. In the printf above, *pC means “the contents of the memory pointed by pC”.

De-referenced pointers may be used in place of a variable anywhere within the variable’s scope. As an example, the following piece of code calculates the hypotenuse (in variable c) of a right angled triangle with sides a and b. Pointers to each of these three variables replace them in calculations throughout the program.

float a=4.0f, b=3.0f, c;
float *pA, *pB, *pC;
pA = &a;
pB = &b;
pC = &c;
*pC = sqrt((*pA)*(*pA) + (*pB)*(*pB));
printf( “The hypotenuse is: %f\n”,c);

Parentheses around the de-referenced variables were used to avoid confusion with any other operation (in particular the multiplication). This is a good practice when dealing with pointers.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205306/download?verifier=lBLI3KGDL91JzCzfJuuV42FvM0zgJGh8w6eHvSw2&wrap=1] AHypotenuse.cpp for a more extensive development of the previous example.

De-referencing should be used only if the pointer contains a proper memory address. In particular NULL pointers should not be de-referenced. It produces an undefined behavior. Many implementations may stop a program running when it tries to de-reference a null pointer, but attackers may use this situation to gain access to memory locations. Before de-referencing a pointer obtained from an external source, programmers should always check if that pointer is not NULL. This situation is likely to occur when a pointer is received as a parameter for a function. The function should review if the parameter is not NULL before any use. Also, the output of functions that return pointers should be checked before they are used. C/C++ functions for dynamic allocation of memory may return such pointers (like malloc that we will study later in this unit). These recommendations constitute our first secure programming rule in this unit:

SPR EXP34-C

Do not de-reference null pointers.

Variables should also not be accessed using pointers of incompatible types. The following example is trying incorrectly to access a double variable to increase its value using a pointer to an integer variable. This will produce an undefined behavior:

double a = 5.0;
int *pA = (int *) &a;
(*pA)++;

This practice is admonished by the following secure programming rule:

SPR EXP39-C

Do not access a variable through a pointer of an incompatible type.

Like any other variable, pointers may also be type casted. Since all pointers have the same size, they could actually be type casted to any other type of pointer. However, this practice should be carefully planned before it is implemented. Programmers must be aware that type casting of pointers may produce differences in interpretation when de-referencing them. For example, a pointer to char may be type casted as a pointer to int, but if the pointer is de-referenced, as a pointer of char it will only consider the first byte to be part of the character, while a pointer to int will assume that the char location together with the next 3 bytes are part of the integer value and may access memory outside the variable’s boundaries. This problem takes us to our next secure programming rule:

SPR EXP36-C

Do not cast pointers into more strictly aligned pointer types.

An int variable has more restrictions than a char variable. A char variable only uses one byte for representation, while the int variable uses four bytes organized from most significant to least significant bits. Therefore, casting a pointer to char onto a pointer to int violates the secure programming rule. A similar problem may occur if a pointer to int is casted as a pointer to float.

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205409/download?verifier=sYLs4Ch6rSEicskrC2iTmdlJHaqWatunKMcYeOGo&wrap=1] BCastingPointers.cpp in which it is shown that the improper casting of pointers leads to erroneous calculations.

Even though type casting of pointers may produce wrong results, programs still use them to pass pointers between functions in a generic manner. For example, some of C/C++ functions that return pointers to dynamically allocated memory may return pointers to void (void *). These are created as generic pointers that need to be casted onto the appropriate data type by the program receiving the memory. This requires a previous knowledge of the final data type for casting, but this may not be a problem as we will see when dealing with dynamic allocation.

Pointers and Functions

We previously saw in units 4 and 5 that pointers can be used as parameters to functions. We used them to represent strings and arrays in the parameter list of a function. They may also be used for any other variable, when the programmer wants to pass the variable by reference, rather than by value.

We should remember that parameters passed to functions in C/C++ are passed by value. This means that the formal argument in the calling function is copied to the formal argument in the called function. In the following example, a copy of the variables x and y is passed to the variables a and b in the badSwap function:

void badSwap (int a, int b) {
     int t ;
     t = a ;   a = b ;   b = t ;
}
int main() {
     int x = 3, y = 5 ;
     badSwap( x, y ) ;

}

The badSwap function is swapping the contents of variables a and b. While this action is successful inside badSwap, the values it is swapping are only of its local variables. These are just copies of the variables x and y in the main function. These original variables in main do not get affected at all. On the other hand, the following function, goodSwap uses the pointers to variables x and y. These pointers act as a reference to the original variables, therefore any change made to these variables inside goodSwap is immediately reflected on the variables in main:

void goodSwap (int *a, int *b) {
     int t ;
     t = *a ;  *a = *b ; *b = t ;
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205310/download?verifier=cJkxViPrmvO8IfA0nTahAId0l5SEZrnaRL52h3Ip&wrap=1] CSwapping.cpp which shows these swapping functions in action.

Pointers and Arrays: Pointer Arithmetic

So far, when using pointers to represent arrays we have always made the pointer obtain the address of the first element of the array. In fact, pointers to arrays may also reference other elements of an array, and we can use this fact to navigate through the array using the pointer. For example, let us define the following array and pointer:

int A[] = {55, 45, 35, 25, 15};
int *pA = &A[0];

The pointer pA is pointing to the beginning of the array A. We can reference the third element of array A if we add 2 to pA. The following line would print the third element of array A using this feature:

printf("A[2] = %d\n",*(pA+2));

Notice that the number 2 is added to the pointer itself. After addition, the pointer is de-referenced and produces the value 35 of the third element of A when printed. We can also create permanent pointers to other elements of the array using a similar operation:

int *qA = pA + 4;           

The pointer qA is pointing to the last element of the array. Using this pointer, we may also print the third element of the array like this:

printf("A[2] = %d\n",*(qA-2));

The operations we just performed on pointers, addition and subtraction, have a special meaning that applies only to pointers.  We can add or subtract integer values to pointers. Compilers interpret these operations as follows: obtain a memory address by taking the number being added or subtracted as the number of displacements from the current location inside the pointer. The result of the operation is therefore another memory address based on a displacement from the original address. The number added or subtracted is a relative number, because it will mean different distances depending on the pointer being used. If the pointer is a pointer to char, the displacement will be in char sizes (usually 1 byte). If the pointer is a pointer to int, the displacement will be in int sizes (usually 4 bytes). There are no other operations like that. We cannot multiply or divide pointers.  Addition and subtraction to pointers is what is known as pointer arithmetic.

This ability to obtain other memory locations by displacement can be used to rewrite loops on arrays. The following example shows a traditional for-loop that prints the elements of the previously defined array A:

for (int i=0;i<5;i++) {
     printf(“A[%d]=%d\n”, i, A[i]);
}

The same effect can be obtained with the following loop:

for (int i=0,*p=&A[0];i<5;i++,p=p+1){
     printf(“A[%d]=%d\n”,i,*p);
}

Because the end of the array can only be detected with the counter i, the previous code does not seem to be an improvement, but if we had a string, we will only need the pointer to navigate it. For example, the following code will print the characters that make string s up until the null character is found:

char s[30] = “Hello and Bye!”;
char *qS = &s[0];
for (char *p=qS;*p!=‘\0’;p=p+1){
     printf(“%c\n”,*p);
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205412/download?verifier=ZWxuB5sgyOTfyCBIv22MIETNUHjfAFDvQ3BH1toh&wrap=1] DPointerArithmetic.cpp which shows these traversals of arrays using pointers.

Pointer arithmetic should only be used on arrays. We are adding and subtracting displacements on arrays based on our knowledge that the elements of an array are all stored contiguously and in order in memory, but we cannot assume anything about the relative position of other variables in memory. Suppose a program declares the following variables:

int a[SIZE]= {1, 2, 3};
int i = 10;

We cannot assume that the variable i is located right after array a in memory. The operating system and the compiler have complete control of memory and they may have it organized in unexpected ways, for operations and optimization.

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205061/download?verifier=JtxrOL66DVk1LLibPnv7FF6PcanLy5XXVs2CcMaP&wrap=1]  EProblemsWithPointersToDifferentObjects.cpp which tries to calculate the size of an array assuming that the variable declared afterwards is located in memory just after the array.

The following secure programming rule summarizes these warnings about using pointer arithmetic on non-arrays:

SPR ARR37-C

Do not add or subtract an integer to a pointer to a non-array object.

 

 

Pointers can also be compared, as long as they refer to the same array. The following piece of code shows how this comparison is possible. It searches the locations of the last characters ‘X’ and ‘Y’ in a string a with pointers, and then the last sentences compare them to know which appears earlier:

char a[] = "aaaaXaaaYaaaa";
char b[] = "bbYbbbbbbbXbb";
char *pA=&a[0], *pB=&b[0], *pXa=NULL, *pYa=NULL;
for (char *p=pA; *p!='\0'; p=p+1) {
      if (*p == 'X') {pXa = p;}
      else if (*p == 'Y') {pYa = p;}
}
if (pXa==NULL || pYa==NULL) {
     printf("Either X or Y where not found in \n[%s}\n",a);}
else if (pYa < pXa) {
     printf ("Last letter Y found before last letter X\n");}
else{printf ("Last letter X found before last letter Y\n");}

The comparison is possible because both pXa and pYa pointers refer to the same array a. On the other hand, the following comparison will produce undefined results:

if (pA < pB){
      printf("String a stored before string b.\n");
}else {
      printf("String b stored before string a.\n");
}

Once again, we shouldn’t cannot compare these pointers because their location in memory with respect each is other is uncertain. The following secure programming rule reinforces this idea:

 

SPR ARR36-C

Do not subtract or compare two pointers that do not refer to the same array.

 

 

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205413/download?verifier=YbR4WkNRH57FFhAwciTJnxuHdudjgo2voFW2GUHq&wrap=1]  FPointerComparison.cpp which shows the correct use of pointers for comparison and a case where the comparison produces unexpected results because of the violation of the previous secure programming rule.

A final point regarding pointer arithmetic is to emphasize that the compiler will take the number that is added or subtracted at face value. The compiler will not care how the number is obtained or which are the units in which it stands for. It will use that number literally as an indication of the number of displacements from the pointer location. The following code presents an observed problem that happened when this information was ignored. This program tries to create an array and fill it with numbers using a loop. This loop is supposed to end when all elements of the array are initialized:

01: int array[5];
02: int *pA = array;
03: int count = 0;
04: while (pA < (array + sizeof(array))) {
05:   *pA = count;
06:    pA++;
07:    count += 1;
08: }  

The loop will begin with pA pointing to the first element of the array and it will move to the next element of the array in line 06, at every loop step. Line 04 is supposed to control that pa does not exceed the boundaries of the array, but the right side of the conditional expression in line 04 has a problem. The address to the right should refer to one element beyond the array, so that pA will not exceed that location. If pA is pointing at memory address #100, the memory address after the array should be #120, because the array has 5 integer elements, each of size 4 bytes (5x4bytes=20bytes).  The operator sizeof produces the total number of bytes on the array, 20. But when adding it to the array (that stands as a pointer to itself, a pointer to int), the compiler does not consider that 20 is a number of bytes, but it considers it as a number of displacements, so rather than pointing to the address #120 is pointing to the address #180, because 20 displacements of integer size are equivalent to 80 bytes (20 displacements x 4 bytes per integer).

The correct way to handle this loop is to provide the number of elements the array has as the number of displacements. This can be obtained from the array itself as we saw in Unit 4:

04: while (pA < (array + (sizeof(array)/size(array[0])))) {

This problem is common enough that the following secure programming rule deals with this precise issue:

SPR ARR39-C

Do not add or subtract a scaled integer to a pointer.

 

 

The term scaled integer refers to the fact that the number to be added or subtracted to the pointer should not be resized by the units used on a problem (having the integer scaled), but that they should reflect the number of true displacements required on the array. 

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205047/download?verifier=TQfSgQrhCN2AjB9I2kDv6qCCtTRFHnYgqeSKZqMW&wrap=1]  GAddingScaledInteger.cpp which shows this example with the incorrect use of the scaled integer being commented out and replaced by the corrected line of code.

Dynamic Allocation

Now that we understand the use of pointers, we can use them to access a very powerful feature in C/C++, the dynamic allocation of memory. Until now we have delegated to the operating system and the compiler the handling of memory for our programs, however, it is possible to have greater control on this process with some functions from the C header file stdlib.h. These functions are malloc, calloc, free, and realloc. We will now describe each one of them in detail.

 [link: #tab-1] malloc

 [link: #tab-2] calloc

 [link: #tab-3] free

 [link: #tab-4] realloc

malloc

With this function, a programmer can request to the operating system a portion of memory with a size of her/his choosing. The syntax for this function is:

void* malloc(size+t size)

The parameter size is the number of bytes requested from memory. Its data type, size_t, is unsigned integer. The maximum number that can be represented with this number is also the largest size in bytes that any object created in C/C++ may have. By using this data type, the compiler assures that the memory being requested does not exceeds this limit. malloc will search for a free contiguous piece of memory that can satisfy this request. If it finds it, it grabs it for the program who called it, and It will return a pointer to the first location of the memory. Because malloc  does not know how this memory is going to be used, it returns a pointer to void that must be type casted by the programmer, according to the intended use. If malloc  cannot find the requested memory size, it returns NULL. For example, the following piece of code uses malloc to create and initialize an integer variable:

int *pi = (int *) malloc(sizeof(int));
if (pi!=NULL) { *pi = 23; }

sizeof(int) provides the number of bytes needed for an integer variable in the given implementation. If malloc can find free memory of this size it will return a pointer to it that will be returned as a pointer to void (void *). To be able to use it properly, this pointer is then type casted to become a pointer to integer (int *). Before being used, programmers must check that the pointer received is not NULL. This indicates that the allocation of memory was successful, at which point, the programmer is free to use the memory at will. The programmer must always initialize the contents of the memory received, since malloc does not do any initialization.

malloc may be used to generate arrays. For example, the following creates and array of 17 float variables:

float *pd = (float *) malloc(17 * sizeof(float));
       if (pd!=NULL) { 
for(int i=0; i<17; i++) { *(pd+i) = (float) i ; }
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205414/download?verifier=ob3bfLO3O3BRaqSigNkmNWoSWOOfBnI7DXfqdAVL&wrap=1] HUsingMalloc.cpp which shows dynamically allocated arrays created with malloc.

calloc

calloc, like malloc, also allocates memory, but returns it filled with zeros. It also takes two parameters, instead of one. Its syntax is as follows:

void* calloc(size_t num, size_t size)

The parameters request a number (num) of contiguous pieces of memory with size bytes each. Both parameters are unsigned integers and the function also returns a pointer to void if successful, NULL if not. The following piece of code shows the same integer and the array of floats created above with malloc, this time created by calloc:

int *pi = (int *) calloc(1, sizeof(int));
       if (pi!=NULL) { *pi = 23; }

float *pd = (float *) calloc(17,  sizeof(float));
if (pd!=NULL) { 
       for(int i=0; i<17; i++) { *(pd+i) = (float) i ; }
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205416/download?verifier=jf6XHjvaiEtydpqWPb3oeiPgPt3z4Rx7mH2iodzY&wrap=1] IUsingCalloc.cpp which shows dynamically allocated arrays created with calloc.

 

free

This function releases the memory that was previously allocated with malloc,calloc or realloc . Its syntax is simple, it takes a pointer to the previously allocated memory and returns nothing:

void free(void * ptr)

It is the duty of the programmer to deallocate all dynamically allocated memory with this command, once it is no longer needed. Not doing so may compromise the optimal management of memory by the operating system. However, only memory that was obtained with malloc,calloc or realloc can be released with free. Trying to free other kind of memory produces undefined results. Once dynamically allocated memory is freed, a program may not reference it again. Not even to call the function free again on that memory. All these guidelines are prescribed by the following secure programming rules:

SPR MEM31-C

Free dynamically allocated memory when no longer needed.

 

SPR MEM34-C

Only free memory allocated dynamically.

 

SPR MEM34-C

Only free memory allocated dynamically.

 

The previously mentioned programs  [link: https://canvas.park.edu/courses/62124/files/8205414/download?verifier=ob3bfLO3O3BRaqSigNkmNWoSWOOfBnI7DXfqdAVL&wrap=1] HUsingMalloc.cpp and [link: https://canvas.park.edu/courses/62124/files/8205416/download?verifier=jf6XHjvaiEtydpqWPb3oeiPgPt3z4Rx7mH2iodzY&wrap=1]  IUsingCalloc.cpp show the proper use of free to release dynamically allocated memory.

realloc

This function reallocates a previously allocated piece of memory. This piece of memory may have originally been obtained from a call to malloc,calloc or realloc, and be currently active (not released with free). Its pointer must then be used as a parameter to realloc, together with a required new size. Its syntax is as follows:

void* realloc(void * ptr, size_t newSize)

To satisfy the request, realloc may expand the area previously allocated, or search for a suitable new area. In either case, the previous contents of memory will be kept, or copied, up to the smallest of the old and new sizes. If the new size is larger than the old one, the contents of the expanded section are undefined and they should be initialized. Like calloc and malloc, if realloc is successful, it will return a pointer to the first address of the new area in memory and it will free the older allocation if necessary. On the other hand, if the call to reallocate fails, the function will return NULL, the old memory allocation will remain untouched and the programmer still need to free it, when it is no longer needed. The following example shows the size of an array created with calloc and then increased in size with realloc:

float *pd = (float *) calloc(17,  sizeof(float));
float *pr  = NULL;
if (pd!=NULL) { 
     for(int i=0;i<17;i++) {*(pd+i)=(float) i; }
     pr = (float *) realloc(pd, 30*sizeof(int));
     if (pr != NULL) {
           for(int i=17;i<30;i++) {*(pr+i)=(float) i; }
     }
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205045/download?verifier=n6iXvN3a2YIAz9XdizKZwX7n38xnQFyTf0N2PMMR&wrap=1] JUsingRealloc.cpp which shows how the size of an array can be reduced or expanded using realloc. Notice the management of pointers to release memory in case the calls to realloc fail, and the use of pointers of pointers to be able to reallocate memory inside a function.

 

Using Dynamic Allocation

In Unit 5 we observed the difficulties of creating an array inside a function for export. An array defined inside a function is considered a local variable and cannot be easily shared with other functions. The alternative is to use dynamic allocation to create the array and to pass a reference to this array (a pointer) to whomever needs to access it. We will review two alternative approaches to do so.

In the first approach, the function receives a pointer to a pointer as a parameter. The function creates the array using dynamic allocation, and a reference to the created array is stored into the pointer to a pointer for return. A program calling this function will receive a reference to the array that can be used outside the function. A second approach would be having the function to return a pointer to the dynamically allocated array as the function output. In both cases, the functions may also receive an integer with the requested size for the array.

For example, suppose that a program wants to use various arrays of integers, but rather than create the arrays itself, it wants to have a function that creates an array of a given size when requested, and call it many times.  Under the first approach, a function call may be organized as follows:

int *pA = NULL; // pointer to hold the array
int n = 10;
// call to createArray1 function passing a pointer to a
// pointer to be filled and the requested array size n
if (createArray1(&pA,n) == 0) {
       //use the array of size n pointed by pA
} 

Notice that we do not pass the pointer to int, pA, but its address  a pointer to a pointer. Whatever variable we pass to a function, it will be passed by value, and the changes made to the variable inside the function will not remain when the functions returns. However, if we pass the address of a variable, it is the address that is passed by value, and the address can be used as a reference to make permanent changes to the referenced variable. Therefore, by passing the address to a pointer (a pointer to a pointer) we can modify the pointer permanently.

The following code shows the function createArray1 that creates and return in a parameter the reference to an array of int of size n:

int createArray1 (int **a, int size) {
     if ((a!=NULL)&&(size>0)) {
          *a = (int *) calloc(size,sizeof(int));
          if (*a == NULL) {
              printf("Array could not be created.\n");
              return -1;
          }
             return 0;
          }
     else {
            printf("Array cannot be created. Null values received.\n");
              return -2;
          }
}

The first parameter in the function is a pointer to a pointer to an integer, a. The second parameter is the requested size for the array, size.The function checks that the parameters have proper values: the pointer is not NULL, indicating that it refers to a possible place in memory, and the requested size of the array to be created is positive. Once parameters are validated, the function uses calloc to create a zero-initialized array of size integers. Notice that the reference returned from calloc is stored in the address that is de-referenced from the pointer to pointer to int, in other words, it is stored in the pointer to int. This is the pointer that can be used beyond this function. If the dynamically allocated array is created correctly, the function return a value of 0, indicating that the operation was successful, if the parameters are incorrect, or calloc could not create the array, values other than zero are returned to indicate that there was a problem.

The second approach can be coded as the following createArray2 function:

int* createArray2 (int size) {
     int *a;
     if (size>0) {
          a = (int *) calloc(size,sizeof(int));
          if (a == NULL) {
              printf("Array could not be created.\n");
              return NULL;
          }
          return a;
          }
     else {
             printf("Array cannot be created. Null values received.\n");
               return NULL;
           }
}

This time, only the required array’s size is passed as parameter. If the size is bigger than zero, the function attempts to create the zero-initialized dynamic array with calloc. If the creation is successful, the function returns a pointer to the first integer in the array, NULL otherwise. The created array can be referenced outside the function, because they were created dynamically. Calling this method can be done as follows:

int *pB = NULL; // pointer to hold the array
int n = 10;
// call to createArray2 function passing
// the requested array size n
pB = createArray2(n); // pointer to hold the array
if (pB != NULL) {
      //use the array of size n pointed by pB
} 

After the array is no longer needed, its memory must be freed. The programmer must be especially careful to perform this task, since the function that created the array is no longer in control. Both, pA and pB can be released with a call to the free function:

free(pA);
free(pB);

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205065/download?verifier=oZvoD6Hqg4r6EXfiWjJAXX64QnCtf9OtSWt46OJI&wrap=1] KCreatingArrayInFunction.cpp in which both strategies described above to create arrays in functions for export are used.

In Unit 4 we also studied bi-dimensional arrays, and we created arrays of strings. Each string had the same maximum size. With dynamic allocation we now can create arrays of strings in which each element has the right size for the characters it holds. We can do this by creating an array of pointers to char. For example, the following array strings will hold 5 strings:

 char* strings[5];

Each element of the array strings may be created with a dynamic allocation function and filled to size. The following would allocate memory and store data in the first element of the array, the other elements can be filled in the same manner:

char word[]=“Good morning!”;
strings[0]=(char *) malloc((strlen(word)+1)*sizeof(char));
memcpy_s(strings[0],strlen(word)+1,word, strlen(word)+1);

Review the Code

You may review the attached program [link: https://canvas.park.edu/courses/62124/files/8205419/download?verifier=WKz04LJU6idBEXISDUKUFsczaN3fQ5lmdp308kkp&wrap=1]  LUsingMallocWArrayOfStrings.cpp in which the same approach is used to fill another bi-dimensional array, using malloc to size each string exactly.

 

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205048/download?verifier=QqvOjz63hJ77cxPe0Ag2ze8v94wyhgB6QSs6WcBX&wrap=1] MUsingCallocWArrayOfStrings.cpp too. This program shows a more complex exercise in which both, the size of the array that holds the string pointers, as well as the individual string elements of the bi-dimensional array are determined when the program is running, from user input. This array is created as pointer to pointers, because it will hold pointers to characters, but it is itself created as a pointer with calloc.

 

Structures

C/C++ also allows the construction of composite data types known as structures. A structure is a list of variables, each with its own independent data type, that are lumped together with a name. The following is the syntax for declaring a structure:

struct strucName { list_of_variable_declarations } ;

where strucName is the given name for the structure, and

list_of_variable_declarations is a list of declarations for variables that are going to be included in the structure. Each variable declaration must include a data type, name, and semicolon (if needed, to separate it from other variables). No initialization of these variables is allowed at this stage. The order of the declarations will matter, as we will shortly see.

The following example declares a structure that contains data for a box:

struct Box {
 float length; 
 float width;
 float height;
}

With this declaration we can create variables of this type of structure, like the following two boxes which are also initialized:

struct Box boxA = {3.0f, 4.0f, 5.0f};
struct Box boxB;
boxB.length=8.0f; boxB.width=7.0f; boxB.height=2.0f; 

 As it can be seen in the example, we can initialize the variables inside the structure using curly brackets, as we have done for arrays. The values will be assigned in the order in which variables were declared. We can further provide values for variables in the structure, if we identify then by preceding their name with the structure name and a dot. This is known as the “dot” notation.

Because structures require the use of the struct keyword when declaring them, it is customary to create an alias for them. In C/C++ aliases for data types can be created with the typedef command. For example, the following will create aliases for the double data type, that will be also known as Real and the Box structure previously defined, that will be known as Record, and use them:

typedef double Real;
typedef struct Box Record;
Real x = 1.4142;
Record boxC = { 5.0f, 6.0f, 7.0f };
Record *pb = &boxC;

The last sentence above creates a pointer to a structure. With such pointer, there is an alternative way to reference the variables inside a structure. Rather than using the pointer notation, we use the “arrow” notation as follows:

pb->length = 10.0f; // this is equivalent to boxC.length = 10.0f;
pb->width  = 12.0f; // this is equivalent to boxC.width  = 12.0f;
pb->height = 14.0f; // this is equivalent to boxC.height = 14.0f;

Notice that to use the “dot” notation we need the name of the structure, but if we use the “arrow” notation, we need a pointer to the structure.

We can finally tie the topic of structures with dynamic allocation by creating dynamic arrays of structures. The following summary code defines and creates such array of three boxes:

struct Box {
     float length;
     float width;
     float height;
}
typedef struct Box Record;
Record *pb = (Record *) calloc(3, sizeof(Record));
if (pb != NULL) {
     for (int i = 0; i < 3; i++) {
          (p+i)->length = 2*i; // Using “arrow” notation
          (p+i)->widtth = 3*i;
          (*(p+i)).height = 4*i; // Using “dot” notation
     }
}

Review the Code

You may review the attached program  [link: https://canvas.park.edu/courses/62124/files/8205049/download?verifier=snVrAT8suBlxPD0igJfcZKP6JUHbep8gE7gdVDrw&wrap=1] NUsingCallocWStructures.cpp,which shows another example of calloc being used to create a dynamically allocated array of structures. In this example it is also shown the need to submit a pointer to the pointer to the structure to be able to change the place in memory where a dynamically structure resides, as previously described.

A particular kind of structure is one that contain a flexible array member. This is a structure that contains an array which does not have a specific size at declaration, but is left to be sized when it is used. This kind of structure is supported as long as the following conditions are respected:

There is only one flexible array member in the structure and it is declared at the end of the structure with no size (empty square brackets).

The flexible array member is not alone in the structure, but there are other variables declared before this array.

A structure containing a flexible array member cannot be part of an array of structures, nor be a part of another structure.

Because of discrepancies among earlier compilers on these conditions, the following secure programming rule encourages programmers to abide by their requirements:

SPR DCL38-C

Use the correct syntax when declaring a flexible array member.

An example of a correct structure with a flexible array member will be:

struct Student {
     int IDnumber;
     char name[20];
     float grades[];
}

The array grades would be the flexible array member in this structure. Variables of these type of structures containing flexible array members should be created using dynamic allocation as prescribed by the following secure programming rule:

SPR MEM33-C

Allocate and copy structures containing a flexible array member dynamically.

Therefore, if we assume that a student has 3 grades, a variable with the struct Student data type can be created as follows:

struct Student *pS = 
    (struct Student *) malloc(sizeof(struct Student)+
                               3 * sizeof(float));

Notice that the operator sizeof calculates the size of the structure without considering the size of the flexible array member. To this, the appropriate size for the flexible array member of 3 float grades must be added when allocating memory. This structure cannot be used as part of an array or other structures.

If the array grades is given a size at declaration, it will no longer be flexible, but will be just an array like the array name declared also in the example. No allocations for extra elements could then be attempted, and accessing those extra elements would produce undefined behavior.

Additional Secure Programming Rules

Besides the secure programming rules already discussed in the previous sections, there are some additional ones that deserved attention:

Be sure to provide correct parameters to the functions that allocate memory, so that the objects being stored in that memory have the right size. This is basically a reminder to check the parameters, since it is very common to make a mistake and provide incorrect sizes, given the somewhat contrived syntax for these functions. The most typical error includes the request of memory of the size of a pointer, rather that the real size of the data to be pointed. For example, the following line mistakenly allocates memory of the size of 10 pointers, rather than the size of 10 structures:

struct Point { float x; float y; float z; }
typedef struct Point Position;
Position *p = (Position *) malloc(10*sizeof(Position *));                                              

To obtain the correct size for the structure the last sentence should be changed to:

Position *p = (Position *) malloc(10*sizeof(Position));

Mistakes like this may go unnoticed, especially if the sizes are correct, despite of the fact that incorrect parameters were used. However, failure to eliminate these errors may lead to undefined behavior that may include buffer overflow and memory leaks. Therefore, the following secure programming rule is prescribed:

SPR MEM35-C

Allocate sufficient memory for an object.

 

Not only sizes must be large enough to accommodate requests from objects, but they also should be within valid ranges for these values. Sizes cannot be negative, and they should not be larger than the maximum for any object. This value is stored in the variable SIXE_MAX in the C library stdint.h. When receiving a value for a size to allocate dynamic memory, it is recommended to check that it is within the above mentioned limits. For example, if we receive a value for a variable named count to create of an array of integers with count elements, the following should be checked:

if ((count<0)||(count>(SIZE_MAX/sizeof(int))) {
       // Handle error: count is outside limits
}

This advice is summarized in the following secure programming rule:

 

SPR ARR32-C

Ensure size arguments for variable length arrays are in a valid range.

 

The fact that a pointer must be initialized should be strongly emphasized. We should not try to use an uninitialized pointer. Doing so will produce undefined behavior. After a pointer is created, it is a good practice to set it to NULL, if no other value will be assigned immediately after declaration. If a pointer is to be obtained from a dynamic allocation function (like malloc, calloc, or realloc), it is recommended to initialize it to NULL, before these functions are called, because if they fail, they may not initialize the pointer at all.  Memory obtained from calloc is ready to be used, because it is initialized to zero. Beware of using memory obtained from malloc or new memory added with realloc. These functions do not initialize it, so the user must do so before use, as prescribed by the following secure rule programming:

 

SPR EXP33-C

Do not read uninitialized memory.

 

Read More

Read more about Pointers in in sections 5.1 thru 5.7 of the textbook.

 

Read More

Read more about Structures in sections 6.1 thru 6.4 of the textbook.

 

Read More

Read more about Dynamic Allocation in sections 7.8.5 of the textbook.

 

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
