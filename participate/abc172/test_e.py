# N <= M < 10くらいを考える
from itertools import permutations
n, m = map(int, input().split())

cnt = 0

for i, a in enumerate(permutations(range(1, m+1), n)):
   t = 0
   for b in permutations(range(1, m+1), n):
      f = True
      for i in range(n):
         if a[i] == b[i]:
            f = False
            break
      if f:
         t += 1
         cnt += 1
   # if i == 0:
   #    print(t)
print(cnt)