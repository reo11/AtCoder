from collections import defaultdict

n = int(input())
a = [int(input()) for _ in range(n)]
hash_keys = [8191, 131071, 524287, 998244353, 1000000007, 2147483647]
hashes = [[0 for _ in range(len(hash_keys))] for _ in range(n)]
hashes_set = [defaultdict(lambda: []) for _ in range(len(hash_keys))]

# setに入れる
for i in range(n):
    for j in range(len(hash_keys)):
        mod = a[i] % hash_keys[j]
        hashes[i][j] = mod
        hashes_set[j][mod].append(i)
ans = 0
for i in range(n):
    for j in range(n):
        ansi = []
        for k in range(len(hash_keys)):
            hash_key = hash_keys[k]
            mod_i = hashes[i][k]
            mod_j = hashes[j][k]
            mod_k = (mod_i * mod_j) % hash_key
            ansi.append(len(hashes_set[k][mod_k]))
        ans += min(ansi)
print(ans)
                
            
        
        