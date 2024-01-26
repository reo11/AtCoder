l1, r1, l2, r2 = map(int, input().split())

s = set(range(l1, r1 + 1)) & set(range(l2, r2 + 1))
print(max(0, len(s) - 1))
