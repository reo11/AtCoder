c = list(str(input()))
c.extend(list(str(input())))

if c == c[::-1]:
    print("YES")
else:
    print("NO")