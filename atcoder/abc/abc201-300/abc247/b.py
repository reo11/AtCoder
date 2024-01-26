from collections import defaultdict

n = int(input())

counter = defaultdict(int)
st = []
for _ in range(n):
    s, t = input().split()
    st.append((s, t))
    if s == t:
        counter[s] += 1
    else:
        counter[s] += 1
        counter[t] += 1

ans = True
for s, t in st:
    if counter[s] == 1 or counter[t] == 1:
        continue
    else:
        ans = False
        break
if ans:
    print("Yes")
else:
    print("No")
