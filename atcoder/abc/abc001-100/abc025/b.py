n, a, b = map(int, input().split())
x = 0

for i in range(n):
    s, d = input().split()
    d = int(d)
    if a > d:
        d = a
    elif b < d:
        d = b
    if s == "East":
        x += d
    elif s == "West":
        x -= d
if x > 0:
    print("East {}".format(x))
elif x < 0:
    print("West {}".format(abs(x)))
else:
    print(0)
