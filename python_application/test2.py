a = [i + 1 for i in range(4)]
b = [i for i in range(4)]
c = [i for i in range(5)][1:]
d = list(i + 1 for i in range(4))

print(a)
print(b)
print(c)
print(d)