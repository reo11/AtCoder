n, q = map(int, input().split())
A = []
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a[1:])

ans = []
for q_i in range(q):
    s, t = map(int, input().split())
    ans.append(str(A[s - 1][t - 1]))
print("\n".join(ans))