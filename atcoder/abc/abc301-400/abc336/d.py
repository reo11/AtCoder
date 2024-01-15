n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]

# 左右から挟む
# 左から
possible = [0 for _ in range(len(a))]
for i in range(1, len(a)):
    possible[i] = min(a[i], possible[i - 1] + 1)

# 右から
for i in range(len(a) - 2, 0, -1):
    possible[i] = min(possible[i], possible[i + 1] + 1)
print(max(possible))
