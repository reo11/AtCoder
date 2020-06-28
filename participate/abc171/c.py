n = int(input())

i = 1
ans = []
while n > 0:
   v = (n % (26 ** i)) // (26 ** (i-1))
   if v == 0:
      ans.append('z')
      n -= (26 ** i)
      i += 1
   else:
      ans.append(chr(ord('a') + v - 1))
      n -= n % (26 ** i)
      i += 1
print("".join(reversed(ans)))
