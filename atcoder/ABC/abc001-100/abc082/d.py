from collections import defaultdict
s = input()
x, y = map(int, input().split())

dpx = defaultdict(lambda: defaultdict(lambda: False))
dpy = defaultdict(lambda: defaultdict(lambda: False))

dpx[0][0] = 0
