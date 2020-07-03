a, b, c = map(int, input().split())
if a % 2 or b % 2 or c % 2:
   print(0)
   exit()
if a == b == c:
   print(-1)
   exit()

cnt = 0
while True:
   if a % 2 or b % 2 or c % 2:
      break
   cnt += 1
   next_a = b // 2 + c // 2
   next_b = a // 2 + c // 2
   next_c = a // 2 + b // 2
   a = next_a; b = next_b; c = next_c
print(cnt)