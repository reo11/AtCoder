n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# N < 1000
# a_i -> a_i + x mod yでb_iを作る
# 基準を決めて、そこに合わせるようにmod操作をすれば良い
# 最小と最大の