#include <stdio.h>
#include <math.h>

// function prototypes
int initFile(char* fileIn);
int outFile(char* fileIn, char* fileOut);

// variables for read values
int posEarth;       int posMass;       int posOrbit;   int position;
float minDistance;  float maxDistance; float avgDistance;
float minMass;      float maxMass;     float avgMass;
float minOrbit;     float maxOrbit;    float avgOrbit;
double closestMass; double closestOrbit;
int minYear;        int maxYear;

// function to read and initialize variables
int initFile(char* fIn) {

    FILE* f = NULL;
    const char header[] = "%d%s%f%f%f%d";

    int index;        // Sequential number in the list
    char name[25];    // Expoplanet's name
    float distance;   // Expoplanet's distance to earth in light years
    float mass;       // Expoplanet's mass ratio with respect to earth
    float orbit;      // Expoplanet's orbit in earth days
    int year;         // Expoplanet's year of discovery

    double absMass = 0;      // temp variable for mass calculations
    double absOrbit = 0;     // temp variable for orbit calculations
    
    int position = 0;     // variable to determine position in file

    // opens file
    f = fopen(fIn, "r");
    if (f == NULL)    {
        fprintf(stderr, "File %s was not found\n", fIn);
        return -1;
    }

    posMass = 0;
    posOrbit = 0;
    posEarth = 0;

    // reads the file and initialize values
    while (fscanf(f, header, &index, name, &distance, &mass, &orbit, &year) >= 6) {
        
        if (position == 0)  // initialize values to first row
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
            closestMass = fabs(mass - 1.0);
            closestOrbit = fabs(orbit - 365.0);
            posEarth = position;
        }
        else 
        {// calculations and sums
            avgDistance += distance;
            avgMass += mass;
            avgOrbit += orbit;
            absMass = fabs(mass - 1.0);
            absOrbit = fabs(orbit - 365.0);
        }

        // checks min and max values, sets positions in file for print
        if (distance < minDistance) { minDistance = distance; posEarth = position; }
        if (distance > maxDistance) { maxDistance = distance; }
        if (mass < minMass) { minMass = mass; }
        if (mass > maxMass) { maxMass = mass; }
        if (orbit < minOrbit) { minOrbit = orbit; }
        if (orbit > maxOrbit) { maxOrbit = orbit; }
        if (year < minYear) { minYear = year; }
        if (year > maxYear) { maxYear = year; }
        if (closestMass > absMass) { closestMass = fabs(mass - 1.0); posMass = position; }
        if (closestOrbit > absOrbit) {  closestOrbit = fabs(orbit - 365.0); posOrbit = position; }

        position++;
    }

    //closes file
    if (fclose(f) == EOF) {
        fprintf(stderr, "There is an error at closing %s\n", fIn);
        return -2;
    }

    return 0;
}
 // function to print and write to new file
int outFile(char* fIn, char* fOut) {
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

    // opens file in and fileIn.txt and fileOut.txt
    fi = fopen(fIn, "r");
    if (fi == NULL)    {
        fprintf(stderr, "File %s was not found\n", fIn);
        return -1;
    }
    fo = fopen(fOut, "w");
    if (fo == NULL)    {
        fprintf(stderr, "File %s was not found\n", fOut);
        return -2;
    }
    printf("                           Statistics - ExoPlanets - ExoTable.txt\n");
    printf("-------------------------------------------------------------------------------\n");
    printf("\n                            Minimum        Maximum     Average\n");
    printf("\nDistance to earth:           %.3f         %.3f      %.3f", minDistance, maxDistance, avgDistance);
    printf("\nMass of earth:               %.3f         %.3f     %.3f", minMass, maxMass, avgMass);
    printf("\nMass of earth:               %.3f         %.3f     %.3f", minMass, maxMass, avgMass);
    printf("\nDiscovery Year:              %d           %d", minYear, maxYear);
    printf("\n-------------------------------------------------------------------------------\n");

    // prints position of planets: closest to earth, closest mass, closest orbit
    int posCheck = 0;
    while (fscanf(fi, header, &index, name, &distance, &mass, &orbit, &year) >= 6) {
        
        if (posEarth == posCheck)        {
            printf("The plannet closest to earth is: %s (%.2f)\n", name, distance);
        }
        if (posMass == posCheck)        {
            printf("The plannet closest in mass to earth: %s (%.2f)\n", name, closestMass);
        }
        if (posOrbit == posCheck)        {
            printf("The plannet closest in orbit to earth: %s (%.2f)\n", name, closestOrbit);
        }
        posCheck++;

        // outputs to new file
        fprintf(fo, header2print, index, name, distance, mass, orbit, year);

    }
    printf("-------------------------------------------------------------------------------\n");
    
    // closes files
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

    char file_in[] = "ExoTable.txt"; //read file name
    char file_out[] = "SummaryExoTable.txt"; //output file

    //calls functions with check
    if (initFile(file_in) != 0)    {
        fprintf(stderr, "There was an error reading file %s\n", file_in);
    }

    if (outFile(file_in, file_out) != 0)    {
        fprintf(stderr, "There was an error creating file %s\n", file_out);
    }
    return 0;
}