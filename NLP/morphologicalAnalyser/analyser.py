import re
from desambiguatorFromPreparedFile import lemmas_freq_POS

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
                lemma_id = self.dictionary[first_letter][word]
                lemma_tag = self.lemmas[lemma_id]
                lemma = lemma_tag[0]
                tag = lemma_tag[1]
            else:
                if word in lemmas_freq_POS:
                    tag = lemmas_freq_POS[word]
                else:
                    # если слово нигде не найдено, в лемму записываю его форму, а тег = сущ.
                    tag = 'A'
                lemma = word
            result += word_trueCase + "{" + lemma + "=" + tag + "} "

        return result.strip()



