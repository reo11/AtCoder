n = int(input())
p = list(map(int, input().split()))

# 最小を更新

min_ = p[0]
count = 1
for i in range(1, n):
    if p[i] < min_:
        count += 1
        min_ = p[i]
print(count)
