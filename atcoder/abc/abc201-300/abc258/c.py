from collections import deque

n, q = map(int, input().split())
s = list(input())

queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))

counters = deque()

for si in s:
    if len(counters) == 0:
        counters.append([si, 1])
    else:
        if si == counters[-1][0]:
            counters[-1][1] += 1
        else:
            counters.append([si, 1])

ans = []
for query_type, x in queries:
    if query_type == 1:
        # 末尾をx回削除して先頭に追加
        head_q = deque()
        while x > 0:
            if x >= counters[-1][1]:
                x -= counters[-1][1]
                head_q.append(counters.pop())
            else:
                counters[-1][1] -= x
                head_q.append([counters[-1][0], x])
                x = 0
                break
        while head_q:
            if counters[0][0] == head_q[0][0]:
                counters[0][1] += head_q[0][1]
                head_q.popleft()
            else:
                counters.appendleft(head_q.popleft())
    else:
        # 先頭からx番目の文字を表示
        ansi = -1
        x -= 1
        count = 0
        for i in range(len(counters)):
            if count <= x and  x < count + counters[i][1]:
                ansi = counters[i][0]
            else:
                count += counters[i][1]
        ans.append(ansi)
    # print(counters)
print("\n".join(ans))