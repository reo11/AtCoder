s = str(input())
k = int(input())

tmp = s + s + s + s

c = [0]
for i in range(1, len(tmp)):
    if tmp[i] == tmp[i-1] and c[-1] == 0:
        c.append(1)
    else:
        c.append(0)

ans = 0

if k == 1:
    ans = sum(c[:len(s)])
elif k == 2:
    ans = sum(c[:2*len(s)])
else:
    if k % 2 == 1:
        ans = sum(c[:len(s)]) + sum(c[len(s):3*len(s)]) * (k - 1) // 2
    else:
        ans = sum(c[:len(s)]) + sum(c[len(s):3*len(s)]) * (k - 1) // 2 + sum(c[3*len(s):])
print(ans)
