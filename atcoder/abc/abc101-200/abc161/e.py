from collections import deque

n, k, c = map(int, input().split())
s = str(input())

# 前後
i = 0
l1 = []
while i <= n - 1:
    if s[i] == "o":
        l1.append(i + 1)
        i += c + 1
    else:
        i += 1
    if len(l1) >= k:
        break
i = n - 1
l2 = []
while i >= 0:
    if s[i] == "o":
        l2.append(i + 1)
        i -= c + 1
    else:
        i -= 1
    if len(l2) >= k:
        break
ans = []
for i, j in zip(l1, l2[::-1]):
    if i == j:
        ans.append(i)
print("\n".join(list(map(str, ans))))
