import sys
input = lambda: sys.stdin.readline().rstrip()

d = dict()
n = int(input())
for i in range(1, n+1):
    d[i] = 0

for i in range(n):
    a = int(input())
    d[a] += 1

x = -1
y = -1
for k, v in d.items():
    if v == 0:
        x = k
    if v == 2:
        y = k

if x == -1 and y == -1:
    print("Correct")
else:
    print(y, x)
