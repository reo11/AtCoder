import bisect

n = int(input())
d = list(map(int, input().split()))
d.sort()
div = n // 2
count = 0
for i in range(10 ** 5 + 1):
    insert_index = bisect.bisect_right(d, i)
    if insert_index == div:
        count += 1
print(count)
