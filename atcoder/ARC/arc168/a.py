n = int(input())
s = list(input())

# https://output-zakki.com/inversion_number/
class BIT:
    def __init__(self, n):
        self.size=n
        self.tree = [0] * (n+1)
    
    def add(self, i,x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

def InversionNumberByBIT(A):
    ans = 0
    Bit = BIT(max(len(A) + 1, max(A) + 1))
    for i in range(len(A)):
        ans += i - Bit.sum(A[i])
        Bit.add(A[i], 1)
    return ans

counter = []
# ">"が連続する数を数える
count = 0
for i in reversed(range(len(s))):
    counter.append(count)
    if s[i] == ">":
        count += 1
    else:
        count = 0
counter.append(count)
counter = counter[::-1]
counter.append(0)

x = [0]
max_x = 0
for i, si in enumerate(s):
    if si == ">":
        x.append(x[-1] - 1)
    else:
        x.append(max_x + counter[i + 1] + 1)
    max_x = max(max_x, x[-1])
min_x = min(x)
for i in range(len(x)):
    x[i] -= min_x
    x[i] += 1
# print(counter)
# print(x)
print(InversionNumberByBIT(x))