n = int(input())
ab = []

for _ in range(n):
    a, b = map(int, input().split())
    ab.append((b - a, a, b))

# (頭の大きさ, 肩までの高さ, 頭までの高さ)

ab.sort(reverse=True)

ans = sum([a for _, a, _ in ab[1:]])
ans += ab[0][2]
print(ans)