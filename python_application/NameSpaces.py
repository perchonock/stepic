spaces = {'global': [[],[]]}
def create(namespace,parent):
    spaces[parent][0].append(namespace)
    spaces[namespace] = [[],[]]

def add(namespace,variable):
    spaces[namespace][1].append(variable)

def get(namespace,variable):
    if variable in spaces[namespace][1]:
        print(namespace)
    else:
        for key, value in spaces.items():
            if namespace in value[0]:
                get(key,variable)
                return
        print('None')

n = int(input())
for i in range(n):
    lst = input().split()
    if lst[0] == 'add':
        add(lst[1],lst[2])
    elif lst[0] == 'create':
        create(lst[1],lst[2])
    elif lst[0] == 'get':
        get(lst[1],lst[2])

print(spaces)






