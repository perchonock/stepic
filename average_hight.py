__author__ = 'YKolotolova'

height_info = {}

for n in range(1,12):
    height_info[n] = []

with open("dataset_3380_5.txt", "r") as in_file:
    for line in in_file:
        ls = line.strip().split("\t")
        height_info[int(ls[0])].append(int(ls[2]))

with open("av_height.txt", "w") as out_file:
    for classes, height in height_info.items():
        if len(height) > 0:
            av_hight = sum(height)/len(height)
            height_info[classes] = av_hight
        else:
            height_info[classes] = "-"
        out_file.write(str(classes)+ " " + str(height_info[classes]) + "\n")
