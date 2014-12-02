__author__ = 'YKolotolova'
in_file = open("dataset_3363_4.txt", 'r')
out_file = open("av_marks.txt", 'w')
num_of_students = 0
math_sum = 0
physics_sum = 0
rus_sum = 0

for line in in_file:
    s = line.strip().split(';')
    av_mark = (int(s[1]) + int(s[2]) + int(s[3]))/3
    num_of_students +=1
    math_sum += int(s[1])
    physics_sum += int(s[2])
    rus_sum += int(s[3])
    out_file.write(str(av_mark) + "\n")

out_file.write(str(math_sum/num_of_students) + " ")
out_file.write(str(physics_sum/num_of_students) + " ")
out_file.write(str(rus_sum/num_of_students))

in_file.close()
out_file.close()
