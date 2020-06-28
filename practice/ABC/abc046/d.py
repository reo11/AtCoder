s = str(input().rstrip())

def battle(s1, s2):
    l = {'g': {'g': 0, 'p': -1}, 'p': {'g': 1, 'p': 0}}
    return l[s1][s2]

hist = ['g']

g = 1
p = 0
ans = 0
if s[0] == 'p':
    ans = -1
for i in range(1, len(s)):
    cur = 'g'
    if s[i] == 'g':
        if p < g:
            cur = 'p'
    if s[i] == 'p':
        if p < g:
            cur = 'p'

    if cur == 'p':
        p += 1
    else:
        g += 1
    hist.append(cur)
    ans += battle(cur, s[i])

# print(list(s))
# print(hist)
print(ans)
