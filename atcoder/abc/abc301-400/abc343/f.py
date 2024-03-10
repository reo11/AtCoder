import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, q = map(int, input().split())
A = list(map(int, input().split()))

queries = []

for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# その区間の最大値とその数を取得できるようなセグメントツリーを作成
class SegTree:
    def __init__(self, n: int) -> None:
        self.tree_size = 2 ** (n - 1).bit_length()  # n以上の最小の2のべき乗数
        self.tree_value = [[(0, 1)] for _ in range(2 * self.tree_size)]

    def init(self, init_val) -> None:
        for i in range(len(init_val)):
            self.tree_value[i + self.tree_size - 1] = init_val[i]
        # built
        for i in range(self.tree_size - 2, -1, -1):
            self.tree_value[i] = self._op(
                self.tree_value[2 * i + 1], self.tree_value[2 * i + 2]
            )

    def _op(self, a: list, b: list) -> list:
        # aの後ろ2つとbの後ろ2つを取得
        # a, b合わせて2番目までに大きい数を取得して出力
        # a, bは降順ソートされているものとする
        counter = dict()
        for i in range(min(2, len(a))):
            if a[i][0] != 0:
                if a[i][0] not in counter:
                    counter[a[i][0]] = 0
                counter[a[i][0]] += a[i][1]
        for i in range(min(2, len(b))):
            if b[i][0] != 0:
                if b[i][0] not in counter:
                    counter[b[i][0]] = 0
                counter[b[i][0]] += b[i][1]
        response = [(num, counter[num]) for num in sorted(counter.keys(), reverse=True)[:2]]
        return response

    def update(self, pos: int, value: int) -> None:
        pos += self.tree_size - 1
        self.tree_value[pos] = value
        while pos:
            pos = (pos - 1) // 2
            self.tree_value[pos] = self._op(
                self.tree_value[pos * 2 + 1], self.tree_value[pos * 2 + 2]
            )

    def query(self, l: int, r: int) -> int:
        r += 1
        if r <= l:
            return []
        l += self.tree_size - 1
        r += self.tree_size - 2
        res = []
        while r - l > 1:
            if l & 1 == 0:
                res = self._op(res, self.tree_value[l])
            if r & 1 == 1:
                res = self._op(res, self.tree_value[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        if l == r:
            res = self._op(res, self.tree_value[l])
        else:
            res = self._op(self._op(res, self.tree_value[l]), self.tree_value[r])
        return res

tree = SegTree(n)
init_values = []

for ai in A:
    init_values.append([(ai, 1)])
tree.init(init_values)

ans = []
for query_type, x, y in queries:
    if query_type == 1:
        tree.update(x - 1, [(y, 1)])
    else:
        ret = tree.query(x - 1, y - 1)
        if len(ret) <= 1:
            ans.append(str(0))
        else:
            ans.append(str(ret[1][1]))
# print(tree.tree_value)
print("\n".join(ans))
