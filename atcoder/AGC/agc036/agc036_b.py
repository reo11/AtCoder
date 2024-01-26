n, k = map(int, input().split())
a = list(map(int, input().split()))
a_idx = [-1] * (2 * 10**5)
ans = [0] * (2 * 10**5)
idx = 0
for i in range(n * k):
    a_i = a[i % n]
    if a_idx[a_i] == -1:
        ans[idx] = a_i
        a_idx[a_i] = idx
        idx += 1
    else:
        idx = a_idx[a_i]
        a_idx[a_i] = -1

    print(" ".join(list(map(str, ans[:idx]))))
