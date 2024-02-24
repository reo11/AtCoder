from collections import defaultdict
n = int(input())
c = list(input())

# 遷移させるだけ
# 遷移元と遷移先の状態によって中間状態を定める
# 状態数はそんなに多くない（多分）のでsetで適当に扱う？

votes = [[0 for _ in range(4)] for _ in range(n + 1)]
c1 = c[0]
c = c[1:]
if c1 == "A":
    votes[0][2] = 1
else:
    votes[0][3] = 1

for i, ci in enumerate(c, start=1):
    if ci == "A":
        votes[i][0] = votes[i - 1][0] + 1
        votes[i][1] = votes[i - 1][1]
        votes[i][2] = votes[i - 1][2] + 1
        votes[i][3] = votes[i - 1][3]
    else:
        votes[i][0] = votes[i - 1][0]
        votes[i][1] = votes[i - 1][1] + 1
        votes[i][2] = votes[i - 1][2]
        votes[i][3] = votes[i - 1][3] + 1

# 最後
if c1 == "A":
    votes[-1][0] = votes[-2][0] + 1
    votes[-1][1] = votes[-2][1]
else:
    votes[-1][0] = votes[-2][0]
    votes[-1][1] = votes[-2][1] + 1

def stats(x, y):
    if x > y:
        return "A"
    elif x < y:
        return "B"
    else:
        return "C"

counter = defaultdict(lambda: defaultdict(lambda: 0))
paths = [set() for _ in range(n - 1)]
for i in range(1, n):
    start1 = stats(votes[i][0], votes[i][1])
    end1 = stats(votes[i][2], votes[i][3])
    end2 = stats(votes[i + 1][0], votes[i + 1][1])
    paths[i - 1].add(f"{start1} {end1} 1")
    paths[i - 1].add(f"{start1} {end2} 2")

    start2 = stats(votes[i - 1][2], votes[i - 1][3])
    paths[i - 1].add(f"{start2} {end1} 3")

start_status1 = stats(votes[1][0], votes[1][1])
start_status2 = stats(votes[0][2], votes[0][3])

for status in list(set([start_status1, start_status2])):
    counter[0][f"{status}_0"] = 1

for i in range(1, len(paths) + 1):
    for path in paths[i - 1]:
        start, end, path_type = path.split()
        counter[i][end] += counter[i - 1][start]

print(paths)
print(counter)
print(sum(counter[n - 1].values()))
