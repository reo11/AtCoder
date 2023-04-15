import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

MOD = 998244353
q = int(input())

s = deque([1])
ans = []
ten_multi = [0 for _ in range((6 * (10 ** 5)) + 1)]
ten = 1
for i in range(len(ten_multi)):
    ten_multi[i] = ten % MOD
    ten = (ten * 10) % MOD

ans_mod = 1
for _ in range(q):
    query = input()
    if query[0] == "1":
        # 末尾に数字xを追加
        _, x = map(int, query.split())
        s.append(x)
        # 前の値を10倍して、xを足している
        ans_mod = ((ans_mod * 10) % MOD + x % MOD)
    elif query[0] == "2":
        # 先頭の数字を削除
        x = s.popleft()
        # 前の値からx * 10 ** nを引いている
        sub = ((x % MOD) * ten_multi[len(s)]) % MOD
        ans_mod = (ans_mod - sub) % MOD
    else:
        # 10進数表記のMOD
        ans.append(str(ans_mod))
print("\n".join(ans))
