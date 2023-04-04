l, r = map(int, input().split())
s = str(input())

s = list(s)
s = s[: l - 1] + list(reversed(s[l - 1 : r])) + s[r:]
print("".join(s))
