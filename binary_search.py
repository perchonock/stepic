__author__ = 'YKolotolova'

import sys
#input = sys.stdin.read()
input = "1 5 8 12 13\n8 1 23 1 11"
input = input.splitlines()
array = [int(n) for n in input[0].split()]
searched_numbers = [int(n) for n in input[1].split()]
print(array)
print(searched_numbers)
def binary_search(number,array):
    if number > array[-1] or number < array[0]:
        return -1
    rigth_limit = 0
    left_limit = len(array)
    while rigth_limit <= left_limit:
        position = int((rigth_limit+left_limit)/2)
        if array[position] == number:
            return position +1
        elif array[position] > number:
            left_limit = position-1
        elif array[position] < number:
            rigth_limit = position+1
    return - 1

index_array = []
for number in searched_numbers:
    index_array.append(binary_search(number, array))

print(index_array)