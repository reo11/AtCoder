import sys
from collections import defaultdict

input = sys.stdin.readline

q, x = map(int, input().split())
a = []
a_dict = defaultdict(int)

for i in range(q):
    y = int(input())
    y %= x

    a_dict[y] += 1

    min_v = 10**6
    ans = 0
    if len(a_dict.keys()) == x:
        for key, value in a_dict.items():
            if value < min_v:
                min_v = value
                ans = ((min_v) * x) + key
            print(key, value, ans)
    else:
        idx = 0
        for idx, (key, value) in enumerate(a_dict.items()):
            if idx != key:
                break
            ans = key + 1
    print(ans)



