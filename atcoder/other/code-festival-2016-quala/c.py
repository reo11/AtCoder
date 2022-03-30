s = list(input())
k = int(input())

for i in range(len(s)):
    cost = ord('z') - ord(s[i]) + 1
    c = s[i]
    if cost <= k:
        k -= cost
        c = 'a'
    s[i] = c
k %= 26
if k > 0:
    c = chr(ord(s[i]) + k)
    if ord(c) > ord('z'):
        c = chr(ord('a') + (ord(c) - ord('z') - 1))
    s[i] = c
print("".join(s))