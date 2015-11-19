import sys
import operator
#input0 = sys.stdin.read()
input0 = "10"

def points_set(segments_string):
    input = input0.splitlines()
    number_of_segments = int(input[0])
    segments = []
    for i in range(1, number_of_segments + 1):
        current_segment = [int(n) for n in input[i].split(" ")]
        segments.append(current_segment)
    segments.sort(key = operator.itemgetter(1))
    points = [-1]
    for i in range(number_of_segments):
        if segments[i][0] > points[-1]:
            points.append(segments[i][1])
    return len(points)-1, points[1:]

# print(points_set(input0)[0])
# print(" ".join(map(str,points_set(input0)[1])))

def thief(stuff_string):
    input = stuff_string.splitlines()
    tmp_array = []
    for i in input:
        current_item = [int(n) for n in i.split(" ")]
        tmp_array.append(current_item)
    things = tmp_array[1:]
    sack_volume = tmp_array[0][1]
    number_of_things = tmp_array[0][0]
    for i in range(len(things)):
        things[i].append(things[i][0]/things[i][1])
    things.sort(key = operator.itemgetter(2), reverse=True)
    i=0
    total_value = 0
    while sack_volume > 0 and i < number_of_things:
        if sack_volume >= things[i][1]:
            total_value += things[i][1]*things[i][2]
            sack_volume -= things[i][1]
        else:
            total_value += sack_volume*things[i][2]
            sack_volume = 0
        i += 1
    return("%.3f" % total_value)

#print(thief(input0))

def dif_numbers(n_string):
    n = int(n_string)
    n2 = int(n)
    numbers = []
    i = 1
    while n2 > 0:
        if n2-i <= i:
            numbers.append(n2)
            break
        else:
            numbers.append(i)
            n2 -= i
        i +=1
    return len(numbers), numbers

# print(dif_numbers(input0)[0])
#print(" ".join(map(str,dif_numbers(input0)[1])))
