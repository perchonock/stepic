# W = 10
# n = 3
# weights = [0,1,4,8]

#D = [[0]*(W+1)]*(n+1)

def KnapSack(W,n,weights):
    D = []
    for n in range(0,n+1):
            tmp = [0 for k in range(0,W+1)]
            D.extend([tmp])

    for i in range(1,n+1):
        for w in range(1,W+1):
            D[i][w] = D[i-1][w]
            if weights[i] <= w:
                D[i][w] = max(D[i][w],D[i-1][w - weights[i]] + weights[i])
    return(D[n][W])

import sys
#input = sys.stdin.read().splitlines()
input = "10 3\n1 4 8".splitlines()
W = int(input[0].split()[0])
n = int(input[0].split()[1])
weights = [int(i) for i in input[1].split()]
weights.insert(0,0)

print(KnapSack(W,n,weights))
