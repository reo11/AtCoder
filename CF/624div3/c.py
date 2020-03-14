t = int(input())
ans = []
for _ in range(t):
    n, m = map(int, input().split())
    s = str(input())
    p = list(map(int, input().split()))
    cnt = m + 1
    pp = [0 for _ in range(n)]
    for i in p:
        pp[i-1] += 1
    out = [0 for _ in range(26)]
    for i in range(n):
        out[ord(s[i]) - ord('a')] += cnt
        cnt -= pp[i]
    ans.append(" ".join(list(map(str, out))))
print("\n".join(ans))
