N = int(input())
t = []
def ftime(ts, te):
  return ("0000" + str(ts))[-4:] + "-" + ("0000" + str(te))[-4:]

for i in range(N):
  s, e = map(int, input().split("-"))
  if e % 100 > 55:
    e = (e//100 + 1) * 100
  else:
    e += (5 - e%5) % 5
  s -= s % 5
  t.append([s, e])

t.sort()

ans = []
ts, te = t[0]
for s, e in t:
  if te < s:
    print(ftime(ts, te))
    ts = s
  te = max(e, te)

print(ftime(ts, te))
