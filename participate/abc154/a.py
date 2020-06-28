s, t = map(str, input().split())
a, b = map(int, input().split())
u = str(input())

if u == s:
    a -= 1
elif u == t:
    b -= 1
print(a, b)