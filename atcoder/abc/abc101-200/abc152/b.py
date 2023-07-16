a, b = map(int, input().split())

ans = ["", ""]
for i in range(a):
    ans[0] += str(b)
for i in range(b):
    ans[1] += str(a)

ans.sort()
print(ans[0])
