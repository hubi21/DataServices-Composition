import math
import csv
import sys 

def To_UniqueList(P):
	L=[]
	for list in P:
		for item in list:
			L.append(item)
	return L

def reputation(P):
	P=To_UniqueList(P)
	somme = 0
	n = len(P) 
	if n == 1:
		## last service
		return P[0][0].reputation
	else: 
	 	for service in P:
	 		somme = somme + 1/n*service.reputation

	 	return somme

def cost(P1):
	P=To_UniqueList(P1)
	somme=0
	n = len(P)
	if n == 1:
		return P[0][0].cost
	else:
		for service in P:
			somme = somme + calls_number(service,P1) * service.cost
		return somme


def reliability(P1):
	P=To_UniqueList(P1)
	product = 1
	n = len(P)
	if n == 1 :
		return P[0][0].reliability

	else :	
		for i,service in enumerate(P):
			res = 1
			nc=calls_number(service,P1)
			for k in range(nc):
				z = service.critical
				res2 = res * math.exp(service.reliability*z)
			product = product * res
		return product 

def availibility(P1):
	P=To_UniqueList(P1)
	product = 0
	n = len(P)
	if n == 1:
		return P[0].availibility

	else: 
		for i,service in enumerate(P):
			res = 0
			nc=calls_number(service,P1)
			for k in range(nc):
				z = service.critical
				res = res * math.exp(service.availibility * z)

			product = product * res
		return product 
