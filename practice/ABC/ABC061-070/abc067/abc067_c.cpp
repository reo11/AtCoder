// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long, long long> LP;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for(int i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (int i = int(a); i <= int(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) sort(ALL(v));v.erase(unique(ALL(v)), v.end());
#define SIZE(x) ((ll)(x).size())
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
    vector<ll> a(n);
    ll a_tmp;
    in >> a[0];
    REP(i, n-1){
        in >> a_tmp;
        a[i+1] = a[i] + a_tmp;
    }
    ll a_max = a[n-1];
    ll ans = 1e10;
    REP(i, n-1){
        ans = min(ans, abs((a_max - a[i]) - a[i]));
    }
    out << ans << endl;
}
