from collections import defaultdict, deque
n = int(input())
s = [list(input()) for _ in range(n)]

# 各行列のoの数をあらかじめ数え上げる
# 基準点を決めて、その行のoの数と列のoの数を数える

counter = defaultdict(lambda: defaultdict(lambda: 0))
queue = deque()
for i in range(n):
    for j in range(n):
        if s[i][j] == "o":
            counter["c"][i] += 1
            counter["r"][j] += 1
            queue.append((i, j))
ans = 0
while queue:
    i, j = queue.popleft()
    ans += (counter["c"][i] - 1) * (counter["r"][j] - 1)
print(ans)
