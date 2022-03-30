import sys
sys.setrecursionlimit(1000000)

MOD = 10**9 + 7
s = str(input())
l = len(s)
l_ = ["05", "18", "31", "44", "57", "70", "83", "96"]

def dfs(n, pre_num, count):
    if len(num) == l:
        return count
    if s[l - n] == "?":

ans = 0
for i in range(10):
    ans = (ans + dfs(i)) % MOD
print(ans)
