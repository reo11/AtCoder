w, a, b = map(int, input().split())
if a <= b <= a + w or a <= b + w <= a + w:
    print(0)
else:
    print(
        min(
            abs(
                a + w - b,
            ),
            abs(-a + b + w),
        )
    )
