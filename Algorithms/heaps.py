heap = [0]
def ShiftUp(i):
    while i > 1:
        if heap[i] > heap[i//2]:
            heap[i], heap[i//2] = heap[i//2], heap[i]
            i //= 2
        else:
            break

def ShiftDown(i):
    length = len(heap)
    left = 2 * i
    right = 2 * i + 1
    if right < length:
        if heap[i] < max(heap[left], heap[right]):
            if max(heap[left], heap[right]) == heap[2*i]:
                heap[i], heap[2*i] = heap[2*i], heap[i]
                ShiftDown(2*i)
            elif max(heap[2*i],heap[2*i + 1]) == heap[2*i + 1]:
                heap[i], heap[2*i + 1]= heap[2*i + 1], heap[i]
                ShiftDown(2*i + 1)
    elif left < length:
        if heap[i] < heap[2*i]:
            heap[i], heap[2*i]= heap[2*i], heap[i]
            ShiftDown(2*i)

def Insert(x):
    heap.append(x)
    ShiftUp(len(heap)-1)

def ExtractMax():
    heap[1], heap[-1] = heap[-1], heap[1]
    print(heap.pop())
    ShiftDown(1)

import sys
input0 = sys.stdin.read()
# input0 = "6\nInsert 200\nInsert 10\nExtractMax\nInsert 5\nInsert 500\nExtractMax"
input = input0.splitlines()
for line in input:
    if line.split()[0] == "Insert":
        x = int(line.split()[1])
        Insert(x)
    elif line == "ExtractMax":
        ExtractMax()





