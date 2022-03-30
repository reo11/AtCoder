s = input()
numbers = list(map(str, range(10)))

ans = ""
for c in s:
   if c in numbers:
      ans += c
print(ans)