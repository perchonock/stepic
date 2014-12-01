__author__ = 'yanina'
x = 0
y = 0
length = int(input())
direction = 1
num = 1
a = [[0]*length for i in range(length)]

cicle=0
while cicle <= y+direction <= length-1-cicle:
    while cicle <= x+direction  <= length-1-cicle:
        a[y][x] = num
        x = x + direction
        num +=1
    a[y][x] = num
    num +=1
    y = y + direction
    if y == len(a[0])-1-cicle:
        direction = -direction

    elif a[y][x]!=0:
        direction = -direction
        cicle+=1
        x=cicle
        y=cicle
if length%2 == 1:
    a[(length)//2][(length)//2]=num
for i in a:
    for j in i:
        print(str(j), end= ' ')
    print()







