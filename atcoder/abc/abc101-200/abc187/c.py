from collections import defaultdict

n = int(input())
s = [input() for _ in range(n)]

counter = defaultdict(int)
for s_i in s:
    counter[s_i] += 1

ans = "satisfiable"
for s_i in s:
    if s_i[0] == "!":
        if counter[s_i[1:]] > 0 and counter[s_i] > 0:
            ans = s_i[1:]
            break
    else:
        if counter["!" + s_i] > 0 and counter[s_i] > 0:
            ans = s_i
            break
print(ans)
