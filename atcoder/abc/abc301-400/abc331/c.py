from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)

counter = defaultdict(int)
for ai in a:
  counter[ai] += 1

uniq_a = list(sorted(list(set(a))))

ans = defaultdict(int)
for ai in uniq_a:
  sum_a -= (ai * counter[ai])
  ans[ai] = sum_a

out = []
for ai in a:
  out.append(ans[ai])
print(*out, sep=" ")
