from bs4 import BeautifulSoup

file = open('annot.opcorpora.no_ambig.xml', 'r', encoding='utf8')
#file = open('test.xml', 'r', encoding='utf8')

soup = BeautifulSoup(file, "xml")
lemmas_str = soup.find_all('l')
lemmas = dict()
tags = {'NOUN': 'S', 'ADJF': 'A', 'ADJS': 'A', 'COMP': 'A', 'VERB': 'V', 'INFN': 'V', 'PRTF': 'V', 'PRTS': 'V', 'GRND': 'V', 'NUMR': 'ADV', 'ADVB': 'ADV', 'NPRO': 'S', 'PRED': 'ADV', 'PREP': 'PR', 'CONJ': 'CONJ', 'PRCL': 'ADV', 'INTJ': 'ADV'}

for i in lemmas_str:
    lemma = i['t']
    POS = i.g['v']
    if POS == 'PNCT':
        continue
    try:
        POS = tags[POS]
        if lemma not in lemmas:
            lemmas[lemma] = {POS: 1}
        else:
            if POS in lemmas[lemma]:
                lemmas[lemma][POS] += 1
            else:
                lemmas[lemma].update({POS: 1})
    except:
        pass

result_file = open('POS_stat.txt', 'w', encoding='utf8')
for key, value in lemmas.items():
    s = key + ' '
    for key2, value2 in value.items():
        s += key2 + ':' + str(value2) + ' '
    s = s.strip()
    s += '\n'
    result_file.write(s)

file.close()
result_file.close()