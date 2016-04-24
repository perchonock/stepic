#n,k = map(int, input().split())

def Cnk(n,k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return Cnk((n-1),k) + Cnk((n-1),(k-1))

print(Cnk(10,5))
