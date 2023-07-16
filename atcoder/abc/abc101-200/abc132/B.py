n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(n - 2):
    p_part = p[i : i + 3]
    if p[i + 1] != max(p_part) and p[i + 1] != min(p_part):
        count += 1
print(count)
