__author__ = 'YKolotolova'
dict_size = int(input())
ls_of_known_words = set()
ls_of_unknown_words = set()
for n in range(dict_size):
    ls_of_known_words.add(input().lower())

lines = int(input())
for l in range(lines):
    ls_of_words = input().lower().split()
    for word in ls_of_words:
        if word not in ls_of_known_words:
            ls_of_unknown_words.add(word)

for unknown_word in ls_of_unknown_words:
    print(unknown_word)

