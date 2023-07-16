n = int(input())

score = 10 ** 9

for i in range(1000):
    for j in range(1000):
        if i * j > n:
            continue
        else:
            score = min(score, abs(i - j) + (n - i * j))
print(score)
