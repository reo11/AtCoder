n, x = map(int, input().split())
s = list(input())

for s_i in s:
    if s_i == "o":
        x += 1
    else:
        x = max(0, x - 1)
print(x)
