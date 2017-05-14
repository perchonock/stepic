# n = int(input().split()[0])
# tasks = [int(i) for i in input().split()]

n = 4
tasks = [int(i) for i in "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1".split()]

processors = [[i, 0] for i in range(n)]

def SiftDown(array, i, l):
    minIndex = i
    left = 2 * i + 1
    if left < l and array[left][1] < array[minIndex][1]:
        minIndex = left
    elif left < l and array[left][1] == array[minIndex][1]:
        if array[left][0] < array[minIndex][0]:
            minIndex = left
    right = 2 * i + 2
    if right < l and array[right][1] < array[minIndex][1]:
        minIndex = right
    elif right < l and array[right][1] == array[minIndex][1]:
        if array[right][0] < array[minIndex][0]:
            minIndex = right
    if i != minIndex:
        array[i], array[minIndex] = array[minIndex], array[i]

        SiftDown(array, minIndex, l)


for task in tasks:
    print(" ".join(map(str, processors[0])))
    processors[0][1] += task
    SiftDown(processors, 0, n)



