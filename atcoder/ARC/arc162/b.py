n = int(input())
p = list(map(int, input().split()))

num = 0
while True:
    if num >= n:
        break
    # 先頭から埋めていく
    if p[num] == num + 1:
        num += 1
        continue
    # 持ってくる
    for i in range(num, n):
        if p[i] == num + 1:
            p[num], p[i] = p[i], p[num]
            num += 1
            break