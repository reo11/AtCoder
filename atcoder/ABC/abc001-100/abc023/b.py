n = int(input())
s = str(input())

t = "b"
i = 0
if t == s:
    print(i)
    exit()

while True:
    i += 1
    if i % 3 == 1:
        t = "a" + t + "c"
    elif i % 3 == 2:
        t = "c" + t + "a"
    else:
        t = "b" + t + "b"

    if t == s:
        print(i)
        exit()
    if len(t) > len(s):
        break

print(-1)
