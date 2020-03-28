x = int(input())

ans = 0
while True:
    if x >= 500:
        x -= 500
        ans += 1000
    else:
        break

while True:
    if x >= 5:
        x -= 5
        ans += 5
    else:
        break
print(ans)