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

int modulo(string s, int mod) {
    int res = 0;
    for (int i = 0; i < s.size(); i++) {
        res = (res * 10 + s[i] - '0') % mod;
    }
    return res;
}


int main(){
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int mod = 10000007;
    vector<int> mod_a(n);
    std::map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int a_mod = a[i] % mod;
        mod_a[i] = a_mod;
        mp[a_mod]++;
    }

    int ans = 0;
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            int mod_aij = (mod_a[i] * mod_a[j]) % mod;
            ans += mp[mod_aij];
        }
    }
    count << ans << endl;
}