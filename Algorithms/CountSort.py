import sys
#input = sys.stdin.read().splitlines()
input = "5\n2 3 9 2 9".splitlines()
length = int(input[0])
array = [int(n) for n in input[1].split()]

def CountSort(array):
    sorted_array = []
    for i in range(1,11):
        c = array.count(i)
        for n in range(c):
            sorted_array.append(i)

    return sorted_array

sorted_array = CountSort(array)
print(" ".join(map(str,sorted_array)))


