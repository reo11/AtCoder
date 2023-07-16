x, y = map(str, input().split())
x = ord(x)
y = ord(y)
ans = "="
if x < y:
    ans = "<"
elif x > y:
    ans = ">"
print(ans)
