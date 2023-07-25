n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])

# 最初Bに投票する人は0人
# Aを上回るようにAに投票する人を減らすか、Bに投票する人を増やす
# そんな感じで貪欲する
# その街へ行った時の利益を最大化する
# 利益は (A + B) + A
cities = []
a_sum = 0
for a, b in ab:
    cities.append([2 * a + b, a, b])
    a_sum += a
cities.sort(reverse=True)
ans = 0
b_sum = 0
for plus, a, b in cities:
    b_sum += plus
    ans += 1
    if b_sum > a_sum:
        break
print(ans)