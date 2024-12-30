from collections import deque
# フラクタル

n = int(input())
ans = []
for i in range(3**n):
    ansi = []
    for j in range(3**n):
        ansi.append('#')
    ans.append(ansi)

q = deque()
q.append((3**n//2, 3**n//2, n))

while q:
    x, y, n = q.popleft()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                for i in range(int(3**(n-1))):
                    for j in range(int(3**(n-1))):
                        ans[x-(3**(n-1))//2+i][y-(3**(n-1))//2+j] = '.'
            elif n - 1 > 0:
                nx = x + dx * (3**(n-1))
                ny = y + dy * (3**(n-1))
                q.append((nx, ny, n-1))

for ansi in ans:
    print(*ansi, sep='')