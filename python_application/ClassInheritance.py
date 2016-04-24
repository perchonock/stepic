classes = {}

n = int(input())
for i in range(n):
    str = input()
    if ":" in str:
        lst = str.split(':')
        classes[lst[0].strip()] = lst[1].split()
    else:
        classes[str] = []

def isparent(parent,child):
    if child == parent:
        print('Yes')

    elif child in classes:
        if parent in classes[child]:
            print("Yes")

        else:
            for child1, parents in classes.items():
                if parent in parents:
                    isparent(child1,child)
                    return
            print('No')

    else:
        print('No')


print(classes)

k = int(input())
for i in range(k):
    lst = input().split()
    isparent(lst[0],lst[1])




