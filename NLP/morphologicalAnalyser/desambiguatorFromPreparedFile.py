import operator
file = open('POS_stat.txt', 'r', encoding='utf8')
lemmas_freq_POS = dict()
for line in file:
    items = line.strip('\n').split()
    if len(items) == 2:
        pos_freq = items[1].split(':')
        lemmas_freq_POS[items[0]] = pos_freq[0]
    else:
        temp = {}
        for i in items[1:]:
            pos_freq = i.split(':')
            temp.update({pos_freq [0]: int(pos_freq [1])})
        max_el = max(temp.items(), key=operator.itemgetter(1))[0]
        lemmas_freq_POS[items[0]] = max_el

file.close()
