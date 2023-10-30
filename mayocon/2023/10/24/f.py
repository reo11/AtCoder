n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def oturi(x):
    # x円おつりが発生した時の最小枚数
    count = 0
    for ai in reversed(a):
        if x >= ai:
            count += x // ai
            x %= ai
    return count

#