n, m = map(int, input().split())
a = list(map(int, input().split()))

# 1. A1を1減らす
# 2. A2を1増やす
# 3. Aiを1増やすか減らす
# 3はする必要がない（1か2をした方が効率が良い）

a1 = a[0]
a2 = a[1]
a_list = a[2:]
a_list.sort()
ans = float("inf")
count = 0
for a_i in a_list:
    if a1 <= a_i and a_i <= a2:
        count += 1
if count >= m:
    print(0)
    exit()

for i in range(len(a_list) - (m - 1)):
    next_a1 = a_list[i]
    next_a2 = a_list[i + m - 1]
    if next_a1 >= a1:
        next_a1 = a1
    if next_a2 <= a2:
        next_a2 = a2
    # print(a_list[i], a_list[i + m - 1], next_a1, next_a2)
    ans = min(ans, abs(next_a1 - a1) + abs(next_a2 - a2))

print(ans)