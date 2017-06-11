from bs4 import BeautifulSoup
openCorporaDict = open('openCorporaDict.txt', 'w', encoding='utf8')
openCorporaLemmas = open('openCorporaLemmas.txt', 'w', encoding='utf8')
openCorporaLinks = open('openCorporaLinks.txt', 'w', encoding='utf8')

class OpenCorporaDict:
    def __init__(self, file):
        self.file = file
        self.lemmas = dict()
        self.dictionary = dict()
        self.links = dict()
        self.soup = BeautifulSoup(file, "xml")
        self.tags = {'NOUN': 'S', 'ADJF': 'A', 'ADJS': 'A', 'COMP': 'A', 'VERB': 'V', 'INFN': 'V', 'PRTF': 'V', 'PRTS': 'V',
                'GRND': 'V', 'NUMR': 'ADV', 'ADVB': 'ADV', 'NPRO': 'S', 'PRED': 'ADV', 'PREP': 'PR', 'CONJ': 'CONJ',
                'PRCL': 'ADV', 'INTJ': 'ADV'}

    def create_dict(self):
        links_str = self.soup.find_all('link')
        for k in links_str:
            derivative = int(k['to'])
            inicial = int(k['from'])
            #self.links[derivative] = inicial
            openCorporaLinks.write(str(derivative) + ' ' + str(inicial) + '\n')

        lemmas_str = self.soup.find_all('lemma')
        for i in lemmas_str:
            lemma_id = int(i['id'])
            lemma = i.l['t']
            POS = i.l.g['v']
            if POS in self.tags:
                POS = self.tags[POS]
            #self.lemmas[lemma_id] = [lemma, POS]
            openCorporaLemmas.write(str(lemma_id) + ' ' + lemma + ' ' + POS + '\n')
            forms_str = i.find_all('f')
            for j in forms_str:
                form = j['t']
                # if form not in self.dictionary:
                #     if lemma_id in self.links:
                #         self.dictionary[form] = [self.links[lemma_id]]
                #     else:
                #         self.dictionary[form] = [lemma_id]
                # else:
                #     if lemma_id in self.links:
                #         self.dictionary[form].append(self.links[lemma_id])
                #     else:
                #         self.dictionary[form].append(lemma_id)
            openCorporaDict.write(form + ' ' + str(lemma_id) + '\n')

dict_file = open('dict.opcorpora.xml', 'r', encoding='utf8')
#dict_file = open('dict4test.xml', 'r', encoding='utf8')

mydict = OpenCorporaDict(dict_file)
dict_file.close()
mydict.create_dict()
dictionary = mydict.dictionary
lemmas = mydict.lemmas
links = mydict.links

def dictsIntoFile(dictionary, lemmas, links):
    for key, value in dictionary.items():
        s = key + ' ' + str(value) + '\n'
        openCorporaDict.write(s)

    for key, value in lemmas.items():
        s = str(key) + ' ' + " ".join(value) + '\n'
        openCorporaLemmas.write(s)

    for key, value in links.items():
        s = str(key) + ' ' + str(value)
        openCorporaLinks.write(s)

openCorporaLinks.close()
openCorporaDict.close()
openCorporaLemmas.close()