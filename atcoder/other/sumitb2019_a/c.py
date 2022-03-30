def solve1(x):
    for c in range(1, x+1):
        if 100*c <= x <= 105*c:
            print(1)
            exit()
    print(0)

def solve2(x):
    dp = [0 for _ in range(100000+1)]
    for i in range(100, 106):
        dp[i] = 1

    for i in range(100, 100000+1):
        for j in range(6):
            if dp[i-(100+j)]:
                dp[i] = 1
    print(dp[x])

x = int(input())
solve2(x)