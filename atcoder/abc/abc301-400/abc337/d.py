from collections import deque
INF = float('inf')
h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = INF
# 横方向探索
for i in range(h):
    q = deque()
    cost = 0
    for j in range(w):
        if len(q) < k:
            if s[i][j] == "x":
                q = deque()
                cost = 0
            elif s[i][j] == ".":
                q.append(s[i][j])
                cost += 1
            else:
                q.append(s[i][j])
        else:
            if s[i][j] == "x":
                q = deque()
                cost = 0
            elif s[i][j] == ".":
                q.append(s[i][j])
                x = q.popleft()
                if x == ".":
                    cost -= 1
                cost += 1
            else:
                q.append(s[i][j])
                x = q.popleft()
                if x == ".":
                    cost -= 1
        if len(q) == k:
            ans = min(ans, cost)

# 縦方向探索
for j in range(w):
    q = deque()
    cost = 0
    for i in range(h):
        if len(q) < k:
            if s[i][j] == "x":
                q = deque()
                cost = 0
            elif s[i][j] == ".":
                q.append(s[i][j])
                cost += 1
            else:
                q.append(s[i][j])
        else:
            if s[i][j] == "x":
                q = deque()
                cost = 0
            elif s[i][j] == ".":
                q.append(s[i][j])
                x = q.popleft()
                if x == ".":
                    cost -= 1
                cost += 1
            else:
                q.append(s[i][j])
                x = q.popleft()
                if x == ".":
                    cost -= 1
        if len(q) == k:
            ans = min(ans, cost)

if ans == INF:
    print(-1)
else:
    print(ans)
