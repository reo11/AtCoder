from collections import defaultdict, deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 前処理でvが最後に登場する場所をメモしておく
memo = defaultdict(lambda: -1)

for i in range(n):
    memo[a[i]] = i


ans = [deque(), set()]

for i in range(n):
    a_i = a[i]
    if a_i in ans[1]:
        continue
    else:
        while True:
            if len(ans[0]) > 0 and ans[0][-1] > a_i and memo[ans[0][-1]] > i:
                ans[1].discard(ans[0][-1])
                ans[0].pop()
            else:
                break
        ans[0].append(a_i)
        ans[1].add(a_i)
print(*ans[0], sep=" ")
