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
    vector<ll> a(n, 0);
    for(ll i=0; i < n; i++) cin >> a[i];
    vector<ll> s(n+1, 0);

    for(ll i=1; i <= n; i++){
        s[i] = s[i-1] + a[i-1];
    }

    ll ans = 0, pre = -10000000000000, cnt = 1;
    sort(s.begin(), s.end());
    for(ll i=0; i <= n; i++){
        if(pre == s[i]){
            cnt += 1;
        }else{
            ans += (cnt * (cnt - 1) / 2);
            cnt = 1;
            pre = s[i];
        }
    }
    ans += (cnt * (cnt - 1) / 2);
    cout << ans << endl;
}