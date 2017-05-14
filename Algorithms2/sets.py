input1 = input().split()
n = int(input1[0])

parents = [i for i in range(0, n+1)]
values = [0]
for i in input().split():
    values.append(int(i))

max_size = max(values)

def find(i):
    if i != parents[i]:
        parents[i] = find(parents[i])
    return parents[i]

def union(destination, source):
    dest_root = find(destination)
    sour_root = find(source)
    global max_size
    if dest_root == sour_root:
        max_size = max(max_size, values[dest_root])
        print(max_size)
        return
    values[dest_root] += values[sour_root]
    values[sour_root] = 0
    parents[sour_root] = dest_root
    max_size = max(max_size, values[dest_root])
    print(max_size)

for i in range(int(input1[1])):
    nums = input().split()
    union(int(nums[0]), int(nums[1]))




