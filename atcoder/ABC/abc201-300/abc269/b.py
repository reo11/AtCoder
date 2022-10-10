s = []
for i in range(10):
  s.append(input())

a = 11
b = 0
c = 11
d = 0

for i in range(10):
  for j in range(10):
    if s[i][j] == "#":
      a = min(a, i + 1)
      b = max(b, i + 1)
      c = min(c, j + 1)
      d = max(d, j + 1)

print(a, b)
print(c, d)
