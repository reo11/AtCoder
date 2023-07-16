from collections import defaultdict

d = defaultdict(int)

n, m = map(int, input().split())
a = list(map(int, input().split()))

for v in a:
    d[v] += 1

for i in range(m):
    b, c = map(int, input().split())
    d[c] += b
ans_list = []
for key, value in d.items():
    temp = [key, value]
    ans_list.append(temp)
ans_list.sort(key=lambda x: x[0])
ans_list.reverse()
ans = 0
for (value, count) in ans_list:
    if 0 > n - count:
        ans += n * value
        break
    else:
        n -= count
        ans += count * value
print(ans)
