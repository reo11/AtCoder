from collections import defaultdict
n, x, y = map(int, input().split())

def process(color, level):
    if level <= 1:
        if color == "red":
            return 0
        else:
            return 1

stones = defaultdict(lambda: defaultdict(lambda: 0))
stones["red"][n] = 1
level = n
while level >= 2:
    if stones["red"][level] > 0:
        stones["red"][level - 1] += stones["red"][level]
        stones["blue"][level] += stones["red"][level] * x
        stones["red"][level] = 0
    if stones["blue"][level] > 0:
        stones["red"][level - 1] += stones["blue"][level]
        stones["blue"][level - 1] += stones["blue"][level] * y
        stones["blue"][level] = 0
    level -= 1
print(stones["blue"][1])