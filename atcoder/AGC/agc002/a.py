a, b = map(int, input().split())

if a <= 0 and 0 <= b:
   print("Zero")
   exit()

cnt_neg = min(0, b) - a
if cnt_neg % 2:
   print("Positive")
else:
   print("Negative")