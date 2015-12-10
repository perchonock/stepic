W = 10
n = 4
weights = [0,6,3,4,2]
c = [0,30,14,16,9]

D = [[0]*(W+1)]*(n+1)

for i in range(1,n+1):
    for w in range(1,W+1):
        D[i][w] = D[i-1][w]
        if weights[i] <= w:
           D[i][w] = max(D[i][w],D[i-1][w - weights[i]] + c[i])

for line in D:
    print(line)
print(D[n][W])
