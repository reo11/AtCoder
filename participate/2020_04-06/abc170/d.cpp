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

vector<ll> divisor(ll n) {
    vector<ll> ret;
    for (ll i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            ret.push_back(i);
            if (i * i != n) ret.push_back(n / i);
        }
    }
    SORT(ret);
    return ret;
}
ll MAX = 1000001;

int main(){
    ll n;
    cin >> n;
    vector<ll> a(n);
    ll cnts[MAX];
    bool is_ok[MAX];
    for(ll i=0; i < MAX; i++){
        is_ok[i] = true;
    }
    for(ll i=0; i < n; i++){
        cin >> a[i];
        cnts[a[i]]++;
        if(cnts[a[i]] > 1){
            is_ok[a[i]] = false;
        }
    }
    SORT(a);
    ll cnt=0;
    bool f = true;
    for(ll i=0; i < n; i++){
        if(is_ok[a[i]] == false){
            continue;
        }
        f = true;
        vector<ll> divs = divisor(a[i]);
        for(ll j=0; j < ll(divs.size()); j++){
            if(!is_ok[divs[j]]){
                f = false;
                break;
            }
        }
        if(f) cnt++;
        is_ok[a[i]] = false;
    }
    cout << cnt << endl;
}