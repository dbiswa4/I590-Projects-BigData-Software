#Python Program to check whether a number is multiple of 2 or 3 or both

import sys

def print_multiple(num):
	print("In print_multiple()")
	for i in range(1,num +1 ):
		if (i % 2 == 0 and i % 3 == 0):
			#print i
			print 'fizzbuzz'
		elif i % 2 == 0:
			#print i
			print 'fiz'
		elif i % 3 == 0:
			#print i
			print 'buzz'
		else:
			print i

if __name__ == '__main__':
	num = int(input("Enter a number: "))
	print_multiple(num)

