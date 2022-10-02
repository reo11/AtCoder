import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = []
for i in range(N):
    AB.append([A[i], B[i]])
AB.sort()

def lis(seq):
    LIS = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > LIS[-1]:
            LIS.append(seq[i])
        else:
            LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

    return len(LIS)

B_dash = []
for i in range(N):
    B_dash.append(AB[i][1])
print(N + lis(B_dash))
