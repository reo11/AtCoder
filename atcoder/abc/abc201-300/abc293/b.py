n = int(input())
a = list(map(int, input().split()))
called = set()
for i, a_i in enumerate(a, start=1):
    if i in called:
        continue
    called.add(a_i)

ans = []
for i in range(1, n + 1):
    if i not in called:
        ans.append(i)
print(len(ans))
if len(ans) > 0:
    ans.sort()
    print(" ".join(list(map(str, ans))))
