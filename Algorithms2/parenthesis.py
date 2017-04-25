import sys
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)

stack = Stack()
#string = sys.stdin.read()
string = '{{[()]]'
i = 1

for s in string:
    if s in ['(', '{', '[']:
        stack.push([s, i])
    elif s in [')', '}', ']']:
        if stack.isEmpty():
            result = str(i)
            break
        elif (s == ')' and stack.peek()[0] != '(') or (s == ']' and stack.peek()[0] != '[') or (s == '}' and stack.peek()[0] != '{'):
            result = str(i)
            break
        else:
            stack.pop()
    i += 1
    #stack.print()
else:
    if stack.isEmpty():
        result = 'Success'
    else:
        result = str(stack.peek()[1])

sys.stdout.write(result)