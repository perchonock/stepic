def NOD(a,b):
    while a !=0 and b != 0:
        if a > b:
            r = a%b
            a = r
        else:
            r = b%a
            b = r
    if a == 0:
        return b
    else:
        return a


print(NOD(49, 21))
