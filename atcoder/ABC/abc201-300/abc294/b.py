h, w = map(int, input().split())
ans = []

for i in range(h):
  a = list(map(int, input().split()))
  ans.append([])
  for a_i in a:
    if a_i == 0:
      ans[-1].append(".")
    else:
      ans[-1].append(chr(ord("A") + a_i - 1))
print("\n".join(["".join(ans_i) for ans_i in ans]))
