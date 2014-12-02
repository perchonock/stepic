__author__ = 'YKolotolova'
num_of_commands = int(input())
pos = [0,0]
for n in range(num_of_commands):
    command = input()
    ls = command.split()
    if ls[0] == "север":
        pos[1] += int(ls[1])
    elif ls[0] == "запад":
        pos[0] -= int(ls[1])
    elif ls[0] == "юг":
        pos[1] -= int(ls[1])
    elif ls[0] == "восток":
        pos[0] += int(ls[1])

print(pos[0],pos[1])

