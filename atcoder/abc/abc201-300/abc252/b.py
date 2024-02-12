n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = set(b)

max_a = max(a)
ab = []
flag = True

for i, ai in enumerate(a, start=1):
    print(i, ai)
    if ai == max_a and i in b:
        flag = False
        break
if flag:
    print("No")
else:
    print("Yes")
