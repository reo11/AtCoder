#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int64_t gcd(int64_t a, int64_t b){
    while(b > 0){
        int64_t tmp = a;
        a = b;
        b = tmp % b;
    }
    return a;
}

void solve(){
    int64_t k, ans = 0;
    cin >> k;
    for(int64_t i = 1; i <= k; i++){
        for(int64_t j = 1; j <= k; j++){
            for(int64_t l = 1; l <= k; l++){
                ans += gcd(gcd(i, j), l);
            }
        }
    }
    cout << ans << endl;
}

int main(){
    solve();
}