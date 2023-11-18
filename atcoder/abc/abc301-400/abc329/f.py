import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

n, q = map(int, input().split())
c = list(map(int, input().split()))

boxes = defaultdict(lambda: set())
for i in range(n):
    boxes[i + 1].add(c[i])

# 重複していない色は数字として管理する
ans = []
for _ in range(q):
    a, b = map(int, input().split())
    if len(boxes[a]) <= len(boxes[b]):
        for ai in boxes[a]:
            boxes[b].add(ai)
    else:
        for bi in boxes[b]:
            boxes[a].add(bi)
        boxes[b] = boxes[a]
    boxes[a] = set()
    ans.append(len(boxes[b]))
print(*ans, sep="\n")