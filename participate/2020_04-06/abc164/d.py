import sys
from collections import defaultdict
s = str(input())
n = len(s)
p = 2019

a = []
t = 1
for i in range(n-1, -1, -1):
    a.append((ord(s[i])-ord("0")) * t % p)
    t = t * 10 % p
cum = [0]
for v in a:
    cum.append((cum[-1] + v) % p)

dic = defaultdict(int)
ans = 0
for v in cum:
    ans += dic[v]
    dic[v] += 1
print(ans)
