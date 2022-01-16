n = str(input())

s = 0
for i in range(len(n)):
    s += int(n[i])

if s % 9 == 0:
    print("Yes")
else:
    print("No")