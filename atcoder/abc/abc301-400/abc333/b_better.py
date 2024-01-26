from collections import defaultdict

s = input()
t = input()

# N角形まで
N = 5
groups = defaultdict(lambda: set())
for start in range(ord("A"), ord("A") + N):
    for end in range(ord("A"), ord("A") + N):
        if start == end:
            continue
        start_alphabet = chr(start)
        end_alphabet = chr(end)
        length = min(abs(start - end), N - abs(start - end))
        groups[length].add(f"{start_alphabet}{end_alphabet}")

ans = False
for length in groups.keys():
    if s in groups[length] and t in groups[length]:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
