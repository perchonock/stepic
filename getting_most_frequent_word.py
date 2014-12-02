__author__ = 'YKolotolova'

in_file = open("dataset_3363_3.txt", 'r')
out_file = open("most_freq.txt", 'w')
text = in_file.read()
list_of_words = text.split()
dict_of_words = {}
for word in list_of_words:
    word = word.lower()
    if word in dict_of_words:
       dict_of_words[word] +=1
    else:
        dict_of_words[word] = 1

max = 0
word = ''
for key in sorted(dict_of_words):
    if dict_of_words[key] > max:
        max = dict_of_words[key]
        word = key

s = str(word) + ' ' + str(max)
out_file.write(s)

in_file.close()