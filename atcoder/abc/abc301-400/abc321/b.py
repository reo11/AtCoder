n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = -1
for i in range(101):
    tmp_a = a[:]
    tmp_a.append(i)
    sorted_a = sorted(tmp_a)
    if sum(sorted_a[1:-1]) >= x:
        ans = i
        break
print(ans)
