// template
#include <bits/stdc++.h>
using namespace std;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for(int i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (int i = int(a); i <= int(b); ++i)
typedef long long int ll;
#define SIZE(x) ((int)(x).size())
int gcd(int a,int b){return b?gcd(b,a%b):a;}
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
typedef pair<long long, long long> LP;
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
    ll seet[100000] = {0};
    ll l, r;
    REP(i, n){
        in >> l >> r;
        seet[l-1] += 1;
        seet[r] -= 1;
    }
    ll ans = 0;
    ll num = 0;
    REP(i, 100000){
        num += seet[i];
        ans += num;
    }
    out << ans << endl;

}
