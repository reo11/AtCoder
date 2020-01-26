#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define MOD 1000000007

ll rep_sqr(ll base, ll k){
    if(k == 0){
        return 1;
    }else if(k % 2 == 0){
        ll p = rep_sqr(base, k / 2);
        return (p * p) % MOD;
    }else{
        return (rep_sqr(base, k - 1) * base) % MOD;
    }
}

ll inv(ll a){
    return rep_sqr(a, MOD-2);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll facts[1000001];
    facts[0] = 1;
    facts[1] = 1;

    ll x, y;
    cin >> x >> y;

    ll r = 0, u = 0;
    while(x > 0 || y > 0){
        if(x > y){
            r ++;
            x -= 2;
            y -= 1;
        }else{
            u ++;
            y -= 2;
            x -= 1;
        }
    }

    for(ll i=2; i <= u+r; i++){
        facts[i] = (facts[i-1] * i) % MOD;
    }

    ll ans = 0;
    if(x == 0 && y == 0){
        ans = (((facts[r + u] * inv(facts[r])) % MOD) * inv(facts[u])) % MOD;
        cout << ans << endl;
    }else{
        cout << ans << endl;
    }
}
