import operator
#string = input()

def Encode(string):
    tree = []
    code = dict()
    for char in string:
        if char not in code:
            f = string.count(char)
            tree.append([char,f])
            code[char] = ""
    tree.sort(key = operator.itemgetter(1), reverse=True)
    if len(tree) == 1:
        code[tree[0][0]] = '0'
    else:
        while len(tree)>1:
            for sign in tree[-1][0]:
                    code[sign] += '0'
            for sign in tree[-2][0]:
                    code[sign] += '1'
            tree[-2][1] += tree[-1][1]
            tree[-2][0] += tree[-1][0]
            tree.pop()
            tree.sort(key = operator.itemgetter(1), reverse=True)
    for c in code:
        code[c] = code.get(c)[::-1]
    encoded = ''
    for char in string:
        encoded += code.get(char)

    print(len(set(string)), len(encoded))
    for key, value in code.items():
        print(key + ": " + value)
    print(encoded)

    return len(set(string)), len(encoded), code


#inp = input()
input = "4 14\na: 0\nb: 10\nc: 110\nd: 111\n01001100100111"
input = input.splitlines()
input = input[1:]
string = input.pop()
code = dict()
for i in input:
    items = i.split(": ")
    code[items[1]] = items[0]

def Decode(string, code):
    tmp = ''
    decoded_string = ''
    for char in string:
        tmp += char
        if tmp in code:
            decoded_string += code[tmp]
            tmp = ''
    print(decoded_string)

Decode(string,code)


