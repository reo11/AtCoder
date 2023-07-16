from collections import defaultdict

n, q = map(int, input().split())
ans = []
status = defaultdict(lambda: [0, 0, "No"])
for _ in range(q):
    event_type, x = map(int, input().split())

    if event_type == 1:
        status[x][0] += 1
        if status[x][0] >= 2:
            status[x][2] = "Yes"
    elif event_type == 2:
        status[x][1] += 1
        status[x][2] = "Yes"
    else:
        ans.append(status[x][2])
print("\n".join(ans))
