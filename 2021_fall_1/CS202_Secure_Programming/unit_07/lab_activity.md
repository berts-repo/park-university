# Unit 7: Lab Activity

**Due:** 2021-10-04T04:59:00Z
**Points Possible:** 10.0
**Submission Types:** online_upload

## Instructions

Introduction 

The purpose of this assignment is to practice the use of files for input and output in C/C++.

 

Directions 

Write a C/C++ program that will reads a table from an ASCII file and produces statistical information in an ASCII output file. The program should read the information about some exoplanets from the file named [link: https://canvas.park.edu/courses/62124/files/8205024/download?verifier=L1V3dKUM3Bz2dktzwGxxvLjCHjF77v1tPLv8EaWp&wrap=1]  “ExoTable.txt”. This file contains one row for each exoplanet with the following information in order:

Sequential number in the list (integer starting at 1)

Exoplanet’s name (a string with up-to 25 characters)

Exoplanet’s distance to earth in light years (float)

Exoplanet’s mass ratio with respect to earth (float|)

Exoplanet’s orbit in earth days (float)

Exoplanet’s year of discovery

The program should read the information in the file and determine the following information from the exoplanets to be printed in the file “SummaryExoTable.txt”:

Minimum, maximum, and average distance to the earth in light years

Minimum, maximum, and average mass ratio with respect to the earth

Minimum, maximum, and average orbit in earth days

Minimum and maximum discovery years

The name of the exoplanet that is closest to the earth

The name of the exoplanet that is closest in mass to the earth

The name of the exoplanet that is closest in orbit days to the earth

Requirements for the program include:

Name the C/C++ file with the following format: LastNameFirstNameUnit7cpp. For example the Instructor may create a file with the following name: [INSTRUCTOR]Unit7.cpp.

Select appropriate identifiers and data types for all variables. Declare all of them correctly.

The program will read the information from the ASCII input file and print the required information in the ASCII output file. With so many options to read and write files, students are free to decide perform these activities, but it is recommended that the simplest method is to read the input file using the fscanf() function, and to write the output file using the fprintf() function. Students may follow the examples given in program “CWritingASCIIFiles.cpp” in the course material.

Minimum and maximum values can be evaluated, by reviewing and keeping the smallest and largest values of each column in the table, after reading each row of information. Total numbers for the averages can be also added in the same fashion. A counter should also be added to evaluate averages after all values are read.

The name of the exoplanet closest to the earth must be saved whenever a smallest distance to the earth is found.

The name of the exoplanet closest in mass to the earth is the one that has the smallest absolute difference in mass ratio to the number one (fabs(mass-1.0)). The fabs() function can be found in the <math.h> C library.

Similarly, the name of the exoplanet that is closest in orbit days to the earth is the one that has the smallest absolute difference in orbit days to the number (fabs(orbit-365.0)).

Include appropriate comments. In particular include a header for the main function and description of all variables.

The program should compile and run. The output file should be close to the example provided below.

Do not use advanced concept that were not reviewed in the class yet to solve this assignment. Assignments that use these concepts will only be granted 1 point for presentation.

Deliverables 

Submit only the C/C++ program file when completed. Do not submit anything else. This file is the .cpp file you created with the right name.

Due Date

By 11:59 p.m., Sunday, CT

Examples

The program should reproduce the following session:

                        Statistics - ExoPlanets - ExoTable.txt
------------------------------------------------------------------------------------------------------
                             Minimum        Maximum        Average

Distance to Earth             4.244          11.753         9.972
Mass of Earth                 0.900          490.000        35.906
Orbit in Earth Days           2.690          2940.000       408.388
Discovery Year                2000           2019

------------------------------------------------------------------------------------------------------ 
 The planet closest in distance to Earth is: Proxima-Centauri-b (4.24 light years)
The planet closest in mass to Earth is: Proxima-Centauri-b (0.10 times)
 The planet closest in orbit to the Earth is: Barnard's-Star-b (133.00 days)

------------------------------------------------------------------------------------------------------

---

## My Submission

**Score:** 10.0/10.0
**Grade:** 10
**Submitted:** 2021-10-05T06:46:17Z
**Late:** Yes

### Submitted Files

- **BertUnit7.cpp**
  - Downloaded: `files/BertUnit7.cpp`
- **Capture.PNG**
  - Downloaded: `files/Capture.PNG`

### Instructor Feedback

**Bert** (2021-10-05T06:46:18Z):

> Hello Professor,
I don't know how this assignment didn't get submitted. I took a screenshot and highlighted the date and time to show that I have not altered the project since the due date. Sorry for the inconvenience

**Luke Donoho** (2021-10-05T19:40:46Z):

> No issues on my side Bert, it came across okay.
