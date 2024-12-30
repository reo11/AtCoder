h = int(input())

x = 0
ans = 0
for i in range(10000):
    x += 2**i
    if x > h:
        ans = i + 1
        break
print(ans)