import sys
#input = sys.stdin.read()
input = '10\n9 7 5 5 2 9 9 9 2 -1'

tree = [int(i) for i in input.split('\n')[1].split()]
l = int(input.split('\n')[0])

def getHeight(node, tree, length):
    h = 1
    all_nodes = range(length)
    all_parents = tree
    leaves = set(all_nodes) - set(all_parents)
    for i in leaves:
        h = max(h, getHeight(tree[i], tree, length))

print(getHeight(tree, l)) #4
#print(getHeight([4, -1, 4, 1, 1], 5)) #3
#print(getHeight([-1, 0, 4, 0, 3], 5)) #4
#print(getHeight([9, 7, 5, 5, 2, 9, 9, 9, 2, -1], 10)) #4
#print(getHeight([-1], 1)) #1
#print(getHeight([-1, 0], 2)) #2

#sys.stdout.write(str(getHeight(tree, l)))

