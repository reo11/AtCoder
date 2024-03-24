from collections import defaultdict
t = int(input())
periods = [[1, 1]]
# [l, r]

for i in range(1, 10):
    # 10**9まで
    num1 = ""
    for j in range(i - 1):
        num1 += "9"
    num1 += "8"
    for j in range(i):
        num1 += "0"
    periods.append([int(num1), int(num1)])

    nines = "9" * i
    tens = "1" + "0" * i
    periods.append([int(nines) * int(tens), int(tens) * (10 ** len(nines)) + int(nines)])

def solve(x):
    ansi = 0
    for l, r in periods:
        if r < x:
            ansi += r - l + 1
        else:
            if l <= x and x <= r:
                ansi += x - l + 1
    return ansi

ans = []
for _ in range(t):
    n = int(input())
    ans.append(solve(n))
    # ans.append(simple_solve(n))
print(*ans, sep='\n')