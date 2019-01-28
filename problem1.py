def isMultiple(num):
	if(num % 3 == 0):
		return True;
	elif(num % 5 == 0):
		return True;
	else:
		return False

sumNum = 0;

for i in range(1, 1000):
	if isMultiple(i):
		sumNum += i;
	

print sumNum;
