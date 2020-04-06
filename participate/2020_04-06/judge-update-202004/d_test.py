from math import gcd

n, q = map(int, input().split())
A = list(map(int, input().split()))
S = list(map(int, input().split()))

ans = []
for s in S:
    x = s
    tmp = x
    for j, a in enumerate(A):
        x = gcd(a, x)
        print(x)
        if x == 1:
            tmp = j + 1
            break
        else:
            tmp = x
    ans.append(tmp)
print("\n".join(list(map(str, ans))))
