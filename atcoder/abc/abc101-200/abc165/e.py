n, m = map(int, input().split())

s1 = 1
f1 = n // 2
s2 = f1 + 1
f2 = n
if (f1 - s1) % 2 == (f2 - s2) % 2:
    f2 -= 1
ans = []
while f1 > s1:
    ans.append(f"{s1} {f1}")
    s1 += 1
    f1 -= 1

while f2 > s2:
    ans.append(f"{s2} {f2}")
    s2 += 1
    f2 -= 1

print("\n".join(ans[:m]))
