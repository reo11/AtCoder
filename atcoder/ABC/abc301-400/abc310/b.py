n, m = map(int, input().split())
pcf = []
for _ in range(n):
    pcf_i = list(map(int, input().split()))
    p = pcf_i[0]
    c = pcf_i[1]
    f = set(pcf_i[2:])
    pcf.append([p, c, f])


flag = False
for i in range(n):
    pi = pcf[i][0]
    fi_set = pcf[i][2]
    for j in range(n):
        if i == j:
            continue
        pj = pcf[j][0]
        fj_set = pcf[j][2]

        over_lap = fi_set - fj_set
        plus = fj_set - fi_set
        if (pj < pi and len(over_lap) == 0) or (
            pj <= pi and len(over_lap) == 0 and len(plus) > 0
        ):
            flag = True
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")
