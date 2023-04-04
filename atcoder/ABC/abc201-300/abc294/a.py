n = int(input())
a = list(map(int, input().split()))

ans = []

for a_i in a:
    if a_i % 2 == 0:
        ans.append(str(a_i))
print(" ".join(ans))
