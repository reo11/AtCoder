n = int(input())

ab = []

for i in range(n):
    a, b = map(int, input().split())
    a = b - a
    ab.append([a, b])

ab.sort(key=lambda x: (x[1], x[0]))

flag = True
time = 0
for i in range(n):
    a, b = ab[i]
    time += b - a
    if time > b:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
