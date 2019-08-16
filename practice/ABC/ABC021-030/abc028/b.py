s = input()
d = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

for i in list(s):
    d[i] += 1

print("{} {} {} {} {} {}".format(d["A"], d["B"], d["C"], d["D"], d["E"], d["F"]))
