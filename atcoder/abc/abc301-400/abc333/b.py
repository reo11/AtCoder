s = list(input())
t = list(input())

groups = [
    [
        set(["A", "B"]),
        set(["B", "C"]),
        set(["C", "D"]),
        set(["D", "E"]),
        set(["A", "E"])
    ],
    [
        set(["A", "C"]),
        set(["B", "D"]),
        set(["C", "E"]),
        set(["D", "A"]),
        set(["E", "B"])
    ]
]
g1 = groups[0]
g2 = groups[1]
ans = False
if set(s) in g1 and set(t) in g1:
    ans = True
elif set(s) in g2 and set(t) in g2:
    ans = True

if ans:
    print("Yes")
else:
    print("No")
