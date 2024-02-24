from typing import Callable, List


class SegTree:
    def __init__(self, n: int, e: int, op: Callable) -> None:
        """
        Args:
            n (int): 要素数
            e (int): 単位元
            op (Callable): 演算
        """
        self.n = n
        self.e = e
        self.lv = (self.n - 1).bit_length()
        self.tree_size = 2**self.lv
        self.tree_value = [self.e] * (2 * self.tree_size)
        self.tree_lazy = [None] * (2 * self.tree_size)
        self._op = op

    def gindex(self, l, r):
        """
        lazy load
        Args:
            l (_type_): _description_
            r (_type_): _description_
        Yields:
            _type_: _description_
        """
        L = (l + self.tree_size) >> 1
        R = (r + self.tree_size) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range((self.n - 1).bit_length()):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1
            R >>= 1

    def propagates(self, *ids):
        """lazy load
        """
        for i in reversed(ids):
            v = self.tree_lazy[i - 1]
            if v is None:
                continue
            self.tree_lazy[2 * i - 1] = self.tree_value[2 * i - 1] = self.tree_lazy[
                2 * i
            ] = self.tree_value[2 * i] = v
            self.tree_lazy[i - 1] = None

    def build(self, init_array: List[int]) -> None:
        """
        Use if you have initial values array
        Args:
            init_array (List[int]): array
        """
        for i in range(len(init_array)):
            self.tree_value[i + self.tree_size - 1] = init_array[i]
        # build
        for i in range(self.tree_size - 2, -1, -1):
            self.tree_value[i] = self._op(
                self.tree_value[2 * i + 1], self.tree_value[2 * i + 2]
            )

    def update(self, x: int, value: int) -> None:
        """
        Args:
            x (int): position x
            value (int): value
        """
        # 更新
        self.update_range(l=x, r=x, value=value)

    def update_range(self, l: int, r: int, value: int) -> None:
        """
        [l, r] range update
        Args:
            l (int): left
            r (int): right
            value (int): value
        """
        r += 1
        (*ids,) = self.gindex(l, r)
        self.propagates(*ids)
        L = self.tree_size + l
        R = self.tree_size + r
        while L < R:
            if R & 1:
                R -= 1
                self.tree_value[R - 1] = value
                self.tree_lazy[R - 1] = value
            if L & 1:
                self.tree_value[L - 1] = value
                self.tree_lazy[L - 1] = value
                L += 1
            L >>= 1
            R >>= 1
        for i in ids:
            self.tree_value[i - 1] = self._op(
                self.tree_value[2 * i - 1], self.tree_value[2 * i]
            )

    def query(self, l: int, r: int) -> int:
        """
        [l, r] range query
        Args:
            l (int): left
            r (int): right

        Returns:
            int: _description_
        """
        self.propagates(*self.gindex(l, r))
        L = self.tree_size + l
        R = self.tree_size + r

        s = self.e
        while L < R:
            if R & 1:
                R -= 1
                s = self._op(s, self.tree_value[R - 1])
            if L & 1:
                s = self._op(s, self.tree_value[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return s


if __name__ == "__main__":
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    lr = []
    for _ in range(q):
        l, r = map(int, input().split())
        lr.append((l, r))
    tree = SegTree(n, 10**10, lambda x, y: min(x, y))
    tree.init(a)
    ans = []
    for l, r in lr:
        ans.append(tree.query(l, r))
print(*ans, sep="\n")
