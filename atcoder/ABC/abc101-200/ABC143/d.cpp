// template
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long, long long> LP;
#define INF 999999999
#define MOD 1000000007
#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i <= ll(b); ++i)
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define UNIQUE(v) \
    sort(ALL(v)); \
    v.erase(unique(ALL(v)), v.end());
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


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    cin >> n;
    vector<ll> L(n);
    INSERT(L, 0, 1001);
    INSERT(L, 0, 0);

    REP(i, n){
        cin >> L[i];
    }
    SORT(L);

    ll i, r, l, ans = 0;
    REP_AB(i, 1, n+1){
        REP_AB(j, 1, n+1){
            if(i == j){
                continue;
            }
            ll count = 0;
            ll b = L[i];
            ll c = L[j];
            r = BIN_LEFT(L, b + c);
            ll max_ = b - c;
            if(b - c < c - b){
                max_ = c - b;
            }
            l = BIN_RIGHT(L, max_);
            count += r - l;
            if(b > L[l-1]){
                count--;
            }
            if(c > L[l-1]){
                count--;
            }
            if(count > 0){
                ans += count;
            }
        }
    }
    cout << ans << endl;
}
