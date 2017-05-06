#input = '5\npush 2\npush 1\nmax\npop\nmax'
#input = '1\npush 2\npush 1'
#input = '6\npush 7\npush 1\npush 7\nmax\npop\nmax'
#input = '5\npush 1\npush 2\nmax\npop\nmax\n'
#input = '10\npush 2\npush 3\npush 9\npush 7\npush 2\nmax\nmax\nmax\npop\nmax'
#input = '3\npush 1\npush 7\npop'
#input = '7\npush -1\npush 2\npush 2\npush 10\nmax\nmax\npop'

class StackWithMaxSize:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        self.items.append(int(item))
        if len(self.max) == 0:
            self.max.append(item)
        else:
            if item > self.max[-1]:
                self.max.append(item)
            else:
                last = self.max[-1]
                self.max.append(last)

    def pop(self):
        self.max.pop()
        return self.items.pop()

    def print(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def get_max(self):
        return self.max[-1]

import sys
input = sys.stdin.read()
stack = StackWithMaxSize()
operations = input.strip('\n').split('\n')[1:]

for o in operations:
    oper = o.split()
    if oper[0] == 'push':
        stack.push(int(oper[1]))
    elif oper[0] == 'pop':
        stack.pop()
    elif oper[0] == 'max':
        sys.stdout.write(str(stack.get_max()) + '\n')


