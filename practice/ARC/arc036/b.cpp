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
    vector<ll> h(n);
    for(ll i=0; i < n; i++) cin >> h[i];
    // 左右からメモしておく
    vector<ll> l(n+1, 0), r(n+1, 0);
    ll cnt = 0;
    for(ll i=1; i < n; i++){
        if(h[i-1] < h[i]){
            cnt += 1;
        }else{
            cnt = 0;
        }
        l[i] = cnt;
    }
    cnt = 0;
    for(ll i=n-1; i > 0; i--){
        if(h[i-1] > h[i]){
            cnt += 1;
        }else{
            cnt = 0;
        }
        r[i-1] = cnt;
    }
    ll ans = 0;
    for(ll i=0; i < n; i++){
        chmax(ans, r[i] + l[i] + 1);
    }
    // for(ll i=0; i < n; i++) cout << l[i] << " ";
    // cout << endl;
    // for(ll i=0; i < n; i++) cout << r[i] << " ";
    // cout << endl;
    cout << ans << endl;
}