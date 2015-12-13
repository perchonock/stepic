import random

def QuickSort(array, l, r):
    def Partition(array, l, r):
        x = array[l]
        j = l
        for i in range(l+1,r+1):
            if array[i] <= x:
                j+=1
                if j != i:
                    array[j], array[i] = array[i], array[j]
        array[l], array[j] = array[j], array[l]
        return j
    while l<r:
        rand_i = random.randint(l,r)
        array[l],array[rand_i] = array[rand_i], array[l]
        m = Partition(array, l, r)
        QuickSort(array, l, m-1)
        l = m+1

def QuickSort3_InPlace(array, l, r):
    def Partition(array, l, r):
        x = array[l]
        j = l
        k = l
        for i in range(l+1,r+1):
            if array[i] < x:
                j+=1
                k+=1
                if j != i:
                    if k != i:
                        array[j], array[k] = array[k],array[j]
                    array[j], array[i] = array[i], array[j]
            elif array[i] == x:
                k += 1
                if k != i:
                    array[k], array[i] = array[i], array[k]
        array[l], array[j] = array[j], array[l]
        return j,k

    while l<r:
        rand_i = random.randint(l,r)
        array[l],array[rand_i] = array[rand_i], array[l]
        j,k = Partition(array, l, r)
        QuickSort3_InPlace(array, l, j)
        l = k+1

def QuickSort3(array):
    smaller = []
    equal = []
    bigger = []
    if len(array) > 1:
        rand_i = random.randint(0,len(array)-1)
        x = array[rand_i]
        for i in array:
            if i < x:
                smaller.append(i)
            elif i == x:
                equal.append(i)
            else:
                bigger.append(i)
        return QuickSort3(smaller) + equal + QuickSort3(bigger)
    else:
        return array

A = [8, 10, 14, 12, 14, 9, 7, 6, 3, 9, 23, 4, 22, 56, 123, 86,1,1,1,1,0,3]
B = list(A)
C = list(A)
QuickSort(A,0,len(A)-1)
QuickSort3_InPlace(B,0,len(A)-1)
print(A)
print(B)
print(QuickSort3(C))