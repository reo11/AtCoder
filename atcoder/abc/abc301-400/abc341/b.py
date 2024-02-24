n = int(input())
a = list(map(int, input().split()))
st = []
for i in range(n - 1):
    s, t = map(int, input().split())
    st.append((s, t))

for i in range(n - 1):
    cnt = a[i] // st[i][0]
    if cnt > 0:
        a[i] -= st[i][0] * (cnt)
        a[i + 1] += st[i][1] * (cnt)
# print(a)
print(a[-1])
