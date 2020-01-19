// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long, long long> LP;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i <= ll(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) \
    sort(ALL(v)); \
    v.erase(unique(ALL(v)), v.end());
#define SIZE(x) ((ll)(x).size())
#define REVERSE(v) reverse(ALL(v))
// true / false
#define BIN_SEARCH(v, a) binary_search(ALL(v), a)
// index
#define BIN_LEFT(v, a) (lower_bound(ALL(v), a) - v.begin())
#define BIN_RIGHT(v, a) (upper_bound(ALL(v), a) - v.begin())
#define BIN_INSERT(v, a) (v.insert(v.begin() + BIN_LEFT(v, a), a))
#define DEL(v, i) v.erase(v.begin() + i)
#define INSERT(v, i, a) v.insert(v.begin() + i, a)
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
#define out cout
#define in cin
template <class T>
bool chmax(T &a, const T &b)
{
    if (a < b)
    {
        a = b;
        return 1;
    }
    return 0;
}
template <class T>
bool chmin(T &a, const T &b)
{
    if (b < a)
    {
        a = b;
        return 1;
    }
    return 0;
}
// template end
ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
ll lcm(ll a, ll b) { return (a / gcd(a, b)) * b; }
// Returns LCM of array elements
long long rep_sqr(long long a, long long n)
{
    if(n == 0){
        return 1;
    }
    if(n % 2 == 0){
        ll p = rep_sqr(a, ll(n / 2));
        return (p * p) % MOD;
    }else{
        return (rep_sqr(a, n - 1) * a) % MOD;
    }
}

long long inv(long long a)
{
    return rep_sqr(a, MOD - 2);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    in >> n;
    ll a[n];
    REP(i, n){
        in >> a[i];
    }
    ll lcm_ = a[0];
    REP(i, n){
        lcm_ = lcm(lcm_, a[i]);
    }
    ll b[n];
    REP(i, n){
        b[i] = (lcm_ % MOD) * (inv(a[i]) % MOD);
    }
    ll ans = 0;
    REP(i, n){
        ans += b[i];
        ans %= MOD;
    }
    out << ans << endl;
}