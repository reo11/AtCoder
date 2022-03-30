#include <bits/stdc++.h>
using namespace std;
#define endl "\n"
using ll = long long;
using P = pair<ll, ll>;
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))

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

bool cmp(int n, pair<int, int> const& p)
{
    return ((p.first < n) && (p.second < n));
}


ll n, q;
vector<P> vw(100001);
map<ll, vector<ll>> vl;
map<P, ll> ans;

void dfs(vector<P> l, ll num){
    ll next_num1 = num * 2;
    ll next_num2 = num * 2 + 1;
    cout << next_num1 << next_num2 << endl;
    for(ll i=0; i < ll(l.size()); i++){
        l.push_back(P(l[i].first + vw[num].first, l[i].second + vw[num].second));
    }
    SORT(l);
    ll max_w = 0;
    if(vl[num].size() > 0){
        for(ll i=0; i < ll(vl[num].size()); i++){
            max_w = vl[num][i];
            auto Iter1 = upper_bound(l.begin(), l.end(), max_w, cmp);
            ll idx = (Iter1 - l.begin()) - 1;
            ans[P(num, max_w)] = l[idx].second;
        }
    }
    if(next_num1 <= n){
        dfs(l, next_num1);
    }
    if(next_num2 <= n){
        dfs(l, next_num2);
    }
    if(next_num1 > n && next_num2 > 2){
        return;
    }
}

int main(){
    cout << "aaa" << endl;
    cin >> n;
    for(ll i=0; i < n; i++){
        cin >> vw[i].second >> vw[i].first;
    }
    cin >> q;
    cout << "aaa" << endl;
    ll v, l;
    vector<P> query(q);
    for(ll i=0; i < q; i++){
        cin >> v >> l;
        vl[v].push_back(l);
        query.push_back(P(v, l));
    }
    cout << "aaa" << endl;
    vector<P> list;
    list.push_back(P(0, 0));
    dfs(list, 1);
    for(ll i=0; i < q; i++){
        cout << ans[P(query[i].first, query[i].second)] << endl;
    }
}