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

// from https://qiita.com/drken/items/ae02240cd1f8edfc86fd
inline long long mod(long long a, long long m) {
    long long res = a % m;
    if (res < 0) res += m;
    return res;
}

long long extGCD(long long a, long long b, long long &p, long long &q) {
    if (b == 0) { p = 1; q = 0; return a; }
    long long d = extGCD(b, a%b, q, p);
    q -= a/b * p;
    return d;
}

long long modinv(long long a, long long m) {
    long long x, y;
    extGCD(a, m, x, y);
    return mod(x, m);
}

long long Garner(vector<long long> b, vector<long long> m, long long MOD) {
    m.push_back(MOD); // banpei
    vector<long long> coeffs((int)m.size(), 1);
    vector<long long> constants((int)m.size(), 0);
    for (int k = 0; k < (int)b.size(); ++k) {
        long long t = mod((b[k] - constants[k]) * modinv(coeffs[k], m[k]), m[k]);
        for (int i = k+1; i < (int)m.size(); ++i) {
            (constants[i] += t * coeffs[i]) %= m[i];
            (coeffs[i] *= m[k]) %= m[i];
        }
    }
    return constants.back();
}

int main(){
    ll n, a, b, c, d;
    ll mod = 998244353;
    cin >> n >> a >> b >> c >> d;
    vector<ll> b_vec(n);
    vector<ll> m_vec(n);
    for(ll i=0; i<n; i++){
        b_vec[i] = (a + i * b) % (c + i * d);
        m_vec[i] = (c + i * d);
    }
    ll ans = Garner(b_vec, m_vec, mod) % mod;
    for (ll i = 0; i < n; ++i) {
        // cout << ans << " " << b_vec[i] << " " << m_vec[i] << endl;
        if ((ans % m_vec[i]) != b_vec[i] % mod) {
            ans = -1;
            break;
        }
    }
    cout << ans << endl;
}