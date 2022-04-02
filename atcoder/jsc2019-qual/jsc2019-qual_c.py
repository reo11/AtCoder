MOD = 10 ** 9 + 7

n = int(input())
s = input()

if s[0] == "W" or s[-1] == "W":
    print(0)
    exit()

kai = [1 for _ in range(n + 1)]
for i in range(1, n + 1):
    kai[i] = kai[i - 1] * i
    kai[i] %= MOD


def mul(a, b):
    return (a * b) % MOD


a = "L"
l_ = ["L", "R"]
c = 0

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c = not c
    a = a + l_[c]

ans = 1
num = 0
for i in range(len(s)):
    if a[i] == "L":
        num += 1
    else:
        ans *= num
        ans %= MOD
        num -= 1

if num > 0:
    print(0)
    exit()

ans *= kai[n]
ans %= MOD

print(ans)
