r, g, b = map(int, input().split())
k = int(input())

def check(r, g, b):
    return g > r and b > g

cnt = 0
while g <= r:
    g *= 2
    cnt += 1
while b <= g:
    b *= 2
    cnt += 1

if cnt <= k:
    print("Yes")
else:
    print("No")