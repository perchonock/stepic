import sys
#n = int(sys.stdin.read())
n = 32718
tmp = [None for n in range(n+1)]
tmp[0] = 0
tmp[1] = 0
answer = [n]

for n in range(2,n+1):
    three = n%3
    two = n%2
    if three == 0 and two == 0:
        tmp[n] = min(tmp[n//3]+1, tmp[n//2]+1, tmp[n-1]+1)
    elif three == 0:
        tmp[n] = min(tmp[n//3]+1, tmp[n-1]+1)
    elif two == 0:
        tmp[n] = min(tmp[n//2]+1, tmp[n-1]+1)
    else:
        tmp[n] = tmp[n-1]+1

k = tmp[-1]
print(k)

while k != 0:
    if k-1 == tmp[n-1]:
        answer.append(n-1)
        n = n-1
    elif n%2 == 0:
        if k-1 == tmp[n//2]:
            answer.append(n//2)
            n = n//2
        elif n%3 == 0:
            if k-1 == tmp[n//3]:
                answer.append(n//3)
                n = n//3
    elif n%3 == 0:
        if k-1 == tmp[n//3]:
            answer.append(n//3)
            n = n//3
    k -= 1

answer = answer[::-1]
print(" ".join(map(str,answer)))