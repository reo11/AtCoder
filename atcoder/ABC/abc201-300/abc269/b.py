s = []
for i in range(10):
  s.append(input())

a = 1
b = 10
c = 1
d = 10

flag_type_x = 0
flag_type_y = 0

for i in range(10):
  for j in range(10):
    if flag_type_y == 0 and s[j][i] == "#":
      a = j + 1
      flag_type_y = 1
    elif flag_type_y == 1 and s[j][i] == ".":
      b = j
      flag_type_y = 2

for i in range(10):
  for j in range(10):
    if flag_type_x == 0 and s[i][j] == "#":
      c = j + 1
      flag_type_x = 1
    elif flag_type_x == 1 and s[i][j] == ".":
      d = j
      flag_type_x = 2

print(a, b)
print(c, d)
