n = int(input())
s = input()

even = set()
odd = set()
for i in range(n):
    if i % 2:
        even.add(s[i])
    else:
        odd.add(s[i])
if len(even) <= 1 and len(odd) <= 1:
    print("Yes")
else:
    print("No")