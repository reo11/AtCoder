s = str(input())
k = int(input())

for _ in range(k):
    s = s[1:] + s[0]

print(s)
