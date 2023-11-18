import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
a = list(map(int, input().split()))

def dfs(ai):
    