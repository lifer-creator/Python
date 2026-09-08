#include<stdio.h>
int main()
{
    int i,m,t;
   for(i=100;i<200;i++)
   {
    t=1;
       for(m=2;m<i;m++)
       {
        
        if(i%m==0 )
        {
        t=0;
        break;
        }
       }
        if(t==1)
        printf("%d \n",i );
       
   }
  
  return 0;
}
