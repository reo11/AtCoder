n = int(input())
ans = [i for i in range(n + 1)]
ans.sort(reverse=True)
print(*ans, sep="\n")