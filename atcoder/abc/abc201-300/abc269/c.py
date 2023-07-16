import itertools

n = int(input())

l = []
for i in range(61):
    if n % 2:
        l.append(i)
    n = n // 2

ans = [0]
for i in range(1, len(l) + 1):
    for v in itertools.combinations(l, i):
        ans_num = 0
        for num in v:
            ans_num += 2 ** num
        ans.append(ans_num)
ans.sort()
for v in ans:
    print(v)
