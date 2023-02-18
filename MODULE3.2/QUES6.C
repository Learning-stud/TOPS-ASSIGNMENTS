#include<stdio.h>
                ////_____________FACTORALS OF AN GIVEN NUMBERS______________________/////
void main ()
{

    int num , count , fact=1;

    printf(" enter an number to find its factorals \n ");
    scanf("d", &num);


    for (count  = 1; count <= num; count++)
    {
            fact=fact*count;
    }
    
}