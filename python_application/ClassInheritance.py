classes = {}
#nodes = []

n = int(input())
for i in range(n):
    str = input()
    #nodes.extend(str.split())
    if ":" in str:
        lst = str.split(':')
        classes[lst[0].strip()] = lst[1].split()
    else:
        classes[str] = []

def isparent(parent, child):
    global status
    #if child not in nodes or parent not in nodes:
    #    return
    if child == parent:
        status = 'Yes'
    elif child in classes:
        if parent in classes[child]:
            status = "Yes"
        else:
            for cl in classes[child]:
                if cl in classes:
                    isparent(parent,cl)

k = int(input())
for i in range(k):
    lst = input().split()
    status = 'No'
    isparent(lst[0],lst[1])
    print(status)






