from collections import defaultdict

counter = defaultdict(int)

s = list(input())

for si in s:
    counter[si] += 1

ans = [-1, ""]
for i in range(26):
    si = chr(ord("a") + i)
    cnt = counter[si]
    if ans[0] < cnt:
        ans = [cnt, si]
print(ans[1])
