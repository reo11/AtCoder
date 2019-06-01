import itertools
n, m = map(int, input().split())
input_set = []
for _ in range(m):
    x, y = map(int, input().split())
    input_set.append((x, y))
input_set = set(input_set)
ans = 0
for i in range(2**n):
    size = 0
    l = []
    for bit in range(n):
        if i & 2**bit > 0:
            size += 1
            l.append(bit+1)
    if len(l) < 2:
        ans = max(ans, 1)
    else:
        flag = True
        for s in set(itertools.permutations(l, 2)):
            if not(s in input_set or (s[1], s[0]) in input_set):
                flag = False
                break
        if flag:
            ans = max(ans, size)
print(ans)
