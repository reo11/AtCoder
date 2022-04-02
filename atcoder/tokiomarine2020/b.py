a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if a == b:
    print("YES")
    exit()
if v <= w:
    print("NO")
    exit()

if abs(a - b) / abs(w - v) <= t:
    print("YES")
else:
    print("NO")
