import numpy as np

def minimum(Q,j):
	n, nc = Q.shape
	minimum = float(1.)
	for i in range(0,n):
		if Q[i,j]<minimum:
			minimum=Q[i,j]
	return minimum
def maximum(Q,j):
	n, nc = Q.shape
	maximum = float(0.)
	for i in range(0,n):
		if Q[i,j]>maximum:
			maximum=Q[i,j]
	return maximum

##Compute the SAW values for positive criteria
def positive(Q,i,j,V):
	if maximum(Q,j)-minimum(Q,j)!=0:
		V[i,j]=(Q[i,j]-minimum(Q,j))/(maximum(Q,j)-minimum(Q,j))
	else:
		V[i,j]=1
	return V[i,j]

##Compute the values SAW for negative criteria
def negative(Q,i,j,V):
	if maximum(Q,j)-minimum(Q,j)!=0:
		V[i,j]=(maximum(Q,j)-Q[i,j])/(maximum(Q,j)-minimum(Q,j))
	else:
		V[i,j]=1
	return V[i,j]

##Compute the quality score for a set of an executable plans 
def quality_score(Q,W,C):
	num_rows, num_cols = Q.shape
#	print(num_rows,num_cols)
	V=np.full((num_rows, num_cols), 0.)
	for j in range(num_cols):
		if C[j]==0:
			for i in range(num_rows):
				V[i,j]=positive(Q,i,j,V)
		else:
			for i in range(num_rows):
				V[i,j]=negative(Q,i,j,V)
	Quality=np.full((num_rows),0.)
	for i in range(num_rows):
		quality=0
		for j in range(num_cols):
			quality=quality+V[i,j]*W[j]
		Quality[i]=quality
	return Quality