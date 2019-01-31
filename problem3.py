import math
n = 600851475143


def isPrime(num):
	for x in range(2, num - 1):
		if (num % x == 0):
			return False
	return True



i = 2

while i * i <= n:
	if(n % i == 0 and isPrime(i)):
		n = n / i;
	i+=1

print n
