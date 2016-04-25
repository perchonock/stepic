classes = {}
nodes = []

n = int(input())
for i in range(n):
    str = input()
    nodes.extend(str.split())
    if ":" in str:
        lst = str.split(':')
        classes[lst[0].strip()] = lst[1].split()

    else:
        classes[str] = []


def isparent(parent,child):
    if child not in nodes or parent not in nodes:
        print('No')
        return
    if child == parent:
        print('Yes')
    elif child in classes:
        if parent in classes[child]:
            print("Yes")

        else:
            for cl in classes[child]:
                if cl in classes:
                    isparent(parent,cl)
                    return
            print('No')
    else:
        print("No")

#print(classes)

k = int(input())
for i in range(k):
    lst = input().split()
    isparent(lst[0],lst[1])






