/****************************************************************************
Bert Darnell
09/11/2021
CS202

This program reads two new actors and adds them to an array, along with
the provided 3 arrays of names. It then prints the list and determines
the shortest name and who it belongs to.
******************************************************************************/

#include <stdio.h>
#include <string.h>

int main() {

// Parallel arrays with first name, middle initial, and last name
char first_name[8][7] = {"Robert", "Al", "Nicole", "Pamela", "Denzel", "Jackie", "Lucy", "Salma"};
char initial[8][2] = { "A", "B", "C", "D", "E", "F", "G", "H" };
char last_name[8][11] = {"De Niro", "Pacino", "Kidman", "Grier", "Washington", "Chan", "Liu", "Hayek"};

char new_first[2][100]; //read first names
char new_last[2][100];  //read last name
char new_initial[2][100];  //read initial 

char blank[100] = "";   //blank str to wipe aux string
char aux[100] = "";     //auxillery sting to set length to 20
char full_name[10][21]; //final array of names

int new_entry = 2;  //number of new actors
for (int i=0; i < new_entry; i++)
{
    printf("first name of actor %d: ", i+1);
    scanf("%s", new_first[i]);
    printf("middle initial of actor %d: ", i+1);
    scanf("%s", new_initial[i]);
    printf("last name of actor %d: ", i+1);
    scanf("%s", new_last[i]);

    // Adds read actor entries into full_name array
    strcpy(aux, blank);
    strcat(aux, new_first[i]);
    strcat(aux, " ");
    strcat(aux, new_initial[i]);
    strcat(aux, ". ");
    strcat(aux, new_last[i]);
    if (strlen(aux) > 20)
    {
        strncpy_s(full_name[i], aux, 20);
        strcat(full_name[i], "\0");
    }
    else { strcpy(full_name[i], aux); }    
}
printf("\n");

for (int i = new_entry; i < 10; i++)
{
    strcpy(aux, blank);
    strcat(aux, first_name[i - new_entry]);
    strcat(aux, " ");
    strcat(aux, initial[i - new_entry]);
    strcat(aux, ". ");
    strcat(aux, last_name[i - new_entry]);
    if (strlen(aux) > 20)
    {
        strncpy_s(full_name[i], aux, 20);
        strcat(full_name[i], "\0");
    }
    else { strcpy(full_name[i], aux); }
}

// prints list of actors
printf("Final list of actors\n");
printf("**********************************\n");
for (int i = 0; i < 10; i++)    {printf("%s\n", full_name[i]);}


int shortest = strlen(full_name[0]); // shortest number of characters
char shortest_name[21] = "";    // name of actor with shortest number of characters

// determines the actor with the shortest number of characters and prints amount
for (int i = 0; i < 10; i++)
{
    if (shortest > strlen(full_name[i]))
    {
        shortest = strlen(full_name[i]);
        strcpy(shortest_name, full_name[i]);
    }
}
printf("\nthe shortest name is [%s] with [%d] characters\n", shortest_name, shortest);

return 0;
}
