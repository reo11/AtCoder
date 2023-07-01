from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

count = defaultdict(int)
ans = []

for i, a_i in enumerate(a):
    count[a_i] += 1
    if count[a_i] == 2:
        ans.append([i, a_i])

ans.sort()
ans = [a_i for i, a_i in ans]
print(*ans, sep=" ")
