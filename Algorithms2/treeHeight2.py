import sys
sys.setrecursionlimit(20000)

#input = sys.stdin.read()
input = '10\n9 7 5 5 2 9 9 9 2 -1'
#input = '2\n-1 0'
tree = [int(i) for i in input.split('\n')[1].split()]
l = int(input.split('\n')[0])

all_nodes = range(l)
all_parents = tree
leaves = set(all_nodes) - set(all_parents)
hs = [0 for i in range(l)]
#print(hs)

def getHeight(node, tree):
    print(hs)
    if hs[node] == 0:
        if tree[node] == -1:
            h = 1
            hs[tree[node]] = h
            print(hs)
        else:
            h = getHeight(tree[node], tree)
            h += 1
            hs[tree[node]] = h
            print(hs)
    else:
        h = hs[node]
    return h


# print(getHeight(7, tree)) #4
# print(getHeight([4, -1, 4, 1, 1], 5)) #3
# print(getHeight(3, [-1, 0, 4, 0, 3])) #4
# print(getHeight([9, 7, 5, 5, 2, 9, 9, 9, 2, -1], 10)) #4
# print(getHeight([-1], 1)) #1
# print(getHeight([-1, 0], 2)) #2

# sys.stdout.write(str(getHeight(tree, l)))

h_max = 1
for leave in leaves:
    h_max = max(h_max, getHeight(leave, tree))

# print(h_max)

sys.stdout.write(str(h_max))
