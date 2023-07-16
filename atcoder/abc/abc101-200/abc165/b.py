x = int(input())
a = 100

i = 0
while True:
    a = int(a * 1.01)
    i += 1
    if a >= x:
        break
print(i)
