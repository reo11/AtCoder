#include <bits/stdc++.h>
using namespace std;
#define INF 1000000000000000

int64_t max(int64_t a, int64_t b){
    int64_t ret;
    if(a > b){
        ret = a;
    }else{
        ret = b;
    }
    return ret;
}

void solve(){
    int64_t n, ans;
    cin >> n;
    int64_t a[n];
    for(int64_t i = 0; i < n; i++){
        cin >> a[i];
    }

    ans = -INF;
    int64_t dp[3][n+4];
    for(int64_t i = 0; i < 3; i++){
        for(int64_t j = 0; j < n + 4; j++){
            dp[i][j] = -INF;
        }
    }
    dp[0][2] = 0;

    for(int64_t i = 4; i < n + 4; i++){
        dp[2][i] = max(max(dp[2][i], dp[1][i-3] + a[i-4]), max(dp[0][i-4] + a[i-4], dp[2][i-2] + a[i-4]));
        dp[1][i] = max(max(dp[1][i], dp[0][i-3] + a[i-4]), dp[1][i-2] + a[i-4]);
        dp[0][i] = max(dp[0][i], dp[0][i-2] + a[i-4]);
    }
    if(n % 2 == 1){
        ans = max(ans, max(max(dp[0][n], dp[1][n+2]), dp[2][n+3]));
    }else{
        ans = max(ans, max(dp[0][n+2], dp[1][n+3]));
    }
    cout << ans << endl;
}

int main(){
    solve();
}