num1 = 1
num2 = 2
num3 = 0
sumOfEvens = 2;

while(num2 < 4000000):
	num3 = num1+num2
	if(num3 % 2 ==0):
		sumOfEvens += num3
	num1=num2
	num2=num3

print(sumOfEvens)
