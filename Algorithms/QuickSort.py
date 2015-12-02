import random
#array = [random.randint(-(10**8),(10**8)) for i in range(5000)]
#array = [i for i in range(5000)]
#print(array)

import sys
#input = sys.stdin.read().splitlines()
# input = "2 3\n0 5\n7 10\n0 5\n7 10\n1 6 11".splitlines()
# n_of_seg = int(input[0].split()[0])
#
# segments = []
# for i in range(1, n_of_seg+1):
#     current_segment = [int(n) for n in input[i].split(" ")]
#     segments.append(current_segment)
#
# points = [int(n) for n in input[-1].split()]


def QuickSort(array, l, r):
    def Partition(array, l, r):
        x = array[l][0]
        j = l
        for i in range(l+1,r+1):
            if array[i][0] <= x:
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

segments = [[1,4],[1,6],[7,8],[5,8]]
points = [2,1,9,10,3,2,2,2,2]

def Solution1(segments,points):
    QuickSort(segments,0,len(segments)-1)
    output = []
    points_segments = {}

    for point in points:
        if point in points_segments:
            output.append(points_segments[point])
        else:
            intersected_segs = 0
            for seg in segments:
                if point < seg[0]:
                    break
                elif point <= seg[1]:
                    intersected_segs += 1
            output.append(intersected_segs)
            points_segments[point] = intersected_segs

    print(" ".join(map(str,output)))

Solution1(segments,points)

