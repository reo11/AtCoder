import collections

n = int(input())


def convert(x):
    if x > 2:
        if x % 2 == 1:
            return 3
        else:
            return 2


def solve(a):
    a = [convert(a) for x in a]
    c = collections.Counter(a)
    if c[1] > 3:
        if c[1] % 2 == 1:
            c[1] = 1
        else:
            c[1] = 0


for _ in range(n):
    m = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

# https://ikatakos.com/pot/programming_algorithm/game/nim
