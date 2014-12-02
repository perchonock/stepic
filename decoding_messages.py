__author__ = 'YKolotolova'
keys = input()
values = input()
dict_for_coding = dict(zip(keys,values))
coded = ''
decoded = ''
for char in input():
    coded += dict_for_coding[char]

for char in input():
    for key, value in dict_for_coding.items():
        if char == value:
            decoded += key

print(coded)
print(decoded)


