def LIS(array):
    length = len(array)
    D = [1]*length
    for i in range(length):
        for j in range(i):
            if array[i]%array[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    n = max(D)
    return n


import sys
#input = sys.stdin.read().splitlines()
input = "4\n3 6 7 12".splitlines()
array = [int(n) for n in input[1].split()]

#print(LIS([7,2,1,3,8,4,9,1,2,6,5,9,3,8,1]))
print(LIS(array))

