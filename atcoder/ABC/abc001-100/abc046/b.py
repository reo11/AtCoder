n, k = map(int, input().split())

ans = 1

ans *= k
ans *= (k-1)**(n-1)
print(ans)