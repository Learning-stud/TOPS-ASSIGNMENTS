#include<stdio.h>

      //---------WAP TO TAKE 10 NO INPUT FROM USER AND FIND OUT ....
                                //QUES---1// 

void main()
{
   int i;
	printf("Even numbers between 1 to 50 (inclusive):\n");
    scanf("%d",i);
	for (i = 1; i <= 50; i++) 
	{
		if(i%2 == 0) 
		{
		  printf("%d ", i);
		}
	}
}