n = int(input())
exceptions = {}

for i in range(n):
    str = input()
    if ":" in str:
        lst = str.split(':')
        exceptions[lst[0].strip()] = lst[1].strip()
    else:
        exceptions[str] = ''

proccessedExceptions = []
redundantExceptions = []
m = int(input())
for k in range(m):
    exc = input()
    #print(exc)
    #print(exceptions[exc])
    proccessedExceptions.append(exc)
    exc1 = exc
    try:
        while exceptions[exc1] != '':
            if exceptions[exc1] in proccessedExceptions:
                redundantExceptions.append(exc)
                break
            else:
                exc1 = exceptions[exc1]
    except KeyError:
        pass

for key in redundantExceptions:
    if redundantExceptions.count(key) == 1:
        print(key)
#print(exceptions)
#print(proccessedExceptions)


