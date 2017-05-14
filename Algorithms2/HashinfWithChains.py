class HashingWithChains():
    def __init__(self, m):
        self.m = m
        self.list = [[] for i in range(m)]

    def hashing(self, str):
        leng = len(str)
        x = 263
        p = 1000000007
        sum = 0
        mult = 1
        for i in range(leng):
            # print(str[i], ord(str[i]))
            sum += (ord(str[i]) * mult)
            sum %= p
            mult = (mult * x) % p
        return sum % self.m

    def add(self, str):
        h = self.hashing(str)
        if str not in self.list[h]:
            self.list[h].insert(0, str)

    def find(self, str):
        h = self.hashing(str)
        if str in self.list[h]:
            print('yes')
        else:
            print('no')

    def delete(self, str):
        h = self.hashing(str)
        if str in self.list[h]:
            self.list[h].remove(str)

    def check(self, i):
        if len(self.list[i]) > 0:
            res = ' '.join(self.list[i])
        else:
            res = ''
        print(res)



m = int(input())
h = HashingWithChains(m)
n = int(input())
for i in range(n):
    params = input().split()
    if params[0] == 'add':
        h.add(params[1])
    elif params[0] == 'check':
        h.check(int(params[1]))
    elif params[0] == 'del':
        h.delete(params[1])
    elif params[0] == 'find':
        h.find(params[1])