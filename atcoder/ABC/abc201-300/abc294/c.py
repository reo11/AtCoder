n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = []
for a_i in a:
    ab.append([a_i, 0])
for b_i in b:
    ab.append([b_i, 1])
ab.sort()
ans = [[], []]

for i, (ab_i, num) in enumerate(ab, start=1):
    ans[num].append(i)
print(" ".join(list(map(str, ans[0]))))
print(" ".join(list(map(str, ans[1]))))
