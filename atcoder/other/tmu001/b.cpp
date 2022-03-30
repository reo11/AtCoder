// 深さ優先探索
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

ll visited[501][501] = {};
char c[501][501];

bool check(ll x, ll y){
    if(c[x][y] == '#') return false;
    if(visited[x][y] > 0) return false;
    visited[x][y] = 1;
    if(c[x][y] == 'g') return true;
    bool flag = false;
    for(int i=0; i < 4; i ++){
        if(x+dx[i] >= 0 && x+dx[i] < 501){
            if(y+dy[i] >= 0 && y+dy[i] < 501){
                flag = flag || check(x + dx[i], y + dy[i]);
            }
        }
    }
    return flag;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll h, w;
    in >> h >> w;
    REP(i, 501){
        REP(j, 501){
            c[i][j] = '#';
        }
    }
    bool gool = false;
    ll s_x, s_y;
    REP(i, h){
        REP(j, w){
            in >> c[i][j];
            if(c[i][j] == 's'){
                s_x = i;
                s_y = j;
            }
        }
    }
    if(check(s_x, s_y)){
        out << "Yes" << endl;
    }else{
        out << "No" << endl;
    }
}
