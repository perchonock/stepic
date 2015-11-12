def fib_num(n):
    fibonacci_nums = [0,1]
    i = 2
    while len(fibonacci_nums) <= n:
        current_num = fibonacci_nums[i-1] + fibonacci_nums[i-2]
        fibonacci_nums.append(current_num)
        i += 1
    return fibonacci_nums[n]

def last_figure(n):
    last_figures = [0,1]
    for i in range(n-1):
        current_num_figure = (last_figures[0] + last_figures[1])%10
        last_figures.append(current_num_figure)
        last_figures.pop(0)
    return last_figures[1]

def fib_mod(n,m):
    mods = [0,1]
    k=2
    if n > 1:
        for i in range(2,n+1):
            current_num_mod = (mods[i-1] + mods[i-2])%m
            mods.append(current_num_mod)
            if mods[i-1] == 0 and mods[i] == 1:
                return mods[(n%(k))]
            k=i
        else:
            return mods[-1]
n=2345
m=8
print(fib_mod(n,m))

print(fib_num(n)%m)



