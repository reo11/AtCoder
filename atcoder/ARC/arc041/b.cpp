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

ll dxy[4][2] = {
    {1, 0},
    {-1, 0},
    {0, 1},
    {0, -1}
};

int main(){
    ll n, m;
    cin >> n >> m;
    string s;
    ll a[n][m] = {};
    ll ans[n][m] = {};
    for(ll i=0; i < n; i++){
        cin >> s;
        for(ll j=0; j < m; j++) a[i][j] = s[j] - '0';
    }

    for(ll i=1; i < n-1; i++){
        for(ll j=1; j < m-1; j++){
            ll num = inf;
            for(ll k=0; k < 4; k++){
                chmin(num, a[i+dxy[k][0]][j+dxy[k][1]]);
            }
            for(ll k=0; k < 4; k++){
                a[i+dxy[k][0]][j+dxy[k][1]] -= num;
            }
            ans[i][j] += num;
        }
    }
    for(ll i=0; i < n; i++){
        for(ll j=0; j < m; j++){
            cout << ans[i][j];
        }
        cout << endl;
    }
}