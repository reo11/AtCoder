# 9876543210 が最大
from collections import deque

k = int(input())

que = deque([])

for i in range(10):
    que.append([i])

ans = set()
while que:
    nums = que.popleft()
    ans.add(int("".join(list(map(str, nums)))))
    last_num = nums[-1]
    for i in range(last_num):
        que.append(nums + [i])
ans = sorted(list(ans))[1:]
print(ans[k - 1])
print(len(ans))
