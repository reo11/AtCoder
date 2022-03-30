#include <bits/stdc++.h>
using namespace std;
using ll = long long;
ll a[1000001] = {};
ll b[1000001] = {};
ll dp[1000001][2][2] = {};
#define MAX_A 2000000000
#define A 0
#define B 1
#define MIN 0
#define MAX 1

void solve(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    ll n;
    cin >> n;
    for(ll i=0; i < 2*n; i++){
        cin >> a[i];
    }
    for(ll i=0; i < 2*n; i++){
        cin >> b[i];
    }
    for(ll i=0; i < 2*n; i++){
        for(ll j=0; j < 2; j++){
            dp[i][j][MIN] = MAX_A;
            dp[i][j][MAX] = 0;
        }
    }
    dp[0][0][0] = 1;
    dp[0][0][1] = 1;
    dp[0][1][0] = 0;
    dp[0][1][1] = 0;

    for(ll i=1; i <= 2*n-1; i++){
        if (a[i-1] <= a[i]){
            dp[i][A][MIN] = min(dp[i][A][MIN], dp[i-1][A][MIN]+1);
            dp[i][A][MAX] = max(dp[i][A][MAX], dp[i-1][A][MAX]+1);
        }
        if(b[i-1] <= a[i]){
            dp[i][A][MIN] = min(dp[i][A][MIN], dp[i-1][B][MIN]+1);
            dp[i][A][MAX] = max(dp[i][A][MAX], dp[i-1][B][MAX]+1);
        }
        if(a[i-1] <= b[i]){
            dp[i][B][MIN] = min(dp[i][B][MIN], dp[i-1][A][MIN]);
            dp[i][B][MAX] = max(dp[i][B][MAX], dp[i-1][A][MAX]);
        }
        if(b[i-1] <= b[i]){
            dp[i][B][MIN] = min(dp[i][B][MIN], dp[i-1][B][MIN]);
            dp[i][B][MAX] = max(dp[i][B][MAX], dp[i-1][B][MAX]);
        }
    }

    char ans[2*n];
    ll cnt_a = n;
    ll pre = -1;
    for(ll i = 2*n-1; i >= 0; i--){
        ll f = 0;
        for(ll j = 0; j < 2; j++){
            if(j == 0){
                if(pre == 0 && a[i] > a[i+1]) continue;
                if(pre == 1 && a[i] > b[i+1]) continue;
            }else{
                if(pre == 0 && b[i] > a[i+1]) continue;
                if(pre == 1 && b[i] > b[i+1]) continue;
            }
            if(dp[i][j][MIN] <= cnt_a && cnt_a <= dp[i][j][MAX]){
                if(j==0){
                    ans[i] = 'A';
                    pre = 0;
                    cnt_a--;
                }else{
                    ans[i] = 'B';
                    pre = 1;
                }
                f = 1;
                break;
            }
        }
        if(f == 0){
            cout << "-1" << "\n";
            return;
        }
    }
    for(ll i=0; i < 2*n; i++){
        cout << ans[i];
    }
    cout << "\n";
    return;
}

int main(){
    solve();
    return 0;
}