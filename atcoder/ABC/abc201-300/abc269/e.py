from math import ceil

n = int(input())
# n * nの盤面


def question(a, b, c, d):
    print(f"? {a} {b} {c} {d}")
    return int(input())


def answer(x, y):
    print(f"! {x} {y}")


count = 0
ans = [1, n, 1, n]
for _ in range(20):
    a, b, c, d = ans
    if a != b:
        # 横方向に探索
        num = question(a, ((a + b) // 2), 1, n)
        if b - a == 1:
            if num == 1:
                a = b
            else:
                b = a
        elif b - a == 2:
            if num == 2:
                a = b
            else:
                b = (a + b) // 2
        elif num < ((a + b) // 2) - a + 1:
            b = (a + b) // 2
        else:
            a = ((a + b) // 2) + 1
    elif c != d:
        # 縦方向に探索
        num = question(1, n, c, ((c + d) // 2))
        if d - c == 1:
            if num == 1:
                c = d
            else:
                d = c
        elif d - c == 2:
            if num == 2:
                c = d
            else:
                d = (c + d) // 2
        elif num < ((c + d) // 2) - c + 1:
            d = (c + d) // 2
        else:
            c = ((c + d) // 2) + 1
    else:
        break
    ans = [a, b, c, d]
answer(ans[0], ans[2])
