a, b = map(str, input().split())

ans = 'H'

if a == 'H':
    if b != 'H':
        ans = 'D'
else:
    if b == 'H':
        ans = 'D'

print(ans)