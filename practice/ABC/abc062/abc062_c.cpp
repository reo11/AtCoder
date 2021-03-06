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

ll calc(ll g, ll b, ll r){
    return max(g, max(b, r)) - min(g, min(b, r));
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll h, w, gh, gw, bh, bw, rh, rw, score = INF;
    in >> h >> w;
    REP(i, h-1){
        gh = i + 1;
        gw = w;

        bw = w;
        rw = w;
        bh = int((h - gh) / 2.0);
        rh = h - gh - bh;
        chmin(score, calc(gh*gw, bh*bw, rh*rw));

        bw = int(w / 2.0);
        rw = w - bw;
        bh = h - gh;
        rh = h - gh;
        chmin(score, calc(gh*gw, bh*bw, rh*rw));
    }
    REP(i, w-1){
        gw = i + 1;
        gh = h;
    
        bw = int((w - gw) / 2.0);
        rw = w - gw - bw;
        bh = h;
        rh = h;
        chmin(score, calc(gh*gw, bh*bw, rh*rw));

        bw = w - gw;
        rw = w - gw;
        bh = int(h / 2.0);
        rh = h - bh;
        chmin(score, calc(gh*gw, bh*bw, rh*rw));
    }

    out << score << endl;
}
