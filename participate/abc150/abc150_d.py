from functools import reduce
from math import ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

start = 0
a_max = a[-1]
while a_max * (start + 0.5) <= m:
    flag = True
    for i in range(len(a)-1):
        num = (a_max * (start + 0.5) / a[i]) - 0.5
        if num.is_integer():
            continue
        else:
            flag = False
            break
    if flag:
        break
    else:
        start += 1

if a_max * (start + 0.5) > m:
    print(0)
    exit()

ans = 0
base_num = int(a_max * (start + 0.5))

d = reduce(lcm, a)
ans = int(1 + ((m - base_num) // d))
print(ans)


