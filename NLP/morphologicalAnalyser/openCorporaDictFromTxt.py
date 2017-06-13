dict_file = open('dict4test.txt', 'r', encoding='utf8')
text = dict_file.read()
forms_str = text.split('\n\n')
dictionary = dict()
lemmas = dict()

for f in forms_str:
    elements = f.split('\n')
    lemma_id = elements[0]
    if lemma_id in
    forms_gram = elements[1].split('\t')
    lemma = forms_gram[0]
    POS = forms_gram[1].split(',')[0]
    lemmas[lemma_id] = [lemma, POS]

    if len(elements) > 2:
        for el in elements[2:]:
            forms_gram = el.split('\t')
            form = forms_gram[0]
            dictionary[form] = lemma_id

dict_file.close()

print(dictionary)
print(lemmas)
