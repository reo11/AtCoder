n, l = map(int, input().split())
s = input()

ans = 0
cnt = 1
for c in s:
    if c == '+':
        cnt += 1
    else:
        cnt -= 1
    if cnt > l:
        ans += 1
        cnt = 1
print(ans)