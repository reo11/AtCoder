n = int(input())

a = []
ans = []

for i in range(n):
    a.append(int(input()))

a_sorted = sorted(a)
a_max1 = a_sorted[-1]
a_max2 = a_sorted[-2]
for a_value in a:
    if a_value != a_max1:
        ans.append(str(a_max1))
    else:
        ans.append(str(a_max2))

print("\n".join(ans))
