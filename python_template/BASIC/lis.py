# Longest Increasing Subsequence
# 最長増加部分列
import bisect

def lis(seq):
    LIS = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

    return len(LIS)