#include<stdio.h>
#define  DAYSINWEEK 7
void main()
{
                                                       //  1. Take the number of days as input.
                                                     //  2. For the number of years, divide the input by 365 and obtain its quotient.
                                                   //  3. For the number of weeks, divide the input by 365 and obtain its remainder.
                                                 //       Further divide the remainder by 7(no of days in a week) and obtain its quotient.
                                               //  4. For the number of days, divide the input by 365 and obtain its remainder.
                                             //     Further divide the remainder by 7(no of days in a week) and obtain its remainder.
                                           // ------------CONVERT YEARS INTO WEEKS , WEEKS INTO DAY---------//
    int ndays, year, week, days;

 

    printf("Enter the number of days\n");

    scanf("%d", &ndays);

    year = ndays / 365;

    week =(ndays % 365) / DAYSINWEEK;

    days =(ndays % 365) % DAYSINWEEK;

    printf ("%d is equivalent to %d years, %d weeks and %d daysn",

            ndays, year, week, days);


}