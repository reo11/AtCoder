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
    vector<ll> a(n);
    double mean=0;
    for(ll i=0; i < n; i++){
        cin >> a[i];
        mean += a[i] / double(n);
    }
    double ans_d = 1000000.0;
    ll ans_i = 0;
    for(ll i=0; i < n; i++){
        if(ans_d > abs(mean - a[i])){
            ans_i = i;
            ans_d = abs(mean - a[i]);
        }
    }
    cout << ans_i << endl;
}