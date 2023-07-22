#include <bits/stdc++.h>
using namespace std;
using ll = long long;
// 大きい配列はグローバルで書く

void solve(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    // input
    ll n;
    cin >> n;
    vector<ll> x(n), y(n);
    for(ll i = 0; i < n; i++){
        cin >> x[i] >> y[i];
    }
    ll ans = 0;
    for(ll i = 0; i < n - 1; i++){
        for(ll j = i + 1; j < n; j++){
            if (abs(1.0 * (y[j] - y[i]) / (x[j] - x[i])) <= 1.0) {
                ans++;
            }
        }
    }
    cout << ans << endl;
}

int main(){
    solve();
}
