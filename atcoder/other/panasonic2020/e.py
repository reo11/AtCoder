import sys

input = sys.stdin.readline

a, b, c = [list(map(lambda x: ord(x), list(str(input().rstrip())))) for _ in range(3)]
M = 2000
base = M * 4 + 5
ab, ac, bc = [[False for _ in range(base * 2)] for _ in range(3)]
q = ord("?")


def match_chr(c1, c2):
    return c1 == q or c2 == q or c1 == c2


A, B, C = len(a), len(b), len(c)

for i in range(A):
    for j in range(B):
        if not match_chr(a[i], b[j]):
            ab[i - j + base] = True
    for j in range(C):
        if not match_chr(a[i], c[j]):
            ac[i - j + base] = True
for i in range(B):
    for j in range(C):
        if not match_chr(b[i], c[j]):
            bc[i - j + base] = True

ans = 3 * M
for i in range(-2 * M, 2 * M + 1):
    for j in range(-2 * M, 2 * M + 1):
        if ab[i + base] or ac[j + base] or bc[j - i + base]:
            continue
        l = min(0, min(i, j))
        r = max(A, max(B + i, C + j))
        ans = min(ans, r - l)
print(ans)
