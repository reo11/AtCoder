t = list(input())

for i in range(len(t)):
    if t[i] == '?':
        t[i] = 'D'

print("".join(t))