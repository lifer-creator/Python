#include<stdio.h>
#include<time.h>
#include<stdlib.h>
void game()
{
  int a=5,r,s;
   srand((unsigned int)time(NULL));
  r=1+rand()%100;
 
  while(a)
  {
  printf("请输入数字1-100\n还有%d 次机会\n",a);
  scanf("%d",&s);
  if(s>r)
  {
    printf("偏大了");
  }
  else if(s==r)
  {
    printf("猜对了");
    break;
  }
  else
  {
    printf("偏小了");
  }
a--;
  }
  if(a==0)
  printf("失败了");
}
void menu()
{
  int c;
  do
  {
  printf("************************\n");
  printf("****请选择是否开始******\n");
  printf("*****1.开始***2.结束****\n");
  printf("************************\n");
  
  scanf("%d\n",&c);
  if(c==1)
  game();
  else
  {
  printf("游戏结束");
  break;
  }
 }while(c!=2);
}
int main()
{
  menu();
  return 0;
}

