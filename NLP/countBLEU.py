import math

def get_bigrams(sentence):
    words = sentence.split()
    bigrams = []
    for i in range(len(words)-1):
        bigrams.append(words[i] + " " + words[i+1])
    return bigrams


def count_bleu2(s, r1, r2):
    s_uni = s.split()
    s_bi = get_bigrams(s)
    s_len = len(s_uni)

    r1_uni = r1.split()
    r1_bi = get_bigrams(r1)
    r1_len = len(r1_uni)

    r2_uni = r2.split()
    r2_bi = get_bigrams(r2)
    r2_len = len(r2_uni)

    ref_uni = set(r1_uni)
    ref_uni.update(r2_uni)

    ref_bi = set(r1_bi)
    ref_bi.update(r2_bi)

    if abs(r1_len-s_len) > abs(r2_len-s_len):
        ref_len = r2_len
    elif abs(r1_len-s_len) < abs(r2_len-s_len):
        ref_len = r1_len
    else:
        if r1_len < r2_len:
            ref_len = r1_len
        else:
            ref_len = r2_len


    BP = min(1, s_len/ref_len)
    #print(s_len)
    #print(r1_len)
    #print(r2_len)
    #print(BP)

    def intersect(s, ref):
        count = 0
        for el in s:
            if el in ref:
                count += 1
                print(el)
        return count
    a1 = intersect(s_uni, ref_uni)
    print('пересечение униграм =', a1)
    a2 = len(s_uni)
    print("кол-во слов в МТ переводе =", a2)
    a = a1/a2
    b1 = intersect(s_bi, ref_bi)
    print("пересечение биграм =", b1)
    b2 = len(s_bi)
    print('кол-во биграм в МТ переводе =', b2)
    b = b1/b2
    sq = math.sqrt(a * b)
    print(a)
    print(b)
    print(sq)

    bleu = sq * BP

    return bleu


r1 = 'назовите меня каким угодно инструментом вы хоть и можете меня терзать но играть на мне не можете'
r2 = 'объявите меня каким угодно инструментом вы можете расстроить меня но играть на мне нельзя'

s6 = 'назови меня каким угодно инструментом ты можешь меня расстроить но не играть на мне'
s3 = 'позвони мне на каком инструменте вы будете хотя вы можете беспокоиться меня но вы не можете играть на мне'
s2 = 'назовите меня какой инструмент вы будете хотя вы можете раздражать меня все же вы не можете играть на меня'
s5 = 'назовите мне какой инструмент вы хотите хотя можете меня беспокоить но вы не можете играть на меня'
s4 = 'считай меня чем тебе угодно ты можешь мучить меня но не играть мною'
s1 = 'позвони мне какой инструмент ты будешь хотя ты можешь меня волновать но ты не можешь играть на меня'

print('s1', count_bleu2(s1, r1, r2))
#print('s2', count_bleu2(s2, r1, r2))
#print('s3', count_bleu2(s3, r1, r2))
#print('s4', count_bleu2(s4, r1, r2))
#print('s5', count_bleu2(s5, r1, r2))
#print('s6', count_bleu2(s6, r1, r2))

#print(sorted([count_bleu2(s1, r1, r2), count_bleu2(s2, r1, r2), count_bleu2(s3, r1, r2), count_bleu2(s4, r1, r2), count_bleu2(s5, r1, r2), count_bleu2(s6, r1, r2)]))