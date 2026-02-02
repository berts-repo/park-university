#include <stdio.h>
#include <stdlib.h>

struct myBox {
    int someNumber;
    int dynArray[];
};

typedef struct myBox box;      // nickname for structure
box* point = NULL;             // pointer for dynamic array
int size = 5;                  // size of array

int main() {

    // this line initializes the array
    point = (box*)malloc(sizeof(box) + size * sizeof(box));

    // this block sets values to the array
    for (int i = 0; i < size; i++)
    {   
        // dot notation
        (*(point + i)).dynArray[i] = (2 * i);
    }

    // this block prints the array index, the dynamic array values, and the location in memory
    for (int i = 0; i < size; i++)
    {
        // dot notation
        printf("dynArray[%d]: %d | address: %d\n", i, (*(point+i)).dynArray[i], &(*(point + i)).dynArray[i]);
    }
    return 0;
}