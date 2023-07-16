l, r = map(int, input().split())

list_ = []
c = 0

while c < 2019:
    if c > r - l:
        break
    list_.append((l + c) % 2019)
    c += 1

list_.sort()
ans = 1000000
for i in range(len(list_)):
    for j in range(len(list_)):
        if i != j:
            ans = min(ans, (list_[i] * list_[j]) % 2019)
print(ans)
