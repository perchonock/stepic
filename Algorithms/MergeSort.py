import sys
import math
#input = sys.stdin.read()
input = "5\n2 3 9 2 9"
input = input.splitlines()
length = int(input[0])
array = [int(n) for n in input[1].split()]
max_length = 2**(int(math.log2(length)) + 1)
for i in range(max_length-length):
    array.append(10**9+1)
#print(array)
k = 0

def MergeRecursive(array1, array2, array12 = []):
    l1 = len(array1)
    l2 = len(array2)
    if l1 > 0 and l2 > 0:
        if array1[0] <= array2[0]:
            array12.append(array1.pop(0))
            MergeRecursive(array1, array2, array12)
        else:
            array12.append(array2.pop(0))
            global k
            k += l1
            MergeRecursive(array1, array2, array12)
    elif l1 > 0:
        array12.extend(array1)
    elif l2 > 0:
        array12.extend(array2)
    return array12

def MergeIterative(array1, array2):
    array12 = []
    l1 = len(array1)
    l2 = len(array2)
    i1 = 0
    i2 = 0
    while i1 < l1 and i2 < l2:
        if array1[i1] <= array2[i2]:
            array12.append(array1[i1])
            i1 += 1
            if i1 == l1:
                for i in range(i2,l2):
                    array12.append(array2[i])
        else:
            array12.append(array2[i2])
            i2 += 1
            global k
            k += (l1-i1)
            if i2 == l2:
                for i in range(i1,l1):
                    array12.append(array1[i])
    return array12

def IterableMergeSort(array):
    tmp = []
    for i in array:
        tmp.append([i])
    while len(tmp) > 1:
        a1 = tmp.pop(0)
        a2 = tmp.pop(0)
        a12 = MergeRecursive(a1,a2,[])
        tmp.append(a12)
    return tmp[0]


def IterableMergeSort2(array):
    import queue
    q = queue.Queue()
    for i in array:
        q.put([i])
    while q.qsize() > 1:
        a1 = q.get()
        a2 = q.get()
        a12 = MergeIterative(a1,a2)
        q.put(a12)
    return q.get()

#print(MergeIterative([2,3,4,6],[1,2,5,7,8]))

#IterableMergeSort2(array)
#print(k)

def MergeSort(array, l, r):
    if l < r:
        m = (l + r)//2
        MergeIterative(MergeSort(array,l,m),MergeSort(array,m+1,r))
    return [array[l]]

MergeSort(array, 0, len(array)-1)
print(array)




