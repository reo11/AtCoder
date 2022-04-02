import itertools

for n in range(2, 6):
    for m in range(2, 6):
        for k in range(2, n * m + 1):
            seq = []
            A = list(range(n))
            B = list(range(m))
            for a, b in list(itertools.product(A, B)):
                seq.append((a, b))
            comb_sum = 0
            for comb in list(itertools.combinations(seq, k)):
                for x in list(itertools.combinations(comb, 2)):
                    comb_sum += abs(x[0][0] - x[1][0]) + abs(x[0][1] - x[1][1])
            print("n:{} m:{} k:{}: result:{}".format(n, m, k, comb_sum))
        print("\n\n")
