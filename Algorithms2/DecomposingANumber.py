import sys
#n = int(sys.stdin.read())
n = 6
nums = []

def IsPrimeNum(k):
    for i in range(2, int(k**0.5)+1):
        if k % i == 0:
            return False
    return True

def DecomposeNum(n):
    if IsPrimeNum(n):
        nums.append(n)
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and IsPrimeNum(i):
            nums.append(i)
            DecomposeNum(n//i)
            break

if n > 0:
    DecomposeNum(n)
    print(" ".join(map(str,nums)))
