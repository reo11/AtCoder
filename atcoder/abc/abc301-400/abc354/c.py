n = int(input())
ac = []
for i in range(n):
    a, c = map(int, input().split())
    ac.append((c, a, i + 1))
ac.sort()

new_ac = []
max_a = 0
for c, a, i in ac:
    if a > max_a:
        new_ac.append((a, c, i))
        max_a = max(a, max_a)

print(len(new_ac))
print(*sorted([x[2] for x in new_ac]), sep= " ")