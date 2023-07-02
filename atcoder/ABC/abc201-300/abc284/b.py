t = int(input())
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for a_i in a:
        if a_i % 2 == 1:
            count += 1
    return count

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep='\n')