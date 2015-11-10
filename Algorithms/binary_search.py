__author__ = 'YKolotolova'

import sys
#input = sys.stdin.read()
input = "5 1 5 8 12 13\n5 8 1 23 1 11"
input = input.splitlines()
array = [int(n) for n in input[0].split()]
searched_numbers = [int(n) for n in input[1].split()]
length=array[0]
#print(input[0])
#print(input[1])

def binary_search(number,array):
    if number > array[-1] or number < array[0]:
        return -1
    left_limit = 0
    right_limit = length
    while left_limit <= right_limit:
        position = int((left_limit+right_limit)/2)
        if array[position] == number:
            return position +1
        elif array[position] > number:
            right_limit = position-1
        elif array[position] < number:
            left_limit = position+1
    return - 1

index_array = []
for number in range(1,len(searched_numbers)):

    index_array.append(binary_search(searched_numbers[number], array[1:]))

print(" ".join(map(str,index_array)))