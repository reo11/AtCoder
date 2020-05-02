f = False
k = int(input())
a, b = map(int, input().rstrip().split())
for i in range(a, b+1):
    if i % k == 0:
        f = True
if f:
    print("OK")
else:
    print("NG")