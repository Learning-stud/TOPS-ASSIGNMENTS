  #include<stdio.h>
  ///  fibonacci series up given 
  void main ()
  {

    int n,y,a,b,c;
    
    printf("\n enter no of terms");
    
    scanf("%d",&n);
    a=0; b=1;
    
    printf("\n %d \t %d",a,b);
    for (y=3;y<=n;y++);
    
    
    

    {
         c=a+b;
         printf("\t%d",c);   
        a=b;
        b=c;
    }
     

  }