#include<stdio.h>

      //---------WAP TO TAKE 10 NO INPUT FROM USER AND FIND OUT ....
                                //QUES---3// 

void main()
{

    int a=1,n,sum=0;
    printf("\n enter number");
    scanf("%d",n);
     do
     {
        if (a%2==0)
        {
            printf("\n%d",a);
            sum=sum+a;      
        }
        
     } while (a<=n);
     
    printf("\ntotal sum=%d",sum);
   
}