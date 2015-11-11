input0 = "3"
input = int(input0)

def get_fib_num(n):
    fibonacci_nums = [0,1]
    i = 2
    while len(fibonacci_nums) <= n:
        current_num = fibonacci_nums[i-1] + fibonacci_nums[i-2]
        print(current_num)
        fibonacci_nums.append(current_num)
        print(fibonacci_nums)
        i += 1
    return fibonacci_nums[n]

print(get_fib_num(input))




