class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.ranks = [0 for i in range(n+1)]

    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def unite(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.ranks[i_id] > self.ranks[j_id]:
            self.parents[j_id] = i_id
        else:
            self.parents[i_id] = j_id
            if self.ranks[i_id] == self.ranks[j_id]:
                self.ranks[j_id] += 1


input1 = input().split()
n = int(input1[0])
equals = Union(n)

for e in range(int(input1[1])):
    pair = input().split()
    i = int(pair[0])
    j = int(pair[1])
    equals.unite(i,j)

for d in range(int(input1[2])):
    pair = input().split()
    i = int(pair[0])
    j = int(pair[1])
    if equals.find(i) == equals.find(j):
        print('0')
        break
else:
    print('1')




