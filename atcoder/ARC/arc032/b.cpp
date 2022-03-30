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

struct UnionFind {
    vector<ll> data;

    UnionFind(ll sz){
        data.assign(sz, -1);
    }
    bool unite(ll x, ll y){
        x = find(x), y = find(y);
        if(x == y) return (false);
        if(data[x] > data[y]) swap(x, y);
        data[x] += data[y];
        data[y] = x;
        return (true);
    }
    ll find(ll k){
        if(data[k] < 0) return (k);
        return (data[k] = find(data[k]));
    }
    ll size(ll k) {
        return (-data[find(k)]);
    }
};

int main(){
    ll n, m;
    cin >> n >> m;
    UnionFind uf(n);
    for(ll i=0; i < m; i++){
        ll a, b;
        cin >> a >> b;
        uf.unite(a-1, b-1);
    }
    ll ans = 0;
    for(ll i=1; i < n; i++){
        if(uf.find(0) != uf.find(i)){
            ans++;
            uf.unite(0, i);
        }
    }
    cout << ans << endl;
}