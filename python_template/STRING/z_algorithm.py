def z_algo(S):
    N = len(S)
    A = [0] * N
    i = 1
    j = 0
    A[0] = N
    while i < N:
        while i + j < N and S[j] == S[i + j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while N - i > k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A
