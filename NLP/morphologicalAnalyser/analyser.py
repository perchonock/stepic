import re
from desambiguatorFromPreparedFile import lemma__totalfreq_POS_freq
import operator

class Analyser:
    def __init__(self, dictionary, lemmas):
        self.dictionary = dictionary
        self.lemmas = lemmas

    def preproccess(self, text):
        #GROUPING_SPACE_REGEX = re.compile('([^\w_-]|[+])', re.U)
        #words = [t for t in GROUPING_SPACE_REGEX.split(text)
        #            if t and not t.isspace()]
        words = re.sub('\W', ' ', text).split() #нужно чтобы по тире не разбивало
        return words

    def analyse(self, text):
        words = self.preproccess(text)
        result = ''
        for word in words:
            word_trueCase = word
            word = word.lower()
            if 'ё' in word:
                word = re.sub(r'ё', 'е', word)
            first_letter = word[0]
            if word in self.dictionary[first_letter]:
                #print(word)
                #print(self.dictionary[first_letter][word])
                lngth = len(self.dictionary[first_letter][word])
                if lngth == 1:
                    for i in self.dictionary[first_letter][word]:
                        lemma_id = i
                    #print('lemma_id ', lemma_id)
                    lemma_tag = self.lemmas[lemma_id]
                    #print('lemma_tag', lemma_tag)
                    lemma = lemma_tag[0]
                    tag = lemma_tag[1]
                elif lngth > 1:
                    temp = {}
                    for lemma_id in self.dictionary[first_letter][word]:
                        lemma_tag = self.lemmas[lemma_id]
                        lemma = lemma_tag[0]
                        if lemma in lemma__totalfreq_POS_freq:
                            freq = int(lemma__totalfreq_POS_freq[lemma][0])
                            tag = lemma__totalfreq_POS_freq[lemma][1]
                        else:
                            freq = 0
                            tag = lemma_tag[1]
                        temp[freq] = [lemma, tag]
                    #print('temp = ', temp)
                    max_freq = max(temp.keys())
                    #print('max_freq = ', max_freq)
                    lemma = temp[max_freq][0]
                    #print('lemma = ', lemma)
                    tag = temp[max_freq][1]
                    #print('tag = ', tag)
            else:
                #закомментированный блок нужен для разрешения омонимии при использовании одикт
                #if word in lemmas_freq_POS:
                #    tag = lemmas_freq_POS[word]
                #else:
                # если слово нигде не найдено, в лемму записываю его форму, а тег = сущ.
                tag = 'S'
                lemma = word
            result += word_trueCase + "{" + lemma + "=" + tag + "} "

        return result.strip()



