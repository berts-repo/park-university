#include "header.hpp"

// function to dynamicaly allocate an array of integers. Returns errors
int iInit(int** p, int n) 
{
    if ((p != NULL) && (n > 0)) 
    {
        *p = (int*)calloc(n, sizeof(int));
        if (*p == NULL) 
        {
            printf("Could not create array.\n");
            return -1;
        }
        return 0;
    }
    else {
        printf("Array cannot be created. Null values received.\n");
        return -2;
    }
}

// function to dynamically allocate an array of floats. Returns errors
int fInit(float** p, int n) 
{
    if ((p != NULL) && (n > 0)) 
    {
        *p = (float*)calloc(n, sizeof(float));
        if (*p == NULL) 
        {
            printf("Could not create array.\n");
            return -1;
        }
        return 0;
    }
    else    
    {
        printf("Array cannot be created. Null values received.\n");
        return -2;
    }
}

// function to print dynamically allocated arrays
void print(int* p1, float* p2, float* p3, int n) {
    
    printf("\n Temperature - Conversion Table\n");
    printf("----------------------------------\n");

    for (int i = 0; i < n; i++)
    {
        printf("  %-05d   %-010.3f   %-010.3f\n", *p1+i, *(p2+i), *(p3+i));
    }
    printf("----------------------------------\n");


    return;
}



