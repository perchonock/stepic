import sys
#input = sys.stdin.read().splitlines()
input = "5 1 5 8 12 13\n5 8 1 23 1 11".splitlines()
array = [int(n) for n in input[0].split()]
searched_numbers = [int(n) for n in input[1].split()]
length=array[0]
array = array[1:]

def binary_search(number,array):
    left_limit = 0
    right_limit = length-1
    while left_limit <= right_limit:
        position = (left_limit+right_limit)//2
        if array[position] == number:
            return position + 1
        elif array[position] > number:
            right_limit = position-1
        else:
            left_limit = position+1
    return -1

# for number in range(1,len(searched_numbers)):
#     print(binary_search(searched_numbers[number], array), end = " ")

index_array = []
for number in range(1,len(searched_numbers)):
    index_array.append(binary_search(searched_numbers[number], array))
print(" ".join(map(str,index_array)))



