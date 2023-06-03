l1 = [(f"B{i}", 9-i) for i in range(1, 10)]
l2 = [(f"{i}F", 8+i) for i in range(1, 10)]
d = {}
for v in l1 + l2:
    d[v[0]] = v[1]
s, t = input().split()
print(abs(d[s] - d[t]))
