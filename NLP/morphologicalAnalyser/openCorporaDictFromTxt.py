import re
dict_file = open('dict4test.txt', 'r', encoding='utf8')
text_raw = dict_file.read()
text = re.sub(r'ё', 'е', text_raw)
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
    lemma_id = int(elements[0])
    if lemma_id in links:
        lemma_id = links[lemma_id]
    forms_gram = elements[1].split('\t')
    lemma = forms_gram[0].lower()
    POS = forms_gram[1].split(',')[0]
    lemmas[lemma_id] = [lemma, POS]
    dictionary[lemma] = lemma_id
    if len(elements) > 2:
        for el in elements[2:]:
            forms_gram = el.split('\t')
            form = forms_gram[0].lower()
            dictionary[form] = lemma_id



print(dictionary)
print(lemmas)
