import sys
import heapq
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

# 表で取りたいもの、裏で取りたいものを考える
# Aliceは表で取りたいものから裏にしていく
# Bobは取りたいものの最大値から取っていく
ans = 0
print(ans)