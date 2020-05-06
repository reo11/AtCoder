import sys
input = lambda: sys.stdin.readline().rstrip()

d, l, n = map(int, input().split())
c = list(map(int, input().split()))
kft = [list(map(int, input().split())) for _ in range(n)]
