n = int(input())
c = sorted(list(map(int, input().split())), reverse=True)
p = 10**9+7
print(sum([(i+2) * c[i] for i in range(n)]) * pow(4, n-1, p) % p)