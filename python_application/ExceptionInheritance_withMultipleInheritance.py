n = int(input())
exceptions = {}

for i in range(n):
    str = input()
    if ":" in str:
        lst = str.split(':')
        exceptions[lst[0].strip()] = lst[1].split()
    else:
        exceptions[str] = []


def isparent(parent, child):
    global status
    if child == parent:
        status = True
    elif child in exceptions:
        if parent in exceptions[child]:
            status = True
        else:
            for cl in exceptions[child]:
                if cl in exceptions:
                    isparent(parent,cl)

proccessedExceptions = []
redundantExceptions = []

m = int(input())

for k in range(m):
    exc = input()
    status = False
    for proc_exc in proccessedExceptions:
        isparent(proc_exc, exc)
        if status == True:
            redundantExceptions.append(exc)
    proccessedExceptions.append(exc)

used = []
for key in redundantExceptions:
    if key not in used:
        print(key)
        used.append(key)





