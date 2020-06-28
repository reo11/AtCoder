// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define M 1000000007

ll fac[1000000002]; //n!(mod M)
ll ifac[1000000002]; //k!^{M-2} (mod M)
//a,bの範囲的にこれだけ配列を用意していけば十分

ll mpow(ll x, ll n){ //x^n(mod M) ←普通にpow(x,n)では溢れてしまうため，随時mod計算
    ll ans = 1;
    while(n != 0){
        if(n&1) ans = ans*x % M;
        x = x*x % M;
        n = n >> 1;
    }
    return ans;
}

ll comb(ll a, ll b){ //aCbをmod計算
    if(a == 0 && b == 0)return 1;
    if(a < b || a < 0)return 0;
    ll tmp = ifac[a-b]* ifac[b] % M;
    return tmp * fac[a] % M;
}

int main()
{
    ll n,a,b;
    cin >> n >> a >> b;

    fac[0] = 1;
    ifac[0] = 1;
    for(ll i = 0; i<1000000003; i++){
        fac[i+1] = fac[i]*(i+1) % M; // n!(mod M)
        ifac[i+1] = ifac[i]*mpow(i+1, M-2) % M; // k!^{M-2} (mod M) ←累乗にmpowを採用
    }


    ll ans=0;
    ans = comb(n+1, n)%M;
    ans -= comb(a, n+1)%M;
    ans -= comb(b, n+1)%M;
    cout << ans << endl;
    return 0;
}