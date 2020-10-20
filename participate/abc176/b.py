n = input()

ans = 0
for i in range(len(n)):
    ans += int(n[i])
    ans %= 9
if ans == 0:
    print('Yes')
else:
    print('No')
