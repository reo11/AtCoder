s = str(input())
k = int(input())

for i in range(k):
    s = s[1:] + s[0]

print(s)
