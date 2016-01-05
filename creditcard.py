"""
Credit card validation - Luhn algorithm
"""
def sumdigits(n):
	s = 0
	while n>0:
		s+=n%10
		n = n/10
	return s
def credit(n):
	digits = [ int(c) for c in n]
	even = True
	sums = 0
	for i in range(len(digits)-1,-1,-1):
		if even:
			k=digits[i]
			even = False
		else:
			k = 2*digits[i]
			if k>9:
				k = sumdigits(k)
			even = True
		sums+=k
	if sums%10==0:
		print "Valid card"
	else:
		print "Invalid card"
def main():
	while True :
		n = raw_input("Enter credit card : type q to quit  ")
		if n=="q":
			break
		n = n.replace(" ","")
		credit(n)
main()
