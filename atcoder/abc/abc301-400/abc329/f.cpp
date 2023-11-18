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

    ll n, q;
    in >> n >> q;
    ll c[n] = {};
    vector<tuple<set<ll>, ll>> boxes(n);
    set<ll> uniq_colors;
    vector<ll> color_counter(n + 1);

    REP(i, n){
        in >> c[i];
        color_counter[c[i]]++;
        boxes[i] = make_tuple(set<ll>(), 0);
    }
    REP(i, n){
        if (color_counter[c[i]] == 1) {
            uniq_colors.insert(c[i]);
            get<1>(boxes[i])++;
        } else {
            get<0>(boxes[i]).insert(c[i]);
        }
    }

    ll a, b;
    vector<ll> ans;
    REP(i, q){
        in >> a >> b;
        a--;
        b--;
        for (auto ite = get<0>(boxes[a]).begin(); ite != get<0>(boxes[a]).end(); ite++) {
            get<0>(boxes[b]).insert(*ite);
        }
        get<1>(boxes[b]) += get<1>(boxes[a]);
        get<0>(boxes[a]).clear();
        get<1>(boxes[a]) = 0;
        ans.push_back(get<0>(boxes[b]).size() + get<1>(boxes[b]));
    }
   
    REP(i, ans.size()){
        out << ans[i] << endl;
    }
}
