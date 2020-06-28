def z_algo(S):
    N = len(S)
    A = [0]*N
    i = 1
    j = 0
    A[0] = N
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while N-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k
        j -= k
    return A


n = int(input())
s = input()


ans = 0
for i in range(n - 1):
    r = z_algo(s[i:])
    for j in range(1, len(r)):
        if r[j] <= j:
            ans = max(ans, r[j])
print(ans)
