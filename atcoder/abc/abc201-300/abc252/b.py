n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = set(b)

max_a = max(a)
ab = []
flag = False

for i, ai in enumerate(a, start=1):
    if ai == max_a and i in b:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
