from collections import defaultdict

counter = defaultdict(int)

ans = []
n = int(input())
for _ in range(n):
    s = input()
    if counter[s] == 0:
        ans.append(s)
    else:
        ans.append(s + f"({counter[s]})")
    counter[s] += 1

print(*ans, sep="\n")