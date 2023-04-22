import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

s = input()

MOD = 998244353


def generate_subsequences(s):
    subsequences = set()

    def helper(current, index):
        if index == len(s):
            if current:
                subsequences.add(current)
            return

        helper(current, index + 1)
        helper(current + s[index], index + 1)

    helper("", 0)
    return subsequences

def count_common_subsequences(s1, s2):
    s1_subsequences = generate_subsequences(s1)
    s2_subsequences = generate_subsequences(s2)

    s1_counter = Counter(s1_subsequences)
    s2_counter = Counter(s2_subsequences)

    common_subsequences = s1_counter & s2_counter
    return dict(common_subsequences)

# 区切りを全探索
# i = 左の最後の要素
ans = set()
for i in range(1, len(s)):
    s1 = s[:i]
    s2 = s[i:]
    # print(s1, s2)
    d = count_common_subsequences(s1, s2)
    for sub_s in d.keys():
        # print(sub_s)
        ans.add(sub_s)

# print(ans)
print(len(ans) % MOD)