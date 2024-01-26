n = int(input())

# nの5進数を考える
def base_5(n):
    ans = []
    if n == 0:
        return [0]
    while n > 0:
        ans.append(n % 5)
        n //= 5
    return ans[::-1]


mapping = [0, 2, 4, 6, 8]
ans = int("".join(map(str, [mapping[x] for x in base_5(n - 1)])))
print(ans)
