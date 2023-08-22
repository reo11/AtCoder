s = list(input())
s += ["0"]
t = list(input())

for i in range(1, len(t) + 1):
    if s[i-1] != t[i-1]:
        print(i)
        exit()