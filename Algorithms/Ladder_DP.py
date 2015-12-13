import sys
input = sys.stdin.read().splitlines()
steps = [int(n) for n in input[1].split()]
tmp = [0 for n in range(len(steps)+1)]
tmp[1] = steps[0]
for i in range(2,len(steps)+1):
    tmp[i] = steps[i-1]
    tmp[i] = max(tmp[i] + tmp[i-2],tmp[i-1]+tmp[i])

print(tmp[-1])


