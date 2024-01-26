print(200, 10)
a = []
for i in range(10):
    ai = []
    for j in range(1, 21):
        ai.append(j + i * 20)
    a.append(" ".join(list(map(str, ai))))
print("\n".join(a))
