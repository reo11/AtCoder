import sys

input = sys.stdin.readline

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
s = [list(map(int, input().split())) for i in range(h)]
