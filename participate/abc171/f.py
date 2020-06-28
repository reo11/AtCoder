k = int(input())
s = input()
MOD = 10**9+7

class Facts():
   # O(max_num)
   def __init__(self, max_num=10**5, p=10**9+7):
      self.p = p
      self.max_num = max_num
      self.fact = [1] * (self.max_num + 1)
      self.rev = [1] * (self.max_num + 1)
      for i in range(1, self.max_num + 1):
         self.fact[i] = (self.fact[i-1] * i) % self.p
      self.rev[self.max_num] = self.mod_pow(self.fact[self.max_num], self.p-2)
      for i in range(self.max_num-1, 0, -1):
         self.rev[i] = self.rev[i+1] * (i + 1) % self.p

   def comb(self, n, k):
      if n < 0 or k < 0 or n < k:
         return 0
      if n == 0 or k == 0:
         return 1
      res = ((self.fact[n] * self.rev[k] % self.p) * self.rev[n - k]) % self.p
      return res

   def comb_base(self, n, k):
      if n < 0 or k < 0 or n < k:
         return 0
      if n == 0 or k == 0:
         return 1
      a, b = 1, 1
      for i in range(k):
         a *= (n-i)
         a %= MOD
      for i in range(k):
         b *= (k-i)
         b %= MOD
      return (a*self.mod_pow(b, self.p-2)) % self.p

   def perm(self, n, k):
      if n < 0 or k < 0 or n < k:
         return 0
      if n == 0 or k == 0:
         return 1
      a = self.fact[n]
      b = self.fact[n-k]
      return (a * self.mod_pow(b, self.p-2)) % self.p

   def mod_pow(self, a, b):
      ans = 1
      while b > 0:
         if b & 1:
            ans = ans * a % self.p
         a = a * a % self.p; b >>= 1
      return ans

r26 = [1 for _ in range(k + 1)]
r25 = [1 for _ in range(k + 1)]
for i in range(1, k+1):
   r26[i] = (r26[i-1] * 26) % MOD
   r25[i] = (r25[i-1] * 25) % MOD
facts = Facts(max_num=len(s)+k+1, p=MOD)

total = len(s) + k
ans = 0
for s_n in range(len(s), total+1):
   d = total - s_n
   ans += facts.comb(total - d - 1, len(s) - 1) * r25[k-d] * r26[d]
   ans %= MOD

print(ans)
