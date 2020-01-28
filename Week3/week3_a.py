#!/usr/bin/env python3

# A) Write a Python and R program that has the following:
#
# 	- Variable declarations
# 	- Functions
# 	- If/Else statements
# 	- Control Loops

# Variable Declaration
# Reference:
# 	* https://docs.python.org/3/tutorial/introduction.html#numbers
x = 42
print(42)

# Functions
# Reference:
# 	* https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def double(n):
	return n * 2
print(double(x))

# If / Else
# Reference:
# 	* https://docs.python.org/3/tutorial/controlflow.html#if-statements
#
def is_even(n):
	"""Determines if the number is even or not"""
	if n % 2 == 0:
		return True
	else:
		return False
print(f'Is Even: {is_even(2)}')
print(f'Is Even: {is_even(5)}')

# Loops
# 1) loop while the number is less equal than 10 and greater to 0
# Reference:
# 	* https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
n = 10
while True:
	n += 1
	if n > 9 and is_even(n):
		break

# 2) While with conditional
# Reference:
# 	* https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
n = 10
while n > 0 and n <= 10:
	n -= 1
	print(n)

# 3) for
# loop over a list's elements
# Reference:
# 	* https://docs.python.org/3/tutorial/controlflow.html#for-statements
elems = [1, 2, 3, 99, 187]
for n in elems:
	print(f'Double of {n} is {double(n)}')