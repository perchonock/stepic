class SearchTree:
    def __init__(self):
        self.nodes = []

    def add(self, key, left_son, right_son):
        node = [key, left_son, right_son]
        self.nodes.append(node)

    def check(self, index, min_el, max_el):
        cur_key = self.nodes[index][0]
        left_son = self.nodes[index][1]
        right_son = self.nodes[index][2]

        if index == -1:
            return True
        if min_el is not None and cur_key < min_el:
            return False
        if max_el is not None and cur_key >= max_el:
            return False

        return self.check(left_son, min_el, cur_key) & self.check(right_son, cur_key, max_el)

import sys
sys.setrecursionlimit(20000)

n = int(input())
tree = SearchTree()
for i in range(n):
    nodes = input().split()
    v = int(nodes[0])
    l = int(nodes[1])
    r = int(nodes[2])
    tree.add(v, l, r)

print('CORRECT' if n == 0 or tree.check(0, None, None) else 'INCORRECT')