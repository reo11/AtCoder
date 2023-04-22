n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

winner = -1
ans_list = []
if t not in c:
    t = c[0]
for i in range(n):
    if c[i] == t:
        ans_list.append([r[i], i + 1])
ans_list.sort(reverse=True)
print(ans_list[0][1])