import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
lr = []

queue = []

for i in range(n):
    l, r = map(int, input().split())
    lr.append((l, r))
    queue.append((l, "in", i))
    queue.append((r + 0.5, "out", i))
queue.sort(reverse=True)

current_size = 0
ans = 0

while queue:
    x, io, i = queue.pop()
    if io == "in":
        ans += current_size
        current_size += 1
    else:
        current_size -= 1
print(ans)
