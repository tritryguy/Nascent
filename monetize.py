#!/usr/bin/python3

# monotize.py
"""
Python Monotize

Formats int() to money form

1.) adds $ to start
2.) Only 2 decimal places format (var, '.2f')
3.) ',' at 3 zeros

"""
def monetize(n):
	n = ("$"+str(format(float(n), ',.2f')))
	return n

print (monetize(input("numm=== ")))

"""
# Format Practice

n = input("Num=== ")
print(n)
print ("$"+str(format(float(n), ',.2f')))
"""
