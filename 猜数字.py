import random
s=random.randint(1,100)

c=6
while c!=0:
	print("您还有",c, "次机会")
	guess=int(input("请输入数字"))
	if(s>guess):
		print("偏小了")
	elif(s<guess):
		print("偏大了")
	else:
		print("猜对了")
		break
	c=c-1
if c==0:
	print("失败了")
	print("素数为",s)
        
