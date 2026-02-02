#include <iostream>
#include <ctype.h>
int main() {

unsigned char u1 = 128;
signed char s1 = u1;
printf("%d", isprint(u1));
printf("%d", isprint(s1));

char s1[6] = ("Hello");
s1[6] = '!';
printf("%s", s1);


signed char s1 = 'A';
    signed char s2 = '7';
    unsigned char u1 = s1;
    unsigned char u2 = s2;
    printf("signed %c\n",s1+s2);
    printf("unsigned %c\n", u1 + u2);

    if (s1 > s1 + s2)
    {
    printf("s1 > s1 + s2\n");
    }
    else
    {
        printf("s1 <= s1 + s2\n");
    }
    if (u1 > u1 + u2)
    {
        printf("u1 > u1 + u2\n");
    }
    else
    {
        printf("u1 <= u1 + u2\n");
    }


    signed char sc1 = '1';
    signed char sc2 = 128;
    unsigned char uc1 = sc1;
    unsigned char uc2 = sc2;
    if (sc1 > sc2) {
        printf("sc1 > sc2\n");
    }
    else {
        printf("sc1 <= sc2\n");
    }
    if (uc1 > uc2) {
        printf("uc1 > uc2\n");
    }
    else {
        printf("uc1 <= uc2\n");
    }
}





