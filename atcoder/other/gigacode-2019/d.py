class TwoDimSum:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.counts = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
        self.s = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    def add_count(self, x, y, v):
        # 1-indexed
        self.counts[y][x] += v

    def build(self):
        for i in range(self.h):
            for j in range(self.w):
                self.s[i + 1][j + 1] = (
                    self.s[i][j + 1]
                    + self.s[i + 1][j]
                    - self.s[i][j]
                    + self.counts[i + 1][j + 1]
                )

    def solve(self, x1, y1, x2, y2):
        # 1-indexed
        # (x1, y1): left up
        # (x2, y2): right down
        return (
            self.s[x2][y2]
            - self.s[x1 - 1][y2]
            - self.s[x2][y1 - 1]
            + self.s[x1 - 1][y1 - 1]
        )


h, w, k, v = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]

twodim = TwoDimSum(h, w)
for i in range(h):
    for j in range(w):
        twodim.add_count(j + 1, i + 1, a[j][i])
twodim.build()

# for i in range(1, h+1):
#     for j in range(1, w+1):
