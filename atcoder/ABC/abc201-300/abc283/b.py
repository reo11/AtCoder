n = int(input())
a = list(map(int, input().split()))
q = int(input())

ans = []
for _ in [0] * q:
    q_i = list(map(int, input().split()))
    if q_i[0] == 1:
        a[q_i[1] - 1] = q_i[2]
    else:
        ans.append(a[q_i[1] - 1])
print(*ans, sep='\n')