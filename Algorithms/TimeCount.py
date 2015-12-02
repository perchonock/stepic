import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

import random
segments = []
points = []
for i in range (5000):
    a = random.randint(-(10**8),(10**8))
    b = random.randint(a,(10**8))
    seg = [a,b]
    segments.append(seg)
    p = random.randint(-(10**8),(10**8))
    points.append(p)


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


QuickSort(segments,0,len(segments)-1)

with Profiler() as p:
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

        #print(" ".join(map(str,output)))

    Solution1(segments,points)

    #print(output)