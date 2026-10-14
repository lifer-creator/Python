a=1
b=1
n=int(input("请输入数字"))
m=n
if n<=0 :
    print("请输入正整数")
elif n==1:
    m=1
    c=1
    print("第",m,"个斐波那契数为",c)
else:
    while n-1:
        c=a+b
        b=a
        a=c
        n=n-1
    print("第",m,"个斐波那契数为",b)