x=int(input("num:"))
asd=[]
for num in range(1,x):
	for i in range(2,num):
		if num%i == 0:
			break
	else:
		asd.append(num)
print(asd)


