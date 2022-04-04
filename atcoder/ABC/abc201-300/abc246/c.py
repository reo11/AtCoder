n, k, x = map(int, input().split())
a = list(map(int, input().split()))


sum_cost = 0
full_discount = 0
nokori = []

for a_i in a:
    full_discount += a_i // x
    nokori.append(a_i % x)

nokori.sort(reverse=True)

if full_discount >= k:
    sum_cost = sum(nokori) + (full_discount - k) * x
else:
    sum_cost = sum(nokori[k - full_discount :])
print(sum_cost)
