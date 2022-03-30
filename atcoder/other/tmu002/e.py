from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

MOD = 10**9 + 7
n, m = map(int, input().split())

def fact(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

l = fact(m)
ans = 1

if l[0][0] == 1 and len(l) == 1:
    print(1)
    exit()

for i in range(len(l)):
    b = l[i][1]
    ans *= cmb(b+n-1, b)
    ans %= MOD

print(ans)