from collections import Counter

n, k = map(int, input().split())
s = list(input())
s_sort = sorted(s)
t = ""

diff = 0
counter = Counter(s[:1])
counts = sum(counter.values())

for i in range(n):
    for c in s_sort:
        diff1 = diff + (c != s[i])
        diff2 = counts - (counter[c] > 0)

        if diff1 + diff2 <= k:
            t += c
            s_sort.remove(c)
            diff = diff1
            counter = Counter(s[: i + 2]) - Counter(t)
            counts = sum(counter.values())
            break
print(t)
