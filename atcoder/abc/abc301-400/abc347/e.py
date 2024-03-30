from collections import defaultdict

n, q = map(int, input().split())
x = list(map(int, input().split()))

s = set()
size_of_s = []
histories = defaultdict(lambda: [])

for i, xi in enumerate(x):
    if xi in s:
        s.discard(xi)
        histories[xi].append(["removed", i])
    else:
        s.add(xi)
        histories[xi].append(["added", i])

    size_of_s.append(len(s))

# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r

size_of_s = cumsum(size_of_s)

# print(size_of_s)

ans = [0 for _ in range(n)]

for i in range(1, n + 1):
    sum_span = [-1, -1]
    for h in histories[i]:
        if h[0] == "added":
            sum_span[0] = h[1]
        else:
            sum_span[1] = h[1]
            ans[i - 1] += size_of_s[sum_span[1]] - size_of_s[sum_span[0]]
            sum_span = [-1, -1]
    if sum_span[0] != -1 and sum_span[1] == -1:
        ans[i - 1] += size_of_s[-1] - size_of_s[sum_span[0]]

print(*ans, sep=" ")