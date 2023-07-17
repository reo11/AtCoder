l = int(input())

# (l - 1)C11

ans = 1
for i in range(1, 12):
    ans *= l - i

for i in range(1, 12):
    ans //= i
print(ans)
