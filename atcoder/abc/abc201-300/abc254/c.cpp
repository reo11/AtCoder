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
    ll n, k;
    cin >> n >> k;
    vector<ll> a;
    vector<vector<ll>> b(n);

    for(ll i = 0; i < n; i++){
        ll tmp;
        cin >> tmp;
        b[i % k].push_back(tmp);
    }
    for(ll i = 0; i < k; i++){
        sort(b[i].begin(), b[i].end());
    }

    string ans = "Yes";
    ll pre_value = -1;
    for(ll i = 0; i < n; i++){
        if (b[i % k][i / k] < pre_value) {
            ans = "No";
            break;
        }
        pre_value = b[i % k][i / k];
    }
    cout << ans << endl;
}