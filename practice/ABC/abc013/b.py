a = int(input())
b = int(input())

a_tmp = a
b_tmp = b
i = 0
while True:
    if a == b:
        break
    a += 1
    a %= 10
    i += 1

a = a_tmp
b = b_tmp
j = 0
while True:
    if a == b:
        break
    b += 1
    b %= 10
    j += 1
print(min(i, j))