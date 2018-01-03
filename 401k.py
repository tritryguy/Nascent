#!/usr/bin/python3

# ma-6k
from sys import argv
script, invest, apy, years = argv

print("\n\n\n\t\t\033[1;33m$$$\033[1;32m 401k \033[1;33m$$$\033[0m\n\n")

"""
invest_ammount = int(input("\033[1;32mAmmount \033[1;33m>>>\033[0m "))
intrest = int(input("\n\033[1;32mIntrest \033[1;33m>>>\033[0m "))
term_lenght = int(input("\n\033[1;32mTerm \033[1;33m>>>\033[0m "))
"""

def monetize(n):
	n = ("$"+str(format(float(n), ',.2f')))
	return n

def mak(init,rate,term):
	def monetize(n):
		n = ("$"+str(format(float(n), ',.2f')))
		return n

	num = 0
	og_init = init

	while num < term:
		num += 1
		init = init * (rate / 100 +1 )
		print ("Year " + str(num) + ": " + monetize(init))
		init = init  + og_init


mak(int(invest), int(apy), int(years))
