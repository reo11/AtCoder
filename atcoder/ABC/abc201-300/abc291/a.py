s = list(input())
ans = 0
for i, c in enumerate(s, start = 1):
    if ord(c) < ord('a'):
        ans = i
        break
print(ans)