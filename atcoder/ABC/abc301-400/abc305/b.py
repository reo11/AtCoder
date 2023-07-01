p, q = input().split()

sorted_l = sorted([p, q])

d = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}

print(d[sorted_l[1]] - d[sorted_l[0]])
