#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    int arr[100];
    int i,l,left=0,right=99,mid,a=0;
       
    for(i=0;i<100;i++)
    {
        arr[i]=i+1;
    }
    srand((unsigned int)time(NULL));
    l=rand()%100+1;
    while(left<=right)
    {
        mid=(left+right)/2;
        if(arr[mid]<l)
        left++;
        else if(arr[mid]>l)
        right--;
        else
        {
            a=1;
            break;
        }


    }
    if(a==1)
    printf("找到了");
}