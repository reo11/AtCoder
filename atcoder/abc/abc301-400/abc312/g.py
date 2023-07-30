import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
ab = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    ab.append((a - 1, b - 1))

# 2頂点を選んだ時に通ることができない頂点の数を求める
# 木DPっぽい
# ある頂点を根とした時に、その頂点を通ることができない頂点の数を求める


