import sys
class BinaryTree:
    def __init__(self):
        self.nodes = []

    def add(self, key, left_son, right_son):
        node = [key, left_son, right_son]
        self.nodes.append(node)

    def inorder(self, v):
        left_son = self.nodes[v][1]
        right_son = self.nodes[v][2]
        if left_son != -1:
            self.inorder(left_son)
        if v != -1:
            sys.stdout.write(str(self.nodes[v][0]) + ' ')
        if right_son != -1:
            self.inorder(right_son)


    def preorder(self, v):
        result = ""
        left_son = self.nodes[v][1]
        right_son = self.nodes[v][2]
        if v != -1:
            sys.stdout.write(str(self.nodes[v][0]) + ' ')
        if left_son != -1:
            self.preorder(left_son)
        if right_son != -1:
            self.preorder(right_son)


    def postorder(self, v):
        result = ""
        left_son = self.nodes[v][1]
        right_son = self.nodes[v][2]
        if left_son != -1:
            self.postorder(left_son)
        if right_son != -1:
            self.postorder(right_son)
        if v != -1:
            sys.stdout.write(str(self.nodes[v][0]) + ' ')



n = int(input())
tree = BinaryTree()
for i in range(n):
    nodes = input().split()
    v = int(nodes[0])
    l = int(nodes[1])
    r = int(nodes[2])
    tree.add(v, l, r)

tree.inorder(0)
print()
tree.preorder(0)
print()
tree.postorder(0)

