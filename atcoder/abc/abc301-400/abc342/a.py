from collections import defaultdict

s = list(input())
counter = defaultdict(lambda: 0)
for si in s:
    counter[si] += 1

for i in range(1, len(s) + 1):
    if counter[s[i - 1]] == 1:
        print(i)
        exit()
