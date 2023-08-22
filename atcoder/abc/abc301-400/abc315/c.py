from collections import defaultdict

INF = float("inf")

n = int(input())
same_colors = defaultdict(lambda: [])
diff_colors = defaultdict(lambda: -INF)

for _ in range(n):
    f, s = map(int, input().split())
    same_colors[f].append(s)
    diff_colors[f] = max(diff_colors[f], s)
same_colors = {k: sorted(v, reverse=True) for k, v in same_colors.items()}

# 最大化したいので-infで初期化
ans = -INF

# 同じ味の場合は1番目 + 2番目の半分
for color in same_colors.keys():
    if len(same_colors[color]) >= 2:
        first = same_colors[color][0]
        second = same_colors[color][1]
        ans = max(ans, first + second // 2)

# 違う味の場合は各色の1番のみで、上位2色を選ぶ
if len(diff_colors) >= 2:
    diff_colors = sorted(diff_colors.items(), key=lambda x: x[1], reverse=True)
    color1, v1 = diff_colors[0]
    color2, v2 = diff_colors[1]
    ans = max(ans, v1 + v2)

print(ans)
