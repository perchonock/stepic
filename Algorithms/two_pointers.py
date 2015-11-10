__author__ = 'YKolotolova'

array = [1, 5, 8, 12, 13, 32, 32, 56, 76]

def two_pointers(sum, array):
    if sum > array[-1] or sum < array[0]:
        return -1
    left_limit = 0
    right_limit = len(array)-1
    while left_limit <= right_limit:
        if array[left_limit] + array[right_limit] == sum:
            return left_limit, right_limit
        elif array[left_limit] + array[right_limit] > sum:
            right_limit -= 1
        elif array[left_limit] + array[right_limit] < sum:
            left_limit += 1
    return - 1

print(two_pointers(57, array))