#include <stdio.h>
#include "Header.hpp"


int main() 
{
    printf("The external variable before second translation: %d\n", externalInteger);
    changeBase();
    printf("The external variable after second translation: %d\n", externalInteger);
}
