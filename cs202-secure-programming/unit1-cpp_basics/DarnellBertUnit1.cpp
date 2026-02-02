/*******************************************************************
Bert Darnell
08/24/2021
CS202

This program calculates a spherical segment of a sphere.
It also outputs the radius of different dementions of the segment.

*********************************************************************/

#include <math.h>
#include <iostream>

#define pi 3.14159265359    //defines constant for PI

int main() {

    float volume, top_surface_area, bottom_surface_area, sphere_radius, lateral_surface_area;   //declared variables for calculations block
    float a, b, h;  //declared variables for prompted user input

    printf("What is the size of the top radius of the spherical segment?\n");   //prompted user input block
    scanf_s("%f", &a);
    printf("What is the size of the bottom radius of the spherical segment?\n");
    scanf_s("%f", &b);
    printf("What is the size of the height of the spherical segment?\n");
    scanf_s("%f", &h);


    volume = (3*a*a+3*b*b+h*h)*pi*h/6;  //calculations block
    top_surface_area = pi*(a*a);
    bottom_surface_area = pi*(b*b);
    sphere_radius = sqrt(((b-a) * (b-a) + h*h) * ((a+b) * (a+b) + h*h) / (4*h*h));
    lateral_surface_area = 2 * pi * sphere_radius * h;

    printf("\nThe data you entered is:");   //output block
    printf("\nThe top radius of the spherical segment is %.2f", a);
    printf("\nThe bottom radius of the spherical segment is %.2f", b);
    printf("\nThe height of the spherical segment is %.2f", h);
    printf("\nWith this data you have the following results:");
    printf("\nThe volume of the spherical segment is %.2f", volume);
    printf("\nThe top surface area of the spherical segment %.2f", top_surface_area);
    printf("\nThe bottom surface area of the spherical segment is %.2f", bottom_surface_area);
    printf("\nThe sphere radius of the spherical segment is %.2f", sphere_radius);
    printf("\nThe lateral surface area of the spherical segment is %.2f\n", lateral_surface_area);

    return 0;
} 

