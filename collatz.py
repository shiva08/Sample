"""
 Take any natural number n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process
 """
 def main():
	try:
		n = input('Enter number')
	except ValueError:
		print "Enter integer greater than 1"

	hailstones = [n]
	while n>1:
		if n%2==0:
			n = n/2
		else:
			n = 3*n+1
		hailstones.append(n)
	print len(hailstones)
	print hailstones
main()
