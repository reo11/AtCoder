n = int(input())
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

a = l[n // 16]
b = l[n % 16]
print(str(a) + str(b))
