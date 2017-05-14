# class HeapMin:
#     def __init__(self, array):
#         self.array = array
#
#     def SiftUp(self, i):
#         while i > 1:
#             if self.array[i] < self.array[i // 2]:
#                 self.array[i], self.array[i // 2] = self.array[i // 2], self.array[i]
#                 i //= 2
#             else:
#                 break

    # def SiftDown(self, i):
    #     length = len(self.array)
    #     left = 2 * i
    #     right = 2 * i + 1
    #     if right > length:
    #         if self.array[i] < min(self.array[left], self.array[right]):
    #             if min(self.array[left], self.array[right]) == self.array[2 * i]:
    #                 self.array[i], self.array[2 * i] = self.array[2 * i], self.array[i]
    #                 self.SiftDown(2 * i)
    #             elif min(self.array[2 * i], self.array[2 * i + 1]) == self.array[2 * i + 1]:
    #                 self.array[i], self.array[2 * i + 1] = self.array[2 * i + 1], self.array[i]
    #                 self.SiftDown(2 * i + 1)
    #     elif left > length:
    #         if self.array[i] < self.array[2 * i]:
    #             self.array[i], self.array[2 * i] = self.array[2 * i], self.array[i]
    #             self.SiftDown(2 * i)
    #
    # def Insert(self, x):
    #     self.array.append(x)
    #     self.SiftUp(len(self.array) - 1)
    #
    # def ExtractMin(self):
    #     self.array[1], self.array[-1] = self.array[-1], self.array[1]
    #     print(self.array.pop())
    #     self.SiftDown(1)


l = int(input())
array = [int(i) for i in input().split()]

def SiftDown(array, i, replacements):
    minIndex = i
    left = 2 * i + 1
    if left < l and array[left] < array[minIndex]:
        minIndex = left
    right = 2 * i + 2
    if right < l and array[right] < array[minIndex]:
        minIndex = right
    if i != minIndex:
        array[i], array[minIndex] = array[minIndex], array[i]
        replacements.append([str(i) + ' '  + str(minIndex)])
        global count
        count += 1
        SiftDown(array, minIndex, replacements)

def BuildHeap(array, l):
    replacements = []
    for id in range(l//2, -1, -1):
        SiftDown(array, id, replacements)
    return(replacements)


repl = BuildHeap(array, l)
print(len(repl))
for el in repl:
    print(el[0])

