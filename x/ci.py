#!/usr/bin/python3

# ci

def monetize(n):
	n = ("$"+str(format(float(n), ',.2f')))
	return n

P=int(input("Princapal >>" ))
i=float(input("Intrest >>> "))/100
#i=ni/100
n=int(input("Compound Periods >> "))



iEarned=(P*(1+i)**n)-P
#pTotal=P*((1+i)**n-1)
pTotal=iEarned + P
print("Intrest earned = " + monetize(iEarned)) 
print("Total = " + monetize(pTotal))
