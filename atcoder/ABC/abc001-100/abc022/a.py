n, s, t = map(int, input().split())
w = int(input())
count = 0
if s <= w <= t:
    count += 1

for i in range(n - 1):
    a = int(input())
    w += a
    if s <= w <= t:
        count += 1
print(count)
