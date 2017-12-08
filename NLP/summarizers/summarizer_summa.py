#from summa.summarizer import summarize
import json
import codecs

in_file = codecs.open('dataset_43428_1.txt', 'r', encoding='utf8')

file = in_file.read()

print(json.loads(in_file))



in_file.close()