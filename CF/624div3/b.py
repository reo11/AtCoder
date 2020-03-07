t = int(input())
ans = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    p = set(map(int, input().split()))
    for j in range(n):
        for i in range(n-1):
            if i+1 in p:
                if a[i] > a[i+1]:
                    tmp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = tmp
    a_sort = sorted(a)
    if a == a_sort:
        ans.append("YES")
    else:
        ans.append("NO")
print("\n".join(ans))

