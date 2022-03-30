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

int main(){
    string s, base = "AKIHABARA", base2 = "KIHBR";
    cin >> s;

    ll j = 0;
    for(ll i=0; i < ll(base.size()); i++){
        if(s[j] == base[i]) j++;
    }
    ll k = 0;
    for(ll i=0; i < ll(s.size()); i++){
        if(base2[k] == s[i]) k++;
    }
    if(j == ll(s.size()) && k == ll(base2.size())){
        cout << "YES\n";
    }else{
        cout << "NO\n";
    }
}