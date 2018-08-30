#!/usr/bin/python3

"""
USEAGE

- Amount is standard @max (%5500)

- intrest rate is a given 7% (0.07)
"""


# 35IRA
def monetize(n):
	n = ("$"+str(format(float(n), ',.2f')))
	return n

###


amt=5500 #int(input("Ammount >>> "))
years=int(input("Years >>> "))
n=0
while years > 0:
    amt *= 1.07 
    n +=1
    print(str(n)+".) "+monetize(amt))
    years -= 1
    amt = amt + 5500
   

#print (amt)
