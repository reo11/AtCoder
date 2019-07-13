x, y, z = map(int, input().split())
a = x // (y + z)
b = (y + z) * a
ans = a
if b + z > x:
    ans -= 1
print(ans)
