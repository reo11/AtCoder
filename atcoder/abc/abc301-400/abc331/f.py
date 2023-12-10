import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, q = map(int, input().split())
s = list(input())

queries = []

for _ in range(q):
  query = list(input().split())
  queries.append(query)

ans = []

def is_re(s):
  for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
      return "No"
  return "Yes"

for query in queries:
  if query[0] == "1":
    _, x, c = query
    x = int(x) - 1
    s[x] = c
  else:
    _, l, r = query
    l = int(l) - 1
    r = int(r) - 1
    ans.append(is_re(s[l:r + 1]))
print(*ans, sep="\n")
