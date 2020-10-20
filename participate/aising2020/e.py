import sys
input = lambda: sys.stdin.readline().rstrip()

ans = []

def solve():
    n = int(input())

    klr = [[0 for _ in range(4)] for _ in range(n)]
    groups = [[] for _ in range(3)]
    for i in range(n):
        k, l, r = map(int, input().split())
        klr[i][0] = k; klr[i][1] = l; klr[i][2] = r;
        score = l - r
        if score == 0:
            groups[1].append([score, k, l, r])
        elif score < 0:
            groups[2].append([score, k, l, r])
        else:
            groups[0].append([score, k, l, r])
    # pos, eq, neg
    groups[0] = sorted(groups[0], key=lambda x: (-x[1], x[0]))
    groups[1] = sorted(groups[0], key=lambda x: x[1], reverse=True)

    # 後ろから埋めていく
    out = 0
    for i, day in enumerate(reversed(range(1, len(groups[0])+1))):
        if groups[0][i][1] <= day:
            out += groups[0][i][2]
        else:
            out += groups[0][i][3]
    for i in range(len(groups[1])):
        out += groups[1][i][2]
    day = len(groups[0]) + len(groups[1])
    for i in range(len(groups[2])):
        if groups[2][i][1] <= day:
            out += groups[2][i][2]
        else:
            out += groups[2][i][3]
        day += 1
    return out


t = int(input())
for _ in range(t):
    ans.append(str(solve()))
print("\n".join(ans))