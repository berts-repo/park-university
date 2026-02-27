//
// Bert
// CS351 - Unit 7 Linux assignment
// 10/2/2022
//
//
// This program uses predetermined offesets to find a predermined word (string) in
// different files and print their output. It also calcules the memory usage and
// system uptime.
//
//

#include <stdio.h>
#include <string.h>    
#include <ctype.h>     
#include <stdlib.h>

//
// This function is for getting the system total uptime and idle times.
//
void OpenUptime(double* total, double* idle)
{
        FILE* uptime_file;

        uptime_file = fopen("/proc/uptime", "r");

        if (uptime_file == NULL) { printf("Can't open.\n");}
        else
        {
                fscanf(uptime_file, "%lf", total);
                fscanf(uptime_file, "%lf", idle);
                fclose(uptime_file);
        }
}
//
// This function prints the found word from the dynamic array
//
void PrintWord(char* p)
{
	for ( int i = 1; i < strlen(p); i++ )
		if (p != "\n" ) 
		{
			printf("%c", p[i] );
		}
}
//
// This function reads a file and seeks an offset and stores the word before the next whitespace,
// it also creates a dynamic array for the found word and returns the pointer to it.
//
char* OpenFile(char file_location[], int offset)
{	
	int word_length = 0;
	char c;
	char* p;
	FILE* fp;	

	fp = fopen(file_location, "r");
	if (fp == NULL)	{ printf("Could not open %s!", file_location); }	
        else 
	{
// Streams file from seek and ends at whitespace, which determines the length of found word.
		c = fgetc(fp);
		fseek( fp, offset, SEEK_SET);
		while ( c != EOF && isspace(c) == 0 )
		{
			c = fgetc(fp);
			word_length++;
		}
		
// Dynamic array for found word
		p = (char*)malloc(word_length);
		if(!p)	{ printf("Memory allocation error!\n"); }
		else 
		{	
			fseek( fp, offset, SEEK_SET );
			for ( int i = 0; i < word_length; i++ )
			{
				p[i] = c;
				c = fgetc(fp);
			}
		}	
		
		fclose(fp);
		return p;
	}
}

int main()
{
	
	double uptime_start, uptime_idle, uptime_percent;
	double mem_percentage;
	int mem_total, mem_free;

// Predetermined offsets for the word in a file	
	int offset1 = 0, offset2 = 11, offset3 = 31, offset4 = 14, offset5 = 17, offset6 = 45;

// Pointers for each file to open and be dynamically allocated	
	char* p1;
        char* p2;
        char* p3; 
	char* p4;
	char* p5;
	char* p6;

// Pointers to dynamic arrays to find the word offset in a file
	p1 = OpenFile("/proc/sys/kernel/hostname", offset1);
	p2 = OpenFile("/proc/driver/rtc", offset2);
	p3 = OpenFile("/proc/driver/rtc", offset3);
	p4 = OpenFile("/proc/version", offset4); 
	p5 = OpenFile("/proc/meminfo", offset5);
	p6 = OpenFile("/proc/meminfo", offset6);

// Prints found words 
	printf("Machine name: ");
	PrintWord(p1);
	
	printf("\nSystem time and date: ");
	PrintWord(p2);
	printf(" ");
	PrintWord(p3);
	
	printf("\nLinux verision: ");
	PrintWord(p4);

// Prints and converts char to int for percentages	
	mem_total = atoi(p5);
	mem_free = atoi(p6);	

	printf("\nMemory usage:");
	printf("\n	total: ");
	printf("%d kB", mem_total);
	printf("\n	 free: ");
	printf("%d kB", mem_free);

// Calculates and prints memory usage	
	mem_percentage = ( (double)mem_total - (double)mem_free) / mem_total;
	printf("\n       %% used: ");
	printf("%.2f", mem_percentage);

	printf("\nSystem usage (time):");
	OpenUptime(&uptime_start, &uptime_idle);
	printf("\n 	  Total up time: %f", uptime_start);
	printf("\n	Total idle time: %f", uptime_idle);

	uptime_percent = (uptime_start - uptime_idle) / uptime_start;
	printf("\n		 %% busy: %.2f\n", uptime_percent);

// Free dynamic arrays
	free(p1);
	free(p2);
	free(p3);
	free(p4);
	free(p5); 

	return 0;
}
