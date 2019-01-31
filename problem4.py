def isPalindrome(num):
	numString = str(num)
	revString = numString[::-1]
	
	if(numString == revString):
		return True
	else:
		return False

maxPal = 0

for a in range(100,999):
	for b in range(100,999):
		prod = a * b
		if isPalindrome(prod) and (prod > maxPal):
			maxPal = prod

print maxPal
