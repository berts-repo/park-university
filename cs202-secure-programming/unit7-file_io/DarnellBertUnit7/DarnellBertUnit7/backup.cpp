#include <stdio.h>


int printT(char* fileIn, char* fileOut);  // function prototypes

int printT(char* fIn, char* fOut) {

    FILE* fi = NULL;
    FILE* fo = NULL;
    const char header[] = "%d%s%f%f%f%d";
    const char header2print[] = "%d, %s, %f, %f, %f, %d\n";

    int index;        // Sequential number in the list
    char name[25];    // Expoplanet's name
    float distance;   // Expoplanet's distance to earth in light years
    float mass;       // Expoplanet's mass ratio with respect to earth
    float orbit;      // Expoplanet's orbit in earth days
    int year;         // Expoplanet's year of discovery

    fi = fopen(fIn, "r");
    if (fi == NULL)    
    {
        fprintf(stderr, "File %s was not found\n", fIn);
        return -1;
    }

    fo = fopen(fOut, "w");
    if (fo == NULL)
    {
        fprintf(stderr, "File %s was not found\n", fOut);
        return -2;
    }


    float minDistance;
    float maxDistance;
    float avgDistance;
    float minMass;
    float maxMass;
    float avgMass;
    float minOrbit;
    float maxOrbit;
    float avgOrbit;
    int minYear;
    int maxYear;
    int counter = 0;

    while (fscanf(fi, header, &index, name, &distance, &mass, &orbit, &year) >= 6) {
        fprintf(fo, header2print, index, name, distance, mass, orbit, year);
        
        if (counter == 0)  // initialize values to first row
        {
            minDistance = distance;
            maxDistance = distance;
            minMass = mass;
            maxMass = mass;
            minOrbit = orbit;
            maxOrbit = orbit;
            minYear = year;
            maxYear = year;
            avgDistance = distance;
            avgMass = mass;
            avgOrbit = orbit;
        }
        else 
        {
            avgDistance += distance;
            avgMass += mass;
            avgOrbit += orbit;
        }
        if (distance < minDistance) { minDistance = distance; }
        if (distance > maxDistance) { maxDistance = distance; }
        if (mass < minMass) { minMass = mass; }
        if (mass > maxMass) { maxMass = mass; }
        if (orbit < minOrbit) { minOrbit = orbit; }
        if (orbit > maxOrbit) { maxOrbit = orbit; }
        if (year < minYear) { minYear = year; }
        if (year > maxYear) { maxYear = year; }

        counter++;
    }


    if (fclose(fi) == EOF) {
        fprintf(stderr, "There is an error at closing %s\n", fIn);
        return -4;
    }
    if (fclose(fo) == EOF) {
        fprintf(stderr, "There is an error at closing %s\n", fOut);
        return -3;
    }

    return 0;
}

int main() {

    char file_in[] = "ExoTable.txt";
    char file_out[] = "ExoTableOut.txt";

    if (printT(file_in, file_out) != 0)
    {
        fprintf(stderr, "There was an error creating file %s\n", file_out);
    }

    return 0;
}