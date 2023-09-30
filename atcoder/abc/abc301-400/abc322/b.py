n, m = map(int, input().split())
s = input()
t = input()

prefix = False
suffix = False

if t[:len(s)] == s:
    prefix = True
if t[-len(s):] == s:
    suffix = True
if prefix and suffix:
    print(0)
elif prefix:
    print(1)
elif suffix:
    print(2)
else:
    print(3)