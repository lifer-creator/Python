#include<stdio.h>
int main()
{

int a=1;
int b=0;

for(int a=1;a<=100;a++)
{
    if(a%3==0)
    {
        b=b+a;
    }
}
printf("%d",b);
return 0;
}