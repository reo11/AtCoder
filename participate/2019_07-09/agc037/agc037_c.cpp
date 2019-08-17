// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long int, long long int> lp;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for(ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i <= ll(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) sort(ALL(v));v.erase(unique(ALL(v)), v.end());
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
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
ll lcm(ll a,ll b){return (a / gcd(a, b)) * b;}
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
#define out cout
#define in cin
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
// template end

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    in >> n;
    ll a[n];
    ll b[n];
    REP(i, n){
        in >> a[i];
    }
    REP(i, n){
        in >> b[i];
    }
    priority_queue<pair<ll, ll> > q;
    ll cnt = 0;
    REP(i, n){
        q.push(lp(b[i], i));
    }

    ll idx, p_idx, n_idx;
    ll minus, times;
    ll pre_idx = -1;
    while(!q.empty()){
        idx = q.top().second;
        q.pop();

        if(b[idx] == a[idx]) continue;
        p_idx = idx - 1;
        n_idx = idx + 1;
        if(p_idx == -1) p_idx = n - 1;
        if(n_idx == n) n_idx = 0;

        times = 1;
        minus = b[p_idx] + b[n_idx];
        if(b[idx] - minus <= 0 or pre_idx == idx){
            out << "-1" << endl;
            return 0;
        }
        times = min((b[idx] - a[idx]) / minus, ll(ceil((b[idx] - minus) / double(minus))));

        b[idx] -= minus * times;
        // out << idx << " " << b[idx] << endl;
        cnt += times;
        pre_idx = idx;
        if(b[idx] == a[idx]){
            continue;
        }else{
            q.push(lp(b[idx], idx));
        }
    }
    out << cnt << endl;
}
