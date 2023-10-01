from collections import defaultdict
from copy import deepcopy
MAX_NUM = 5

n, k, p = map(int, input().split())
INF = 10 ** 18
cas = []
for _ in range(n):
    c, *a = list(map(int, input().split()))
    cas.append((c, a))

dp = defaultdict(lambda: defaultdict(lambda: INF))
for i in range(n + 1):
    dp[i]["_".join(list(map(str, [0] * k)))] = 0

def value_of_num(num, k, p) -> list:
    # 数字numのk進数における各桁の値をList[int]で返す
    ret = [0 for _ in range(p)]
    for i in range(p):
        ret[i] = num // (p ** i) % p
    return ret[::-1]

def fix_index(idx, max_value=p):
    return min(idx, max_value)
    
for i, (c, a) in enumerate(cas):
    # (p + 1)進数でk桁まで全探索
    for num in range((p + 1)**k):
        lists = value_of_num(num, k, p + 1):
            
    dp[i + 1][]