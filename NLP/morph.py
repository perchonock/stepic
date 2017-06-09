#Сделать: 1. разрешение омонимии хотя бы на статистике

import re
#file = open('odict_small.csv', 'r', encoding='utf8')
dict_file = open('odict.csv', 'r', encoding='utf8')
odict = dict()
lemmas = dict()
tags = {'мо-жо': 'S', 'мс-п': 'A', 'вводн.': 'ADV', 'жо': 'S', 'п': 'A', 'мо': 'S', 'предик.': 'ADV',
        'предл.': 'PR', 'межд.': 'ADV', 'св': 'V', 'мн.': 'S', 'с': 'S', 'св-нсв': 'V', 'част.': 'ADV',
        'сравн.': 'A', 'нсв': 'V', 'м': 'S', 'числ.-п': 'ADV', 'числ.': 'ADV', 'со': 'S', 'союз': 'CONJ', 'ж': 'S', 'н': 'ADV'}

for letter in 'абвгдежзийклмнопрстуфхцчшщыэюя':
    odict[letter] = dict()

count = 0

for line in dict_file:
    words = line.lower().strip(',\n').split(',')
    lemma = words[0]
    bad_tag = words[1]
    true_tag = tags[words[1]]
    lemma_id = count
    count += 1
    lemmas[lemma_id] = [lemma, true_tag]
    first_letter = words[0][0].lower()
    try:
        odict[first_letter].update({lemma: lemma_id })
        if len(words) > 2:
            #Добавить условие, что если словоформа уже есть и у нее  другая лемма, то добавлять еще одну лемму
            for word in words[2:]:
                first_letter = word[0].lower()
                odict[first_letter].update({word: lemma_id})
    except:
        pass
dict_file.close()

#text = 'Стала стабильнее экономическая и политическая обстановка, предприятия вывели из тени зарплаты сотрудников. Все Гришины одноклассники уже побывали за границей, он был чуть ли не единственным, кого не вывозили никуда дальше Красной Пахры.'

file2parse = open('dataset_37845_1.txt', 'r', encoding='utf8')
result_file = open('result.txt', 'w', encoding='utf8')


def preproccess(text):
    text = text
    words = re.sub('\W', ' ', text).split() #нужно чтобы по тире не разбивало
    return words

for line in file2parse:
    w = preproccess(line.strip('\n'))
    result = ''
    for word in w:
        word_trueCase = word
        word = word.lower()
        if 'ё' in word:
            word = re.sub(r'ё', 'е', word)
        first_letter = word[0]
        if word in odict[first_letter]:
            lemma_id = odict[first_letter][word]
            lemma_tag = lemmas[lemma_id]
            lemma = lemma_tag[0]
            tag = lemma_tag[1]
        else:
            #если слово не найдено, в лемму записываю его форму, а тег = сущ.
            lemma = word
            tag = 'A'
        result += word_trueCase + "{" + lemma + "=" + tag + "} "

    result = result.strip()
    result_file.write(result + '\n')

file2parse.close()
result_file.close()