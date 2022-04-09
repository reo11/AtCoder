def counting_primes(n: int) -> int:
    # O(n^(3/4)/logn)
    if n <= 1:
        return 0
    elif n <= 3:
        return 2
    v = int(n ** 0.5) - 1
    while v ** 2 <= n:
        v += 1
    v -= 1
    smalls = [(i + 1) // 2 for i in range(v + 1)]
    s = (v + 1) // 2
    roughs = [2 * i + 1 for i in range(s)]
    larges = [(n // (2 * i + 1) + 1) // 2 for i in range(s)]
    skip = [False] * (v + 1)

    pc = 0
    for p in range(3, v + 1, 2):
        if skip[p]:
            continue
        q = p * p
        pc += 1
        if q * q > n:
            break
        skip[p] = True
        for i in range(q, v + 1, 2 * p):
            skip[i] = True
        ns = 0
        for k in range(s):
            i = roughs[k]
            if skip[i]:
                continue
            d = i * p
            if d <= v:
                x = larges[smalls[d] - pc]
            else:
                x = smalls[n // d]
            larges[ns] = larges[k] + pc - x
            roughs[ns] = i
            ns += 1
        s = ns
        i = v
        for j in range(v // p, p - 1, -1):
            c = smalls[j] - pc
            e = j * p
            while i >= e:
                smalls[i] -= c
                i -= 1
    ret = larges[0] + (s + 2 * (pc - 1)) * (s - 1) // 2 - sum(larges[1:s])

    for l in range(1, s):
        q = roughs[l]
        m = n // q
        e = smalls[m // q] - pc
        if e <= l:
            break
        t = 0
        for r in roughs[l + 1 : e + 1]:
            t += smalls[m // r]
        ret += t - (e - l) * (pc + l - 1)
    return ret
