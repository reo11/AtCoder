s = str(input())
t = int(input())

x = 0
y = 0
q = 0
for c in list(s):
    if c == "L":
        x -= 1
    elif c == "R":
        x += 1
    elif c == "U":
        y += 1
    elif c == "D":
        y -= 1
    else:
        q += 1
if t == 1:
    print(abs(x) + abs(y) + q)
else:
    if (abs(x) + abs(y) - q) % 2 == 1:
        print(max(1, abs(x) + abs(y) - q))
    else:
        print(max(0, abs(x) + abs(y) - q))
