from desambiguatorFromPreparedFile import lemmas_freq_POS

class OdictBasedDictionary:
    def __init__(self, file):
        self.file = file
        self.dictionary = dict()
        self.lemmas = dict()
        self.tags = {'мо-жо': 'S', 'мс-п': 'A', 'вводн.': 'ADV', 'жо': 'S', 'п': 'A', 'мо': 'S', 'предик.': 'ADV',
                'предл.': 'PR', 'межд.': 'ADV', 'св': 'V', 'мн.': 'S', 'с': 'S', 'св-нсв': 'V', 'част.': 'ADV',
                'сравн.': 'A', 'нсв': 'V', 'м': 'S', 'числ.-п': 'ADV', 'числ.': 'ADV', 'со': 'S', 'союз': 'CONJ', 'ж': 'S', 'н': 'ADV'}

        for letter in 'абвгдежзийклмнопрстуфхцчшщыэюя':
            self.dictionary[letter] = dict()

        self.count = 1

    def createDict(self):
        for line in self.file:
            words = line.lower().strip(',\n').split(',')
            lemma = words[0]
            if lemma in lemmas_freq_POS:
                tag = lemmas_freq_POS[lemma]
            else:
                tag = self.tags[words[1]]

            lemma_id = self.count
            self.count += 1
            self.lemmas[lemma_id] = [lemma, tag]
            first_letter = words[0][0].lower()
            try:
                self.dictionary[first_letter].update({lemma: lemma_id})
                if len(words) > 2:
                    #Добавить условие, что если словоформа уже есть и у нее  другая лемма, то добавлять еще одну лемму
                    for word in words[2:]:
                        first_letter = word[0].lower()
                        self.dictionary[first_letter].update({word: lemma_id})
            except:
                pass

dict_file = open('odict.csv', 'r', encoding='utf8')
mydict = OdictBasedDictionary(dict_file)
mydict.createDict()
dictionary = mydict.dictionary
lemmas = mydict.lemmas
dict_file.close()


