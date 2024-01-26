n, m = map(int, input().split())
k = []
for i in range(m):
    k.append(list(map(int, input().split())))
p = list(map(int, input().split()))
count = 0
for i in range(2**n):
    flag = True
    for q_idx, query in enumerate(k):
        count_p = 0
        for q in query[1:]:
            if (i & 2 ** (q - 1)) > 0:
                count_p += 1
        if count_p % 2 != p[q_idx]:
            flag = False
    if flag:
        count += 1
print(count)
