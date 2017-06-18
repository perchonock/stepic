import openCorporaDictFromPreparedFile
from analyser import Analyser
dictionary = openCorporaDictFromPreparedFile.dictionary
lemmas = openCorporaDictFromPreparedFile.lemmas
myanalyser = Analyser(dictionary, lemmas)

#text = 'Стала стабильнее экономическая и политическая обстановка, предприятия вывели из тени зарплаты сотрудников. Все Гришины одноклассники уже побывали за границей, он был чуть ли не единственным, кого не вывозили никуда дальше Красной Пахры.'
file2parse = open('dataset_37845_1.txt', 'r', encoding='utf8')
result_file = open('result.txt', 'w', encoding='utf8')

for line in file2parse:
    result = myanalyser.analyse(line.strip('\n'))
    result_file.write(result + '\n')

file2parse.close()
result_file.close()

#text = 'виновный посол напомнил после о столе'
#text = 'мой друг говорит с сестрой о море'
#result = myanalyser.analyse(text)
#print(result)

