a, b, c = map(int, input().split())

if a + b == c or a + c == b or c + b == a:
    print("Yes")
else:
    print("No")
