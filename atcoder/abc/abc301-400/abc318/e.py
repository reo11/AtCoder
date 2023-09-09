from collections import defaultdict, deque
n = int(input())
a = list(map(int, input().split()))

# 残りのjの数を記録して全体からそれ以外の数を求める
counter = defaultdict(lambda: [0, 0, 0])

print(a)
for i in range(len(a)):
    counter[a[i]][1] += (i - counter[a[i]][0])
    counter[a[i]][0] += 1

ans = 0
for i, ai in enumerate(a):
    counter[ai][2] += 1
    if counter[ai][2] == counter[ai][0]:
        # その先にaiはないので条件を満たせない
        continue
    count = counter[ai][1] - (counter[ai][0] * i)
    ans += count
    print(i, ai, ans)
print(ans)
