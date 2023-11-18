from collections import defaultdict
n = int(input())
s = list(input())

counter = defaultdict(int)
pre_s = ""
streak_counter = 0
for i in range(n):
    if s[i] == pre_s:
        streak_counter += 1
        counter[s[i]] = max(counter[s[i]], streak_counter)
    else:
        streak_counter = 1
        counter[s[i]] = max(counter[s[i]], 1)
    pre_s = s[i]

ans = 0
for k, v in counter.items():
    ans += v

print(ans)