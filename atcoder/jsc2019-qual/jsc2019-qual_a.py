M, D = map(int, input().split())
count = 0
for m in range(1, M+1):
    for d in range(1, D+1):
        d10 = d // 10
        d1 = d - (d10*10)
        if d10 >= 2 and d1 >= 2 and d1*d10 == m:
            count += 1
print(count)