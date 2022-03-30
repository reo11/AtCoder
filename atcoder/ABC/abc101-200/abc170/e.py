from heapq import heapify, heappop, heappush
import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

class RMQ:
    def __init__(self, n, e):
        # 単位元
        self.e = e
        # num_min:n以上の最小の2のべき乗
        self.num_min =2**(n-1).bit_length()
        self.seg_min=[self.e]*2*self.num_min

    def init_min(self, init_min_val):
        #初期値が指定されている場合
        #set_val
        for i in range(n):
            self.seg_min[i+self.num_min-1]=init_min_val[i]
        #built
        for i in range(self.num_min-2,-1,-1) :
            self.seg_min[i]=min(self.seg_min[2*i+1],self.seg_min[2*i+2])

    def update_min(self, k, x):
        k += self.num_min-1
        self.seg_min[k] = x
        while k:
            k = (k-1)//2
            self.seg_min[k] = min(self.seg_min[k*2+1],self.seg_min[k*2+2])

    def query_min(self, p, q):
        q += 1
        if q<=p:
            return self.e
        p += self.num_min-1
        q += self.num_min-2
        res=self.e
        while q-p>1:
            if p&1 == 0:
                res = min(res,self.seg_min[p])
            if q&1 == 1:
                res = min(res,self.seg_min[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = min(res,self.seg_min[p])
        else:
            res = min(min(res,self.seg_min[p]),self.seg_min[q])
        return res

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(q)]

EN_MAX = 2*10**5+1
en = [[] for _ in range(EN_MAX)]
rate = defaultdict(lambda: 0)
syozoku = defaultdict(lambda: None)
for i in range(n):
   a, b = ab[i]
   rate[i+1] = a
   syozoku[i+1] = b
   heappush(en[b], (a, i+1))

e = (2**31) - 1
rmq = RMQ(EN_MAX, e)
ans = []
for i in range(EN_MAX):
   if len(en[i]) > 0:
      rmq.update_min(i, en[i][0][0])

for i in range(q):
   c, d = cd[i]
   pre_s = syozoku[c]
   # 最小値の取り出し（更新）
   min_v = e
   while len(en[pre_s]) > 0:
      if syozoku[en[pre_s][0][1]] == pre_s:
         min_v = en[pre_s][0][0]
         break
      else:
         heappop(en[pre_s])
   cur_min = rmq.query_min(pre_s, pre_s)
   rmq.update_min(pre_s, min(cur_min, min_v))
   # 挿入
   syozoku[c] = d
   heappush(en[d], (rate[c], c))
   cur_min = rmq.query_min(d, d)
   rmq.update_min(d, min(cur_min, rate[c]))
   ans.append(str(rmq.query_min(0, EN_MAX)))
print("\n".join(ans))

