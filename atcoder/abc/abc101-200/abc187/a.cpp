#include <bits/stdc++.h>
using namespace std;
using ll = long long;
// 大きい配列はグローバルで書く

void solve(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    ll a, b;
    cin >> a >> b;
    ll sum_a = 0, sum_b = 0;
    while(a > 0){
        sum_a += a % 10;
        a /= 10;
    }
    while(b > 0){
        sum_b += b % 10;
        b /= 10;
    }
    cout << max(sum_a, sum_b) << endl;
}

int main(){
    solve();
}