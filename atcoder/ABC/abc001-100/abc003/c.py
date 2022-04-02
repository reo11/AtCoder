n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
a = a[:k]
rate = 0

for v in a[::-1]:
    rate = (rate + v) / 2
print(rate)
