from collections import defaultdict

s = input()
r = ["0000000000"]

counter = defaultdict(int)
for i in range(len(s)):
  counter[str(s[i])] += 1
  status = ""
  for j in range(10):
    status += str(counter[str(j)] % 2)
  r.append(status)

ans = 0
counter = defaultdict(int)
for i in range(len(r)):
  ans += counter[r[i]]
  counter[r[i]] += 1
print(ans)
