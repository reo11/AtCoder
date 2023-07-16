s = str(input())
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    s = s[: l - 1] + s[l - 1 : r][::-1] + s[r:]
print(s)
