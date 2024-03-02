from collections import defaultdict

n = int(input())
s = list(input())
q = int(input())
cd = []
mapping_rules = defaultdict(lambda: "")
for i in range(26):
    mapping_rules[chr(ord("a") + i)] = chr(ord("a") + i)

for _ in range(q):
    c, d = input().split()
    for i in range(26):
        if mapping_rules[chr(ord("a") + i)] == c:
            mapping_rules[chr(ord("a") + i)] = d

def mapping(s, mapping_rules):
    return "".join([mapping_rules[si] for si in s])

ans = mapping(s, mapping_rules)
print(ans)
