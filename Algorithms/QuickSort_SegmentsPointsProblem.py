import random

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

left_sorted = QuickSort3(left_borders)
right_sorted = QuickSort3(right_borders)

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
    starts = binary_searchIncluding(point, left_sorted)
    ends = binary_searchNotIncluding(point, right_sorted)
    segs = starts - ends
    print(segs, end= " ")
