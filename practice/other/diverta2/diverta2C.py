n = int(input())
a = [int(i) for i in input().split()]
a.sort()

out = ""

# 1つをプラス or 1つをマイナスにする

# 1. 全部がプラス、2. 全部がマイナスの場合
# 1. 最小の数をマイナスにして、それ以外はプラス
# 2. 最大の数をそのままにして、それ以外をマイナス


# マイナスとプラスが混ざっている場合
# 絶対値が小さいものを負の要素にし、それ以外を正にする

