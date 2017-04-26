import sys
sys.setrecursionlimit(20000)

input = sys.stdin.read()
#input = '10\n9 7 5 5 2 9 9 9 2 -1' #4
#input = '5\n4 -1 4 1 1' #3
#input = '2\n-1 0' #2
tree = [int(i) for i in input.split('\n')[1].split()]
l = int(input.split('\n')[0])

all_nodes = range(l)
all_parents = tree
leaves = set(all_nodes) - set(all_parents)
hs = [0 for i in range(l)]

def getHeight(node, tree):
    if hs[node] == 0:
        if tree[node] == -1:
            h = 1
            hs[node] = h
        else:
            h = getHeight(tree[node], tree)
            h += 1
            hs[node] = h
    else:
        h = hs[node]
    return h

h_max = 1
for leave in leaves:
    h_max = max(h_max, getHeight(leave, tree))

sys.stdout.write(str(h_max))
