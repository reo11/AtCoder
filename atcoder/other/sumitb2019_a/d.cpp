#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

void solve(){
    ll n;
    string s;
    cin >> n;
    cin >> s;
    bool dp[n+1][4][1000] = {};
    dp[0][0][0] = true;
    for(ll i=0; i < n; i++){
        for(ll j=0; j < 3; j++){
            for(ll k=0; k < 100; k++){
                if(dp[i][j][k]){
                    int num = k * 10 + int(s[i] - '0');
                    dp[i+1][j+1][num] = true;
                }
            }
        }
        for(ll j=0; j < 4; j++){
            for(ll k=0; k < 1000; k++){
                if(dp[i][j][k]) dp[i+1][j][k] = true;
            }
        }
    }
    ll cnt = 0;
    for(ll k=0; k < 1000; k++){
        if(dp[n][3][k]) cnt++;
    }
    cout << cnt << "\n";
}

int main(){
    solve();
}