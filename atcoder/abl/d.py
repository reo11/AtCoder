import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

# 優先度付きキューでそこまでの最も長い部分列から探索していく？