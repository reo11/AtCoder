
n, m, l = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_with_index = [(ai, i + 1) for i, ai in enumerate(a)]
b_with_index = [(bi, i + 1) for i, bi in enumerate(b)]
a_with_index.sort(reverse=True)
b_with_index.sort(reverse=True)

cd = []
for _ in range(l):
  c, d = map(int, input().split())
  cd.append((c, d))
cd = set(cd)

ans = 0
for ai, a_idx in a_with_index:
  for bi, b_idx in b_with_index:
    if (a_idx, b_idx) in cd:
      continue
    ans = max(ans, ai + bi)
    break
print(ans)