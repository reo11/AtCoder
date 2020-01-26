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
}#include <bits/stdc++.h>
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