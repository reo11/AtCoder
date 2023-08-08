n, t = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
t %= sum_a

for i, a_i in enumerate(a, start=1):
    t -= a_i
    if t <= 0:
        print(f"{i} {a_i + t}")
        break