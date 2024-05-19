from collections import defaultdict

n = int(input())
s = list(input().split())
s = sorted(s)
s = [list(si) for si in s]

rights = defaultdict(int)
for i in range(n - 1):
    if s[i][0] != s[i + 1][0]:
        rights[s[i][0]] = i
rights[s[-1][0]] = n - 1

ans = 0
for i in range(n - 1):
    si = s[i]
    s_head = si[0]
    right = rights[s_head]
    count = 0
    while i < right and count < len(si):
        if si[count] == s[right][count]:
            count += 1
            ans += (right - i)
        else:
            right -= 1

print(ans)