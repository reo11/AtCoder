import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
q = int(input())

ans = []
numbers = defaultdict(lambda: set())
boxes = defaultdict(lambda: [])

for _ in range(q):
    s = input()
    if s[0] == "1":
        _, i, j = map(int, s.split())
        numbers[i].add(j)
        boxes[j].append(i)
    elif s[0] == "2":
        # 箱
        _, j = map(int, s.split())
        sorted_boxes = sorted(list(boxes[j]))
        ans.append(" ".join(list(map(str, sorted_boxes))))
    else:
        # 数字
        _, j = map(int, s.split())
        sorted_numbers = sorted(list(numbers[j]))
        ans.append(" ".join(list(map(str, sorted_numbers))))
print("\n".join(ans))