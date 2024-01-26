from collections import defaultdict

n = int(input())
process = defaultdict(lambda: [])

for i in range(n):
    bin_i = list(str(bin(i)[2:]))
    bin_i.reverse()
    for j, b in enumerate(bin_i):
        if b == "1":
            process[j].append(i + 1)

out = []
for pi in process.values():
    outi = f"{len(pi)} "
    outi += " ".join(list(map(str, pi)))
    out.append(outi)
print(len(out), flush=True)
print(*out, sep="\n", flush=True)

response = list(input())
response.reverse()
response = "".join(response)
x = int(response, 2) + 1

print(x, flush=True)
