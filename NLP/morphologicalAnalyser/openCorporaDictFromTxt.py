import re
#dict_file = open('dict4test.txt', 'r', encoding='utf8')
dict_file = open('dict.opcorpora.txt', 'r', encoding='utf8')
text = dict_file.read()
dict_file.close()
forms_str = text.split('\n\n')
dictionary = dict()
lemmas = dict()
links = dict()

links_file = open('openCorporaLinks.txt', 'r', encoding='utf8')
for line in links_file:
    ids = line.strip('\n').split()
    links[int(ids[0])] = int(ids[1])

links_file.close()

for f in forms_str:
    elements = f.split('\n')
    try:
        lemma_id = int(elements[0])
        forms_gram = elements[1].split('\t')
        lemma = forms_gram[0].lower()
        POS = forms_gram[1].split(',')[0]
        lemmas[lemma_id] = [lemma, POS]
        if lemma_id in links:
            lemma_id = links[lemma_id]
        if lemma not in dictionary:
            dictionary[lemma] = {lemma_id}
        else:
            dictionary[lemma].add(lemma_id)
        if len(elements) > 2:
            for el in elements[2:]:
                forms_gram = el.split('\t')
                form = forms_gram[0].lower()
                if form not in dictionary:
                    dictionary[form] = {lemma_id}
                else:
                    dictionary[form].add(lemma_id)
    except:
        pass


openCorporaDict = open('openCorporaDict.txt', 'w', encoding='utf8')
openCorporaLemmas = open('openCorporaLemmas.txt', 'w', encoding='utf8')

def dictsIntoFile(dictionary, lemmas):
    for key, value in dictionary.items():
        values = [str(i) for i in value]
        s = key + ' ' + " ".join(values) + '\n'
        openCorporaDict.write(s)

    for key, value in lemmas.items():
        s = str(key) + ' ' + " ".join(value) + '\n'
        openCorporaLemmas.write(s)

dictsIntoFile(dictionary, lemmas)

openCorporaDict.close()
openCorporaLemmas.close()
