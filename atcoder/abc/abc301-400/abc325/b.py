n = int(input())
wx = []

def ok(time):
    return 9 <= time and time <= 17

for _ in range(n):
    w, x = map(int, input().split())
    wx.append((w, x))

ans = 0
for t in range(24):
    count = 0
    for w, x in wx:
        if ok((x + t) % 24):
            count += w
    ans = max(ans, count)
print(ans)