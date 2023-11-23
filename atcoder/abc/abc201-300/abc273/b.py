from collections import deque
x, k = map(int, input().split())

ans = [0 for _ in range(16)]
for i, xi in enumerate(reversed(list(str(x)))):
    ans[i] += int(xi)

for i in range(len(ans) - 1):
    # 四捨五入
    if i <= k - 1:
        if ans[i] >= 5:
            ans[i + 1] += 1
        ans[i] = 0
    else:
        if ans[i] >= 10:
            ans[i + 1] += 1
            ans[i] %= 10

ans = deque(reversed(ans))
while len(ans) > 1 and ans[0] == 0:
    ans.popleft()

ans = ''.join(map(str, ans))
print(ans)