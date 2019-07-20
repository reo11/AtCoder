// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long, long long> LP;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for(ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i <= ll(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) sort(ALL(v));v.erase(unique(ALL(v)), v.end());
#define SIZE(x) ((ll)(x).size())
#define REVERSE(v) reverse(ALL(v))
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
    ll x, y;
    in >> x >> y;

    vector<ll> g1 = {1, 3, 5, 7, 8, 10, 12};
    vector<ll> g2 = {4, 6, 9, 11};
    vector<ll> g3 = {2};

    ll xg, yg;
    REP(i, g1.size()){
        if(g1[i] == x) xg = 1;
        if(g1[i] == y) yg = 1;
    }
    REP(i, g2.size()){
        if(g2[i] == x) xg = 2;
        if(g2[i] == y) yg = 2;
    }
    REP(i, g3.size()){
        if(g3[i] == x) xg = 3;
        if(g3[i] == y) yg = 3;
    }
    if(xg == yg) out << "Yes" << endl;
    else out << "No" << endl;
}
