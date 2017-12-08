import json
from gensim.summarization import summarize


in_file = open('dataset_43428_1.txt', 'r', encoding='utf8')
out_file = open('dataset_43428_1_gensim.txt', 'w', encoding='utf8')
file = in_file.read()

texts = json.loads(file)
summas = []
for text in texts:
    #print('ТЕКСТ \n', text)
    try:
        summa = summarize(text, word_count=50)
    except:
        summa = text

    summas.append(summa)

json.dump(summas, out_file, ensure_ascii=False, separators=(",\n"), indent=4)


#out_file.write(out_str)
in_file.close()
out_file.close()