#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
using ll = long long;
using P = pair<ll, ll>;

const ll infll = (1LL << 62) - 1;
const int inf = (1 << 30) - 1;

struct IoSetup {
    IoSetup() {
        cin.tie(nullptr);
        ios::sync_with_stdio(false);
        cout << fixed << setprecision(10);
        cerr << fixed << setprecision(10);
    }
} iosetup;

template< typename T1, typename T2 >
inline bool chmax(T1 &a, T2 b) { return a < b && (a = b, true); }

template< typename T1, typename T2 >
inline bool chmin(T1 &a, T2 b) { return a > b && (a = b, true); }

void fail() {
    cout << -1 << endl;
    exit(0);
}

ll manhattan_distance(ll x1, ll y1, ll x2, ll y2){
    return abs(x1 - x2) + abs(y1 - y2);
}

int main(){
    ll h, w;
    cin >> h >> w;
    string s[h];
    for(ll i = 0; i < h; i++){
        cin >> s[i];
    }
    vector<tuple<ll, ll>> points;
    for(ll i = 0; i < h; i++){
        for(ll j = 0; j < w; j++){
            if (s[i][j] == 'o'){
                points.push_back(make_tuple(i, j));
            }
        }
    }
    ll ans = manhattan_distance(get<0>(points[0]), get<1>(points[0]), get<0>(points[1]), get<1>(points[1]));
    cout << ans << endl;
}