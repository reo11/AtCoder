n, a, b, c, x = map(int, input().split())
abc = [a, b, c]
abc.sort(reverse=True)
a, b, c = abc
ans = 0
# iは全探索する
for i in range(1, n + 1):
    # ここを賢くする
    xi = x - a * i
    mod = xi % b
    # あまりがcの倍数になるようにfor文を回す

    for j in range(1, n + 1):
        if j * b + c > xi:
            break
        if (xi - j * b) % c == 0 and (xi - j * b) // c >= 1 and (xi - j * b) // c <= n:
            ans += 1
print(ans)
