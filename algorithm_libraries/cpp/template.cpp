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
#define BIN_SEARCH(v, a) binary_search(ALL(v), a)
#define BIN_LEFT(v, a) (lower_bound(ALL(v), a) - v.begin())
#define BIN_RIGHT(v, a) (upper_bound(ALL(v), a) - v.begin())
#define BIN_INSERT(v, a) (v.insert(v.begin() + BIN_LEFT(v, a), a))
#define DEL(v, i) v.erase(v.begin() + i)
#define INSERT(v, i, a) v.insert(v.begin() + i, a)
ll gcd(ll a, ll b)
{
    return b ? gcd(b, a % b) : a;
}
ll lcm(ll a, ll b) { return (a / gcd(a, b)) * b; }
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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n, W;
    in >> n >> W;
    ll w[n + 1] = {};
    ll v[n + 1] = {};
    ll sum_v = 0;

    REP(i, n)
    {
        in >> w[i + 1] >> v[i + 1];
        sum_v += v[i + 1];
    }
    ll dp[n + 1][sum_v + 1] = {};
    REP(i, n + 1)
    REP(j, sum_v + 1) dp[i][j] = INF;
    REP(i, n + 1)
    dp[i][0] = 0;

    REP_AB(i, 1, n)
    {
        REP(j, v[i])
        dp[i][j] = dp[i - 1][j];
        REP_AB(j, v[i], sum_v)
        {
            // dp[n番目][価値jの時] = 価値をjにできる最小のw
            dp[i][j] = dp[i - 1][j];
            if (dp[i - 1][j - v[i]] > W)
                continue;
            dp[i][j] = min(dp[i - 1][j - v[i]] + w[i], dp[i][j]);
        }
    }
    ll ans = 0;
    REP(i, sum_v + 1)
    {
        if (dp[n][i] <= W)
        {
            ans = i;
        }
    }
    out << ans << endl;
}
