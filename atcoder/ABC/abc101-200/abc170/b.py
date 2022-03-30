x, y = map(int, input().split())

for kame in range(100):
   for turu in range(100):
      if kame + turu == x and kame * 4 + turu * 2 == y:
         print("Yes")
         exit()
print("No")