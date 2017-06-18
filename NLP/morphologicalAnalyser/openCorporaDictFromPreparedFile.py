dictionary = dict()
lemmas = dict()
for letter in 'абвгдежзийклмнопрстуфхцчшщыэюя':
    dictionary[letter] = dict()

tags = {'NOUN': 'S', 'ADJF': 'A', 'ADJS': 'A', 'COMP': 'A', 'VERB': 'V', 'INFN': 'V', 'PRTF': 'V', 'PRTS': 'V', 'GRND': 'V', 'NUMR': 'ADV', 'ADVB': 'ADV', 'NPRO': 'S', 'PRED': 'ADV', 'PREP': 'PR', 'CONJ': 'CONJ', 'PRCL': 'ADV', 'INTJ': 'ADV'}

dict_file = open('openCorporaDict.txt', 'r', encoding='utf8')
for line in dict_file:
    items = line.strip('\n').split()
    form = items[0]
    first_letter = form[0]
    try:
        dictionary[first_letter][form] = set()
        for lemma_id in items[1:]:
            dictionary[first_letter][form].add(int(lemma_id))
    except:
        pass
dict_file.close()

lemmas_file = open('openCorporaLemmas.txt', 'r', encoding='utf8')
for line in lemmas_file:
    items = line.strip('\n').split()
    lemma_id = int(items[0])
    lemma = items[1]
    POS = items[2]
    if POS in tags:
        POS = tags[POS]
    lemmas[lemma_id] = [lemma, POS]
lemmas_file.close()
