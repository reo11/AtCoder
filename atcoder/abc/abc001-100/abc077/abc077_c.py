import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

b_num = [0 for _ in range(n)]
for b_i in range(n):
    c_i = bisect.bisect_right(c, b[b_i])
    b_num[b_i] = n - c_i

for i in range(1, len(b_num)):
    b_num[len(b_num) - 1 - i] += b_num[len(b_num) - i]

ans = 0
for a_i in range(len(a)):
    b_i = bisect.bisect_right(b, a[a_i])
    if b_i >= n:
        continue
    ans += b_num[b_i]
print(ans)
