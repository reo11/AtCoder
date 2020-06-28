import itertools

n = int(input())
seq = ["a", "b", "c"]
ans = []
for v in itertools.product(seq, repeat=n):
    ans.append("".join(v))
ans.sort()
print("\n".join(ans))
