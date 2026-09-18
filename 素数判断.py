su=int(input("请输入数字"))
a=2
c=1
if su<=0:
	print("请输入正数")
elif su==1:
	print("输入为1")
	
else:
	while a*a<su:
		if su%a!=0:
			a+=1
		else:
			print("合数")
			c=0
			break
	if c==1:
		print("质数")
	