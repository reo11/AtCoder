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
    if (int(n / 10) == 9 or n % 10 == 9){
        out << "Yes" << endl;
    }
    else{
        out << "No" << endl;
    }
}
