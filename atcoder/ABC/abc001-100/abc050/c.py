import collections

MOD = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)

ans = 1
for key, value in c.items():
    if key == 0:
        if n % 2 == 1 and value != 1:
            print(0)
            exit()
        else:
            continue
    elif value == 2:
        ans *= 2
        ans %= MOD
    else:
        print(0)
        exit()
print(ans)
