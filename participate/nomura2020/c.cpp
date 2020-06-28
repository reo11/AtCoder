#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
using ll = long long;
using P = pair<ll, ll>;

const ll infll = (1LL << 62) - 1;
const int inf = (1 << 30) - 1;

struct IoSetup {
    IoSetup() {
        cin.tie(nullptr);
        ios::sync_with_stdio(false);
        cout << fixed << setprecision(10);
        cerr << fixed << setprecision(10);
    }
} iosetup;

template< typename T1, typename T2 >
inline bool chmax(T1 &a, T2 b) { return a < b && (a = b, true); }

template< typename T1, typename T2 >
inline bool chmin(T1 &a, T2 b) { return a > b && (a = b, true); }

void fail() {
    cout << -1 << endl;
    exit(0);
}

int main(){
    ll n;
    cin >> n;
    ll a[n+1];
    for(ll i=0; i < n+1; i++){
        cin >> a[i];
    }
    ll INF = infll;
    if(n == 0 && a[0] == 0){
        fail();
    }
    ll max_i[n+1];
    max_i[0] = 1;
    for(ll i=1; i < n+1; i++){
        if(max_i[i-1] * 2 - a[i] < INF){
            max_i[i] = max_i[i-1] * 2 - a[i];
        }else{
            max_i[i] = INF;
        }
    }
    for(ll i=1; i < n+1; i++){
        max_i[i] += a[i];
    }

    ll cnt = 0;
    ll pre_cnt = 0;
    for(ll i = 0; i < n+1; i++){
        ll idx = n - i;
        ll v = a[idx];
        if(v+ceil(pre_cnt/2.0) > max_i[idx]){
            fail();
        }
        pre_cnt = min(v+pre_cnt, max_i[idx]);
        cnt += pre_cnt;
    }
    cout << cnt << endl;
}