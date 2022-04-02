from math import gcd

n, q = map(int, input().split())
A = list(map(int, input().split()))
S = list(map(int, input().split()))

# 前処理
gcds = [A[0]]
for a in A[1:]:
    gcds.append(gcd(gcds[-1], a))

# print(gcds)
# 二分探索っぽくやる
ans = []
for s in S:
    if gcd(s, gcds[-1]) != 1:
        ans.append(gcd(s, gcds[-1]))
    else:
        left = -1
        right = n + 1
        mid = (left + right) // 2
        while True:
            if right - left <= 1:
                break
            mid = (left + right) // 2
            # print(s, l, r, mid)
            if gcd(gcds[mid], s) == 1:
                right = mid
            else:
                left = mid
        for i in range(mid - 1, mid + 2):
            if 0 <= i <= n - 1:
                if gcd(gcds[i], s) == 1:
                    ans.append(i + 1)
                    break
print("\n".join(list(map(str, ans))))
