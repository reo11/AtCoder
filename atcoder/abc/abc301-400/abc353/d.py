from collections import deque, defaultdict

MAX_SHIFT = 12
MOD = 998244353

n = int(input())
a = list(input().split())
ai_lens = [len(ai) for ai in a]
a = [int(ai) for ai in a]

a_patterns = [[0 for _ in range(MAX_SHIFT)] for _ in range(n)]

for shift_i in range(MAX_SHIFT):
    mod_i = (10**shift_i) % MOD
    for i in range(n):
        ai = a[i]
        a_patterns[i][shift_i] = (ai * mod_i) % MOD

counter = defaultdict(int)
for ai_len in ai_lens:
    counter[ai_len] += 1

ans = 0
for i in range(n):
    ai = a[i]
    ai_len = ai_lens[i]
    counter[ai_len] -= 1
    for shift_i in range(MAX_SHIFT):
        count = counter[shift_i]
        if count == 0:
            continue
        ans += a_patterns[i][shift_i] * count
        ans %= MOD
    ans += (ai * i)
    ans %= MOD

print(ans)