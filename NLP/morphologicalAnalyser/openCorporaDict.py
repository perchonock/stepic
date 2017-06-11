from bs4 import BeautifulSoup

dict_file = open('dict.opcorpora.xml', 'r', encoding='utf8')
#dict_file = open('dict4test.xml', 'r', encoding='utf8')
lemmas = dict()
dictionary = dict()
links = dict()
soup = BeautifulSoup(dict_file, "xml")

links_str = soup.find_all('link')
for k in links_str:
    derivative = int(k['to'])
    inicial = int(k['from'])
    links[derivative] = inicial

print(links)
lemmas_str = soup.find_all('lemma')

for i in lemmas_str:
    lemma_id = int(i['id'])
    lemma = i.l['t']
    POS = i.l.g['v']
    lemmas[lemma_id] = [lemma, POS]
    forms_str = i.find_all('f')
    for j in forms_str:
        form = j['t']
        if lemma_id in links:
            dictionary[form] = links[lemma_id]
        else:
            dictionary[form] = lemma_id

dict_file.close()

print(dictionary)
print(lemmas)