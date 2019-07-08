import numpy as np
import math
n, d = map(int, input().split())
x = []
for i in range(n):
    x.append(np.array(list(map(int, input().split()))))

count = 0
for i in range(n):
    for j in range(n):
        if i != j:
            d = np.linalg.norm(x[i] - x[j])
            if math.floor(d) == d:
                count += 1
print(count//2)
