#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007

int64_t modPow(int64_t a, int64_t n, int64_t p) {
    int64_t ret = 1;
    while(n > 0){
        if(n & 1){
            ret = (ret * a) % p;
        }
        a = (a * a) % p;
        n >>= 1;
    }
    return ret % p;
}

void solve(){
    int64_t n, k;
    cin >> n >> k;

    int64_t gcd[k+1];
    for(int64_t i = 0; i <= k; i++){
        gcd[i] = 0;
    }

    int64_t g, ans = 0;
    for(int64_t i = k; i >= 1; i--){
        g = k / i;
        gcd[i] = modPow(g, n, MOD);
        for(int64_t j = i * g; j > i; j -= i){
            gcd[i] -= gcd[j];
        }
        ans += gcd[i] * i;
        ans %= MOD;
    }
    while(ans < 0){
        ans += MOD;
    }
    cout << ans << endl;
}

int main(){
    solve();
}