# 括弧の対応を取った後に深いところから処理していく？
from collections import deque
s = input()

stack = deque([])
for i in list(s):
    