# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    Keep= [[0 for x in range(W+1)] for x in range(n+1)]
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w and val[i-1]+K[i-1][w-wt[i-1]] > K[i-1][w]:
                K[i][w] = val[i-1] + K[i-1][w-wt[i-1]]
                Keep[i][w]=1
            else:
                K[i][w] = K[i-1][w]
                Keep[i][w]=0
    T = W
    cost=0
    ser=[]
    for i in range(n+1,1,-1):
    	if Keep[i-1][T]==1:
    		ser.append(i-1)
    		cost=cost+wt[i-2]
    		T = T - wt[i-2]
    print(cost/100)
    return (K[n][W]/100)/len(ser),cost/100,ser

# Driver program to test above function
# val = [6, 76, 73,76,76]####value to maximize =quality score 
# wt = [1, 2, 2,2,2] ###weight to respect=cost
# W = 3 ###maximal cost(threshold to not be exceeded)
# n = len(val) ### number of executable query plans
# print(knapSack(W, wt, val, n))
