__author__ = 'yanina'

import sys
#input = sys.stdin.read()
input = "6\n2 3 9 2 9 10"
input = input.splitlines()
array = [int(n) for n in input[1].split()]

def count_sort(array):
    temp_array = [0]*11
    for current_number in array:
        temp_array[current_number] += 1
    array=[]
    for index in range(11):
        number_of_elements = temp_array[index]
        array.extend([index]*number_of_elements)
    return array

print(' '.join(map(str,count_sort(array))))
