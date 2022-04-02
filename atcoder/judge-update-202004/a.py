s, l, r = map(int, input().split())
while True:
    if s < l:
        s += 1
    elif r < s:
        s -= 1
    else:
        break
print(s)
