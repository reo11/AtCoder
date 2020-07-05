from math import log10
n, k = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10**9+7
a.sort()

cnt_neg = 0
cnt_pos = 0
for i in a:
   if i <= 0:
      cnt_neg += 1
   else:
      cnt_pos += 1
is_minus = False
k_tmp = k
while k_tmp > 0:
   if k_tmp >= 2:
      if cnt_neg >= 2:
         cnt_neg -= 2
      elif cnt_pos >= 2:
         cnt_pos -= 2
      else:
         is_minus = True
         break
      k_tmp -= 2
   else:
      if cnt_pos > 0:
         cnt_pos -= 1
         k_tmp -= 1
      else:
         is_minus = True
         break

k_1 = k
ans1 = 1
l = 0
r = n - 1
if k_1 % 2:
   ans1 *= a[-1]
   r -= 1
   k_1 -= 1
while k_1 >= 2:
   if a[l] * a[l+1] > a[r-1] * a[r]:
      ans1 *= a[l] * a[l+1]
      l += 2
   else:
      ans1 *= a[r-1] * a[r]
      r -= 2
   k_1 -= 2
   ans1 %= MOD

a.sort(key=abs)
# print(a)
ans2 = 1
for i in a[:k]:
   ans2 *= i
   ans2 %= MOD

if is_minus:
   print(ans2)
else:
   print(ans1)