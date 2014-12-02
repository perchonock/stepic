__author__ = 'YKolotolova'
import re
in_file = open("dataset_3363_2.txt", 'r')
out_file = open("decoded.txt", 'w')
s = in_file.readline().strip()
letters = re.findall("[a-z,A-Z]+", s)
numbers = re.findall("[0-9]+", s)
print(letters)
print(len(letters))
print(numbers)
print(len(numbers))
length = len(letters)
out = ''
for i in range(length):
    out += letters[i]*int(numbers[i])

print(out)
out_file.write(out)


in_file.close()
out_file.close()