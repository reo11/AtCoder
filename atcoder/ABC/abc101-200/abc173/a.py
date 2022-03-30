n = int(input())
ans = (1000 - (n % 1000))
if ans == 1000:
   print(0)
else:
   print(ans)