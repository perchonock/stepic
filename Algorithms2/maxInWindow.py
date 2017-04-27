#import sys
#input = sys.stdin.read()

def getMaxNaive(input):
    n = int(input.split('\n')[0])
    nums = [int(i) for i in input.split('\n')[1].split()]
    w = int(input.split('\n')[2])
    result = ''
    r = n-w+1
    for i in range(r):
        m = max(nums[i:(i+w)])
        result += str(m) + ' '
    return result.strip()

class StackWithMaxElement:
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

    def isEmpty(self):
        return self.items == []

class QueueWithMaxElement:
    def __init__(self):
        self.stack1 = StackWithMaxElement()
        self.stack2 = StackWithMaxElement()

    def pushBack(self, item):
        self.stack1.push(item)

    def popFront(self):
        if self.stack2.isEmpty():
            while len(self.stack1.items) != 0:
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def get_max(self):
        if(self.stack1.isEmpty()):
            return self.stack2.get_max()
        elif(self.stack2.isEmpty()):
            return self.stack1.get_max()
        else:
            return max(self.stack1.get_max(), self.stack2.get_max())

    def print(self):
        print('stack1', self.stack1.items)
        print('max', self.stack1.max)
        print('stack2', self.stack2.items)
        print('max', self.stack2.max)

def getMax(input):
    n = int(input.split('\n')[0])
    nums = [int(i) for i in input.split('\n')[1].split()]
    w = int(input.split('\n')[2])
    qu = QueueWithMaxElement()
    for i in range(w):
        qu.pushBack(nums[i])
    result = str(qu.get_max()) + ' '
    for j in range(w,n):
        qu.popFront()
        qu.pushBack(nums[j])
        result += str(qu.get_max()) + ' '

    return result.strip()

#sys.stdout.write(getMax(input))

# q = QueueWithMaxElement()
# q.pushBack(2)
# q.pushBack(7)
# q.pushBack(3)
# q.pushBack(1)
# q.print()
# print(q.get_max())
# q.popFront()
# q.pushBack(5)
# q.print()
# print(q.get_max())
# q.popFront()
# q.pushBack(2)
# q.print()
# print(q.get_max())
# q.popFront()
# q.pushBack(6)
# q.print()
# print(q.get_max())
# q.popFront()
# q.pushBack(2)
# q.print()
# print(q.get_max())

#print(getMax('8\n2 7 3 1 5 2 6 2\n4'))