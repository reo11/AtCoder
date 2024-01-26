n = int(input())

w = [int(i) for i in input().split()]

min_abs = 10**9
for i in range(1, len(w) + 1):
    s1 = sum(w[:i])
    s2 = sum(w[i:])
    min_abs = min(abs(s1 - s2), min_abs)
print(min_abs)
