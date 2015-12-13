import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

import random
left_borders = []
right_borders = []
points = []
for i in range (5000):
    #a = random.randint(-(10**8),(10**8))
    #b = random.randint(a,(10**8))
    a = 9
    b = 876
    left_borders.append(a)
    right_borders.append(b)
    p = random.randint(-(10**8),(10**8))
    points.append(p)
n_of_seg = 5000



with Profiler() as p:
    def QuickSort3(array, l, r):
        def Partition(array, l, r):
            x = array[l]
            j = l
            k = r
            for i in range(l+1,k+1):
                if array[i] < x:
                    j+=1
                    if j != i:
                        array[j], array[i] = array[i], array[j]
                elif array[i] > x:
                    array[k], array[i] = array[i], array[k]
                    k -= 1
            array[l], array[j] = array[j], array[l]
            return j,k
        while l<r:
            rand_i = random.randint(l,r)
            array[l],array[rand_i] = array[rand_i], array[l]
            j,k = Partition(array, l, r)
            QuickSort3(array, l, j-1)
            l = k+1

    QuickSort3(left_borders,0,n_of_seg-1)
    QuickSort3(right_borders,0,n_of_seg-1)