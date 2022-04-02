s = input()
a = list(map(int, input().split()))

ans = ""
if a[0] == 0:
    ans = '"'
    a.pop(0)
for i, c in enumerate(s, start=1):
    ans += c
    if len(a) > 0:
        if a[0] == i:
            ans += '"'
            a.pop(0)
print(ans)
