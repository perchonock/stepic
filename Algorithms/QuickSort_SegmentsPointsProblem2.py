import random

def QuickSort3(array, l, r):
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
        QuickSort3(array, l, j)
        l = k+1

import sys
#input = sys.stdin.read().splitlines()
#input = "4 3\n0 5\n7 10\n1 5\n3 8\n1 6 11".splitlines()
input = "3 11\n2 8\n1 3\n5 6\n0 1 2 3 4 5 6 7 8 9 10".splitlines()
n_of_seg = int(input[0].split()[0])
left_borders = []
right_borders = []
for i in range(1, n_of_seg+1):
     left_borders.append(int(input[i].split(" ")[0]))
     right_borders.append(int(input[i].split(" ")[1]))
points = [int(n) for n in input[-1].split()]

QuickSort3(left_borders,0,n_of_seg-1)
QuickSort3(right_borders,0,n_of_seg-1)

def binary_searchIncluding(number,array):
    l = 0
    r = len(array)-1
    while l <= r:
        m = (l+r)//2
        if array[m] <= number :
            l = m+1
        else:
            r = m-1
    return l

def binary_searchNotIncluding(number,array):
    l = 0
    r = len(array)-1
    while l <= r:
        m = (l+r)//2
        if array[m] < number :
            l = m+1
        else:
            r = m-1
    return l

for point in points:
    starts = binary_searchIncluding(point, left_borders)
    ends = binary_searchNotIncluding(point, right_borders)
    segs = starts - ends
    print(segs, end= " ")
