n = int(input())
a = list(map(int, input().split()))

base = 0
for v in a:
   base ^= v

out = []
for v in a:
   ans = base ^ v
   out.append(str(ans))
print(" ".join(out))