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

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll h, w;
    in >> h >> w;
    ll s_y, s_x, g_y, g_x;
    in >> s_y >> s_x;
    s_y--;s_x--;
    in >> g_y >> g_x;
    g_y--;g_x--;

    char c[h][w];
    ll visited[h][w] = {};
    queue<pair<pair<ll, ll>, ll>> q;
    q.push(pair<pair<ll, ll>, ll>(pair<ll, ll>(s_x, s_y), 0));
    bool gool = false;
    REP(i, h){
        REP(j, w){
            in >> c[i][j];
        }
    }

    while(!q.empty()){
        ll x = q.front().first.first;
        ll y = q.front().first.second;
        ll count = q.front().second;
        if(x == g_x && y == g_y){
            out << count << endl;
            return 0;
        }
        q.pop();
        if(visited[y][x] == 0 && c[y][x] == '.'){
            visited[y][x] = 1;
            REP(i, 4){
                if(x+dx[i] >= 0 && x+dx[i] < w && y+dy[i] >= 0 && y+dy[i] < h && c[y+dy[i]][x+dx[i]] != '#'){
                    q.push(pair<pair<ll, ll>, ll>(pair<ll, ll>(x+dx[i], y+dy[i]), count+1));
                }
            }
        }
    }
}
