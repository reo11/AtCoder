import math

d, g = map(int, input().split())
p = [0] * d
c = [0] * d

for i in range(d):
    p[i], c[i] = map(int, input().split())

# 完全に解く 1
# 全く解かない 0
min_cost = 10**10
for i in range(2**d):
    count = 0
    score = 0
    use_list = []
    for bit in range(d):
        if i & 2**bit > 0:
            use_list.append(bit + 1)
            count += p[bit]
            score += (bit + 1) * 100 * p[bit] + c[bit]
    if score < g:
        p_i = max(set(range(1, d + 1)) - set(use_list))
        p_count = math.ceil((g - score) / (p_i * 100))
        if p_count <= p[p_i - 1]:
            count += p_count
            score += p_count * (p_i * 100)
    if score >= g:
        min_cost = min(min_cost, count)
print(min_cost)
