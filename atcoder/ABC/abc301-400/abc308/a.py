flag = True
s = list(map(int, input().split()))

for i in range(7):
    if s[i] > s[i+1]:
        flag = False
        break

for i in range(8):
    if s[i] < 100 or 675 < s[i]:
        flag = False
        break

for i in range(8):
    if s[i] % 25 != 0:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')