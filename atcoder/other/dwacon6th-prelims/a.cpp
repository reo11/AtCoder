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
    string s[n];
    ll t[n];
    string x;
    for(ll i=0; i < n; i++){
        cin >> s[i] >> t[i];
    }
    cin >> x;
    ll ans = 0;
    bool f = false;
    for(ll i=0; i < n; i++){
        if(f){
            ans += t[i];
        }
        if(x == s[i]){
            f = true;
        }
    }
    cout << ans << endl;
}