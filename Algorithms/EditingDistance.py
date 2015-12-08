import sys
#input = sys.stdin.read().splitlines()
input = "ab\nab".splitlines()
A = input[0]
B = input[1]

def ED(A,B):
    n = len(A)
    m = len(B)
    D = [[i for i in range(n+1)]]
    for j in range(1,m+1):
        tmp = [None for k in range(1,n+1)]
        D.extend([[j]+tmp])

    for i in range(1,n+1):
        for j in range(1,m+1):
            #print('i=',i,'j=',j)
            if A[i-1] != B[j-1]:
                c = 1
            else:
                c = 0
            D[j][i] = min(D[j][i-1] + 1, D[j-1][i] + 1, D[j-1][i-1] + c)
    # for line in D:
    #     print(line)
    return D[m][n]


print(ED(A,B))


