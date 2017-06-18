import operator
file = open('POS_stat.txt', 'r', encoding='utf8')
lemma__totalfreq_POS_freq = dict()
for line in file:
    items = line.strip('\n').split()
    if len(items) == 2:
        pos_freq = items[1].split(':')
        lemma__totalfreq_POS_freq[items[0]] = [int(pos_freq[1]), pos_freq[0]]
    else:
        temp = {}
        total_freq = 0
        for i in items[1:]:
            pos_freq = i.split(':')
            temp.update({pos_freq [0]: int(pos_freq [1])})
            total_freq += int(pos_freq[1])
        max_el = max(temp.items(), key=operator.itemgetter(1))[0]
        lemma__totalfreq_POS_freq[items[0]] = [total_freq, max_el]

file.close()

#print(lemma__totalfreq_POS_freq)
