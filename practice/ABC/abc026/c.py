n = int(input())

b = [int(input()) for _ in range(n-1)]

member = [[] for _ in range(n)]

for i, j in enumerate(b):
    member[j-1].append(i+1)

def dfs(num):
    if member[num] == []:
        return 1
    else:
        l = []
        for i in member[num]:
            l.append(dfs(i))
        money = max(l) + min(l) + 1
        return money

print(dfs(0))