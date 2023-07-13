n, l, r = map(int, input().split())
a = list(map(int, input().split()))

# lとrは独立（多分）
# lの最適解を求める

# 累積和
# 累積和
def cumsum(a):
    r = [0]
    for v in a:
        r.append(r[-1] + v)
    return r

ans_l = [0, 0]
ans_r = [0, 0]
left_a = cumsum(a)
for i in range(len(left_a)):
    a_i = left_a[i]
    if l * i - a_i < ans_l[0]:
        ans_l = [l * i - a_i, i]

for i in range(ans_l[1]):
    a[i] = l

a = a[::-1]
right_a = cumsum(a)
for i in range(len(right_a)):
    a_i = right_a[i]
    if r * i - a_i <= ans_r[0]:
        ans_r = [r * i - a_i, i]

for i in range(ans_r[1]):
    a[i] = r

# print(left_a)
# print(right_a)
# print(a)
print(sum(a))