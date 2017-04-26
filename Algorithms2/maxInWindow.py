#import sys
#input = sys.stdin.read()


def getMaxNaive(input):
    n = int(input.split('\n')[0])
    nums = [int(i) for i in input.split('\n')[1].split()]
    w = int(input.split('\n')[2])
    result = ''
    r = n-w+1
    for i in range(r):
        m = max(nums[i:(i+w)])
        result += str(m) + ' '

    return result.strip()

def getMax(input):
    n = int(input.split('\n')[0])
    nums = [int(i) for i in input.split('\n')[1].split()]
    w = int(input.split('\n')[2])

#sys.stdout.write(getMax(input))