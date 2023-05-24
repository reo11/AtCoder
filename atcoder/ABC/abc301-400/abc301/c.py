from collections import defaultdict

s = list(input())
t = list(input())

counter_s = defaultdict(int)
counter_t = defaultdict(int)

for c in s:
    counter_s[c] += 1
for c in t:
    counter_t[c] += 1

ans = True
alphabets = [chr(ord("a") + i) for i in range(26)]
atcoder = set(list("atcoder"))
minus = defaultdict(int)
for c in alphabets:
    if counter_s[c] < counter_t[c]:
        if c in atcoder:
            minus["s_atcoder"] += counter_t[c] - counter_s[c]
        else:
            minus["s"] += counter_t[c] - counter_s[c]
            ans = False
            break
    if counter_t[c] < counter_s[c]:
        if c in atcoder:
            minus["t_atcoder"] += counter_s[c] - counter_t[c]
        else:
            minus["t"] += counter_s[c] - counter_t[c]
            ans = False
            break

if ans and minus["s_atcoder"] <= counter_s["@"] and minus["t_atcoder"] <= counter_t["@"]:
    ans = True
else:
    ans = False
# print(minus)
# print(counter_s, counter_t)
print(['No', 'Yes'][ans])