from collections import defaultdict

n = int(input())
p = list(map(int, input().split()))


def mex(array) -> int:
    array_set = set(array)
    n = len(array_set)
    for m in range(n + 1):
        if m in array_set:
            continue
        else:
            return m
    return n


# mex
# 先読みする
ans = []
last_ans = mex(p)
ans.append(last_ans)
counter = defaultdict(int)
for p_i in p:
    counter[p_i] += 1

for i in reversed(range(1, n)):
    counter[p[i]] -= 1
    if counter[p[i]] == 0:
        last_ans = min(last_ans, p[i])
    ans.append(last_ans)
ans.reverse()
print(*ans, sep="\n")
