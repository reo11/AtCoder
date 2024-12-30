MOD = 998244353

n, m = map(int, input().split())
m_bits = []
for i in range(0, len(str(bin(m))) - 1):
    if m & (1 << i):
        m_bits.append(i)
m_bits = set(m_bits)
ans = 0
for m_bit in m_bits:
    num = (1 << (m_bit + 1))
    div = (n + 1) // num
    mod = (n + 1) % num
    ans += (div * num // 2) % MOD
    if mod > num // 2:
        ans += (mod - num // 2) % MOD
    ans %= MOD

print(ans)