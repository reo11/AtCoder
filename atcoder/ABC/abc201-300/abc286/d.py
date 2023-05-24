n, x = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
l = [0]

for a, b in ab:
    l = list(set(l))
    l.sort()
    l_len = len(l)
    for j in range(1, b + 1):
        add_num = a * j
        for i in range(l_len):
            if l[i] + add_num > x:
                break
            l.append(l[i] + add_num)
if x in l:
    print("Yes")
else:
    print("No")