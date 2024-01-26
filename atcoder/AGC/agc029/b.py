from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

candidates = []
for i in range(1, 32):
    candidates.append(2**i)
candidates.sort(reverse=True)

counter = defaultdict(int)
for i in range(n):
    counter[a[i]] += 1

ans = 0
a.sort(reverse=True)
for ai in a:
    if counter[ai] == 0:
        continue
    for ci in candidates:
        bi = ci - ai
        if bi < 1:
            continue
        if ai == bi:
            cnt = counter[ai] // 2
            ans += cnt
            counter[ai] -= cnt * 2
        elif counter[bi] > 0 and counter[ai] > 0:
            counter[ai] -= 1
            counter[bi] -= 1
            ans += 1

print(ans)
