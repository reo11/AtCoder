MAX = 10**18
n = int(input())
a = list(map(int, input().split()))

values = [MAX]

for ai in a:
    values.append(values[-1] + ai)

min_value = min(values)
for i in range(len(values)):
    values[i] -= min_value
print(values[-1])
