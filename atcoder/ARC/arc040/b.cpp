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
    ll n, r;
    cin >> n >> r;
    string s;
    cin >> s;
    ll x = 0, ans = 0, cnt = 0;
    for(auto c: s){
        if(c == '.') cnt++;
    }
    ll move_cost = 0;
    for(ll i=n-1; i>=0; i--){
        if(s[i] == '.'){
            move_cost = max(ll(0), i-r+1);
            break;
        }
    }
    reverse(s.begin(), s.end());
    while(x < n){
        if(s[x] == '.'){
            ans++;
            for(ll i=x; i<x+r; i++){
                if(i >= n) break;
                if(s[i] == '.'){
                    s[i] = 'o';
                    cnt--;
                }
            }
        }
        if(cnt > 0){
            x++;
        }else{
            break;
        }
    }
    cout << ans + move_cost << endl;
}