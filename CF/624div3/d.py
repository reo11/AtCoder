t = int(input())
ans = []
for _ in range(t):
    a, b, c = map(int, input().split())
    out = 10**9
    out_l = [a, b, c]
    for A in range(1, 2*a):
        B = A
        while B <= 2*b:
            C = int(c/B) * B
            cost = abs(a - A) + abs(b - B) + abs(c - C)
            if cost < out:
                out = cost
                out_l = [A, B, C]
            cost = abs(a - A) + abs(b - B) + abs(c - (C + B))
            if cost < out:
                out = cost
                out_l = [A, B, C+B]
            B += A
    ans.append(str(out))
    ans.append(" ".join(list(map(str, out_l))))
print("\n".join(ans))